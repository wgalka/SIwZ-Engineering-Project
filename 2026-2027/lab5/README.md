---
title: "Laboratorium 5: Architektura, UML/ERD i technologie"
permalink: /2026-2027/lab5/
---

# Laboratorium 5: Architektura, UML/ERD i technologie

## Cel zajęć

Na tych zajęciach należy przełożyć wymagania, dane i pierwszy prototyp na projekt techniczny. Diagramy mają pomóc zespołowi wspólnie zrozumieć rozwiązanie i zaplanować implementację. Nie chodzi o narysowanie wielu ozdobnych schematów, ale o pokazanie najważniejszych elementów, zależności i przepływów.

Po zajęciach każdy zespół powinien:

- znać główne elementy projektowanego rozwiązania;
- mieć opisane najważniejsze przypadki użycia;
- posiadać model danych odpowiedni do problemu;
- umieć pokazać przepływ danych od źródła do wyniku;
- mieć zapisane decyzje technologiczne i ich uzasadnienie.

## Projektować od wymagań, nie od listy technologii

Najpierw należy ustalić, jakie zachowania i dane są potrzebne, a dopiero potem dobrać narzędzia. Wybrana technologia powinna wspierać wymagania, sposób pracy zespołu i ograniczenia projektu. Jeżeli prostsze rozwiązanie spełnia kryteria akceptacji, nie ma potrzeby zastępować go bardziej złożonym stosikiem.

Przejść od wymagania do przypadku użycia, od przypadku użycia do elementów systemu, a następnie do modelu danych i przepływu. Każdy element diagramu powinien mieć znaczenie dla implementacji albo dla wyjaśnienia działania projektu.

### Pytania pomocnicze

1. Kto korzysta z systemu i z jakich funkcji?
2. Jakie komponenty są potrzebne, aby zrealizować główny przepływ?
3. Gdzie przechowywane są dane i jakie relacje między nimi występują?
4. Jak dane przechodzą od źródła do wyniku pokazywanego użytkownikowi?
5. Co stanie się, gdy dane będą niepełne albo usługa zewnętrzna nie odpowie?
6. Które decyzje będzie trudno zmienić po rozpoczęciu implementacji?

## Diagramy i decyzje

Przygotować co najmniej diagram kontekstowy, opis przypadków użycia, model danych oraz diagram przepływu lub komponentów. Wybrać tylko te elementy notacji UML, które zespół potrafi objaśnić. Dla mniejszych projektów jeden czytelny diagram może być wartościowszy niż kilka niespójnych schematów.

Każdą ważną decyzję technologiczną zapisać razem z rozważanymi alternatywami i powodem wyboru. Taka notatka może być krótkim plikiem ADR w repozytorium albo dobrze opisanym Issue.

## Przydatne narzędzia

Zrzuty demonstracyjne i opis pełnego przepływu znajdują się w [przewodniku po narzędziach](../narzedzia/#zrzuty-demonstracyjne). Należy pokazać utworzenie diagramu, zapisanie go w repozytorium i powiązanie z wymaganiem oraz elementem implementacji.

1. **diagrams.net** - przygotować diagram kontekstowy, przypadki użycia i ERD, a następnie eksportować je do pliku używanego w dokumentacji.
2. **Mermaid lub PlantUML** - zapisać diagram jako tekst, aby można było go przeglądać i zmieniać razem z kodem.
3. **VS Code** - przejść przez strukturę projektu i pokazać, gdzie w implementacji znajdą się poszczególne elementy projektu.
4. **SQLite lub DB Browser for SQLite** - utworzyć przykładowe tabele, relacje i zapytanie potrzebne dla głównego przepływu.
5. **GitHub Issues lub plik ADR w Markdownie** - zapisać decyzję, alternatywy, konsekwencje i osobę odpowiedzialną za dalszą weryfikację.

Podczas pokazu wybrać jedno wymaganie z Lab 2 i prześledzić jego drogę przez diagram przypadku użycia, komponenty, model danych i fragment implementacji. Dzięki temu studenci zobaczą, jak dokumentacja łączy się z kodem.

## Zadania samodzielne

1. Narysować diagram kontekstowy rozwiązania z użytkownikiem, systemem i najważniejszymi systemami zewnętrznymi.
2. Opisać co najmniej trzy przypadki użycia, w tym główny przepływ i jeden scenariusz błędny.
3. Przygotować ERD albo inny model danych odpowiedni dla projektu oraz opisać kluczowe pola i relacje.
4. Narysować przepływ danych od źródła do wyniku pokazywanego użytkownikowi.
5. Zapisać trzy najważniejsze decyzje technologiczne wraz z alternatywami i uzasadnieniem.
6. Porównać projekt techniczny z pierwszym prototypem i wskazać jedną rzecz do poprawy przed implementacją MVP.
7. Zapisać opis architektury w `docs/architecture.md` oraz przechować diagram w formacie Mermaid, PlantUML, Draw.io lub równoważnym.
8. Utworzyć Issue dla jednej decyzji technologicznej i zamknąć je po dodaniu notatki ADR do repozytorium.

Każdy członek zespołu powinien przygotować lub poprawić konkretny element projektu technicznego. Rezultatem może być diagram, model danych, decyzja ADR, opis błędnego scenariusza albo powiązanie wymagania z elementami implementacji.

## Rezultat do zapisania

- diagramy zapisane w repozytorium;
- model danych i opis najważniejszych relacji;
- opis architektury i przepływu danych;
- lista decyzji technologicznych;
- wskazanie, które elementy trzeba zaimplementować w pierwszej kolejności.

## Zasady pracy zespołowej

Na koniec poprosić inną osobę o odczytanie diagramów bez dodatkowych wyjaśnień. Jeżeli nie potrafi wskazać głównego użytkownika, przepływu i miejsca zapisu danych, diagram wymaga uproszczenia albo doprecyzowania.
