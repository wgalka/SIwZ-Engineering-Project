# Laboratorium 2: Doprecyzowanie problemu, użytkownicy i wymagania

## Cel zajęć

Na tych zajęciach należy przejść od ogólnego pomysłu z Lab 1 do konkretnej specyfikacji pierwszej wersji rozwiązania. Zespół powinien opisać problem językiem użytkownika, określić odbiorcę, zapisać wymagania i rozpocząć budowanie małego, działającego fragmentu systemu.

Po zajęciach każdy zespół powinien:

- umieć opisać problem bez odwoływania się do konkretnej technologii;
- znać użytkownika, jego sytuację i najważniejszą potrzebę;
- mieć zapisane wymagania oraz kryteria akceptacji;
- mieć określony zakres pierwszej wersji rozwiązania;
- mieć repozytorium i pierwszy działający fragment projektu.

## Od pomysłu do problemu

W Lab 1 zespół wybrał obszar i problem, który chce rozwiązać. Teraz trzeba sprawdzić, czy opis nie jest zbyt ogólny. Dobry opis problemu mówi, kto go doświadcza, w jakiej sytuacji się pojawia i jaki skutek powoduje. Nie zaczyna się od nazwy technologii ani od listy funkcji.

„Zbudować aplikację mobilną” jest zadaniem technicznym, a nie problemem. Problemem może być na przykład brak szybkiego sposobu sprawdzania dostępności zasobów albo trudność w porównywaniu wyników. Dopiero później można ustalić, czy najlepszym rozwiązaniem będzie aplikacja, strona internetowa, API, notebook czy inne narzędzie.

### Pytania pomocnicze

1. Kto dokładnie doświadcza problemu?
2. W jakiej sytuacji problem się pojawia?
3. Jak użytkownik radzi sobie obecnie?
4. Co jest obecnie czasochłonne, niejasne albo podatne na błąd?
5. Jaki rezultat będzie dla użytkownika użyteczny?
6. Po czym poznamy, że rozwiązanie rzeczywiście pomaga?

## Użytkownik i zakres pierwszej wersji

Opisać jednego głównego użytkownika oraz jedną najważniejszą sytuację użycia. Jeżeli rozwiązanie ma kilku odbiorców, pozostałe role zapisać jako drugorzędne. Pozwoli to ograniczyć zakres i zbudować pierwszą wersję wcześniej, zamiast próbować rozwiązać wszystkie problemy naraz.

Ustalić także, co wchodzi do pierwszej wersji, a co pozostaje poza zakresem. Poza zakresem nie znaczy „nigdy tego nie zrobimy”. Oznacza tylko, że zespół nie będzie tego realizował w pierwszym działającym przyroście.

## Wymagania i kryteria akceptacji

Wymaganie opisuje potrzebę lub zachowanie systemu. Zadanie opisuje pracę, którą trzeba wykonać. Kryterium akceptacji pozwala sprawdzić, czy wymaganie zostało spełnione.

Przykład:

- wymaganie: użytkownik może wyszukać zasób po nazwie;
- zadanie: dodać pole wyszukiwania i obsługę zapytania;
- kryterium akceptacji: dla istniejącej nazwy system pokazuje pasujące rekordy, a dla braku wyników wyświetla jasny komunikat.

Każde najważniejsze wymaganie zapisać tak, aby można było je później przetestować. Unikać sformułowań typu „system ma być nowoczesny” albo „interfejs ma być intuicyjny”, jeśli nie wiadomo, jak sprawdzić ich spełnienie.

## Narzędzia do pokazania

1. **GitHub Issues** - utworzyć zgłoszenie, opisać rezultat, dodać kryteria akceptacji, przypisać osobę i oznaczyć zadanie etykietą.
2. **GitHub Projects** - utworzyć prosty widok tablicy, dodać statusy i połączyć zadania z repozytorium.
3. **VS Code** - pokazać pracę z plikami Markdown, terminalem i strukturą repozytorium.
4. **diagrams.net lub Mermaid** - narysować prosty przepływ użytkownika od wejścia do wyniku.
5. **Środowisko wybrane przez zespół** - uruchomić minimalny projekt, notebook albo prototyp i pokazać pierwszy wynik.

Podczas pokazu pokazać nie tylko gdzie znajduje się funkcja, ale też kiedy warto jej użyć. Na przykład jedno wymaganie można najpierw zapisać w karcie projektu, następnie zamienić na Issue, a na końcu podzielić na zadania implementacyjne.

## Pierwszy działający fragment

Nie czekać z implementacją do końca semestru. Zbudować cienki przepływ obejmujący wejście, jedną istotną operację i widoczny wynik. Może to być formularz z przykładowymi danymi, komenda w terminalu, endpoint API, notebook albo prosty ekran aplikacji.

Pierwszy fragment nie musi obsługiwać wszystkich przypadków. Powinien jednak dać zespołowi odpowiedź, czy wybrane rozwiązanie jest wykonalne i czy prowadzi do rezultatu ważnego dla użytkownika.

## Zadania samodzielne

1. Sformułować problem w jednym zdaniu, bez opisywania technologii.
2. Opisać głównego użytkownika, jego sytuację oraz obecną trudność.
3. Zapisać 3-5 wymagań i 2-3 kryteria akceptacji.
4. Określić zakres pierwszej wersji oraz elementy pozostające poza zakresem.
5. Narysować jeden przepływ użytkownika od wejścia do wyniku.
6. Utworzyć co najmniej pięć zadań w backlogu, przypisać odpowiedzialność i dodać kryteria akceptacji.
7. Zbudować pierwszy cienki przepływ: przykładowe dane wejściowe, jedna operacja i widoczny wynik.

Każdy członek zespołu powinien mieć przypisane zadanie kończące się własnym, możliwym do pokazania rezultatem. Rezultatem może być na przykład fragment kodu, diagram, przygotowany zbiór danych, test, opis decyzji albo konfiguracja narzędzia.

## Rezultat do zapisania

- zaktualizowana karta projektu z opisem problemu, użytkownika i zakresem pierwszej wersji;
- backlog z wymaganiami, kryteriami akceptacji i przypisanymi osobami;
- diagram pierwszego przepływu użytkownika;
- działający pierwszy fragment systemu lub notebooka;
- commit opisujący wykonany krok.

## Zasady pracy zespołowej

Na koniec zajęć krótko sprawdzić, czy każdy członek zespołu wie, jaki rezultat ma dostarczyć i po czym będzie można uznać jego zadanie za wykonane. Jeżeli zadanie nie ma właściciela albo nie da się ocenić jego wyniku, doprecyzować je przed rozpoczęciem pracy.
