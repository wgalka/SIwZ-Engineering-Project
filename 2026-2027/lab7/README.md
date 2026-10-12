# Laboratorium 7: Implementacja i pierwsza wersja MVP

## Cel zajęć

Na tych zajęciach należy rozwinąć prototyp do pierwszej spójnej wersji MVP, którą można uruchomić i pokazać użytkownikowi. Pracę należy prowadzić pionowo: od wejścia przez logikę i dane aż do wyniku. Lepiej ukończyć jeden ważny przepływ niż rozpocząć wiele funkcji, których nie da się uruchomić razem.

Po zajęciach każdy zespół powinien:

- mieć uruchamialny główny przepływ użytkownika;
- korzystać z przygotowanych danych lub modelu zgodnie z projektem z Lab 5;
- obsługiwać podstawowe błędne sytuacje;
- mieć instrukcję uruchomienia na przykładowych danych;
- posiadać historię pracy w branchach i Pull Requestach.

## Najpierw działanie, potem rozbudowa

Wybrać jeden przepływ o największej wartości dla użytkownika i doprowadzić go do końca. Ograniczyć liczbę funkcji dodatkowych, dopóki podstawowa ścieżka nie działa. Każdy kolejny fragment powinien być możliwy do uruchomienia, sprawdzenia i opisania.

Podczas implementacji dokumentować decyzje, które mogą utrudnić późniejszą zmianę: format danych, sposób komunikacji między modułami, wymagane biblioteki i konfigurację środowiska. Nie umieszczać haseł ani kluczy dostępowych w kodzie i historii Git.

### Pytania pomocnicze

1. Jaki jeden przepływ użytkownika musi działać w pierwszej kolejności?
2. Jakie dane wejściowe są potrzebne do jego uruchomienia?
3. Jaki wynik użytkownik powinien zobaczyć?
4. Co stanie się przy pustym, błędnym lub niepełnym wejściu?
5. Czy inny członek zespołu potrafi uruchomić projekt według README?
6. Który fragment implementacji jest rezultatem pracy każdej osoby?

## Przydatne narzędzia

Zrzuty demonstracyjne i opis pełnego przepływu znajdują się w [przewodniku po narzędziach](../narzedzia/README.md#zrzuty-demonstracyjne). Należy pokazać implementację jednej funkcji od Issue przez branch i Pull Request aż do uruchomienia działającej wersji MVP.

1. **VS Code** - przejść przez strukturę projektu, uruchomić komendę w terminalu, ustawić punkt przerwania i odczytać log.
2. **Menedżer zależności wybranej technologii** - dodać bibliotekę, zapisać wersję i odtworzyć środowisko na czystym katalogu.
3. **Git i Pull Request** - podzielić implementację na małe zmiany, opisać je i przejrzeć przed scaleniem.
4. **Plik `.env` i ustawienia sekretów** - oddzielić konfigurację od kodu oraz pokazać bezpieczny plik przykładowy.
5. **README** - opisać wymagania, instalację, uruchomienie, dane przykładowe i oczekiwany wynik.

Podczas pokazu zrealizować jedno zadanie od Issue do działającego Pull Requesta. Pokazać również celowo wywołany błąd i sposób znalezienia przyczyny w komunikacie lub logu.

## Zadania samodzielne

1. Zaimplementować najważniejszy przepływ użytkownika opisany w Lab 2 i zaprojektowany w Lab 5.
2. Podłączyć przygotowane dane, model bazowy albo warstwę przechowywania danych.
3. Obsłużyć co najmniej trzy błędne sytuacje, na przykład brak pliku, pusty wynik i błędne dane wejściowe.
4. Dodać instrukcję uruchomienia oraz mały zestaw danych lub polecenie jego przygotowania.
5. Wykonać pracę w branchach i zamknąć zadania przez Pull Requesty.
6. Dodać logowanie albo komunikaty diagnostyczne pozwalające znaleźć podstawowy błąd.
7. Pokazać indywidualny wkład każdej osoby w postaci kodu, testu, danych, dokumentacji, automatyzacji albo innego artefaktu.
8. Zapisać w `docs/evidence.md` link do Pull Requesta oraz krótko opisać własny rezultat.

Każdy członek zespołu powinien mieć rezultat, który można uruchomić, przeczytać albo zademonstrować. Wkład zapisać w Issue, commitach, Pull Requestach lub plikach repozytorium.

## Rezultat do zapisania

- uruchamialna wersja MVP;
- instrukcja uruchomienia od zera;
- przykładowe dane i oczekiwany wynik;
- obsługa podstawowych błędów;
- zamknięte zadania i Pull Requesty;
- krótka demonstracja głównego przepływu.

## Zasady pracy zespołowej

Przed zakończeniem zajęć uruchomić projekt na komputerze osoby, która nie implementowała głównego przepływu. Jeżeli instrukcja nie wystarcza, poprawić README, konfigurację albo skrypty uruchomieniowe.
