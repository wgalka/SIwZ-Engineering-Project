---
title: "Laboratorium 6: Plan realizacji, GitHub i podział zadań"
permalink: /2026-2027/lab6/
---

# Laboratorium 6: Plan realizacji, GitHub i podział zadań

## Cel zajęć

Na tych zajęciach należy przełożyć architekturę i zakres MVP na plan pracy możliwy do wykonania przez zespół. Repozytorium ma zacząć pokazywać nie tylko kod, ale też sposób organizacji pracy: kto odpowiada za rezultat, jakie są zależności i po czym można uznać zadanie za zakończone.

Po zajęciach każdy zespół powinien:

- mieć backlog podzielony na małe, zrozumiałe zadania;
- znać kolejność prac i najbliższy kamień milowy;
- mieć przypisany rezultat dla każdego członka zespołu;
- umieć przejść od zadania do brancha, commita i Pull Requesta;
- mieć uruchomioną podstawową automatyczną kontrolę projektu.

## Każde zadanie powinno kończyć się rezultatem

Nie zapisywać zadań w formie „pracować nad aplikacją” albo „zrobić backend”. Takie sformułowania są zbyt szerokie i nie pozwalają sprawdzić postępu. Lepsze zadanie opisuje konkretną zmianę, jej zakres i warunek akceptacji, na przykład „dodać endpoint wyszukiwania zasobów i test dla pustego wyniku”.

Podzielić duże epiki na zadania, które można wykonać w jednym etapie pracy i zademonstrować. Zaznaczyć zależności: na przykład test nie może zostać przygotowany przed ustaleniem interfejsu funkcji, a ekran nie może korzystać z danych, których jeszcze nie ma w modelu.

### Pytania pomocnicze

1. Jaki konkretny rezultat powstanie po wykonaniu zadania?
2. Kto jest właścicielem tego rezultatu?
3. Jakie są kryteria akceptacji?
4. Od jakich innych zadań zależy rozpoczęcie pracy?
5. Jak sprawdzić, że zadanie jest ukończone?
6. Czy zadania są rozdzielone tak, aby każdy członek zespołu miał własny wkład?

## Przydatne narzędzia

Zrzuty demonstracyjne i opis pełnego przepływu znajdują się w [przewodniku po narzędziach](../narzedzia/#zrzuty-demonstracyjne). Należy pokazać cały cykl: Issue, branch, commit, Pull Request, review, merge oraz wynik GitHub Actions.

1. **GitHub Projects** - utworzyć tablicę z kolumnami backlog, do zrobienia, w trakcie, do przeglądu i zakończone; dodać etykiety, osoby i milestone.
2. **GitHub Issues** - opisać zadanie, dodać kryteria akceptacji, zależności, właściciela i link do powiązanego wymagania.
3. **Git** - utworzyć branch o czytelnej nazwie, wykonać mały commit i pokazać różnicę względem głównej gałęzi.
4. **Pull Request** - przejść przez opis zmiany, checklistę, review i poprawki przed scaleniem.
5. **GitHub Actions** - uruchomić prosty workflow, na przykład instalację zależności, testy albo sprawdzenie formatowania.

Podczas pokazu przejść cały cykl na jednym małym zadaniu: utworzyć Issue, przypisać osobę, założyć branch, wykonać commit, otworzyć Pull Request, przejrzeć zmianę i dopiero wtedy ją scalić.

## Zadania samodzielne

1. Rozbić MVP na epiki i zadania możliwe do wykonania w jednym etapie pracy.
2. Uzupełnić każde zadanie o rezultat, kryteria akceptacji, właściciela i zależności.
3. Utworzyć tablicę projektu oraz milestone obejmujący najbliższą wersję systemu.
4. Przypisać każdemu członkowi zespołu co najmniej jedno zadanie kończące się mierzalnym rezultatem.
5. Wykonać zmianę na osobnym branchu i przeprowadzić ją przez Pull Request z krótkim review.
6. Dodać do repozytorium prostą automatyczną kontrolę, na przykład uruchomienie testów lub sprawdzenie formatowania.
7. Zaktualizować tablicę po zakończeniu pracy i dopisać, co pozostało do wykonania.
8. Zapisać w `docs/evidence.md` link do własnego Issue, brancha, Pull Requesta i commita.
9. Umieścić w repozytorium workflow `.github/workflows/check.yml` i doprowadzić do jego pomyślnego wykonania.

Indywidualny wkład nie musi oznaczać wyłącznie dużego fragmentu kodu. Może nim być test, moduł danych, diagram techniczny, automatyzacja, dokumentacja albo analiza wyników, ale rezultat powinien być zapisany w repozytorium i możliwy do wskazania podczas podsumowania.

## Rezultat do zapisania

- uporządkowany backlog z epikami, zadaniami i zależnościami;
- tablica projektu i milestone;
- zadania z właścicielami oraz kryteriami akceptacji;
- co najmniej jeden zamknięty Pull Request;
- działająca podstawowa kontrola automatyczna;
- lista indywidualnych rezultatów członków zespołu.

## Zasady pracy zespołowej

Przed rozpoczęciem kolejnego etapu wspólnie sprawdzić, czy obciążenie i odpowiedzialność są rozłożone rozsądnie. Jeżeli jedna osoba ma wszystkie zadania techniczne, a pozostali nie mają własnych rezultatów, podzielić pracę ponownie.
