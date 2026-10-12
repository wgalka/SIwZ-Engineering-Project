# Laboratorium 4: Źródła i przygotowanie danych

## Cel zajęć

Na tych zajęciach należy pozyskać dane do projektu, ocenić ich jakość i przygotować powtarzalny pierwszy etap przetwarzania. Dane nie są tylko plikiem potrzebnym do uruchomienia programu. Ich pochodzenie, licencja, struktura i ograniczenia wpływają na wiarygodność całego rozwiązania.

Po zajęciach każdy zespół powinien:

- znać źródło danych i warunki ich wykorzystania;
- posiadać słownik najważniejszych pól;
- znać podstawowe problemy jakościowe w danych;
- mieć zapisany sposób czyszczenia i przygotowania danych;
- umieć odtworzyć przetwarzanie na innej próbce.

## Od źródła do danych używanych przez system

Najpierw należy opisać, skąd dane pochodzą, kto je udostępnia, w jakim są formacie i kiedy zostały pobrane. Należy sprawdzić licencję oraz ograniczenia wykorzystania. Jeżeli plik jest duży, wrażliwy albo nie może być rozpowszechniany, w repozytorium należy umieścić małą próbkę, schemat i instrukcję pobrania zamiast całego zbioru.

Następnie sprawdzić, czy dane odpowiadają problemowi z Lab 1 i wymaganiom z Lab 2. Nie zakładać, że nazwa kolumny albo format pliku są jednoznaczne. Zapisać, co oznacza każda ważna kolumna, jaka jest jednostka wartości i które pola mogą być puste.

### Pytania pomocnicze

1. Kto jest właścicielem lub wydawcą danych?
2. Czy licencja pozwala na użycie danych w projekcie i ich publikację?
3. Jak często dane są aktualizowane?
4. Czy zbiór obejmuje przypadki ważne dla naszego użytkownika?
5. Które pola zawierają braki, duplikaty albo nieprawidłowe typy?
6. Czy inna osoba może odtworzyć sposób przygotowania danych?

## Kontrola jakości danych

Wykonać krótki przegląd danych przed rozpoczęciem właściwej implementacji. Sprawdzić liczbę rekordów, nazwy i typy kolumn, wartości puste, duplikaty, zakresy liczb, formaty dat oraz wartości odstające. Nie usuwać problematycznych rekordów bez zapisania powodu i wpływu tej decyzji na wynik.

Każdy krok czyszczenia zapisać w skrypcie albo notebooku. Ręczna edycja pliku może być dopuszczalna jako jednorazowa analiza, ale nie powinna być jedynym sposobem przygotowania danych używanych przez system.

## Narzędzia do pokazania

1. **Przeglądarka i narzędzia pobierania danych** - znaleźć źródło publiczne, odczytać metadane, sprawdzić licencję i pobrać małą próbkę.
2. **Python z pandas lub narzędzie wybrane przez zespół** - wczytać CSV albo JSON, sprawdzić strukturę i wykonać proste przekształcenia.
3. **Jupyter** - dokumentować kolejne kroki analizy razem z obserwacjami i wynikami.
4. **SQLite i DB Browser for SQLite** - zapisać dane tabelaryczne, pokazać relacje i wykonać proste zapytania.
5. **Git** - przechowywać skrypt przetwarzania, słownik danych i instrukcję bez dodawania dużych lub wrażliwych plików.

Podczas pokazu przejść od surowego pliku do przygotowanego wyniku, a następnie uruchomić ten sam skrypt ponownie. Pokazać także, co należy zrobić, gdy dane nie mogą zostać zapisane w repozytorium.

## Zadania samodzielne

1. Sporządzić tabelę źródeł danych z informacją o właścicielu, formacie, licencji, dacie pobrania i ograniczeniach.
2. Pobrać małą próbkę danych i utworzyć słownik najważniejszych pól.
3. Wykryć braki, duplikaty, błędne typy, niepoprawne formaty i wartości odstające.
4. Przygotować skrypt lub notebook wykonujący co najmniej trzy kroki czyszczenia.
5. Opisać, które problemy rozwiązano automatycznie, a które pozostawiono i dlaczego.
6. Zapisać wynik przetwarzania oraz sprawdzić, czy można odtworzyć całą procedurę na kopii próbki.

Każdy członek zespołu powinien odpowiadać za konkretny fragment kontroli danych albo przygotowania przetwarzania. Rezultatem może być na przykład opis źródła, słownik pól, analiza jakości, funkcja czyszcząca lub test sprawdzający wynik.

## Rezultat do zapisania

- opis źródeł i warunków wykorzystania danych;
- słownik danych;
- mała próbka danych albo instrukcja jej pobrania;
- skrypt lub notebook przetwarzania;
- raport podstawowej jakości danych;
- commit pozwalający odtworzyć przygotowanie danych.

## Zasady bezpieczeństwa i powtarzalności

Nie umieszczać w repozytorium danych osobowych, haseł, kluczy API ani dużych plików, jeśli nie ma ku temu wyraźnego powodu. W przypadku wątpliwości zapisać w repozytorium opis i próbkę, a pełne dane przechowywać zgodnie z zasadami kursu.
