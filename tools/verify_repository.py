"""Wstępny weryfikator repozytorium projektu.

Skrypt korzysta z publicznego GitHub REST API i nie wymaga dodatkowych bibliotek.
Przykład:

    python tools/verify_repository.py \
      --repo https://github.com/zespol/projekt \
      --students anna123,jan456 \
      --lab lab6

Dla repozytoriów prywatnych można podać zmienną środowiskową GITHUB_TOKEN.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


LAB_RULES: dict[str, dict[str, Any]] = {
    "lab2": {
        "paths": ["README.md", "docs/problem.md", "docs/agent-log.md"],
        "issue_min": 1,
    },
    "lab3": {
        "paths": ["docs/sources.md"],
    },
    "lab4": {
        "paths": ["docs/data.md"],
    },
    "lab5": {
        "paths": ["docs/architecture.md"],
    },
    "lab6": {
        "paths": [".github/workflows/check.yml", "docs/evidence.md"],
        "issue_min": 1,
        "pr_min": 1,
        "workflow_required": True,
    },
    "lab7": {
        "paths": ["README.md", "src", "tests"],
        "pr_min": 1,
    },
    "lab8": {
        "paths": ["tests"],
        "workflow_required": True,
    },
    "lab9": {
        "paths": ["README.md", "docs"],
        "release_or_tag": True,
    },
    "lab10": {
        "paths": ["README.md", "docs/evidence.md"],
    },
}


@dataclass
class Check:
    name: str
    status: str
    details: str


def parse_repo_url(value: str) -> tuple[str, str]:
    parsed = urlparse(value if "://" in value else f"https://{value}")
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2 or parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        raise ValueError("Oczekiwano adresu repozytorium GitHub, np. https://github.com/owner/repo")
    return parts[0], re.sub(r"\.git$", "", parts[1])


class GitHub:
    def __init__(self, token: str | None = None) -> None:
        self.token = token

    def get(self, path: str) -> Any:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "projekt-informatyczny-repo-check/0.1",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = Request(f"https://api.github.com{path}", headers=headers)
        with urlopen(request, timeout=20) as response:
            return json.load(response)

    def exists(self, owner: str, repo: str, path: str) -> bool:
        try:
            self.get(f"/repos/{owner}/{repo}/contents/{path}")
            return True
        except HTTPError as error:
            if error.code == 404:
                return False
            raise

    def read_text(self, owner: str, repo: str, path: str) -> str | None:
        try:
            payload = self.get(f"/repos/{owner}/{repo}/contents/{path}")
            encoded = payload.get("content", "").replace("\n", "")
            return base64.b64decode(encoded).decode("utf-8")
        except (HTTPError, UnicodeDecodeError, ValueError):
            return None


def safe_get(api: GitHub, path: str, fallback: Any) -> Any:
    try:
        return api.get(path)
    except (HTTPError, URLError, TimeoutError):
        return fallback


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="Adres repozytorium GitHub")
    parser.add_argument("--lab", choices=sorted(LAB_RULES), default="lab6")
    parser.add_argument("--students", default="", help="Loginy GitHub oddzielone przecinkami")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    parser.add_argument("--json", action="store_true", help="Zwróć raport w formacie JSON")
    args = parser.parse_args()

    try:
        owner, repo = parse_repo_url(args.repo)
        api = GitHub(args.token)
        metadata = api.get(f"/repos/{owner}/{repo}")
    except (ValueError, HTTPError, URLError, TimeoutError) as error:
        print(f"Nie można odczytać repozytorium: {error}", file=sys.stderr)
        return 2

    rules = LAB_RULES[args.lab]
    checks: list[Check] = []
    checks.append(Check("repozytorium", "PASS", f"{metadata.get('full_name', owner + '/' + repo)} jest dostępne"))

    required_paths = [".course/members.json", *rules.get("paths", [])]
    for path in dict.fromkeys(required_paths):
        status = "PASS" if api.exists(owner, repo, path) else "FAIL"
        checks.append(Check(f"plik: {path}", status, "znaleziono" if status == "PASS" else "brak wymaganego elementu"))

    issues = safe_get(api, f"/repos/{owner}/{repo}/issues?state=all&per_page=100", [])
    issues = [item for item in issues if "pull_request" not in item]
    pulls = safe_get(api, f"/repos/{owner}/{repo}/pulls?state=all&per_page=100", [])
    workflows = safe_get(api, f"/repos/{owner}/{repo}/actions/workflows", {}).get("workflows", [])

    if "issue_min" in rules:
        minimum = rules["issue_min"]
        status = "PASS" if len(issues) >= minimum else "FAIL"
        checks.append(Check("Issues", status, f"{len(issues)} znaleziono, wymagane co najmniej {minimum}"))
    if "pr_min" in rules:
        minimum = rules["pr_min"]
        status = "PASS" if len(pulls) >= minimum else "FAIL"
        checks.append(Check("Pull Requesty", status, f"{len(pulls)} znaleziono, wymagane co najmniej {minimum}"))
    if rules.get("workflow_required"):
        status = "PASS" if workflows else "FAIL"
        checks.append(Check("GitHub Actions", status, f"{len(workflows)} workflow znaleziono"))

    commits = safe_get(api, f"/repos/{owner}/{repo}/commits?per_page=100", [])
    students = [value.strip() for value in args.students.split(",") if value.strip()]
    if not students:
        members_text = api.read_text(owner, repo, ".course/members.json")
        if members_text:
            try:
                members = json.loads(members_text).get("members", [])
                students = [member.get("github", "").strip() for member in members if member.get("github")]
            except json.JSONDecodeError:
                checks.append(Check(".course/members.json", "FAIL", "plik nie zawiera poprawnego JSON"))
    for student in students:
        authored = [item for item in commits if (item.get("author") or {}).get("login", "").lower() == student.lower()]
        student_prs = [item for item in pulls if (item.get("user") or {}).get("login", "").lower() == student.lower()]
        status = "PASS" if authored or student_prs else "FAIL"
        details = f"{len(authored)} commitów, {len(student_prs)} Pull Requestów"
        checks.append(Check(f"wkład: {student}", status, details))

    if args.json:
        print(json.dumps({"repo": f"{owner}/{repo}", "lab": args.lab, "checks": [check.__dict__ for check in checks]}, ensure_ascii=False, indent=2))
    else:
        print(f"Repozytorium: {owner}/{repo} | {args.lab}")
        for check in checks:
            print(f"{check.status:5} {check.name}: {check.details}")

    return 1 if any(check.status == "FAIL" for check in checks) else 0


if __name__ == "__main__":
    raise SystemExit(main())
