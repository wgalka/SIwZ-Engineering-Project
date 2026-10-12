# Laboratorium 2: Doprecyzowanie problemu, danych i wymagań

**Specjalność: Analiza danych społeczno-gospodarczych**

## Cel zajęć

Na tych zajęciach należy przejść od ogólnego pomysłu z Lab 1 do konkretnej specyfikacji pierwszej wersji rozwiązania. Zespół powinien opisać zjawisko lub problem językiem użytkownika, określić jednostkę analizy, dobrać wstępne źródła danych, zapisać pytania badawcze i wymagania oraz rozpocząć budowanie małego, działającego fragmentu rozwiązania.

Po zajęciach każdy zespół powinien:

- umieć opisać problem bez rozpoczynania od nazwy technologii;
- znać użytkownika, interesariuszy, zjawisko i decyzję, którą ma wspierać rozwiązanie;
- mieć określoną populację, jednostkę analizy, zakres czasu i przestrzeni;
- mieć wstępnie ocenione źródła danych, ich jakość, dostępność i ograniczenia;
- mieć zapisane pytania badawcze, wymagania oraz kryteria akceptacji;
- mieć określony zakres pierwszej wersji rozwiązania;
- mieć repozytorium i pierwszy działający fragment analizy, modelu albo interfejsu.

## Od pomysłu do problemu badawczo-projektowego

W Lab 1 zespół wybrał obszar i problem, który chce rozwiązać. Teraz należy sprawdzić, czy opis nie jest zbyt ogólny. Dobry opis problemu wskazuje, jakie zjawisko jest analizowane, kogo dotyczy, w jakiej sytuacji występuje oraz jaka decyzja lub działanie może zostać wsparte wynikiem analizy. Nie należy zaczynać od nazwy algorytmu, języka programowania ani listy ekranów.

„Zbudować dashboard danych społecznych” jest zadaniem technicznym, a nie problemem. Problemem może być na przykład trudność w porównaniu dostępności usług publicznych między gminami albo brak wiarygodnego sposobu wskazania obszarów wymagających dalszej analizy. Dopiero później można ustalić, czy najlepszym rozwiązaniem będzie raport, dashboard, mapa, notebook, model prognostyczny, API czy inne narzędzie.

### Pytania pomocnicze

1. Jakie zjawisko społeczne lub gospodarcze jest analizowane?
2. Kogo dotyczy zjawisko i kto będzie korzystał z wyniku?
3. Jaka jest jednostka analizy: osoba, gospodarstwo domowe, przedsiębiorstwo, gmina, powiat, województwo, miesiąc czy rok?
4. Jaka decyzja lub działanie może zostać wsparte wynikiem?
5. Jak obecnie przygotowuje się taką informację?
6. Jakie dane są rzeczywiście potrzebne i skąd można je pozyskać?
7. Po czym można poznać, że analiza jest użyteczna i powtarzalna?

## Weryfikacja zgodności ze specjalnością

Przed zatwierdzeniem problemu należy sprawdzić, czy projekt wpisuje się w profil specjalności **Analiza danych społeczno-gospodarczych**. Projekt może dotyczyć rynku pracy, edukacji, zdrowia publicznego, demografii, przedsiębiorczości, transportu, mieszkalnictwa, ubóstwa, usług publicznych, konsumpcji lub innego obszaru, jeżeli analizuje rzeczywiste zjawisko przy użyciu odpowiednich danych.

Problem można uznać za zgodny ze specjalnością, jeżeli:

- wskazano konkretne zjawisko społeczne lub gospodarcze oraz grupę, obszar albo organizację, których ono dotyczy;
- określono jednostkę analizy, zakres czasu i zakres przestrzenny;
- sformułowano pytanie badawcze albo decyzję, którą ma wspierać wynik;
- wskazano mierzalne zmienne lub wskaźniki oraz ich źródła;
- dobrano metodę odpowiednią do pytania, danych i dostępnego czasu;
- można ocenić jakość, kompletność, porównywalność i możliwe obciążenia danych;
- określono mierzalne kryteria oceny wyniku oraz ograniczenia interpretacji.

Samo „zbudowanie dashboardu”, „zastosowanie sztucznej inteligencji” albo „wyświetlanie danych GUS” nie wystarcza. Należy wyjaśnić, jakie pytanie zostanie dzięki temu rozstrzygnięte, dla kogo wynik będzie użyteczny i jakie decyzje można podejmować na jego podstawie. Nie należy utożsamiać korelacji z przyczynowością ani przedstawiać rankingu jako obiektywnej oceny osób lub obszarów bez omówienia przyjętych wskaźników.

## Myślenie krytyczne i kreatywne

Nie należy rozpoczynać pracy od pytania „jaki model albo dashboard zbudować?”. Najpierw trzeba sprawdzić, czy problem można rozwiązać prościej, taniej i w sposób bardziej wiarygodny. W wielu projektach wystarczy dobrze opisany zbiór danych, powtarzalny notebook, raport, mapa albo prosty model bazowy. Mocny komputer, płatna usługa lub skomplikowany model nie są celem samym w sobie.

### Pytania, które należy zadać przed wyborem metody i technologii

| Obszar | Pytania krytyczne | Możliwe kierunki rozwiązania |
|---|---|---|
| Pytanie badawcze | Czy chcemy opisać zjawisko, porównać obszary, prognozować wartość, wykryć anomalię czy wyjaśnić zależność? | Statystyki opisowe, porównanie wskaźników, prognoza, klasyfikacja, grupowanie albo analiza przestrzenna. |
| Jednostka analizy | Czy porównujemy osoby, gospodarstwa, przedsiębiorstwa, gminy, powiaty czy okresy? Czy jednostki są porównywalne? | Normalizacja na mieszkańca, pracownika lub przedsiębiorstwo; podział na grupy; jawne określenie poziomu agregacji. |
| Dane | Jakie dane są rzeczywiście potrzebne? Kto je posiada? Jak często są aktualizowane? Czy można odtworzyć pobranie danych? | GUS/BDL, Eurostat, dane.gov.pl, dane samorządowe, otwarte API, eksport instytucjonalny, ankieta albo dane syntetyczne. |
| Jakość | Ile jest braków? Czy zmieniała się definicja wskaźnika? Czy dane są obciążone doborem próby albo zmianą metodologii? | Profil jakości, tabela braków, dokumentacja metadanych, analiza wrażliwości i porównanie z drugim źródłem. |
| Koszt i sprzęt | Czy potrzebny jest mocny komputer, GPU, chmura lub płatne API? Czy obliczenia można wykonać na laptopie? | Notebook, skrypt uruchamiany okresowo, model bazowy, obliczenia lokalne albo mały serwis zamiast rozbudowanej infrastruktury. |
| Metoda | Czy bardziej złożony model wnosi wartość względem średniej, trendu, regresji lub prostego rankingu? | Najpierw baseline, następnie jedna metoda porównawcza i dopiero później rozszerzenia. |
| Interpretacja | Czy wynik opisuje współwystępowanie, czy pozwala wnioskować o przyczynie? Jakie czynniki mogą zniekształcać wynik? | Ostrożny język, przedziały niepewności, kontrola zmiennych, analiza ograniczeń i unikanie nieuzasadnionych wniosków przyczynowych. |
| Prywatność i etyka | Czy dane mogą ujawniać informacje o osobach lub małych grupach? Czy wynik może prowadzić do stygmatyzacji? | Agregacja, anonimizacja, minimalizacja danych, ograniczenie dostępu i opis ryzyka niewłaściwej interpretacji. |
| Rezultat | Czy użytkownik otrzymuje informację, na podstawie której może wykonać konkretne działanie? | Raport, mapa, ranking, prognoza z przedziałem, alert, rekomendacja albo narzędzie wspomagania decyzji. |

Przed zebraniem własnej ankiety należy sprawdzić, czy potrzebne informacje nie są już dostępne w publicznym rejestrze, raporcie, API albo systemie instytucji. Jeżeli ankieta jest konieczna, należy uzasadnić dobór próby, określić sposób ograniczenia stronniczości i nie zbierać danych osobowych, które nie są potrzebne do realizacji celu. Jeżeli wystarczą dane zagregowane, nie należy pozyskiwać danych jednostkowych.

Nie należy zakładać, że najbardziej rozbudowany model da najlepszy rezultat. Trzeba porównać co najmniej trzy warianty, na przykład: **analizę publicznych danych gotowych do użycia**, **wykorzystanie istniejącego eksportu lub rejestru instytucji** oraz **samodzielne zebranie danych w ankiecie albo pomiarze**. Następnie należy wskazać, który wariant zostaje w MVP i dlaczego.

## Wykorzystywanie agentów AI

Agent AI może wspierać analizę problemu, wyszukiwanie słów kluczowych, przygotowanie wariantów pytań, planowanie eksperymentu, tworzenie prototypu, pisanie testów i przegląd rozwiązania. Nie powinien jednak samodzielnie potwierdzać prawdziwości źródeł, jakości danych, poprawności wniosków ani zgodności projektu z zasadami ochrony prywatności.

Pracę z agentem należy prowadzić w następujących krokach:

1. Opisać zjawisko, użytkownika, jednostkę analizy, zakres danych, ograniczenia i oczekiwany rezultat.
2. Poprosić agenta o co najmniej trzy warianty rozwiązania, w tym wariant oparty na prostym modelu bazowym i wariant niewymagający zakupu sprzętu ani płatnej usługi.
3. Poprosić o wskazanie założeń, możliwych obciążeń, braków danych, kosztów i sytuacji, w których każdy wariant zawiedzie.
4. Samodzielnie sprawdzić oryginalne źródła, definicje wskaźników, licencje i daty aktualizacji.
5. Wybrać wariant oraz zapisać uzasadnienie, a następnie poprosić agenta o przygotowanie małego prototypu lub testu.
6. Sprawdzić kod, dane i wynik, wykonać zmianę na branchu, uruchomić testy i poddać Pull Request przeglądowi drugiej osoby.

Przykładowe polecenie dla agenta:

> Rozważ analizę różnic w dostępie do usług publicznych między powiatami. Zaproponuj trzy warianty: opisowy ranking oparty na publicznych danych, prosty model prognostyczny oraz wariant wykorzystujący dane z ankiety. Dla każdego określ jednostkę analizy, źródła danych, koszty, ryzyka obciążenia, sposób walidacji i minimalny prototyp. Nie zakładaj przyczynowości i nie wybieraj rozwiązania za zespół.

W `docs/agent-log.md` należy zapisać datę, wykorzystane narzędzie, cel rozmowy, najważniejsze propozycje agenta, sprawdzone źródła, decyzję zespołu oraz sposób weryfikacji. Nie należy kopiować bezkrytycznie kodu ani umieszczać w rozmowie danych osobowych, poufnych danych instytucji, haseł i kluczy dostępu.

## Przykład analizy problemu

Poniższy przykład jest anonimowym przykładem dydaktycznym. Zawiera wszystkie informacje potrzebne do wykonania ćwiczenia, dlatego nie wymaga dostępu do karty żadnego zespołu.

### Proponowany problem

Rozważany przykład dotyczy narzędzia wspomagającego wskazanie powiatów, w których warto przeanalizować dostęp do usług aktywizacji zawodowej. Narzędzie wykorzystuje publiczne dane o bezrobociu, liczbie ofert pracy, strukturze ludności i dostępności usług. Ma umożliwiać porównanie powiatów w kilku latach, pokazanie zmian wskaźników oraz przygotowanie listy obszarów wymagających dalszej analizy. Wynik nie ma samodzielnie rozstrzygać, że dany powiat jest „gorszy”, ani dowodzić, że jedna obserwowana zmienna powoduje inną.

### Ocena zgodności ze specjalnością

Problem dobrze wpisuje się w specjalność **Analiza danych społeczno-gospodarczych**, ponieważ:

- dotyczy rynku pracy i dostępu do usług publicznych;
- wskazuje jednostkę analizy — powiat — oraz możliwość porównania jej w czasie;
- wykorzystuje mierzalne wskaźniki pochodzące z publicznych źródeł;
- prowadzi do konkretnego rezultatu: wskazania obszarów wymagających dalszego rozpoznania;
- wymaga oceny braków, porównywalności, skali i jakości danych;
- pozwala porównać prosty wskaźnik bazowy z inną metodą oraz omówić ograniczenia interpretacji.

To jest dobry kierunek. Należy jednak wyraźnie zaznaczyć, że wynik jest narzędziem do wstępnego ustalania priorytetów analitycznych, a nie automatyczną decyzją o przyznaniu środków ani oceną mieszkańców powiatu.

### Przykłady elementów sformułowanych poprawnie

Poniższe przykłady pokazują, jakie informacje warto uznać za wystarczająco konkretne:

- **Zjawisko i użytkownik:** „Jednostka samorządowa porównuje dostęp do usług aktywizacji zawodowej w powiatach”. Wskazano obszar i odbiorcę wyniku.
- **Jednostka analizy:** „Podstawową jednostką jest powiat, a obserwacje obejmują lata 2019–2025”. Można określić zakres i porównywalność danych.
- **Dane:** „Dla każdego powiatu zapisuje się stopę bezrobocia, liczbę ofert pracy na 1000 mieszkańców, liczbę osób bezrobotnych oraz liczbę punktów obsługi”. Można sprawdzić definicje i przygotować tabelę danych.
- **Rezultat:** „Raport pokazuje wartości wskaźników, zmianę rok do roku, ranking według jawnej reguły i ostrzeżenia o brakach danych”. Wynik można zademonstrować i zweryfikować.
- **Wkład osoby:** „Przygotować skrypt, który pobiera jeden wskazany zestaw danych, zapisuje źródło i datę pobrania oraz zgłasza brakujące powiaty”. Zadanie kończy się konkretnym artefaktem.

### Przykłady elementów wymagających poprawy

| Sformułowanie wymagające poprawy | Dlaczego jest niewystarczające | Jak poprawić |
|---|---|---|
| „Zrobić dashboard społeczeństwa” | Nie wiadomo, jakie zjawisko, dla kogo i w jakiej decyzji ma znaczenie. | Wskazać zjawisko, jednostkę analizy, użytkownika i rezultat, na przykład porównanie dostępu do usług między powiatami. |
| „Wykorzystać dane GUS” | GUS udostępnia wiele zbiorów o różnych definicjach, zakresach i częstotliwości. | Podać konkretną tabelę lub API, zmienne, lata, jednostkę, licencję i sposób zapisania metadanych. |
| „Znaleźć przyczyny bezrobocia” | Sam opis korelacji nie dowodzi przyczynowości, a zakres problemu jest zbyt szeroki. | Ograniczyć pytanie do związku między wybranymi zmiennymi albo zaprojektować metodę, która uzasadnia ostrożny wniosek przyczynowy. |
| „Wytrenować model AI przewidujący ubóstwo” | Brak jednostki, zmiennej celu, danych, metody bazowej i kryterium oceny. | Określić populację, zmienną celu, horyzont prognozy, baseline, metryki i ograniczenia etyczne. |
| „Przeprowadzić ankietę wśród studentów i wnioskować o całym społeczeństwie” | Próba może nie reprezentować badanej populacji. | Ograniczyć wniosek do badanej grupy albo uzasadnić dobór próby i wskazać ograniczenia generalizacji. |
| „Stworzyć ranking najgorszych gmin” | Etykieta może stygmatyzować, a wynik zależy od arbitralnie wybranych wskaźników. | Nazwać wynik neutralnie, ujawnić regułę agregacji, pokazać niepewność i opisać, że ranking służy do dalszej analizy. |

### Jak poprawić opis krok po kroku?

1. Zastąpić ogólną nazwę dashboardu opisem zjawiska, użytkownika i decyzji.
2. Określić jednostkę analizy, populację, okres i obszar.
3. Przygotować najmniejszy zestaw danych pozwalający wykonać powtarzalną demonstrację offline.
4. Sprawdzić definicje zmiennych, braki, zmianę metodologii, licencję i datę pobrania.
5. Zdefiniować metodę bazową, główny rezultat i sposób oceny wyniku.
6. Zapisać ograniczenia interpretacji, w szczególności ryzyko błędnej generalizacji i utożsamiania korelacji z przyczynowością.
7. Przenieść dodatkowe źródła danych, metody i funkcje do listy rozszerzeń.

### Przykład poprawionej specyfikacji

| Pole | Wersja doprecyzowana |
|---|---|
| Nazwa robocza | Analiza zmian dostępu do usług aktywizacji zawodowej w powiatach |
| Problem | Osoba planująca działania publiczne potrzebuje porównać powiaty pod względem wybranych wskaźników rynku pracy i dostępu do usług. Aktualne zestawienia nie pokazują jednocześnie zmian w czasie, braków danych i różnic między wskaźnikami. |
| Użytkownik | Pracownik jednostki publicznej lub organizacji analizującej potrzeby lokalnych usług rynku pracy. |
| Pytanie analityczne | Które powiaty wymagają dalszego rozpoznania ze względu na niekorzystny poziom lub trend wybranych wskaźników? |
| Jednostka i zakres | Powiat, lata 2019–2025, dane roczne; w MVP analizowane są trzy wybrane wskaźniki. |
| Dane MVP | Publiczne dane o stopie bezrobocia, ofertach pracy i liczbie osób bezrobotnych, wraz z metadanymi, datą pobrania i informacją o brakach. |
| Rezultat MVP | Powtarzalna tabela lub dashboard pokazujący wskaźniki, zmianę w czasie, jawny wynik metody bazowej i ostrzeżenia o ograniczeniach. |
| Poza zakresem | Automatyczne decyzje o przyznaniu środków, dane osobowe, ustalanie przyczyn bezrobocia na podstawie samej korelacji, prognoza dla wszystkich regionów i integracja z systemem urzędu. |
| Kryterium sukcesu | Dla ustalonego zestawu powiatów i lat system odtwarza wynik z pliku źródłowego, pokazuje definicje wskaźników, oznacza braki danych oraz umożliwia sprawdzenie reguły porównania z metodą bazową. |

Tak sformułowany problem pokazuje związek między zjawiskiem społeczno-gospodarczym, danymi, metodą, systemem informatycznym i użytkownikiem wyniku. Rozszerzenie o dane miesięczne, dodatkową metodę, mapę lub analizę wrażliwości można zapisać jako zadanie opcjonalne, ale nie powinno ono zagrażać ukończeniu MVP.

## Zadanie analizy przykładowej karty

1. Przeczytać opis przykładowego problemu i zaznaczyć elementy dotyczące zjawiska, użytkownika, jednostki analizy, danych, metody i rezultatu.
2. Wskazać trzy elementy, które świadczą o zgodności ze specjalnością Analiza danych społeczno-gospodarczych.
3. Wskazać co najmniej trzy ryzyka albo niejasności dotyczące jakości danych, reprezentatywności, prywatności lub interpretacji.
4. Przepisać pytanie analityczne w jednym zdaniu, uwzględniając jednostkę analizy, zakres czasu i mierzalny rezultat.
5. Podzielić zakres na trzy grupy: **MVP**, **rozszerzenie** i **poza zakresem**.
6. Zaproponować co najmniej trzy kryteria akceptacji, które można sprawdzić na danych testowych.
7. Zapisać wynik analizy w `docs/problem.md`, utworzyć Issue przypisane do osoby wykonującej zadanie i dodać link do `docs/evidence.md`.

## Użytkownik, populacja i zakres pierwszej wersji

Należy opisać jednego głównego użytkownika oraz jedną najważniejszą sytuację użycia. Jeżeli rozwiązanie ma kilku odbiorców, pozostałe role należy zapisać jako drugorzędne. Należy także określić, czy wniosek dotyczy całej populacji, określonej próby, grupy jednostek czy wyłącznie analizowanego zbioru.

Ustalić także, co wchodzi do pierwszej wersji, a co pozostaje poza zakresem. Poza zakresem nie znaczy „nigdy tego nie zrobimy”. Oznacza tylko, że zespół nie będzie tego realizował w pierwszym działającym przyroście.

## Dane, wymagania i kryteria akceptacji

Wymaganie opisuje potrzebę lub zachowanie rozwiązania. Zadanie opisuje pracę, którą trzeba wykonać. Kryterium akceptacji pozwala sprawdzić, czy wymaganie zostało spełnione.

Przykład:

- wymaganie: użytkownik może wyświetlić wartość wskaźnika dla wybranego powiatu i roku;
- zadanie: przygotować tabelę danych, filtr oraz widok wyniku;
- kryterium akceptacji: dla wskazanego powiatu i roku system pokazuje wartość ze źródłowego pliku, jednostkę, definicję wskaźnika i informację o braku danych, jeżeli wartość jest niedostępna.

Każde najważniejsze wymaganie należy zapisać tak, aby można było je później przetestować. Należy unikać sformułowań typu „analiza ma być profesjonalna”, „model ma być inteligentny” albo „dane mają być dobre”, jeżeli nie wiadomo, jak sprawdzić ich spełnienie.

## Przydatne narzędzia

Zrzuty demonstracyjne i opis pełnego przepływu znajdują się w [przewodniku po narzędziach](../../narzedzia/README.md#zrzuty-demonstracyjne). Podczas zajęć należy pokazać narzędzie, wykonać przykład na repozytorium prowadzącego, a następnie pozostawić studentom czas na wykonanie analogicznego zadania.

1. **GitHub Issues** — utworzyć zgłoszenie, opisać pytanie analityczne, kryteria akceptacji, przypisać osobę i dodać etykietę.
2. **GitHub Projects** — utworzyć prosty widok tablicy, dodać statusy i połączyć zadania z repozytorium.
3. **VS Code** — pokazać pracę z plikami Markdown, notebookiem, terminalem i strukturą repozytorium.
4. **Jupyter, Google Colab lub Kaggle** — przygotować małą tabelę, wykonać kontrolę braków i pokazać jeden wynik analizy.
5. **GUS/BDL, Eurostat, dane.gov.pl lub API instytucji** — pokazać, jak sprawdzić definicję wskaźnika, metadane, zakres dat i sposób pobrania danych.
6. **diagrams.net lub Mermaid** — narysować przepływ od źródła danych przez przygotowanie i analizę do wyniku dla użytkownika.
7. **Agent AI** — wygenerować warianty pytań i metod, poprosić o krytykę założeń oraz przygotować mały prototyp lub test; decyzję i wynik weryfikacji zapisać w repozytorium.

Podczas pokazu należy przedstawić nie tylko miejsce, w którym znajduje się funkcja, lecz także moment, w którym warto jej użyć. Na przykład pytanie analityczne można najpierw zapisać w karcie projektu, następnie zamienić na Issue, powiązać ze źródłem danych, wykonać w notebooku i poddać przeglądowi w Pull Requeście.

## Pierwszy działający fragment

Nie należy czekać z analizą do końca semestru. Należy zbudować cienki przepływ obejmujący źródło lub mały plik danych, jedną kontrolę jakości, jedną istotną operację oraz widoczny wynik. Może to być tabela wskaźników, wykres trendu, mapa, notebook, komenda w terminalu, endpoint API albo prosty ekran aplikacji.

Pierwszy fragment nie musi obsługiwać wszystkich przypadków. Powinien jednak dać zespołowi odpowiedź, czy dane są dostępne, czy wybrana metoda jest wykonalna i czy rezultat odpowiada na pytanie użytkownika.

## Zadania samodzielne

1. Sformułować problem w jednym zdaniu, bez opisywania technologii.
2. Opisać głównego użytkownika, analizowane zjawisko, jednostkę analizy, populację oraz zakres czasu i przestrzeni.
3. Zapisać pytanie analityczne, 3–5 wymagań i 2–3 kryteria akceptacji.
4. Określić zakres pierwszej wersji oraz elementy pozostające poza zakresem.
5. Przygotować tabelę źródeł danych zawierającą właściciela, zakres, definicje, licencję, datę pobrania, braki i ryzyka.
6. Porównać trzy warianty pozyskania danych: publiczne dane gotowe, istniejący eksport lub rejestr oraz samodzielną ankietę albo pomiar.
7. Wskazać metodę bazową i uzasadnić, dlaczego bardziej złożony model jest albo nie jest potrzebny.
8. Przygotować pierwszy cienki przepływ: dane wejściowe, jedna kontrola jakości, jedna operacja i widoczny wynik.
9. W repozytorium utworzyć `docs/problem.md`, `docs/data-sources.md` oraz `docs/user-flow.md`, a następnie podlinkować je w `README.md`.
10. Utworzyć Issue dla każdego wymagania i dodać do niego kryterium akceptacji.
11. Umieścić linki do Issue, brancha, Pull Requesta i commita w `docs/evidence.md`.
12. Wykorzystać agenta AI do zakwestionowania założeń projektu, a następnie zapisać propozycje, decyzję zespołu, sprawdzone źródła i sposób weryfikacji w `docs/agent-log.md`.
13. Określić, czy dane można pozyskać z istniejących publicznych źródeł lub usług. Jeżeli nie, przygotować uzasadnienie użycia danych syntetycznych albo zebrania własnych danych.

Każdy członek zespołu powinien mieć przypisane zadanie kończące się własnym, możliwym do pokazania rezultatem. Rezultatem może być na przykład przygotowany zbiór danych, opis metadanych, kontrola jakości, wykres, model bazowy, diagram, test, opis decyzji albo konfiguracja narzędzia.

## Rezultat do zapisania

- zaktualizowana karta projektu z opisem zjawiska, użytkownika, pytania i zakresu pierwszej wersji;
- opis jednostki analizy oraz źródeł danych z ograniczeniami;
- backlog z wymaganiami, kryteriami akceptacji i przypisanymi osobami;
- diagram przepływu danych od źródła do wyniku;
- działający pierwszy fragment analizy, modelu albo notebooka;
- commit opisujący wykonany krok.

## Zasady pracy zespołowej

Na koniec zajęć należy krótko sprawdzić, czy każdy członek zespołu zna swój rezultat, źródła danych, sposób weryfikacji oraz ograniczenia interpretacji. Jeżeli zadanie nie ma właściciela albo nie da się ocenić jego wyniku, trzeba je doprecyzować przed rozpoczęciem pracy.
