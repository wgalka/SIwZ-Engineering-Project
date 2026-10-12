# Laboratorium 2: Analiza problemu i pozyskiwanie informacji

**Specjalność: Systemy informatyczne w zarządzaniu**

## Cel zajęć

W ramach 90 minut należy określić, jakich danych wymaga projekt, skąd można je pozyskać oraz czy znalezione źródło rzeczywiście nadaje się do wykorzystania. Repozytorium ma dokumentować potrzeby informacyjne, ocenę źródła, sprawdzoną próbkę oraz wstępny pomysł realizacji.

## Zakres laboratorium

Na zajęciach należy:

- sformułować problem i wskazać użytkownika oraz decyzję, którą ma wspierać rozwiązanie;
- określić, jakie dane są potrzebne, w jakim zakresie i z jaką częstotliwością;
- zidentyfikować 4–6 wymagań i określić sposób ich sprawdzenia;
- znaleźć źródło danych lub informacji oraz wykonać próbę jego wykorzystania;
- ocenić, czy źródło odpowiada potrzebom projektu;
- zapisać braki, ograniczenia i wstępny pomysł realizacji.

## Punkt wyjścia

Przed zajęciami zespół powinien mieć kartę projektu z Lab 1 oraz loginy GitHub wszystkich członków. Repozytorium należy utworzyć na początku tych zajęć.

## Rezultat pracy

W repozytorium powinny znajdować się:

```text
projekt-zespolu/
├── data/
│   └── sample.csv lub sample.json
├── docs/
│   ├── problem.md
│   └── data.md
└── README.md
```

Próbka powinna pochodzić z rzeczywistego źródła. Jeżeli źródło zawiera dane chronione, należy zapisać najmniejszy dozwolony fragment, dane zanonimizowane albo odpowiedź API bez danych osobowych oraz opisać ograniczenie w `docs/data.md`. Nie należy umieszczać w publicznym repozytorium karty projektu, danych osobowych, haseł ani kluczy API.

## Gdzie szukać danych?

| Kategoria danych | Przykładowe źródła | Przykład zastosowania | Co należy sprawdzić |
|---|---|---|---|
| Urządzenia, czujniki i usługi | licznik, termostat, aplikacja producenta, eksport CSV, API | zużycie energii, temperatura, stan urządzenia | czy dane można pobrać, jakie są uprawnienia, jednostki i częstotliwość pomiarów |
| Dane meteorologiczne | [Open-Meteo](https://open-meteo.com/en/docs), [OpenWeather](https://openweathermap.org/api), [IMGW](https://danepubliczne.imgw.pl/) | temperatura, opady, wiatr, prognoza pogody | lokalizację pomiaru, okres, jednostki, dokładność i ewentualny klucz API |
| Mapy, adresy i geolokalizacja | [OpenStreetMap](https://www.openstreetmap.org/), [Overpass Turbo](https://overpass-turbo.eu/), [Geoportal](https://www.geoportal.gov.pl/), Nominatim | adresy, budynki, drogi, punkty usługowe, odległości | kompletność obiektów, układ współrzędnych, aktualność, limity i licencję |
| Transport publiczny i mobilność | miejskie portale danych, pliki GTFS/GTFS-RT, [Mobility Database](https://mobilitydatabase.org/), OpenStreetMap | przystanki, trasy, rozkłady, przejazdy i opóźnienia autobusów | obszar miasta, wersję rozkładu, zakres danych, format i możliwość regularnego pobierania |
| Ludność i statystyki publiczne | [GUS — Bank Danych Lokalnych](https://bdl.stat.gov.pl/bdl/start), [dane.gov.pl](https://dane.gov.pl/), BIP, portale miejskie | liczba mieszkańców, gospodarstwa domowe, bezrobocie, usługi publiczne | definicję wskaźnika, jednostkę, poziom agregacji, okres i metodologię |
| Gospodarka, finanse i kursy walut | [API NBP](https://api.nbp.pl/), [ECB Data Portal](https://data.ecb.europa.eu/), GUS | kursy walut, inflacja, stopy procentowe, ceny | walutę, datę obowiązywania, jednostkę, sposób obliczenia i aktualność |
| Statystyki międzynarodowe | [Eurostat](https://ec.europa.eu/eurostat/web/main/data/database), [OECD Data Explorer](https://data-explorer.oecd.org/), [World Bank Open Data](https://data.worldbank.org/), [UN Data](https://data.un.org/) | porównanie państw, regionów i okresów | definicje wskaźników, jednostki, okresy, poziom agregacji i porównywalność |
| Środowisko i jakość powietrza | [GIOŚ](https://powietrze.gios.gov.pl/), [OpenAQ](https://openaq.org/), dane IMGW | pyły, temperatura, hałas, jakość powietrza | stację pomiarową, metodę pomiaru, braki, częstotliwość i aktualność |
| Obserwacja Ziemi | [Copernicus Data Space](https://dataspace.copernicus.eu/), dane satelitarne | pokrycie terenu, susza, zmiany przestrzenne, roślinność | rozdzielczość, zachmurzenie, zasięg, datę pozyskania i licencję |
| Otwarte katalogi danych | [Otwarte Dane](https://dane.gov.pl/), [Europejski Portal Danych](https://data.europa.eu/en) | wyszukanie zbioru administracji publicznej lub samorządu | pierwotnego wydawcę, format, licencję, datę aktualizacji i sposób pobrania |
| Publiczne zbiory do analizy | [Kaggle Datasets](https://www.kaggle.com/datasets), [UCI Machine Learning Repository](https://archive.ics.uci.edu/), [Hugging Face Datasets](https://huggingface.co/datasets), [Our World in Data](https://ourworldindata.org/) | dane do ćwiczeń, porównań, klasyfikacji lub prototypu | źródło pierwotne, sposób przetworzenia, jakość, aktualność, licencję i wersję zbioru |
| Dane organizacji i procesów | rejestr, raport, arkusz, log systemu, procedura | obsługa zgłoszeń, zapasy, zużycie zasobów, przebieg procesu | właściciela danych, aktualność, kompletność, poufność i ograniczenia dostępu |
| Dokumentacja techniczna i metadane | instrukcja urządzenia, opis API, słownik zmiennych, metodologia | ustalenie znaczenia pól i sposobu pobierania danych | czy dokument potwierdza możliwość uzyskania wymaganej informacji |
| Własna obserwacja lub pomiar | obserwacja procesu, formularz, pomiar | uzupełnienie brakującej informacji lub sprawdzenie założenia | koszt, zgodę, anonimizację, powtarzalność i możliwe błędy |


## Jak wykorzystać wybrane dane?

Po sprawdzeniu źródeł danych dla swojego projektu należy zapisać, jak można je wykorzystać. Zespół powinien wskazać jeden wybrany wariant — analizę pliku, pobieranie danych z API, mapę, raport, notebook lub prosty skrypt — oraz uzasadnić wybór dostępnością i ograniczeniami danych. Nie należy na tym etapie budować rozwiązania.

Każdy członek zespołu powinien przeanalizować co najmniej jedno źródło, jeden aspekt danych albo jeden etap samodzielnego pozyskiwania danych i zapisać wynik swojej pracy w repozytorium. Jeżeli dane są zbierane przez zespół, pracę można podzielić według miejsca, terminu, rodzaju pomiaru, grupy obserwacji, przygotowania formularza, anonimizacji albo kontroli jakości. Nie trzeba przygotowywać osobnych wariantów realizacji dla każdej osoby — zespół wspólnie wybiera jeden wariant.

Jeżeli projekt wymaga zebrania danych własnych, w `docs/data.md` należy umieścić tabelę:

| Osoba | Co zbiera lub przygotowuje? | Zakres: miejsce, okres lub zmienna | Metoda | Liczba obserwacji lub rezultat | Ograniczenia |
|---|---|---|---|---|---|
| login | ... | ... | ... | ... | ... |

Nie należy wpisywać do publicznego repozytorium danych osobowych. Należy zapisać dane zagregowane lub zanonimizowane oraz opisać sposób ich pozyskania.

| Wariant | Kiedy można go zastosować? | Co należy sprawdzić? |
|---|---|---|
| Odczyt istniejącego eksportu CSV lub JSON | gdy urządzenie albo system już zapisuje dane | możliwość automatycznego pobrania i aktualność pliku |
| Pobieranie danych z API | gdy usługodawca udostępnia API | uwierzytelnianie, limity, zakres odpowiedzi i stabilność API |
| Wykorzystanie istniejących urządzeń smart | gdy można użyć licznika, termostatu lub czujnika dostępnego w domu | czy urządzenie udostępnia dane bez zakupu dodatkowego sprzętu |
| Rekomendacja zamiast automatycznego sterowania | gdy sterowanie urządzeniem byłoby ryzykowne | czy system może najpierw wskazywać decyzję użytkownikowi |
| Lekki skrypt lub usługa lokalna | gdy dane są małe i nie wymagają mocnego serwera | czy wystarczy komputer, który zespół już posiada |
| Dane testowe lub symulator | gdy rzeczywisty dostęp wymaga zgody albo sprzętu | które elementy są rzeczywiste, a które pozostają założeniem |

Należy zapisać w `docs/data.md` jeden wybrany pomysł oraz co najmniej jedną odrzuconą możliwość. Odrzucenie powinno wynikać z kosztu, braku danych, ograniczeń dostępu, ryzyka albo niewystarczającej wartości dla użytkownika.

## Przebieg zajęć — 90 minut

### 1. Repozytorium i podział pracy — 0–15 min

Należy:

1. utworzyć publiczne wspólne repozytorium GitHub i dodać członków jako współpracowników;
2. utworzyć `README.md` z nazwą projektu, krótkim opisem problemu, zespołem i linkami do `docs/problem.md` oraz `docs/data.md`;
3. utworzyć katalog `data/`;
4. wykonać pierwszy commit.

Pracę należy podzielić według zadań merytorycznych, a nie przypisywać jeden plik jednej osobie. Każdy członek zespołu powinien sprawdzić inne źródło, aspekt danych albo etap ich samodzielnego pozyskania. Jedna osoba może przygotować początkowy `README.md`, a inna szkic `docs/problem.md`; pozostali analizują źródła i przygotowują próbkę w `data/`. Wyniki tych prac należy wpisywać do wspólnego `docs/data.md` kolejno: przed edycją trzeba pobrać najnowszą wersję repozytorium, dodać własny wiersz lub sekcję, wykonać commit i udostępnić zmiany pozostałym osobom. Nie należy jednocześnie edytować tego samego pliku.

### 2. Problem i potrzeby informacyjne — 15–35 min

Należy utworzyć `docs/problem.md` i uzupełnić:

```markdown
# Problem projektu
## Użytkownik i decyzja
## Obecna trudność
## Zakres problemu
## Potrzebne dane
## Założenia i pytania otwarte
## Wymagania
```

W sekcji „Wymagania” należy umieścić tabelę:

| ID | Wymaganie | Kryterium sprawdzenia | Źródło lub uzasadnienie | Status | Osoba |
|---|---|---|---|---|---|
| R1 | Użytkownik powinien ... | Można sprawdzić, czy ... | karta / rozmowa / źródło | potwierdzone / założenie / pytanie | login |

Należy zapisać od 4 do 6 wymagań. Każde wymaganie powinno opisywać potrzebę użytkownika albo ograniczenie projektu, a nie nazwę technologii. W `docs/problem.md` należy dodatkowo umieścić tabelę potrzeb informacyjnych:

| Informacja | Do czego jest potrzebna? | Minimalny zakres | Format lub częstotliwość | Czy jest dostępna? |
|---|---|---|---|---|
| ... | ... | ... | ... | tak / częściowo / nie |

Co najmniej jedna pozycja powinna mieć status `częściowo` albo `nie`, aby wskazać rzeczywisty problem do rozwiązania.

### 3. Pozyskanie, ocena i pomysł realizacji — 35–80 min

Źródeł należy szukać w przewodniku, w internecie oraz w rozmowie z czatem. Czat może podpowiedzieć nazwę serwisu lub sposób wyszukania danych, ale każdą informację trzeba sprawdzić w dokumentacji właściciela źródła i zapisać wynik tej weryfikacji.

Należy:

1. wskazać co najmniej dwa możliwe źródła danych lub informacji;
2. dla każdego źródła zapisać, kto je publikuje, co oznaczają pola i do którego wymagania jest potrzebne;
3. wybrać jedno źródło podstawowe i wykonać próbę pobrania danych;
4. pobrać rzeczywistą próbkę do `data/sample.csv`, `data/sample.json` albo innego jasno nazwanego pliku;
5. otworzyć próbkę w VS Code i sprawdzić nazwy pól, liczbę rekordów, kodowanie, format dat, jednostki i brakujące wartości;
6. sprawdzić limity pobierania, wymagany klucz, koszt, licencję oraz możliwość ponownego pobrania danych;
7. ocenić, czy źródło wystarcza do realizacji wymagań;
8. zapisać w `docs/data.md` wybrany pomysł realizacji, braki i plan awaryjny.

W `docs/data.md` należy umieścić tabelę źródeł:

| Źródło | Co można pobrać? | Czy odpowiada potrzebom? | Dowód sprawdzenia | Braki lub ryzyko |
|---|---|---|---|---|
| ... | ... | tak / częściowo / nie | link, plik lub wynik próby | ... |

Przy każdym źródle należy odpowiedzieć na pytania:

| Obszar | Pytanie kontrolne | Przykład wyniku |
|---|---|---|
| Dopasowanie do problemu | Czy źródło zawiera dane potrzebne do realizacji konkretnego wymagania? | Potrzebny jest pomiar co 15 minut, a źródło udostępnia tylko wartości dzienne — źródło odpowiada częściowo. |
| Właściciel i znaczenie danych | Kto publikuje dane? Co oznaczają pola, jednostki i daty? | `temperature_2m` oznacza temperaturę na wysokości 2 m, w stopniach Celsjusza. |
| Jakość | Czy występują braki, duplikaty, błędne jednostki, niepełne okresy albo nieaktualne rekordy? | 8 z 100 rekordów nie ma wartości, a daty zapisano w dwóch formatach. |
| Dostęp i koszt | Ile zapytań można wykonać? Czy wymagany jest klucz, logowanie albo opłata? | Dokumentacja podaje limit zapytań na minutę; klucza nie zapisano w repozytorium. |
| Licencja i prywatność | Czy można użyć danych w projekcie i czy nie zawierają danych osobowych? | Zbiór ma licencję pozwalającą na ponowne wykorzystanie i zawiera dane zagregowane. |
| Powtarzalność | Czy inna osoba może ponownie pobrać podobne dane, korzystając z zapisanego adresu, parametrów i daty? | Kolega wykonał to samo zapytanie i otrzymał plik o tej samej strukturze. |

Następnie należy opisać wybrane źródło:

| Element | Wynik sprawdzenia |
|---|---|
| Źródło i właściciel | ... |
| Link lub sposób dostępu | ... |
| Wymaganie, które źródło obsługuje | ... |
| Data pobrania | ... |
| Format i kodowanie | ... |
| Liczba rekordów w próbce | ... |
| Nazwy pól i ich znaczenie | ... |
| Format dat i jednostki | ... |
| Brakujące wartości lub rekordy | ... |
| Limit zapytań, klucz i koszt | ... |
| Licencja i ograniczenia wykorzystania | ... |
| Próba ponownego pobrania | wykonano / nie wykonano; wynik ... |
| Brakujące dane | ... |
| Plan awaryjny | ... |
| Wybrany pomysł realizacji | ... |
| Odrzucony pomysł i powód | ... |

Jeżeli pobranie danych nie jest możliwe, należy zapisać w `docs/data.md` dokładny powód, wynik próby dostępu, wymagane uprawnienia oraz najmniejszy dostępny dowód, na przykład metadane, schemat albo odpowiedź błędu. Nie należy deklarować, że źródło jest dostępne, bez wykonania próby pobrania.

### 4. Integracja i sprawdzenie rezultatów — 80–90 min

Należy:

1. pobrać najnowszą wersję repozytorium przed zapisaniem zmian;
2. sprawdzić, czy README prowadzi do obu dokumentów;
3. sprawdzić, czy próbka znajduje się w katalogu `data/` i można ją otworzyć;
4. wykonać commit własnej części pracy;
5. sprawdzić historię commitów i obecność wkładu każdego członka zespołu.

Każdy członek zespołu powinien mieć własny, możliwy do wskazania rezultat: opis problemu, wymaganie, analizę źródła, weryfikację próbki albo opis brakujących danych.

