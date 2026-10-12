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

## Weryfikacja zgodności ze specjalnością

Przed zatwierdzeniem problemu należy sprawdzić, czy projekt wpisuje się w profil specjalności **Systemy informatyczne w zarządzaniu**. Nie oznacza to, że każdy projekt musi dotyczyć dużej firmy albo procesu biznesowego. Projekt może dotyczyć gospodarstwa domowego, uczelni, organizacji lub małego przedsiębiorstwa, jeżeli opisuje decyzję, zasoby, koszty albo proces, który ma zostać usprawniony przy użyciu danych i systemu informatycznego.

Problem można uznać za zgodny ze specjalnością, jeżeli:

- wskazano konkretną decyzję, proces lub zasób wymagający wsparcia;
- określono użytkownika podejmującego decyzję;
- wykorzystuje się dane do analizy, prognozy, porównania albo optymalizacji;
- system dostarcza wynik, który pomaga wybrać działanie;
- można zdefiniować mierzalne kryteria oceny rozwiązania.

Samo „zbudowanie aplikacji” albo „wyświetlanie danych” nie wystarcza. Należy wyjaśnić, jak wynik systemu wpłynie na decyzję użytkownika.

## Myślenie krytyczne i kreatywne

Nie rozpoczynać pracy od pytania „jaką aplikację zaprogramować?”. Najpierw należy sprawdzić, czy problem można rozwiązać prościej, taniej albo z wykorzystaniem urządzeń i danych, które już są dostępne. Dobre rozwiązanie może być aplikacją, notebookiem, dashboardem, arkuszem, automatyzacją, integracją kilku usług albo systemem wspomaganym przez agenta AI.

### Pytania, które należy zadać przed wyborem technologii

| Obszar | Pytania krytyczne | Możliwe kierunki rozwiązania |
|---|---|---|
| Dane | Jakie dane są rzeczywiście potrzebne? Kto je posiada? Jak często trzeba je zbierać? Jak sprawdzić ich jakość? | Dane publiczne, pomiary własne, eksport z istniejącego urządzenia, API, formularz lub mała próbka przygotowana ręcznie. |
| Urządzenia | Czy użytkownik ma już licznik energii, termostat, gniazdko smart, czujnik temperatury, telefon albo urządzenie działające w Home Assistant? Czy urządzenie udostępnia dane? | Wykorzystanie istniejącego sprzętu, odczyt pliku lub API, integracja przez MQTT/REST albo symulacja, jeżeli dostęp do sprzętu jest niemożliwy. |
| Koszt | Czy zakup nowego urządzenia jest konieczny? Jaki będzie koszt sprzętu, konfiguracji, utrzymania i wymiany? Czy tańszy wariant dostarczy wystarczających danych? | Porównanie rozwiązania bez dodatkowego sprzętu, z istniejącym urządzeniem i z nowym urządzeniem. |
| Optymalizacja | Co właściwie ma być minimalizowane: koszt energii, zużycie, emisja, czas, liczba zmian temperatury czy zużycie urządzenia? Jakie ograniczenia są ważniejsze od ceny? | Funkcja celu z ograniczeniami komfortu, budżetu, mocy, bezpieczeństwa i liczby przełączeń. |
| Sterowanie | Czy system tylko rekomenduje działanie, czy ma sterować piecem? Co stanie się przy błędzie danych, braku sieci albo nieprawidłowej komendzie? | W pierwszej wersji symulacja i rekomendacja; sterowanie rzeczywistym urządzeniem dopiero po określeniu zabezpieczeń i sposobu awaryjnego wyłączenia. |
| Skala | Czy potrzebny jest mocny komputer, serwer albo model AI? Czy wystarczy laptop, mały komputer, przeglądarka lub obliczenia wykonywane raz dziennie? | Porównanie obliczeń lokalnych, chmury, prostego modelu, reguł decyzyjnych i rozwiązania hybrydowego. |

W przypadku przykładu z ogrzewaniem należy zadać między innymi następujące pytania:

- Czy dane o temperaturze i zużyciu można pobrać z urządzeń, które użytkownik już posiada?
- Czy istnieje bezpieczny tryb odczytu bez wysyłania komend do pieca?
- Czy w MVP wystarczy symulować sterowanie i pokazać rekomendowany harmonogram?
- Czy zakup dodatkowego licznika lub komputera zmieni decyzję użytkownika na tyle, aby był uzasadniony?
- Czy optymalizacja dotyczy tylko rachunku, czy także komfortu, trwałości urządzenia i bezpieczeństwa?

Nie zakładać, że najbardziej rozbudowane rozwiązanie jest najlepsze. Należy porównać co najmniej trzy warianty, na przykład: **bez dodatkowego sprzętu**, **z wykorzystaniem istniejących urządzeń smart** oraz **z nowym elementem pomiarowym**. Następnie trzeba wskazać, który wariant zostaje w MVP i dlaczego.

## Wykorzystywanie agentów AI

Agent AI może wspierać analizę problemu, wyszukiwanie alternatyw, przygotowanie planu, tworzenie prototypu, pisanie testów i przegląd rozwiązania. Nie powinien jednak samodzielnie decydować, jakie dane są wiarygodne, czy sterowanie urządzeniem jest bezpieczne ani czy wynik eksperymentu potwierdza przyjętą tezę.

Pracę z agentem należy prowadzić w następujących krokach:

1. Opisać problem, użytkownika, ograniczenia i oczekiwany rezultat.
2. Poprosić agenta o co najmniej trzy różne warianty rozwiązania, w tym jeden prosty i jeden niewymagający zakupu sprzętu.
3. Poprosić o wskazanie założeń, ryzyk, kosztów i przypadków, w których każdy wariant zawiedzie.
4. Samodzielnie wybrać wariant i zapisać uzasadnienie w repozytorium.
5. Poprosić agenta o przygotowanie małego prototypu lub testu, ale sprawdzić kod, dane i wynik przed zaakceptowaniem zmiany.
6. Wykonać zmianę na branchu, uruchomić testy i poddać Pull Request przeglądowi drugiej osoby.

Przykładowe polecenie dla agenta:

> Rozważ problem planowania ogrzewania na 24 godziny. Zaproponuj trzy warianty: bez dodatkowego sprzętu, z istniejącym urządzeniem smart oraz z nowym licznikiem. Dla każdego określ dane, koszt, ryzyka, sposób weryfikacji i minimalny prototyp. Nie wybieraj rozwiązania za zespół.

W `docs/agent-log.md` należy zapisać datę, wykorzystane narzędzie, cel rozmowy, najważniejsze propozycje agenta, decyzję zespołu oraz sposób weryfikacji. Nie należy kopiować bezkrytycznie kodu ani umieszczać w rozmowie danych osobowych, haseł i kluczy dostępu.

## Przykład analizy problemu

Poniższy przykład jest anonimowym przykładem dydaktycznym. Zawiera wszystkie informacje potrzebne do wykonania ćwiczenia, dlatego nie wymaga dostępu do karty żadnego zespołu.

### Proponowany problem

Rozważany przykład dotyczy narzędzia, które na podstawie godzinowych cen energii, temperatury zewnętrznej i modelu cieplnego budynku wyznacza plan ogrzewania na najbliższą dobę. Plan ma ograniczać koszt energii bez pogorszenia uzgodnionego pasma komfortu. Użytkownik ma móc porównać plan z klasycznym termostatem i zobaczyć koszt oraz oszczędność.

### Ocena zgodności ze specjalnością

Problem dobrze wpisuje się w specjalność **Systemy informatyczne w zarządzaniu**, ponieważ:

- dotyczy zarządzania kosztem energii i zasobem, jakim jest dostępna moc ogrzewania;
- wskazuje użytkownika podejmującego decyzję o harmonogramie ogrzewania;
- wykorzystuje dane, modelowanie i optymalizację;
- prowadzi do konkretnej decyzji: kiedy ogrzewać, a kiedy ograniczyć pracę urządzenia;
- pozwala mierzyć koszt, komfort i różnicę względem przyjętej metody bazowej;
- może zakończyć się systemem wspomagania decyzji z modułem analitycznym, API i interfejsem.

To jest dobry kierunek. Należy jednak wyraźnie zaznaczyć, że w ramach przedmiotu powstaje system wspomagania decyzji dla budynku referencyjnego, a nie uniwersalny sterownik ogrzewania dla wszystkich domów.

### Przykłady elementów sformułowanych poprawnie

Poniższe przykłady pokazują, jakie informacje warto uznać za wystarczająco konkretne:

- **Użytkownik:** „Właściciel lub najemca budynku z ogrzewaniem elektrycznym, który planuje ogrzewanie na kolejną dobę”. Wskazano osobę, sytuację i moment użycia.
- **Decyzja:** „Użytkownik wybiera godziny pracy ogrzewania przy zadanej temperaturze minimalnej i maksymalnej”. Wiadomo, jaką decyzję wspiera system.
- **Dane:** „Powtarzalny scenariusz 24-godzinny zawiera cenę energii, temperaturę zewnętrzną, parametry budynku i moc ogrzewania”. Można przygotować dane testowe i odtworzyć eksperyment.
- **Rezultat:** „System pokazuje plan godzinowy, koszt, liczbę godzin poza komfortem i porównanie z termostatem”. Rezultat można zademonstrować i zmierzyć.
- **Wkład osoby:** „Przygotować adapter danych, który tworzy poprawny plik CSV z 24 wierszami i wymaganymi kolumnami”. Zadanie kończy się konkretnym artefaktem.

### Przykłady elementów wymagających poprawy

| Sformułowanie wymagające poprawy | Dlaczego jest niewystarczające | Jak poprawić |
|---|---|---|
| „Zbudować inteligentną aplikację do optymalizacji ogrzewania” | Nie wiadomo, kto korzysta z aplikacji, jaką decyzję podejmuje i jaki wynik otrzymuje. | Wskazać użytkownika, decyzję, dane oraz rezultat, na przykład plan ogrzewania na 24 godziny i koszt planu. |
| „Wykorzystać dane PSE i Open-Meteo” | Nie wiadomo, czy dane są dostępne przed podjęciem decyzji, jaki mają format i na jakiej licencji można ich użyć. | Najpierw przygotować powtarzalny scenariusz offline, a następnie opisać źródło, licencję, moment pobrania i sposób mapowania pól. |
| „System ma oszczędzać energię i utrzymywać komfort” | Brak metody bazowej, scenariuszy i sposobu pomiaru. | Określić, z czym porównuje się plan, jak liczony jest koszt i ile godzin poniżej temperatury minimalnej jest dopuszczalne. |
| „Zrobić model, API, aplikację React, trzy metody i analizę wrażliwości” | Lista technologii i rozszerzeń może przesłonić główny problem oraz przekroczyć możliwości czasowe zespołu. | Ustalić MVP: jedna doba, dane przykładowe, dwie metody i jeden ekran wyniku; resztę oznaczyć jako rozszerzenie. |
| „Użyć parametrów z cudzej pracy inżynierskiej” | Nie ma informacji o źródle, zakresie legalnego wykorzystania ani zgodności parametrów z analizowanym przypadkiem. | Podać pełne źródło, opisać pochodzenie parametrów i sprawdzić, czy można je wykorzystać w projekcie. |

### Jak poprawić opis krok po kroku?

1. Zastąpić nazwę technologii opisem decyzji, którą system ma wspierać.
2. Wskazać jednego głównego użytkownika i jedną sytuację użycia.
3. Przygotować najmniejszy zestaw danych pozwalający wykonać demonstrację offline.
4. Zdefiniować jeden główny rezultat oraz metodę bazową do porównania.
5. Zapisać warunki sukcesu w sposób możliwy do sprawdzenia testem lub eksperymentem.
6. Przenieść dodatkowe źródła danych, metody i funkcje do listy rozszerzeń.

### Przykład poprawionej specyfikacji

| Pole | Wersja doprecyzowana |
|---|---|
| Nazwa robocza | System wspomagania decyzji o harmonogramie ogrzewania elektrycznego przy godzinowych cenach energii |
| Problem | Właściciel budynku referencyjnego nie wie, w których godzinach uruchamiać ogrzewanie, aby ograniczyć koszt energii i zachować ustalone pasmo komfortu. Należy porównać rekomendowany plan z klasycznym termostatem. |
| Użytkownik | Właściciel lub najemca budynku z ogrzewaniem elektrycznym, który podejmuje decyzję o planie ogrzewania na kolejną dobę. |
| Decyzja wspierana przez system | Wybór godzin pracy ogrzewania przy zadanej temperaturze minimalnej i maksymalnej. |
| Dane MVP | Syntetyczny, powtarzalny scenariusz 24-godzinny: cena energii, temperatura zewnętrzna, parametry budynku i moc ogrzewania. |
| Rezultat MVP | Plan godzinowy, przewidywany koszt, liczba godzin poza komfortem oraz porównanie z termostatem. |
| Poza zakresem | Sterowanie rzeczywistym urządzeniem, logowanie, wiele budynków, prognozowanie pogody i pełna automatyczna integracja z dostawcą energii. |
| Kryterium sukcesu | Dla co najmniej trzech ustalonych scenariuszy system wyznacza plan, który nie narusza warunku komfortu, a koszt i różnica względem termostatu są policzone oraz przedstawione w sposób możliwy do sprawdzenia. |

Tak sformułowany problem pokazuje związek między danymi, metodą, systemem informatycznym i decyzją użytkownika. Rozszerzenie o dane publiczne, dodatkową metodę lub analizę wrażliwości można zapisać jako zadania opcjonalne, ale nie powinno ono zagrażać ukończeniu MVP.

## Zadanie analizy przykładowej karty

1. Przeczytać opis przykładowego problemu i zaznaczyć elementy dotyczące użytkownika, decyzji, danych, metody i rezultatu.
2. Wskazać trzy elementy, które świadczą o zgodności ze specjalnością Systemy informatyczne w zarządzaniu.
3. Wskazać co najmniej trzy ryzyka albo niejasności, które mogą utrudnić wykonanie MVP.
4. Przepisać opis problemu w jednym zdaniu, uwzględniając użytkownika, decyzję i mierzalny rezultat.
5. Podzielić zakres na trzy grupy: **MVP**, **rozszerzenie** i **poza zakresem**.
6. Zaproponować co najmniej trzy kryteria akceptacji, które można sprawdzić na danych testowych.
7. Zapisać wynik analizy w `docs/problem.md`, utworzyć Issue przypisane do osoby wykonującej zadanie i dodać link do `docs/evidence.md`.

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

## Przydatne narzędzia

Zrzuty demonstracyjne i opis pełnego przepływu znajdują się w [przewodniku po narzędziach](../narzedzia/README.md#zrzuty-demonstracyjne). Podczas zajęć należy pokazać narzędzie, wykonać przykład na repozytorium prowadzącego, a następnie pozostawić studentom czas na wykonanie analogicznego zadania.

1. **GitHub Issues** - utworzyć zgłoszenie, opisać rezultat, dodać kryteria akceptacji, przypisać osobę i oznaczyć zadanie etykietą.
2. **GitHub Projects** - utworzyć prosty widok tablicy, dodać statusy i połączyć zadania z repozytorium.
3. **VS Code** - pokazać pracę z plikami Markdown, terminalem i strukturą repozytorium.
4. **diagrams.net lub Mermaid** - narysować prosty przepływ użytkownika od wejścia do wyniku.
5. **Środowisko wybrane przez zespół** - uruchomić minimalny projekt, notebook albo prototyp i pokazać pierwszy wynik.
6. **Agent AI** - wygenerować warianty rozwiązania, poprosić o krytykę założeń i przygotować mały prototyp lub test; decyzję oraz wynik weryfikacji zapisać w repozytorium.

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
8. W repozytorium utworzyć `docs/problem.md` oraz `docs/user-flow.md`, a następnie podlinkować je w `README.md`.
9. Utworzyć Issue dla każdego wymagania i dodać do niego kryterium akceptacji.
10. Umieścić linki do Issue, brancha, Pull Requesta i commita w `docs/evidence.md`.
11. Zaproponować trzy warianty rozwiązania problemu, w tym wariant niewymagający zakupu sprzętu, i porównać je pod względem kosztu, danych, ryzyka oraz wartości dla użytkownika.
12. Wykorzystać agenta AI do zakwestionowania założeń projektu, a następnie zapisać wnioski i sposób weryfikacji w `docs/agent-log.md`.
13. Określić, czy dane można pozyskać z istniejących urządzeń lub usług. Jeżeli nie, przygotować uzasadnienie użycia danych syntetycznych albo zakupu nowego sprzętu.

Każdy członek zespołu powinien mieć przypisane zadanie kończące się własnym, możliwym do pokazania rezultatem. Rezultatem może być na przykład fragment kodu, diagram, przygotowany zbiór danych, test, opis decyzji albo konfiguracja narzędzia.

## Rezultat do zapisania

- zaktualizowana karta projektu z opisem problemu, użytkownika i zakresem pierwszej wersji;
- backlog z wymaganiami, kryteriami akceptacji i przypisanymi osobami;
- diagram pierwszego przepływu użytkownika;
- działający pierwszy fragment systemu lub notebooka;
- commit opisujący wykonany krok.

## Zasady pracy zespołowej

Na koniec zajęć krótko sprawdzić, czy każdy członek zespołu wie, jaki rezultat ma dostarczyć i po czym będzie można uznać jego zadanie za wykonane. Jeżeli zadanie nie ma właściciela albo nie da się ocenić jego wyniku, doprecyzować je przed rozpoczęciem pracy.
