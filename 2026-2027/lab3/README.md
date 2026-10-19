# Laboratorium 3: Akwizycja i przetwarzanie danych

**Specjalność: Systemy informatyczne w zarządzaniu**

## Cel zajęć

Na tych zajęciach należy przejść od wybranego w Lab 2 źródła lub planu własnego pomiaru do przygotowanego, opisanego i możliwego do ponownego odtworzenia zbioru danych.

## Rezultat pracy

Po zajęciach repozytorium powinno zawierać:

```text
projekt-zespolu/
├── README.md                     # wymagany: środowisko i uruchomienie przetwarzania
├── requirements.txt              # gdy używane są dodatkowe pakiety Pythona
├── api/                          # opcjonalnie: kolekcja żądań do API
├── data/
│   ├── raw/
│   │   └── sample-source.ext
│   ├── processed/
│   │   └── sample-clean.ext
│   └── test/                      # opcjonalnie: kopie do testów
├── docs/
│   ├── data.md
│   ├── data-dictionary.md
│   └── processing.md
├── scripts/
│   ├── prepare_data.py lub prepare_data.ipynb  # jeden wariant
│   └── kontrola.sql               # opcjonalnie: zapytania dla projektu
└── examples/
    └── lab3/                      # opcjonalnie: data/, sql/ i docs/ z demonstracji
```

Własną próbkę i wyniki należy przechowywać w `data/`. Pliki z demonstracji opisanej w tym przewodniku należy umieszczać w `examples/lab3/`, aby nie mieszać ich z danymi projektu. Katalog `api/` jest potrzebny tylko przy źródle API, a `requirements.txt` — gdy wybrana ścieżka wymaga dodatkowych pakietów Pythona.

Jeżeli pełny zbiór jest duży, ale może być publikowany, należy umieścić w repozytorium małą próbkę, słownik danych i instrukcję ponownego pobrania. Jeżeli dane są prywatne, chronione albo nie mogą być publikowane, nie wolno umieszczać ich rzeczywistej próbki. Należy wtedy wykorzystać dane syntetyczne zachowujące strukturę zbioru albo zanonimizowaną lub zagregowaną próbkę, jeżeli jej publikacja jest dozwolona. W repozytorium można umieścić schemat, słownik pól, metadane oraz ogólny opis sposobu pozyskania danych, o ile opis nie ujawnia informacji poufnych, danych osobowych, adresów systemów wewnętrznych ani danych dostępowych. Jeżeli nawet opis nie może być opublikowany, należy zapisać ogólną informację o ograniczeniu i jego wpływie na projekt. Nie należy zapisywać haseł ani kluczy API.

## Co należy przygotować?

Należy:

1. ustalić, jakie dane zostaną pobrane lub zebrane oraz jaki zakres jest potrzebny do projektu;
2. zapisać sposób pozyskania danych: adres źródła, parametry zapytania lub opis pomiaru;
3. zachować surową próbkę w katalogu `data/raw/` bez zmieniania jej ręcznie;
4. przygotować słownik najważniejszych pól w `docs/data-dictionary.md`;
5. wykonać czyszczenie i transformacje w skrypcie albo notebooku;
6. zapisać wynik przetwarzania w `data/processed/`;
7. sprawdzić, czy wynik można odtworzyć po ponownym uruchomieniu skryptu;
8. zapisać w `docs/processing.md` wykonane kroki, problemy i decyzje.

## Plan pozyskania danych

W `docs/data.md` należy uzupełnić albo zaktualizować tabelę:

| Element | Ustalenie zespołu |
|---|---|
| Źródło lub sposób pomiaru | ... |
| Właściciel danych | ... |
| Zakres danych | ... |
| Okres i częstotliwość | ... |
| Jednostka obserwacji | ... |
| Sposób pobrania lub zebrania | ... |
| Limit, koszt lub wymagane uprawnienia | ... |
| Licencja i zasady publikacji | ... |
| Osoba odpowiedzialna za pozyskanie | login |
| Plan awaryjny | ... |

Jeżeli dane są zbierane samodzielnie, należy dodatkowo zapisać dla każdej osoby zakres pracy, metodę, liczbę obserwacji i ograniczenia. Zakresy powinny się uzupełniać, na przykład przez podział na miejsca, terminy, zmienne albo etapy pomiaru.

## Słownik danych

Słownik danych (ang. *data dictionary*) to zestawienie definicji wszystkich kolumn (pól) występujących w zbiorze. Jego celem jest jednoznaczne określenie, co reprezentuje dana zmienna, jakiego jest typu i w jakich jednostkach została wyrażona. Pozwala to uniknąć błędnych założeń (np. pomylenia sekund z minutami, kwoty netto z brutto czy błędnej interpretacji skrótów instytucjonalnych).

W `docs/data-dictionary.md` należy umieścić tabelę opisującą kluczowe pola zbioru:

| Kolumna w tabeli słownika | Co należy wpisać? |
|---|---|
| **Pole** | Dokładna, oryginalna nazwa kolumny ze zbioru danych (np. `czas_min`, `WYS_ST`). |
| **Znaczenie** | Krótki, jednoznaczny opis biznesowy lub techniczny: co ta zmienna oznacza w rzeczywistości. |
| **Typ** | Oczekiwany typ danych w kodzie i bazie (np. `INTEGER`, `REAL` / `FLOAT`, `TEXT`, `DATE`, `BOOLEAN`). |
| **Jednostka** | Jednostka miary (np. `minuty`, `PLN`, `sztuki`, `kWh`). Jeżeli pole nie ma jednostki (tekst, kategoria, identyfikator), należy wpisać `brak` lub `—`. |
| **Przykładowa wartość** | Reprezentatywna wartość z pobranej próbki danych (np. `45.0`, `siec`, `2026-10-01`). |
| **Czy może być puste?** | `tak` — jeśli brak wartości jest dopuszczalny biznesowo (np. zgłoszenie w toku nie ma jeszcze daty zamknięcia); `nie` — jeśli brak jest błędem danych (np. identyfikator, klucz główny). |

### Wzór tabeli do umieszczenia w pliku

```markdown
| Pole | Znaczenie | Typ | Jednostka | Przykładowa wartość | Czy może być puste? |
|---|---|---|---|---|---|
| id | Unikalny identyfikator zgłoszenia | INTEGER | brak | 10 | nie |
| data | Data rejestracji zgłoszenia | DATE | dzień | 2026-10-01 | nie |
| kategoria | Kategoria problemu technicznego | TEXT | brak | siec | nie |
| czas_min | Rzeczywisty czas obsługi zgłoszenia | REAL | minuty | 45.0 | tak |
```

Nie należy zakładać znaczenia pola na podstawie samej nazwy. Znaczenie, jednostkę i sposób obliczenia trzeba potwierdzić w dokumentacji źródła (np. w opisie API, metadanych GUS/Eurostat) albo w procedurze własnego pomiaru.

## Czyszczenie i transformacje

W skrypcie albo notebooku należy wykonać co najmniej trzy uzasadnione operacje, na przykład:

- usunięcie lub oznaczenie duplikatów;
- uzupełnienie, odrzucenie albo pozostawienie brakujących wartości z opisem decyzji;
- ujednolicenie typów danych i formatów dat;
- przeliczenie jednostek, na przykład minut na godziny albo watogodzin na kilowatogodziny;
- połączenie dwóch źródeł według wspólnego identyfikatora;
- ograniczenie danych do wybranego okresu lub obszaru;
- utworzenie obliczonego wskaźnika potrzebnego w projekcie.

Każdą operację należy opisać w `docs/processing.md`:

| Krok | Operacja | Powód | Wpływ na dane |
|---|---|---|---|
| 1 | ... | ... | ... |

Nie należy usuwać rekordów, zmieniać wartości ani łączyć zbiorów bez zapisania powodu i możliwego wpływu na wynik analizy.

## Kontrola jakości wyniku

Przed zapisaniem wyniku należy sprawdzić:

- liczbę rekordów przed i po przetwarzaniu;
- nazwy i typy kolumn;
- braki, duplikaty i wartości spoza oczekiwanego zakresu;
- formaty dat, jednostki i strefy czasowe;
- zgodność kluczy przy łączeniu źródeł;
- czy wynik można otworzyć i wykorzystać w następnym etapie projektu.

W `docs/processing.md` należy zapisać krótkie podsumowanie:

| Kontrola | Wynik | Działanie lub ograniczenie |
|---|---|---|
| Liczba rekordów | ... | ... |
| Brakujące wartości | ... | ... |
| Duplikaty | ... | ... |
| Zakresy i jednostki | ... | ... |
| Powtarzalność przetwarzania | ... | ... |

## Przebieg zajęć — 90 minut

### 1. Ustalenie planu danych — 0–15 min

Należy:

1. otworzyć `docs/data.md` z Lab 2;
2. wybrać źródło podstawowe albo zatwierdzić plan własnego pomiaru;
3. jeśli próbka z Lab 2 znajduje się w `data/sample.csv`, utworzyć katalog `data/raw/` i przenieść ją bez zmiany zawartości poleceniem `git mv data/sample.csv data/raw/sample.csv`; dla innej nazwy lub formatu zachować nazwę pliku i zastosować analogiczne przeniesienie;
4. wskazać osobę odpowiedzialną za każdy etap pozyskania danych;
5. ustalić zakres próbki, format i sposób zapisania danych surowych.

### 2. Pobranie lub zebranie próbki — 15–35 min

Należy:

1. jeśli próbka z Lab 2 nie została jeszcze zapisana w repozytorium, pobrać dane z pliku, API, rejestru albo istniejącego urządzenia;
2. w przypadku własnego pomiaru zebrać uzgodniony fragment danych i zapisać metodę pomiaru;
3. sprawdzić limit, koszt, uprawnienia i licencję, jeżeli dotyczą wybranego źródła;
4. sprawdzić, czy surowa próbka znajduje się w `data/raw/`, a jeśli dane pobrano podczas tych zajęć — zapisać ją w tym katalogu;
5. zanotować datę pobrania, adres źródła i parametry zapytania.

### 3. Słownik i profil danych — 35–50 min

Należy:

1. otworzyć próbkę w VS Code, Pythonie, Jupyterze albo DataGrip;
2. sprawdzić pola, typy, jednostki, daty, braki i duplikaty;
3. uzupełnić `docs/data-dictionary.md`;
4. wskazać co najmniej jeden problem jakościowy albo potwierdzić, że nie wykryto problemu w sprawdzonym zakresie.

### 4. Czyszczenie i transformacja — 50–75 min

Należy:

1. utworzyć skrypt lub notebook przygotowania danych;
2. wykonać co najmniej trzy uzasadnione operacje;
3. zapisać przetworzony wynik w `data/processed/`;
4. uzupełnić tabelę kroków w `docs/processing.md`;
5. uruchomić przetwarzanie ponownie i sprawdzić, czy wynik ma oczekiwaną strukturę.

Przed rozpoczęciem pracy należy podzielić zadania i ustalić osoby odpowiedzialne za pliki. Nie należy równocześnie edytować tego samego pliku — w szczególności `scripts/prepare_data.py` — ponieważ zwiększa to ryzyko konfliktów przy scalaniu zmian w Git. Przykładowy podział dla zespołu 3–4-osobowego:

- jedna osoba przygotowuje skrypt czyszczenia i transformacji;
- druga tworzy osobny skrypt lub testy sprawdzające jakość wyniku, np. liczbę rekordów, kolumny i brakujące wartości;
- trzecia uzupełnia słownik danych oraz opis źródła;
- czwarta opisuje operacje w `docs/processing.md` i sprawdza, czy przygotowanie danych można powtórzyć.

Jeśli kilka osób ma pracować nad kodem, należy rozdzielić go na osobne pliki lub moduły i wcześniej uzgodnić sposób ich połączenia. Zmiany należy zintegrować, a następnie ponownie uruchomić skrypt i kontrole jakości.

### 5. Integracja i zapis rezultatów — 75–90 min

Należy:

1. sprawdzić, czy w repozytorium znajdują się próbka surowa, wynik przetwarzania, słownik i opis kroków;
2. dopisać ograniczenia oraz czynności, których nie udało się wykonać;
3. zaktualizować główny `README.md` repozytorium projektu o wymagane środowisko i pakiety, polecenia ich instalacji oraz sposób uruchomienia skryptu lub notebooka, np. `python -m pip install pandas` i `python scripts/prepare_data.py data/raw/sample.csv data/processed/sample-clean.csv`;
4. wykonać commit własnego rezultatu;
5. sprawdzić historię commitów i wkład każdego członka zespołu.

## Przydatne narzędzia

Szczegółowy przewodnik, opisy, zrzuty interfejsów i ćwiczenia znajdują się w dalszej części tego pliku, w rozdziale **Przewodnik po narzędziach do pracy z danymi**. Należy zapoznać się z opisami wszystkich narzędzi, obejrzeć zrzuty, a następnie wybrać ścieżkę pasującą do źródła danych i zadania projektu. Nie trzeba instalować ani wykonywać ćwiczeń ze wszystkich programów.

W `docs/processing.md` należy zapisać wybrane narzędzie główne, ewentualne narzędzie pomocnicze oraz powód ich dopasowania do danych i zadania.

## Przewodnik po narzędziach do pracy z danymi

[Powrót na początek instrukcji](#laboratorium-3-akwizycja-i-przetwarzanie-danych)

### Jak korzystać z przewodnika

Przewodnik przedstawia kilka narzędzi do pracy z danymi. **Należy przeczytać ich opisy, obejrzeć zrzuty interfejsów i dobrać narzędzie do źródła danych oraz zadania. Nie trzeba instalować ani wykonywać ćwiczeń we wszystkich programach.** Wspólne dla zespołu jest zapoznanie się z możliwościami narzędzi; praktyczne ćwiczenie należy wykonać tylko na wybranej ścieżce. Można dobrać narzędzie pomocnicze, jeśli jest potrzebne do kolejnego etapu.

| Potrzeba lub źródło | Narzędzie do rozważenia | Kiedy wybrać? | Możliwy rezultat |
|---|---|---|---|
| Plik CSV lub inna tabela w pliku | Data Wrangler w VS Code | gdy potrzebne jest profilowanie tabeli i przygotowanie prostych reguł czyszczenia | profil danych, kod pandas i przetworzony plik |
| Dane w relacyjnej bazie lub praca w SQL | DataGrip | gdy potrzebne jest przeglądanie tabel, import, zapytania albo eksport | zapisane zapytania i wynik kontroli lub eksportu |
| Źródło udostępnia API | Postman albo Bruno | gdy trzeba wysłać żądanie i obejrzeć lub sprawdzić odpowiedź | zapisana kolekcja żądań i próbka odpowiedzi |
| Powtarzalne przetwarzanie danych | Python z pandas albo Jupyter | gdy operacje mają być zapisane jako skrypt lub notebook i uruchamiane ponownie | skrypt lub notebook oraz wynik przetwarzania |
| Szybkie porównanie rozkładów bez pisania kodu | Orange (opcjonalnie) | gdy wizualny przepływ pomaga obejrzeć dane | przepływ i wykres |

Data Wrangler i DataGrip służą do przeglądania i wstępnej analizy danych, ale pracują głównie z różnymi źródłami: pierwszy z plikami tabelarycznymi, drugi z bazami i SQL. Orange jest dodatkowym sposobem wizualnej eksploracji. Klient API pomaga sprawdzić endpoint, ale sama zapisana kolekcja żądań nie zastępuje próbki ani skryptu przetwarzania.

Zrzuty poniżej pochodzą z oficjalnej dokumentacji i przedstawiają rzeczywiste interfejsy narzędzi na danych demonstracyjnych. Należy obejrzeć zrzuty także tych narzędzi, których zespół nie wybierze, a następnie zapisać uzasadnienie wyboru. Układ przycisków może różnić się między wersjami. Obrazy są ładowane ze stron źródłowych i wymagają internetu; można je otworzyć w nowej karcie, aby powiększyć szczegóły.

### 0. Przykład demonstracyjny: zgłoszenia serwisowe

Poniższa próbka jest całkowicie syntetyczna i służy do pokazania działania narzędzi. Nie trzeba jej tworzyć, jeśli zespół ma już dozwoloną próbkę własnych danych. W przykładzie jedna obserwacja oznacza jedno zgłoszenie, a `czas_min` — czas obsługi w minutach.

W VS Code należy otworzyć katalog repozytorium i utworzyć plik `examples/lab3/data/raw/zgloszenia.csv` w kodowaniu UTF-8:

```csv
id,data,kategoria,czas_min
1,2026-10-01, Siec ,10
2,2026-10-01,siec,15
3,2026-10-01,SPRZET,20
4,2026-10-02,sprzet,25
5,2026-10-02,konto,30
6,2026-10-02,Konto,35
7,2026-10-03,siec,
8,2026-10-03,sprzet,-5
9,2026-10-03,konto,240
10,2026-10-04,siec,40
11,2026-10-04,sprzet,45
12,2026-10-04,konto,50
3,2026-10-01,SPRZET,20
```

Przed rozpoczęciem należy przyjąć następujące reguły:

- identyfikator powinien wskazywać jedno zgłoszenie;
- nazwy kategorii należy zapisywać małymi literami, bez skrajnych spacji;
- brak czasu nie oznacza zera;
- ujemny czas należy uznać w tym przykładzie za błąd i zastąpić brakiem;
- wartość 240 minut należy zachować: długie zgłoszenie może być prawdziwe.

**Kontrola wejścia:** plik zawiera 13 rekordów, 12 różnych identyfikatorów, jeden powtórzony wiersz, jeden pusty czas i jeden czas ujemny.

### 1. Profilowanie i czyszczenie plików CSV (Data Wrangler)

**Kiedy wybrać:** gdy dane projektu są zapisane w pliku tabelarycznym, np. CSV, i trzeba sprawdzić jego strukturę lub przygotować reguły czyszczenia. Poniższy pokaz należy wykonać tylko po wybraniu tej ścieżki; w pozostałych przypadkach wystarczy zapoznać się z opisem i zrzutami.

#### Otwarcie pliku w Data Wrangler

Należy zainstalować [VS Code](https://code.visualstudio.com/), [Pythona](https://www.python.org/downloads/) oraz rozszerzenie **Data Wrangler** firmy Microsoft z panelu Extensions w VS Code. Po uruchomieniu rozszerzenia należy wskazać środowisko Pythona; narzędzie może zaproponować instalację pandas.

W panelu Explorer należy kliknąć `examples/lab3/data/raw/zgloszenia.csv` prawym przyciskiem i wybrać **Open in Data Wrangler**. W ustawieniach importu należy sprawdzić separator przecinek i wiersz nagłówka.

![Otwarcie pliku przez Open in Data Wrangler](https://code.visualstudio.com/assets/docs/datascience/data-wrangler/open-from-file.png)

*Screen: Microsoft, [otwieranie i obsługa Data Wrangler](https://code.visualstudio.com/docs/datascience/data-wrangler). Należy wskazać własny plik CSV.*

**Oczekiwany wynik:** cztery kolumny i 13 rekordów. Jeżeli cały wiersz znajduje się w jednej kolumnie, należy poprawić separator.

#### Identyfikacja błędów i profil kolumn

W trybie **Viewing** należy kolejno zaznaczyć `kategoria` i `czas_min`. W podsumowaniu należy odczytać braki oraz zakres wartości. W nagłówkach można obejrzeć rozkłady lub częstości; filtrowanie i sortowanie ułatwiają znalezienie konkretnych rekordów.

![Profil kolumn i podsumowanie danych w Data Wrangler](https://code.visualstudio.com/assets/docs/datascience/data-wrangler/view-mode-ui.png)

*Screen: Microsoft, [tryb podglądu](https://code.visualstudio.com/docs/datascience/data-wrangler#viewing-mode-interface). Należy zwrócić uwagę na Data Summary i Quick Insights.*

Należy zapisać odpowiedzi:

1. Ile wariantów nazw kategorii występuje przed czyszczeniem?
2. Które identyfikatory wymagają sprawdzenia?
3. Dlaczego minimum wynoszące −5 jest błędem w tym przykładzie, a maksimum 240 nie musi nim być?

#### Wykonanie operacji czyszczenia

Należy przełączyć narzędzie na **Editing**. W panelu operacji należy wyszukać kolejno:

| Kolumna lub zakres | Operacja | Oczekiwany efekt |
|---|---|---|
| `kategoria` | **Strip whitespace** | usunięcie skrajnych spacji |
| `kategoria` | **Convert text to lowercase** | trzy kategorie: konto, siec, sprzet |
| wszystkie kolumny | **Drop duplicate rows** | 12 rekordów po usunięciu identycznego powtórzenia |

Po każdej operacji należy obejrzeć podgląd zmian i zatwierdzić krok. Kod operacji można sprawdzić w **Code Preview**, a historię w **Cleaning Steps**. Ujemny czas zostanie obsłużony jawnie w skrypcie poniżej.

![Panel operacji, historia i wygenerowany kod w Data Wrangler](https://code.visualstudio.com/assets/docs/datascience/data-wrangler/edit-mode-ui.png)

*Screen: Microsoft, [tryb edycji](https://code.visualstudio.com/docs/datascience/data-wrangler#editing-mode-interface). Operacja uzupełniania braków pokazana na screenie jest przykładem producenta; w naszym ćwiczeniu należy pozostawić braki.*

#### Eksport danych i skrypt w Pythonie

Z menu eksportu należy zapisać dane jako nowy CSV. Wygenerowany kod należy przenieść do pliku `scripts/prepare_data.py`; przy pracy z notebookiem można użyć **Export code back to Notebook**.

![Eksport danych i kodu z Data Wrangler](https://code.visualstudio.com/assets/docs/datascience/data-wrangler/export-menu.png)

*Screen: Microsoft, [eksport kodu i danych](https://code.visualstudio.com/docs/datascience/data-wrangler#edit-and-export-code).*

Poniższy kompletny skrypt stanowi wzorzec dla naszego przykładu. Należy porównać go z wygenerowanymi operacjami. Skrypt zachowuje surowy plik, oznacza błędne czasy i sprawdza wynik.

```python
import argparse
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("input", type=Path, help="ścieżka do surowego pliku CSV")
parser.add_argument("output", type=Path, help="ścieżka zapisu oczyszczonego pliku CSV")
args = parser.parse_args()

raw = pd.read_csv(args.input)

clean = raw.copy()
clean["kategoria"] = clean["kategoria"].str.strip().str.lower()
clean = clean.drop_duplicates().copy()
clean["data"] = pd.to_datetime(clean["data"], format="%Y-%m-%d", errors="raise")
clean["czas_min"] = pd.to_numeric(clean["czas_min"], errors="raise")
clean.loc[clean["czas_min"] < 0, "czas_min"] = float("nan")

assert clean["id"].notna().all(), "Puste identyfikatory"
assert clean["id"].is_unique, "Powtórzone identyfikatory wymagają analizy"
assert clean["kategoria"].isin(["siec", "sprzet", "konto"]).all()
assert clean["czas_min"].dropna().ge(0).all(), "Ujemne czasy"

args.output.parent.mkdir(parents=True, exist_ok=True)
clean.to_csv(args.output, index=False, date_format="%Y-%m-%d")

print(f"Rekordy: {len(raw)} -> {len(clean)}")
print(f"Braki czasu: {clean['czas_min'].isna().sum()}")
print(clean["czas_min"].agg(["count", "mean", "median", "min", "max"]))
```

W terminalu repozytorium należy wykonać:

```powershell
python -m pip install pandas
python scripts/prepare_data.py examples/lab3/data/raw/zgloszenia.csv examples/lab3/data/processed/zgloszenia-clean.csv
```

Jeżeli na Windows polecenie `python` jest niedostępne, można sprawdzić `py`. Należy używać tego samego środowiska, w którym zainstalowano pandas.

| Kontrola wyniku | Oczekiwana wartość |
|---|---|
| Rekordy | 12 |
| Kategorie | 3, po 4 zgłoszenia |
| Braki czasu | 2 |
| Czasy wykorzystane w statystykach | 10 |
| Średnia / mediana | 51 / 32,5 min |
| Minimum / maksimum | 10 / 240 min |

Należy ponownie wykonać to samo polecenie z tymi samymi ścieżkami wejściową i wyjściową. Wyniki powinny pozostać takie same. W `docs/processing.md` należy opisać, że drugi brak czasu powstał w wyniku oznaczenia błędnej wartości, a nie awarii importu.

**Zadanie:** należy utworzyć katalog `examples/lab3/data/test/`, skopiować do niego `examples/lab3/data/raw/zgloszenia.csv` jako `zgloszenia-invalid.csv`, dodać w kopii nowe zgłoszenie z nowym identyfikatorem i ujemnym czasem, a następnie przewidzieć wynik kontroli i uruchomić skrypt na kopii:

```powershell
python scripts/prepare_data.py examples/lab3/data/test/zgloszenia-invalid.csv examples/lab3/data/test/zgloszenia-invalid-clean.csv
```

Nie należy edytować pliku w `examples/lab3/data/raw/`.

### 2. Wizualna analiza rozkładów (Orange)

**Kiedy wybrać:** gdy wizualny przepływ pomaga szybko obejrzeć rozkład danych, a zespół chce porównać go z pracą w tabeli lub SQL. Orange jest opcjonalny — nie trzeba go instalować, jeśli inna wybrana ścieżka wystarcza. Poniższy zrzut przedstawia widżet **Distributions** z histogramem. Aby dodatkowo porównać rozkład, można połączyć dane z widżetem **Box Plot**. Do histogramu i statystyk można też użyć Data Wrangler albo DataGrip. [Wersja i przeznaczenie](https://orangedatamining.com/).

![Histogram zmiennej liczbowej w Orange](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/_images/Distributions-Continuous.png)

*Screen z dokumentacji Orange: [Distributions](https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/visualize/distributions.html). W razie użycia Orange należy wczytać przygotowany CSV blokiem File, sprawdzić typ `czas_min`, a następnie połączyć go z Distributions. Oczekiwany jest histogram 10 niepustych czasów.*

### 3. Praca z bazą danych i SQL (DataGrip)

**Kiedy wybrać:** gdy dane są przechowywane w bazie, zespół potrzebuje SQL albo musi zaimportować lub wyeksportować tabelę. Jeśli projekt pracuje wyłącznie na plikach i nie wymaga SQL, wystarczy przeczytać opis i obejrzeć zrzuty. Poniższe ćwiczenia są przykładami funkcji DataGrip — nie trzeba wykonywać ich wszystkich. Należy wybrać te, które odpowiadają zadaniu projektu.

W pokazie lokalną bazą będzie SQLite. Jeżeli wybrano tę ścieżkę, należy zainstalować [DataGrip](https://www.jetbrains.com/datagrip/download/) i aktywować licencję odpowiednią dla swojego sposobu użycia. Aktualne warunki są dostępne na [stronie produktu](https://www.jetbrains.com/datagrip/).

#### Połączenie z lokalną bazą

W **Database Explorer** należy wybrać **+ → Data Source → SQLite**. W polu **File** trzeba wskazać pełną ścieżkę nowego pliku `lab3.sqlite` w katalogu roboczym. W razie komunikatu **Download missing driver files** należy pobrać sterownik, a następnie wykonać **Test Connection**, wybrać schemat `main` i zatwierdzić.

![Konfiguracja źródła SQLite w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_qsg_create_data_source_sqlite.png)

*Screen: JetBrains, [uruchomienie DataGrip z SQLite](https://www.jetbrains.com/help/datagrip/quick-start-guide.html). Należy wskazać własną ścieżkę pliku bazy.*

#### Połączenie z innymi silnikami baz danych

DataGrip może przechowywać kilka źródeł danych w panelu **Database Explorer**. Na zrzucie pokazano przykładowe połączenie z PostgreSQL. Do pracy z bazą serwerową wymagane są adres hosta, port, nazwa bazy i uprawnione konto. Nie trzeba konfigurować zewnętrznego serwera, jeśli projekt z niego nie korzysta; można pozostać przy lokalnym SQLite.

![Ustawienia połączenia PostgreSQL w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_connection_details_postgresql_default.png)

*Screen: JetBrains, [konfiguracja źródła danych](https://www.jetbrains.com/help/datagrip/managing-data-sources.html). Prawdziwe połączenie wymaga działającego serwera i uprawnionego konta; w ćwiczeniu należy wykonać połączenie z lokalnym SQLite. Ustawień dostępowych nie wolno umieszczać w publicznym repozytorium.*

DataGrip obsługuje różne silniki baz; zakres funkcji zależy od rodzaju połączenia. Aktualną listę podaje [dokumentacja JetBrains](https://www.jetbrains.com/help/datagrip/managing-data-sources.html#supported-databases). Na zajęciach należy korzystać wyłącznie z lokalnej bazy demonstracyjnej albo serwera udostępnionego przez prowadzącego.

#### Przeglądanie i filtrowanie tabeli

Po połączeniu należy rozwinąć schemat `main` i dwukrotnie kliknąć tabelę `zgloszenia`. W edytorze tabeli trzeba sprawdzić nagłówki, typy i przykładowe rekordy, posortować kolumnę `czas_min`, a następnie użyć pola filtra, aby wyświetlić rekordy z brakującym czasem. Zmian w tabeli demonstracyjnej nie należy zatwierdzać.

![Edytor tabeli i wyniki w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_data_editor_db_object_data_intro.png)

*Screen: JetBrains, [edytor danych](https://www.jetbrains.com/help/datagrip/data-editor-and-viewer.html). Dwuklik otwiera tabelę; nagłówki umożliwiają sortowanie i filtrowanie.*

#### Import CSV

Na schemacie `main` należy wybrać **Import/Export → Import Data from File(s)** i wskazać `examples/lab3/data/processed/zgloszenia-clean.csv`. W ustawieniach pliku należy zaznaczyć **First row is header**, separator przecinek i UTF-8.

![Ustawienia separatora i nagłówka importowanego CSV](https://resources.jetbrains.com/help/img/idea/2026.2/db_import_csv_source.png)

*Screen: JetBrains, [import CSV](https://www.jetbrains.com/help/datagrip/import-data.html). Podgląd powinien przedstawiać cztery osobne kolumny.*

W mapowaniu należy ustawić nową tabelę `zgloszenia`. Typy powinny odpowiadać danym: `id` — INTEGER, `data` — TEXT, `kategoria` — TEXT, `czas_min` — REAL. Puste czasy powinny zostać zaimportowane jako NULL.

![Mapowanie kolumn i tabeli docelowej w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_import_csv_mapping.png)

*Screen: JetBrains, [mapowanie importu](https://www.jetbrains.com/help/datagrip/import-data.html). W ćwiczeniu nazwą tabeli jest zgloszenia.*

Po imporcie należy otworzyć tabelę dwuklikiem i sprawdzić 12 rekordów. Ponowny import do tej samej tabeli może dopisać dane; przed kolejną próbą należy sprawdzić jej zawartość.

#### Wykres i histogram z tabeli lub wyniku zapytania

W edytorze danych należy wybrać **Show Chart**, a następnie w ustawieniach serii wskazać typ wykresu. Dla `czas_min` należy wybrać **Histogram**; dla porównania liczebności kategorii można użyć wykresu słupkowego. Wynik zapytania można obejrzeć jako wykres, a gotową wizualizację wyeksportować do PNG.

![Wizualizacja danych jako wykres w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_visualize_data_as_a_chart.png)

*Screen: JetBrains, [wykresy w edytorze danych](https://www.jetbrains.com/help/datagrip/tables-view-data.html). W ćwiczeniu należy wybrać `czas_min` i Histogram; puste wartości nie tworzą słupka.*

Należy sprawdzić, jak rekord 240 minut zmienia obraz rozkładu. Histogram pokazuje rozkład obserwacji z próbki, ale sam nie potwierdza, że próba reprezentuje całą populację.

#### Kontrole i agregacje

Należy otworzyć konsolę SQL źródła danych (np. klawiszem **F4**), wkleić zapytanie, zaznaczyć je i wykonać przyciskiem **Execute**. Demonstracyjne zapytania należy zachować w `examples/lab3/sql/kontrola-zgloszenia.sql`.

```sql
-- Liczba rekordów i braków czasu.
SELECT COUNT(*) AS rekordy,
       COUNT(czas_min) AS znane_czasy,
       SUM(CASE WHEN czas_min IS NULL THEN 1 ELSE 0 END) AS braki
FROM zgloszenia;

-- Typ zapisanych wartości: oczekiwane real oraz null.
SELECT typeof(czas_min) AS typ, COUNT(*) AS liczba
FROM zgloszenia
GROUP BY typeof(czas_min);

-- Powtórzone identyfikatory: oczekiwany pusty wynik.
SELECT id, COUNT(*) AS liczba
FROM zgloszenia
GROUP BY id
HAVING COUNT(*) > 1;

-- Zestawienie kategorii. AVG pomija NULL.
SELECT kategoria,
       COUNT(*) AS zgloszenia,
       COUNT(czas_min) AS znane_czasy,
       ROUND(AVG(czas_min), 2) AS srednia_min,
       MIN(czas_min) AS minimum,
       MAX(czas_min) AS maksimum
FROM zgloszenia
GROUP BY kategoria
ORDER BY kategoria;
```

| Kategoria | Zgłoszenia | Znane czasy | Średnia | Minimum | Maksimum |
|---|---:|---:|---:|---:|---:|
| konto | 4 | 4 | 88,75 | 30 | 240 |
| siec | 4 | 3 | 21,67 | 10 | 40 |
| sprzet | 4 | 3 | 30,00 | 20 | 45 |

**Zadanie:** należy napisać zapytanie pokazujące identyfikatory zgłoszeń z brakującym czasem. Oczekiwany wynik to 7 i 8. Następnie trzeba obliczyć średnią całego zbioru i porównać ją z wynikiem Pythona: 51 minut.

#### Eksport wyników i struktury tabeli

Po wykonaniu zapytania należy kliknąć **Export Data** w pasku wyników, wybrać format **CSV**, wskazać plik `examples/lab3/data/processed/kontrola-kategorii.csv` i pozostawić włączony nagłówek kolumn. Dla porównania można wyeksportować wynik do JSON albo XLSX. Eksportuje się bieżący wynik zapytania, a nie całą bazę.

![Eksport wyniku tabeli w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_export_data_from_data_editor.png)

*Screen: JetBrains, [eksport danych](https://www.jetbrains.com/help/datagrip/export-data.html). Format wybiera się w polu Extractor, a docelową ścieżkę w Output file.*

Aby zapisać definicję demonstracyjnej tabeli, w **Database Explorer** należy kliknąć tabelę prawym przyciskiem i wybrać **SQL Scripts → Generate DDL to Query Console**. Następnie należy zapisać wygenerowany kod jako `examples/lab3/sql/schema-demo.sql`. DDL opisuje strukturę tabeli, a CSV/JSON/XLSX zawiera jej dane.

#### Ćwiczenia: autouzupełnianie, historia, diagram i plan zapytania

Ćwiczenia należy wykonać na lokalnym źródle SQLite utworzonym wcześniej. Dodatkowe tabele mają prefiks `demo_`, aby nie zmieniać tabeli `zgloszenia` używanej do analizy danych.

##### 1. Utworzenie małej bazy z relacjami

Aby diagram i złączenia miały widoczne relacje, należy utworzyć tabele demonstracyjne. Kod trzeba zapisać jako `examples/lab3/sql/demo-relacje.sql`, uruchomić w konsoli SQLite i odświeżyć Database Explorer.

```sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS demo_kategorie (
    id INTEGER PRIMARY KEY,
    nazwa TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS demo_statusy (
    id INTEGER PRIMARY KEY,
    nazwa TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS demo_zgloszenia (
    id INTEGER PRIMARY KEY,
    kategoria_id INTEGER NOT NULL REFERENCES demo_kategorie(id),
    status_id INTEGER NOT NULL REFERENCES demo_statusy(id),
    czas_min REAL
);

INSERT OR IGNORE INTO demo_kategorie (id, nazwa) VALUES
    (1, 'siec'), (2, 'sprzet');

INSERT OR IGNORE INTO demo_statusy (id, nazwa) VALUES
    (1, 'otwarte'), (2, 'zamkniete');

INSERT OR IGNORE INTO demo_zgloszenia (id, kategoria_id, status_id, czas_min) VALUES
    (1, 1, 1, 20), (2, 1, 2, 45), (3, 2, 2, 30);
```

W DataGrip należy otworzyć zapisany plik, zaznaczyć cały skrypt, nacisnąć `Ctrl+Enter` i wybrać uruchomienie wszystkich zaznaczonych instrukcji. Po wykonaniu skryptu należy odświeżyć źródło SQLite w Database Explorer. Powinny pojawić się trzy tabele: `demo_kategorie`, `demo_statusy` i `demo_zgloszenia`.

##### 2. Uzupełnianie nazw tabel i kolumn

W konsoli SQL źródła SQLite należy wpisać poniższy fragment. Kursor należy ustawić bezpośrednio za kropką w `SELECT z.` i nacisnąć `Ctrl+Space`. Z listy podpowiedzi należy wybrać kolumnę, np. `id` albo `czas_min`.

```sql
SELECT z.
FROM demo_zgloszenia z;
```

Aby sprawdzić podpowiadanie nazwy tabeli, w drugim wierszu należy tymczasowo zmienić `demo_zgloszenia` na `demo_z`, nacisnąć `Ctrl+Space` i wybrać pełną nazwę tabeli. Propozycje należy zaakceptować klawiszem `Enter`.

![Podpowiedzi nazw kolumn w edytorze DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_completion_fields_for_select.png)

*Zrzut z dokumentacji JetBrains: [uzupełnianie nazw w zapytaniu SELECT](https://www.jetbrains.com/help/datagrip/auto-completing-code.html).*

Następnie należy wykonać poniższe zapytanie. Oczekiwany wynik zawiera trzy zgłoszenia oraz nazwy kategorii i statusów.

```sql
SELECT z.id, k.nazwa AS kategoria, s.nazwa AS status, z.czas_min
FROM demo_zgloszenia z
JOIN demo_kategorie k ON k.id = z.kategoria_id
JOIN demo_statusy s ON s.id = z.status_id
ORDER BY z.id;
```

Jeżeli DataGrip nie proponuje nazw, należy upewnić się, że konsola jest podłączona do źródła SQLite i że schemat `main` jest widoczny w Database Explorer.

##### 3. Odzyskanie zapytania z historii

Po wykonaniu zapytania z poprzedniego kroku należy nacisnąć `Ctrl+Alt+E`, aby otworzyć historię zapytań bieżącego źródła danych. W oknie historii należy wyszukać zapytanie zawierające `demo_zgloszenia`, a następnie dwukrotnie kliknąć jego wpis, aby przywrócić go w edytorze.

![Okno historii zapytań w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_show_history.png)

*Zrzut z dokumentacji JetBrains: [historia zapytań](https://www.jetbrains.com/help/datagrip/find-recent-queries-and-files.html).*

Przywrócone zapytanie należy zapisać w `examples/lab3/sql/kontrola-relacje.sql`. Jest to osobny plik od `examples/lab3/sql/kontrola-zgloszenia.sql`, w którym zapisano kontrole pierwszej tabeli. Historia służy do odzyskiwania zapytań w DataGrip, ale nie jest plikiem projektu i nie zastępuje zapisu w repozytorium.

##### 4. Obejrzenie diagramu relacji

W Database Explorer należy rozwinąć schemat `main`, kliknąć prawym przyciskiem myszy tabelę `demo_zgloszenia` i wybrać **Diagrams → Show Diagram**. Jeżeli na diagramie nie ma tabel referencyjnych, należy przeciągnąć na niego `demo_kategorie` i `demo_statusy` z Database Explorer. Powinny być widoczne połączenia odpowiadające kluczom obcym `kategoria_id` i `status_id`.

![Tworzenie diagramu tabel w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_create_diagram_for_schema.png)

*Zrzut z dokumentacji JetBrains: [diagramy baz danych](https://www.jetbrains.com/help/datagrip/creating-diagrams.html).*

Diagram należy wyeksportować: kliknąć go prawym przyciskiem, wybrać **Export Diagram → Export to Image…** i zapisać jako `examples/lab3/docs/demo-relacje.png`. Należy wskazać, która tabela przechowuje zgłoszenia, a które słowniki kategorii i statusów.

##### 5. Odczytanie planu zapytania

W edytorze należy zaznaczyć zapytanie łączące trzy tabele i wybrać **Explain Plan → Explain Plan** z menu kontekstowego albo z paska narzędzi edytora. W zakładce **Query Plan** należy odczytać operacje wykonane dla zapytania i wskazać, czy silnik przegląda tabelę, czy korzysta z indeksu.

![Menu Explain Plan w DataGrip](https://resources.jetbrains.com/help/img/idea/2026.2/db_explain_plan_toolbar_dropdown.png)

*Zrzut z dokumentacji JetBrains: [plan wykonania zapytania](https://www.jetbrains.com/help/datagrip/query-execution-plan.html).*

Jeżeli polecenie **Explain Plan** nie jest dostępne dla lokalnego SQLite, należy uruchomić zapytanie w natywnej postaci SQLite, dodając przed nim `EXPLAIN QUERY PLAN`:

```sql
EXPLAIN QUERY PLAN
SELECT z.id, k.nazwa AS kategoria, s.nazwa AS status, z.czas_min
FROM demo_zgloszenia z
JOIN demo_kategorie k ON k.id = z.kategoria_id
JOIN demo_statusy s ON s.id = z.status_id
ORDER BY z.id;
```

W wyniku należy odczytać kolumnę `detail` i opisać jednym zdaniem, jak silnik odczytuje tabele. Plan przedstawia wybraną strategię wykonania, a nie rzeczywisty czas zapytania. Dla tej małej próbki nie należy wyciągać wniosków o wydajności bazy.

Dokumentacja: [uzupełnianie kodu](https://www.jetbrains.com/help/datagrip/auto-completing-code.html), [historia zapytań](https://www.jetbrains.com/help/datagrip/find-recent-queries-and-files.html), [diagramy](https://www.jetbrains.com/help/datagrip/creating-diagrams.html), [plan wykonania](https://www.jetbrains.com/help/datagrip/query-execution-plan.html), [`EXPLAIN QUERY PLAN` w SQLite](https://www.sqlite.org/eqp.html).

### 4. Pobieranie i testowanie danych przez API (Postman / Bruno)

**Kiedy wybrać:** gdy źródło projektu udostępnia API i trzeba sprawdzić żądanie oraz zwracaną odpowiedź. Należy wybrać **jedno** narzędzie: **Bruno** zapisuje kolekcję jako pliki w lokalnym katalogu, a **Postman** udostępnia rozbudowany interfejs do pracy z kolekcjami i testami. Jeśli projekt nie korzysta z API, nie trzeba instalować żadnego z nich — wystarczy przeczytać opis i obejrzeć zrzuty.

Klient API pozwala wysłać żądanie HTTP i sprawdzić kod statusu, nagłówki oraz treść odpowiedzi, np. JSON. Demonstracja poniżej używa publicznego API NBP. Dla projektu należy przygotować własne żądanie tylko wtedy, gdy wybranym źródłem jest API.

Jako przykład należy użyć publicznego API Narodowego Banku Polskiego, które zwraca pięć ostatnich dostępnych kursów średnich euro z tabeli A. Żądanie jest tylko do odczytu i nie wymaga klucza API:

```text
GET https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/5/?format=json
```

Dokumentacja: [API NBP — opis i przykłady żądań](https://api.nbp.pl/).

#### Postman

1. Należy otworzyć Postmana i utworzyć nowe żądanie HTTP.
2. Należy wybrać metodę **GET**, wkleić adres API NBP i wybrać **Send**.
3. W panelu odpowiedzi należy sprawdzić kod `200 OK`, format JSON oraz pola `code` i `rates`. Pole `code` powinno zawierać `EUR`, a `rates` — listę obiektów z datą i kursem `mid`.
4. W sekcji **Scripts → Post-response** należy dodać poniższe kontrole i ponownie wysłać żądanie. Wyniki testów pojawią się przy odpowiedzi.

![Rzeczywisty interfejs Postman z widokiem żądania HTTP](https://learning.postman.com/_fern-img/d2bd0453313c5d841ee8526673fa13e2430f9d4a643681072ca81b94749852e2.webp)

*Zrzut z dokumentacji Postmana: [tworzenie i wysyłanie żądania](https://learning.postman.com/docs/use/send-requests/create-requests/request-basics).*

```javascript
pm.test("Status HTTP wynosi 200", () => {
  pm.response.to.have.status(200);
});

const dane = pm.response.json();

pm.test("Odpowiedź zawiera kursy EUR", () => {
  pm.expect(dane.code).to.eql("EUR");
  pm.expect(dane.rates).to.be.an("array").that.is.not.empty;
});

pm.test("Każdy kurs jest dodatnią liczbą", () => {
  pm.expect(
    dane.rates.every((pozycja) => typeof pozycja.mid === "number" && pozycja.mid > 0)
  ).to.eql(true);
});
```

Instrukcja Postmana: [pisanie testów odpowiedzi](https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts).

#### Bruno

1. Należy zainstalować [Bruno](https://www.usebruno.com/downloads), utworzyć kolekcję lokalną i dodać żądanie.
2. Należy ustawić metodę **GET**, wkleić adres API NBP i wybrać **Send**.
3. W panelu odpowiedzi należy sprawdzić status `200`, dane JSON, `code: "EUR"` oraz listę `rates`.
4. W zakładce **Tests** należy dodać testy odpowiedzi. Po ponownym wysłaniu żądania Bruno pokaże, które warunki zostały spełnione.

![Rzeczywisty interfejs Bruno z odpowiedzią JSON po wysłaniu żądania](https://docs.usebruno.com/images/screenshots/quick-start/02-create-a-request/04-after-req.webp)

*Zrzut z oficjalnego [samouczka Bruno](https://docs.usebruno.com/introduction/quick-start).*

```javascript
test("Status HTTP wynosi 200", function () {
  expect(res.getStatus()).to.eql(200);
});

test("Odpowiedź zawiera kursy EUR", function () {
  const dane = res.getBody();
  expect(dane.code).to.eql("EUR");
  expect(dane.rates).to.be.an("array").that.is.not.empty;
});

test("Każdy kurs jest dodatnią liczbą", function () {
  const dane = res.getBody();
  expect(
    dane.rates.every((pozycja) => typeof pozycja.mid === "number" && pozycja.mid > 0)
  ).to.eql(true);
});
```

![Rzeczywisty interfejs Bruno z wynikiem testu odpowiedzi](https://docs.usebruno.com/images/screenshots/quick-start/05-write-test-case/01-write-assert.webp)

*Zrzut z oficjalnego samouczka Bruno: [testowanie odpowiedzi](https://docs.usebruno.com/introduction/quick-start). Kolekcję Bruno można zapisać w repozytorium jako pliki; w Postmanie należy wyeksportować kolekcję do pliku JSON. Przed publikacją należy sprawdzić, czy w kolekcji nie zapisano tokenów ani innych sekretów.*

#### Zadanie dla zespołów wybierających źródło API

1. Należy uruchomić żądanie do wybranego API i zapisać kolekcję w repozytorium, np. w katalogu `api/`. Próbkę odpowiedzi należy zapisać osobno w `data/raw/`, jeśli pozwalają na to warunki publikacji.
2. W demonstracji NBP należy zmienić walutę `EUR` na `USD`, a następnie liczbę notowań `last/5` na `last/10`. Trzeba sprawdzić, które pola odpowiedzi pozostają takie same, a które wartości się zmieniają.
3. W demonstracji NBP należy zmienić jeden warunek testu tak, aby nie był spełniony, np. sprawdzić, czy `code` równa się `USD`, gdy w żądaniu nadal wskazano `EUR`. Po zaobserwowaniu niepowodzenia należy przywrócić prawidłowy warunek.
4. Dla źródła danych wybranego do projektu należy przygotować własne żądanie i sprawdzić: status odpowiedzi, format, obecność wymaganych pól, braki danych oraz aktualność wyników. W dokumentacji źródła trzeba odszukać zasady dostępu, limity zapytań, ograniczenia zakresu danych i warunki ponownego wykorzystania.

Wyniki NBP zmieniają się wraz z publikacją nowych notowań, dlatego testy powinny sprawdzać strukturę i sens wartości, a nie konkretny kurs lub datę. Postman i Bruno służą tu do ręcznego wysyłania żądań oraz testów odpowiedzi; nie są narzędziami do pomiaru obciążenia API.

### 5. Najczęstsze problemy

| Objaw | Co należy sprawdzić? |
|---|---|
| CSV ma tylko jedną kolumnę | separator w oknie importu |
| Data Wrangler nie uruchamia się | wybrane środowisko Pythona i dostępność pandas |
| Skrypt zgłasza powtórzony identyfikator | czy rekordy o tym samym ID różnią się treścią; nie należy automatycznie wybierać jednego |
| Orange pokazuje każdą liczbę jako kategorię | typ pola: Continuous |
| Orange nie pokazuje wszystkich rekordów | czy połączenie przekazuje Data, czy Selected Data, oraz czy część wartości jest pusta |
| DataGrip pokazuje inny wynik średniej | typ REAL, puste pola jako NULL, zgodność pliku wejściowego i liczba rekordów |
| Żądanie API zwraca błąd | poprawność adresu i parametrów; przy statusie 429 — limity zapytań i zasady ponawiania opisane przez dostawcę |
| Po ponownym imporcie jest 24 rekordy | czy import dopisał dane do istniejącej tabeli |
| Przepływ Orange nie działa u innej osoby | dostępność pliku CSV i ścieżka w bloku File |

### 6. Dobór narzędzia do własnego projektu

Po przejrzeniu opisów i zrzutów należy wybrać narzędzie główne odpowiednie dla źródła danych. Można dodać narzędzie pomocnicze, jeśli jest potrzebne do pozyskania, przetworzenia lub sprawdzenia danych. Nie należy instalować i wykonywać ćwiczeń ze wszystkich programów.

W `docs/processing.md` należy dodać krótką sekcję:

```markdown
### Dobór narzędzi
- Źródło i format danych: ...
- Narzędzie główne: ...
- Dlaczego pasuje do tego źródła i zadania: ...
- Narzędzie pomocnicze (jeśli potrzebne): ...
- Wynik zapisany w repozytorium: ...
```

Następnie należy, korzystając z wybranego narzędzia lub zestawu narzędzi:

1. sprawdzić znaczenie, typy, jednostki i braki w polach istotnych dla problemu;
2. wykonać uzasadnione przekształcenia w sposób możliwy do powtórzenia — np. skryptem, notebookiem albo zapytaniem SQL;
3. sprawdzić wynik ponownym uruchomieniem procedury lub zapytania;
4. przygotować wykres, jeśli pomaga ocenić dane; jeśli nie ma odpowiedniej zmiennej, wykonać inną kontrolę jakości i zapisać powód;
5. zapisać w `docs/processing.md` co najmniej jedną decyzję wynikającą z analizy.

Pod wykresem należy podać źródło danych, nazwę zmiennej i jednostkę, liczbę wykorzystanych obserwacji, liczbę braków oraz krótki wniosek. Dla danych syntetycznych trzeba zaznaczyć, że wynik demonstruje działanie procedury, a nie opisuje rzeczywistej populacji.

Każda osoba powinna odpowiadać za konkretny rezultat, np. pozyskanie próbki, kontrolę jakości, regułę czyszczenia, interpretację wykresu albo zapytanie SQL. Nie trzeba dzielić zespołu według programów — wkład należy przypisać do zadania i zapisać w historii repozytorium.

W publicznym repozytorium należy zachować kod, dozwoloną próbkę i opis analizy. Zrzuty oraz pliki Orange także mogą zawierać dane — przed publikacją trzeba sprawdzić ich zawartość.

### 7. Wsparcie analizy z użyciem asystenta AI (opcjonalnie)

**Kiedy rozważyć:** gdy zespół chce uzyskać pomoc w profilowaniu lub interpretacji danych. Wtyczka i skille są dodatkiem — nie trzeba ich instalować ani używać, aby zrealizować Lab 3. Wyniki agenta należy sprawdzić samodzielnie.

W katalogu wtyczek Codexa należy wyszukać **Data** — tak nazywa się wtyczka dostępna dla użytkownika. Pomaga analizować pytania biznesowe i produktowe, wyjaśniać zmiany wskaźników, definiować KPI, oceniać wiarygodność danych oraz przygotowywać raporty, wykresy, dashboardy i notebooki. Może korzystać z podłączonych baz i narzędzi BI, a także z dokumentów, arkuszy, plików i danych wklejonych do rozmowy. Dostępne źródła zależą od konfiguracji i uprawnień. Wtyczka pozwala również tworzyć wielokrotnego użytku kontekst analityczny na podstawie definicji miar, przykładów dashboardów i raportów, materiałów projektowych oraz preferencji zespołu. Szczegóły: [używanie wtyczki Data w Codexie](https://help.openai.com/en/articles/20001518-using-the-data-plugin-in-chatgpt-work-and-codex).

W Codexie należy zainstalować **Data** z katalogu wtyczek. Następnie w zadaniu należy otworzyć **Sources → Use plugins** i wybrać zainstalowaną wtyczkę. Przykładowe polecenie: „Sprawdź jakość pliku `data/raw/próbka.csv`: oceń braki, duplikaty, typy i wartości odstające. Nie poprawiaj danych bez uzasadnienia; pokaż, jak zweryfikować wyniki”. Wtyczka może też poprosić o podłączenie źródła danych, jeśli analiza wymaga niedostępnego jeszcze narzędzia.

Pakiet w repozytorium [`openai/plugins`](https://github.com/openai/plugins/tree/main/plugins/data-analytics) nosi nazwę **Data Analytics** i zawiera zestaw skilli oraz pliki przykładowej wtyczki. Nie jest to nazwa, której należy szukać w katalogu wtyczek Codexa. Skille można przejrzeć w katalogu [`skills`](https://github.com/openai/plugins/tree/main/plugins/data-analytics/skills), a ich zastosowania w [README pakietu](https://github.com/openai/plugins/blob/main/plugins/data-analytics/README.md).

Najprzydatniejsze skille do pracy z danymi:

- [`analyze-data-quality`](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/analyze-data-quality/SKILL.md) — wstępna ocena jednostki obserwacji, aktualności, braków, duplikatów, łączeń i ryzyk w danych;
- [`validate-data`](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/validate-data/SKILL.md) — kontrola źródeł, metodologii, obliczeń, pułapek analitycznych i siły wniosków;
- [`jupyter-notebooks`](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/jupyter-notebooks/SKILL.md) — przygotowanie czytelnego i możliwego do ponownego uruchomienia notebooka w Pythonie lub SQL;
- [`visualize-data`](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/visualize-data/SKILL.md) — dobór wykresu, opisów i sposobu prezentacji danych;
- [`metric-diagnostics`](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/metric-diagnostics/SKILL.md) — badanie przyczyn zmian wskaźnika z rozdzieleniem potwierdzonych przyczyn od hipotez;
- [`design-kpis`](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/design-kpis/SKILL.md) — planowanie wskaźników, ich czynników, zabezpieczeń i sposobów walidacji.

#### Instalacja skilla — tylko gdy zespół chce użyć agenta

Wtyczka **Data** z katalogu Codexa i skille z repozytorium `Data Analytics` to dwa sposoby pracy. Wtyczkę **Data** instaluje się w Codexie z katalogu wtyczek. W Antigravity można dodać pojedynczy skill z repozytorium i użyć go jako instrukcji dla agenta; nie przenosi to wtyczki Data ani jej połączeń z aplikacjami.

##### Pobranie skilla

1. Należy otworzyć [repozytorium OpenAI Plugins](https://github.com/openai/plugins) i wybrać **Code → Download ZIP**.
2. Pobrany plik ZIP należy rozpakować.
3. W rozpakowanym folderze należy przejść do `plugins/data-analytics/skills/` i wybrać potrzebny skill, np. `analyze-data-quality`.
4. Należy skopiować cały folder tego skilla — nie sam plik `SKILL.md`. W folderze powinien znajdować się `SKILL.md` oraz ewentualne materiały pomocnicze.

Pakiet jest oznaczony w manifeście jako **Proprietary**. Dlatego skill należy zainstalować w osobistym katalogu użytkownika, a nie dodawać do publicznego repozytorium zespołu. Katalog projektu `.agents/skills/` można wykorzystać tylko wtedy, gdy pliki skilla nie zostaną opublikowane.

##### Codex — instalacja skilla

Należy skopiować folder, np. `analyze-data-quality`, do osobistego katalogu skilli Codexa:

```text
Windows: %USERPROFILE%\.agents\skills\analyze-data-quality\
macOS/Linux: ~/.agents/skills/analyze-data-quality/
```

W razie potrzeby należy utworzyć brakujące foldery `skills` i `analyze-data-quality`. Po uruchomieniu Codexa w katalogu projektu skill należy wywołać przez wpisanie `$` i wybranie `analyze-data-quality` z listy albo przez wpisanie `$analyze-data-quality`. Jeśli skill nie pojawia się na liście, należy ponownie uruchomić Codex.

Wtyczkę **Data** instaluje się osobno: w katalogu wtyczek należy znaleźć **Data** i wybrać instalację. W zadaniu Codexa należy następnie otworzyć **Sources → Use plugins** i wybrać **Data**. Do samej analizy pliku CSV wystarczy lokalny skill; wtyczka Data przydaje się do szerszych pytań analitycznych i pracy z podłączonymi źródłami.

##### Google Antigravity — instalacja skilla

Antigravity IDE wczytuje skille z katalogu osobistego albo z katalogu bieżącego projektu. Zalecana instalacja osobista wygląda tak:

```text
Windows: %USERPROFILE%\.gemini\config\skills\analyze-data-quality\
macOS/Linux: ~/.gemini/config/skills/analyze-data-quality/
```

Po skopiowaniu całego folderu skilla należy otworzyć Antigravity i sprawdzić, czy skill jest widoczny w panelu agenta w **Customizations**. W nowej rozmowie można wpisać `/analyze-data-quality`, aby wywołać go bezpośrednio. Można też opisać zadanie zwykłym językiem — Antigravity może dobrać skill na podstawie jego opisu.

Jeśli skill ma być dostępny wyłącznie w jednym projekcie, należy zamiast katalogu osobistego skopiować go do `<katalog-projektu>/.agents/skills/analyze-data-quality/`. W publicznym repozytorium nie należy publikować pobranych plików skilla.

Szczegóły: [skille w Codexie](https://developers.openai.com/codex/skills) oraz [skille w Antigravity](https://antigravity.google/docs/skills?app=antigravity-ide). Jeśli zespół zdecyduje się użyć skilla, należy przekazać mu wyłącznie dozwoloną próbkę, a kontrole i wnioski zweryfikować samodzielnie. Konfiguracja MCP nie jest wymagana.

#### Przykładowa analiza jakości danych

W Lab 3 warto przede wszystkim wykorzystać `analyze-data-quality`. Agentowi należy przekazać dozwoloną próbkę, cel analizy, jednostkę obserwacji, znaczenie pól, jednostki, źródło oraz znane reguły jakości. W treści wiadomości należy poprzedzić polecenie składnią właściwą dla używanego narzędzia, a następnie uzupełnić przykładowy opis:

> Należy przeanalizować plik `data/raw/próbka.csv`. Jedna obserwacja oznacza [opisać jednostkę], pola oznaczają [opisać najważniejsze kolumny i jednostki], a dane pochodzą z [podać źródło]. Należy sprawdzić typy, braki, duplikaty i wartości poza znanymi regułami. Podejrzanych rekordów nie należy automatycznie usuwać ani poprawiać. Należy przedstawić wyniki kontroli, zaproponować kod możliwy do ponownego uruchomienia i wskazać ograniczenia oceny.

Wyniki należy sprawdzić w dokumentacji źródła i uruchomić zaproponowane kontrole. W repozytorium należy zapisać reguły, kod i decyzje zespołu, a nie samą odpowiedź agenta. Nie należy przekazywać agentowi danych osobowych, poufnych próbek, haseł ani kluczy API.

### 8. Inne narzędzia opcjonalne

- [OpenRefine](https://openrefine.org/) — przy dużej liczbie niespójnych nazw i literówek.
- [JASP](https://jasp-stats.org/) lub [jamovi](https://www.jamovi.org/) — gdy projekt wymaga klasycznych analiz statystycznych.
- [Frictionless](https://framework.frictionlessdata.io/) — do opisania schematu i automatycznej walidacji plików.
- [marimo](https://docs.marimo.io/) — jako alternatywne środowisko notebooków Pythona, zapisujące pracę w plikach `.py`.

Agenta można też wykorzystać do wyjaśnienia kodu; jego sugestie należy samodzielnie sprawdzić. Opis wtyczki Data i skilli znajduje się w rozdziale [Wsparcie analizy z użyciem asystenta AI](#7-wsparcie-analizy-z-użyciem-asystenta-ai-opcjonalnie). Konfiguracja MCP nie jest wymagana w tym ćwiczeniu.

## Zadania samodzielne

1. Umieścić surowe dane w katalogu `data/raw/` jako niezmienioną próbkę wyjściową oraz zaktualizować w `docs/data.md` dokładne parametry ich pozyskania lub procedurę pomiaru.
2. Uzupełnić słownik co najmniej pięciu najważniejszych pól.
3. Wybrać narzędzie główne i — jeśli jest potrzebne — pomocnicze, uzasadnić ich dobór do źródła i zadania oraz zapisać go w sekcji „Dobór narzędzi” pliku `docs/processing.md`, korzystając z szablonu w przewodniku.
4. Wykryć co najmniej trzy problemy jakościowe albo udokumentować trzy wykonane kontrole.
5. Przygotować skrypt lub notebook wykonujący co najmniej trzy transformacje.
6. Porównać liczbę rekordów i strukturę danych przed oraz po przetworzeniu.
7. Przetestować powtarzalność procedury: usunąć poprzedni plik wynikowy z `data/processed/`, uruchomić skrypt ponownie z terminala albo wykonać wszystkie komórki notebooka w nowej sesji, a następnie sprawdzić, czy wynik został odtworzony bez błędów i ma oczekiwaną strukturę.
8. Opisać decyzję, której nie można jeszcze podjąć z powodu brakujących lub niewystarczających danych, i zapisać ją w sekcji „Ograniczenia” pliku `docs/processing.md`.

Każdy członek zespołu powinien mieć własny rezultat: pozyskaną część danych, wpis w słowniku, kontrolę jakości, fragment skryptu, transformację, opis ograniczenia albo sprawdzenie powtarzalności.

## Rezultat do zapisania

- surowa próbka danych albo instrukcja jej ponownego pobrania;
- przetworzona próbka w ustalonym formacie;
- słownik najważniejszych pól;
- skrypt lub notebook przygotowania danych;
- instrukcja w głównym `README.md` projektu: wymagane środowisko i pakiety oraz sposób uruchomienia przetwarzania;
- opis czyszczenia, transformacji i kontroli jakości;
- uzasadnienie doboru narzędzi w `docs/processing.md`;
- informacja o ograniczeniach i powtarzalności;
- commit wskazujący indywidualny wkład każdego członka zespołu.
