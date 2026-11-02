---
title: "Przydatne narzędzia do realizacji projektu"
permalink: /2026-2027/narzedzia/
---

# Przydatne narzędzia do realizacji projektu

## Po co korzystać z tych narzędzi?

W projekcie należy używać narzędzi, które ułatwiają planowanie pracy, zapisywanie decyzji, współpracę i sprawdzanie rezultatów. Samo użycie narzędzia nie jest jednak celem zajęć. Każde narzędzie powinno zostawić w repozytorium ślad, który można później odtworzyć i zweryfikować.

## Zestaw narzędzi

| Narzędzie | Do czego służy | Dowód zapisany w repozytorium lub GitHubie |
|---|---|---|
| GitHub Repository | przechowywanie kodu, dokumentacji i historii zmian | pliki, commity, branche |
| GitHub Issues | opisywanie wymagań, zadań i błędów | Issue z opisem, właścicielem i kryteriami odbioru |
| GitHub Projects | planowanie pracy zespołu | tablica, statusy, przypisane zadania i milestone |
| Branch i Pull Request | praca nad zmianą oraz jej przegląd | branch, PR, review i merge |
| GitHub Actions | automatyczne sprawdzanie projektu | workflow zakończony statusem `success` |
| VS Code | edycja plików, terminal, Git i debugowanie | zmiana w repozytorium oraz instrukcja uruchomienia |
| Markdown | dokumentowanie problemu, decyzji i wyników | pliki `.md` w katalogu `docs/` |
| Mermaid lub diagrams.net | tworzenie diagramów | plik `.mmd`, `.drawio` albo eksportowany obraz |
| Jupyter lub skrypt analityczny | analiza danych i eksperymenty | notebook lub skrypt z powtarzalnym wynikiem |
| Agent AI | generowanie wariantów, planowanie, prototypowanie, testy i krytyka założeń | opis weryfikacji w dokumentacji etapu (lub `docs/agent-log.md`), zweryfikowany commit i Pull Request |

## Praca z asystentem AI

Agent powinien pomagać w analizie i implementacji, a nie zastępować weryfikację inżynierską. Należy wymagać od niego kilku wariantów rozwiązania, jawnych założeń, wskazania ryzyk i propozycji testów. Następnie zespół powinien samodzielnie wybrać wariant, sprawdzić źródła i zweryfikować działanie kodu.

Zalecany przebieg pracy z agentem:

1. Opisać problem i ograniczenia bez narzucania z góry gotowej technologii.
2. Poprosić o kilka wariantów rozwiązania, w tym wariant prosty (bazowy) i niewymagający dodatkowej infrastruktury.
3. Poprosić o krytykę każdego wariantu: koszty, wymagane dane, bezpieczeństwo, ryzyko i sposób testowania.
4. Wybrać jeden wariant i zapisać decyzję w dokumentacji projektu, Issue albo pliku ADR.
5. Przy generowaniu kodu pracować małymi krokami na osobnej gałęzi.
6. Samodzielnie sprawdzić kod, uruchomić testy, wykonać przegląd (review) i dopiero wtedy scalić zmianę.

Nie należy przekazywać agentowi haseł, kluczy API, danych osobowych ani niezweryfikowanych danych wrażliwych. W dokumentacji odpowiedniego etapu (lub w pomocniczym pliku wg wzoru [`agent-log.example.md`](./agent-log.example.md)) należy zapisać cel użycia agenta, decyzję zespołu i sposób sprawdzenia rezultatu, a nie pełny zapis rozmowy.

## Zrzuty demonstracyjne

Poniżej zamieszczono rzeczywiste zrzuty ekranu z dokumentacji GitHub i Visual Studio Code. Pokazują one elementy interfejsu wykorzystywane na kolejnych etapach projektu. Układ może nieznacznie różnić się między wersjami aplikacji.

### GitHub Projects

![GitHub Projects — widok projektu](https://docs.github.com/assets/cb-4169/images/help/projects-v2/tab-projects.png)

Źródło: [GitHub Docs — Quickstart for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects).

W tablicy projektu należy dodawać zadania, przypisywać osobę odpowiedzialną, aktualizować statusy wraz z postępem prac i wiązać wpisy z odpowiednimi Issues.

### GitHub Issue, branch i Pull Request

![GitHub — zakładka Issues](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)

![GitHub — wybór gałęzi przed utworzeniem Pull Requesta](https://docs.github.com/assets/cb-29825/images/help/pull_requests/branch-dropdown.png)

Źródła: [GitHub Docs — Creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) oraz [GitHub Docs — Creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).

Każdą większą zmianę należy prowadzić od opisu zadania w Issue, przez implementację na osobnej gałęzi i utworzenie Pull Requesta, aż do przeglądu przez inną osobę z zespołu i scalenia.

### VS Code i Git

![Visual Studio Code — inicjalizacja repozytorium w widoku Source Control](https://code.visualstudio.com/assets/docs/sourcecontrol/quickstart/initialize-repository.png)

![Visual Studio Code — widok Pull Requestów](https://code.visualstudio.com/assets/docs/sourcecontrol/github/pull-request-view.png)

Źródła: [VS Code — Quickstart: use source control](https://code.visualstudio.com/docs/sourcecontrol/quickstart) oraz [VS Code — Work with GitHub](https://code.visualstudio.com/docs/sourcecontrol/github).

W codziennej pracy z repozytorium należy przed edycją pobrać aktualne zmiany, a po wykonaniu swojej części zapisać i przesłać commit:

```bash
# jednorazowe pobranie repozytorium na komputer
git clone https://github.com/zespol/projekt.git
cd projekt

# przed rozpoczęciem edycji wspólnych plików
git pull

# sprawdzenie zmienionych plików i różnic
git status
git diff

# dodanie wskazanych plików, zapisanie commita i wysłanie na GitHub
git add docs/problem.md
git commit -m "Opis wprowadzonej zmiany"
git push
```

### GitHub Actions

![GitHub — zakładka Actions](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)

Źródło: [GitHub Docs — Quickstart for GitHub Actions](https://docs.github.com/en/actions/get-started/quickstart).

Zakładka **Actions** pozwala sprawdzić wynik automatycznego uruchomienia testów po każdym pushu lub Pull Requeście, odczytać log błędów i zweryfikować poprawkę w kolejnym commicie.

## Zasady dokumentowania indywidualnego wkładu

Nie należy traktować samego dopisania nazwiska do pliku jako dowodu pracy. Na każdym etapie projektu każdy członek zespołu powinien mieć własny, możliwy do wskazania rezultat (np. analizę źródła danych, słownik pól, skrypt czyszczący, wariant metody, diagram, test lub opis w raporcie) potwierdzony w historii commitów, Issues lub Pull Requestach.
