# Weryfikator repozytorium (narzędzie prowadzącego)

## Cel

Skrypt `verify_repository.py` służy do sprawdzenia, czy publiczne repozytorium zespołu zawiera wymagane artefakty dla danego etapu (`lab2`–`lab8`) oraz czy każdy członek zespołu ma widoczny wkład w historię pracy.

## Uruchomienie

Wystarczy podać link do repozytorium i etap, który ma zostać sprawdzony:

```powershell
python tools/verify_repository.py --repo https://github.com/zespol/projekt --lab lab6
```

Loginy członków zespołu należy przekazać parametrem `--students`:

```powershell
python tools/verify_repository.py --repo https://github.com/zespol/projekt --students anna123,jan456 --lab lab6
```

Dla wyższego limitu zapytań GitHub API można ustawić zmienną środowiskową `GITHUB_TOKEN` albo przekazać token parametrem `--token`.

## Co sprawdza skrypt?

W zależności od wybranego laboratorium (`lab2`–`lab8`) skrypt sprawdza:

- dostępność i publiczną widoczność repozytorium;
- `README.md` oraz wymagane pliki i katalogi dokumentacji (`docs/problem.md`, `docs/data.md`, `docs/data-dictionary.md`, `docs/processing.md`, `docs/methods.md`, `docs/architecture.md`, `docs/implementation.md`, `docs/tests.md`, `docs/user-guide.md`, `docs/report.md`, `docs/presentation.md`);
- obecność próbki danych (`data/sample.*`) w Lab 2;
- obecność Issues i Pull Requestów na etapach projektowania, realizacji i testowania;
- commity przypisane do przekazanych loginów członków zespołu;
- wynik w formacie tekstowym albo JSON (`--json`).
