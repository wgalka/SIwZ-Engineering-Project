---
title: "Przydatne narzędzia do realizacji projektu"
permalink: /2026-2027/narzedzia/
---

# Przydatne narzędzia do realizacji projektu

## Po co korzystać z tych narzędzi?

W projekcie należy używać narzędzi, które ułatwiają planowanie pracy, zapisywanie decyzji, współpracę i sprawdzanie rezultatów. Samo użycie narzędzia nie jest jednak celem zajęć. Każde narzędzie powinno zostawić w repozytorium ślad, który można później odtworzyć i zweryfikować.

Na zajęciach należy najpierw pokazać narzędzie na przykładzie prowadzącego. Po pokazie należy wykonać analogiczne zadanie we własnym repozytorium.

## Zestaw narzędzi

| Narzędzie | Do czego służy | Dowód zapisany w repozytorium lub GitHubie |
|---|---|---|
| GitHub Repository | przechowywanie kodu, dokumentacji i historii zmian | pliki, commity, branche |
| GitHub Issues | opisywanie wymagań, zadań i błędów | Issue z opisem, właścicielem i kryteriami akceptacji |
| GitHub Projects | planowanie pracy zespołu | tablica, statusy, przypisane zadania i milestone |
| Branch i Pull Request | praca nad zmianą oraz jej przegląd | branch, PR, review i merge |
| GitHub Actions | automatyczne sprawdzanie projektu | workflow zakończony statusem `success` |
| VS Code | edycja plików, terminal, Git i debugowanie | zmiana w repozytorium oraz instrukcja uruchomienia |
| Markdown | dokumentowanie problemu, decyzji i wyników | pliki `.md` w katalogu `docs/` |
| Mermaid lub diagrams.net | tworzenie diagramów | plik `.mmd`, `.drawio` albo eksportowany obraz |
| Jupyter lub skrypt analityczny | analiza danych i eksperymenty | notebook lub skrypt z powtarzalnym wynikiem |
| Agent AI | generowanie wariantów, planowanie, prototypowanie, testy i krytyka założeń | `docs/agent-log.md`, zweryfikowany commit i Pull Request |

## Jak uczyć się pracy z agentem?

Agent powinien pomagać w myśleniu, a nie zastępować myślenie. Należy wymagać od niego kilku wariantów rozwiązania, jawnych założeń, wskazania ryzyk i propozycji testów. Następnie zespół powinien samodzielnie wybrać wariant, sprawdzić źródła i zweryfikować działanie prototypu.

Przykładowy przebieg pokazu:

1. Opisać agentowi problem i ograniczenia bez podawania gotowej technologii.
2. Poprosić o trzy warianty rozwiązania, w tym wariant wykorzystujący istniejące urządzenia i wariant bez dodatkowego sprzętu.
3. Poprosić o krytykę każdego wariantu: koszty, dane, bezpieczeństwo, ryzyko i sposób testowania.
4. Wybrać jeden wariant i zapisać decyzję w Issue albo pliku ADR.
5. Poprosić agenta o mały prototyp lub test na branchu.
6. Sprawdzić kod, uruchomić testy, wykonać review i dopiero wtedy scalić zmianę.

Nie należy przekazywać agentowi haseł, kluczy API, danych osobowych ani niezweryfikowanych danych wrażliwych. W `docs/agent-log.md` należy zapisać nie pełną rozmowę, lecz cel, najważniejsze propozycje, decyzję zespołu i sposób sprawdzenia rezultatu.

## Zrzuty demonstracyjne

Poniżej zamieszczono rzeczywiste zrzuty ekranu z dokumentacji GitHub i Visual Studio Code. Pokazują one elementy interfejsu, które należy wykorzystać podczas zajęć. Układ może nieznacznie różnić się od aktualnej wersji aplikacji. Po każdym pokazie należy wykonać analogiczne zadanie we własnym repozytorium.

### GitHub Projects

![GitHub Projects — widok projektu](https://docs.github.com/assets/cb-4169/images/help/projects-v2/tab-projects.png)

Źródło: [GitHub Docs — Quickstart for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects).

Należy pokazać utworzenie tablicy, dodanie zadania, przypisanie osoby, zmianę statusu i powiązanie zadania z Issue.

### GitHub Issue, branch i Pull Request

![GitHub — zakładka Issues](https://docs.github.com/assets/cb-51267/images/help/repository/repo-tabs-issues-global-nav-update.png)

![GitHub — wybór gałęzi przed utworzeniem Pull Requesta](https://docs.github.com/assets/cb-29825/images/help/pull_requests/branch-dropdown.png)

Źródła: [GitHub Docs — Creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) oraz [GitHub Docs — Creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).

Należy pokazać przejście od opisu potrzeby do małej zmiany w branchu, Pull Requesta, review i scalenia.

### VS Code i Git

![Visual Studio Code — inicjalizacja repozytorium w widoku Source Control](https://code.visualstudio.com/assets/docs/sourcecontrol/quickstart/initialize-repository.png)

![Visual Studio Code — widok Pull Requestów](https://code.visualstudio.com/assets/docs/sourcecontrol/github/pull-request-view.png)

Źródła: [VS Code — Quickstart: use source control](https://code.visualstudio.com/docs/sourcecontrol/quickstart) oraz [VS Code — Work with GitHub](https://code.visualstudio.com/docs/sourcecontrol/github).

Należy pokazać otwarcie repozytorium, edycję pliku, sprawdzenie różnicy, commit i przesłanie zmiany do GitHuba.

### GitHub Actions

![GitHub — zakładka Actions](https://docs.github.com/assets/cb-12958/images/help/repository/actions-tab-global-nav-update.png)

Źródło: [GitHub Docs — Quickstart for GitHub Actions](https://docs.github.com/en/actions/get-started/quickstart).

Należy pokazać uruchomienie testów po Pull Requeście, odczytanie wyniku i poprawienie błędu wykrytego przez workflow.

### Bot weryfikujący repozytorium

Bot powinien sprawdzać dowody zapisane w repozytorium i w publicznej historii GitHuba, a następnie wygenerować raport `PASS`, `WARN` albo `FAIL` dla zespołu i poszczególnych osób.

Nie jest to gotowa usługa GitHuba, dlatego nie zamieszczono zrzutu ekranu. Przykładowy wynik działania może wyglądać następująco:

```text
PASS  README.md i wymagane pliki dokumentacji są dostępne
PASS  Każda osoba ma przypisane Issue i Pull Request
WARN  Brak zakończonego workflow GitHub Actions
```

## Zadanie wspólne dla studentów

Każdy student powinien wykonać poniższe czynności we własnym repozytorium zespołu:

1. Utworzyć repozytorium na GitHubie i dodać plik `README.md` z nazwą projektu, problemem oraz instrukcją uruchomienia.
2. Utworzyć katalog `docs/` i zapisać w nim opis problemu, głównego użytkownika oraz zakresu MVP.
3. Utworzyć Issue opisujące własne zadanie. Issue powinno zawierać rezultat, kryteria akceptacji i osobę odpowiedzialną.
4. Utworzyć branch o nazwie związanej z zadaniem, wykonać zmianę i przygotować Pull Request.
5. Poprosić inną osobę z zespołu o review oraz odpowiedzieć na komentarz w Pull Requeście.
6. Utworzyć lub zaktualizować tablicę GitHub Projects, przypisać zadanie i zmienić jego status.
7. Dodać prosty workflow GitHub Actions uruchamiający test albo sprawdzenie formatowania.
8. Zapisać w `docs/evidence.md` linki do własnego Issue, Pull Requesta i commita.

Nie należy traktować samego dopisania nazwiska do pliku jako dowodu pracy. Każda osoba powinna mieć własny rezultat, własny Issue oraz zmianę widoczną w historii repozytorium.


