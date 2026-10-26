---
title: "Laboratorium 4: Metody analityczne, symulacyjne i eksperymentalne"
permalink: /2026-2027/lab4/
---

# Laboratorium 4: Metody analityczne, symulacyjne i eksperymentalne

**Specjalność: Systemy informatyczne w zarządzaniu**

## Cel zajęć

Na tych zajęciach należy wykorzystać dane przygotowane w Lab 3 do porównania dwóch sposobów rozwiązania konkretnego problemu projektu. Należy dobrać metodę, uzasadnić ją na podstawie literatury, przeprowadzić obliczenia lub eksperyment oraz zapisać wynik i jego ograniczenia.

Punktem odniesienia jest **wariant bazowy** (ang. *baseline*): prosta reguła lub obecny sposób działania, z którym porównuje się proponowane rozwiązanie. Przykładem jest prognoza „jutro tyle samo co dziś”, obsługa według kolejności zgłoszeń albo stały próg alarmu. Wariant bardziej złożony nie musi uzyskać lepszego wyniku.

## Przygotowanie przed zajęciami

Należy przygotować:

- wymaganie z `docs/problem.md`, które ma zostać sprawdzone;
- dozwoloną próbkę w `data/processed/`, słownik pól i opis ograniczeń z Lab 3;
- działające narzędzie do obliczeń oraz możliwość odtworzenia przygotowania danych;
- dwa potencjalnie przydatne źródła dotyczące metody lub podobnego problemu, do zweryfikowania podczas zajęć.

Przed zajęciami należy wybrać jeden z poniższych przykładów: prognozowanie, regresję albo symulację kolejki, i sprawdzić jego uruchomienie. Podczas zajęć należy dostosować ten przykład lub istniejący kod projektu, a nie budować nową bibliotekę obliczeniową od podstaw. Pozostałe ścieżki służą do samodzielnego zapoznania się z możliwościami narzędzi.

Pakiety `pandas`, `statsmodels` i `simpy` należy instalować w wirtualnym środowisku projektu, nie w systemowym Pythonie. Należy wykorzystać istniejące środowisko; jeśli go nie utworzono, trzeba w katalogu repozytorium wykonać `python -m venv .venv`. Środowisko o nazwie `.venv` należy aktywować w terminalu:

```powershell
# Windows — PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
source .venv/bin/activate
```

Należy sprawdzić interpreter poleceniem `python -c "import sys; print(sys.executable)"`: ścieżka powinna prowadzić do środowiska projektu. Dopiero wtedy należy wykonać polecenia `python -m pip install ...` z wybranej ścieżki i uruchamiać skrypty w tym samym terminalu. W notebooku trzeba wybrać jądro korzystające z tego samego środowiska. Jeśli środowisko ma inną nazwę niż `.venv`, należy odpowiednio zmienić ścieżki; jego katalogu nie należy dodawać do repozytorium.

Jeżeli rzeczywiste dane są jeszcze niedostępne, można wykonać porównanie na jawnie oznaczonej próbce syntetycznej. Należy wtedy sprawdzić działanie procedury i zapisać, jakie dane rzeczywiste będą potrzebne do oceny jej użyteczności. Wynik na danych syntetycznych nie potwierdza skuteczności rozwiązania w rzeczywistym zastosowaniu.

## Rezultat pracy

Należy rozszerzyć istniejące repozytorium o:

```text
projekt-zespolu/
├── README.md                  # instrukcja uruchomienia porównania
├── data/processed/            # istniejąca, niezmieniana próbka z Lab 3
├── docs/
│   └── experiment.md          # pytanie, źródła, metoda, warunki, wyniki i ograniczenia
├── scripts/
│   └── compare_methods.py     # albo notebook, skrypt SQL lub zapis analizy w użytym narzędziu
├── results/
│   └── lab4/
│       ├── comparison.csv     # porównanie wariantu bazowego i metody
│       └── observations.csv   # prognozy, wyniki powtórzeń albo pomiary jednostkowe
└── examples/
    └── lab4/                  # tylko jeśli wykonywana jest demonstracja z instrukcji
```

Jeżeli wymagane są dodatkowe pakiety, należy zaktualizować plik zależności. W przypadku notebooka, SQL lub aplikacji statystycznej należy zapisać plik pozwalający odtworzyć analizę oraz dokładny sposób jej uruchomienia. Sam zrzut ekranu nie zastępuje obliczeń ani wyników liczbowych. W repozytorium wolno publikować wyłącznie dozwolone dane i wyniki, bez danych osobowych, haseł i kluczy API.

## Dobór metody do projektu

Należy wybrać jedną ścieżkę odpowiadającą problemowi. Nie trzeba wykonywać wszystkich rodzajów analizy.

| Problem projektu | Wariant bazowy | Metoda do porównania | Przykładowa miara |
|---|---|---|---|
| Prognozowanie dziennej liczby zgłoszeń lub zużycia energii | ostatnia znana wartość | średnia z poprzednich okresów lub prosta regresja | średni błąd bezwzględny w zgłoszeniach lub kWh |
| Wykrywanie nieprawidłowych pomiarów | stały próg ustalony z uzasadnieniem | próg zależny od pory lub rozkładu danych | liczba fałszywych alarmów i pominiętych nieprawidłowości na oznaczonych przypadkach |
| Planowanie obsługi lub liczby stanowisk | obecna liczba stanowisk i kolejność obsługi | symulacja dodatkowego stanowiska lub zmiany reguły kolejki | czas oczekiwania, liczba obsłużonych spraw i koszt zasobów |
| Analiza kosztów procesu | jeden koszt jednostkowy dla wszystkich przypadków | oszacowanie kosztu według rodzaju sprawy lub model regresyjny | błąd oszacowania kosztu w PLN |
| Dobór sposobu wyszukiwania lub przetwarzania danych | obecny algorytm lub zapytanie | alternatywny algorytm, indeks albo inna wielkość partii | czas wykonania przy zachowaniu tego samego poprawnego wyniku |

Należy określić, co oznacza pojedyncza obserwacja: np. jeden dzień, pomiar, zgłoszenie albo uruchomienie programu. W modelu przewidującym wynik trzeba wskazać zmienną docelową oraz dane wejściowe dostępne w chwili przewidywania. W symulacji należy określić zasoby, zdarzenia i założenia, a w eksperymencie — zmieniany czynnik i mierzony rezultat.

**Przykład pytania:** „Czy średnia liczby zgłoszeń z trzech poprzednich dni daje mniejszy błąd prognozy na następny dzień niż ostatnia znana wartość?”. Należy dopisać wymaganie projektu, do którego odnosi się odpowiedź, np. planowanie obsady.

## Literatura i podobne rozwiązania

Należy sprawdzić co najmniej dwa źródła: jedno wyjaśniające metodę i jej założenia, drugie opisujące podobne zastosowanie lub metodę alternatywną. Można korzystać z podręczników, artykułów naukowych, raportów z opisaną metodologią i oficjalnej dokumentacji.

Do wyszukania publikacji można wykorzystać Google Scholar lub Semantic Scholar. Należy połączyć nazwę problemu, metodę i kontekst, np. `service desk demand forecasting moving average` lub `queue simulation staffing waiting time`. Trzeba otworzyć materiał źródłowy i sprawdzić odpowiedni rozdział, opis danych lub eksperymentu. Sam abstrakt pozwala ocenić temat, ale może nie wystarczyć do odtworzenia metody.

W `docs/experiment.md` należy zapisać:

| Źródło: autor lub instytucja, tytuł, rok i link/DOI | Metoda lub wniosek przydatny w projekcie | Założenie albo ograniczenie | Co wykorzystano? |
|---|---|---|---|
| R. J. Hyndman, G. Athanasopoulos, *Forecasting: Principles and Practice*, wyd. 3, 2021, [rozdz. 5](https://otexts.com/fpp3/toolbox.html) | Ostatnia znana wartość jako prognoza bazowa; ocena błędu poza danymi do dopasowania | Prognoza korzysta tylko z informacji dostępnych w chwili jej tworzenia | W demonstracji: wariant bazowy i MAE na późniejszych dniach |

Powyższy wiersz jest przykładem zapisu, a nie źródłem obowiązkowym dla każdego projektu. Należy zastąpić go źródłami rzeczywiście wykorzystanymi w swojej pracy. **Przykład uzasadnienia:** „Do próby wybrano średnią z trzech dni i porównanie z ostatnią wartością. Modelu sezonowości tygodniowej nie wybrano, ponieważ próbka obejmuje tylko 12 dni i nie pozwala rzetelnie ocenić powtarzalności tygodniowej”. Wybór okna 3 dni jest tutaj założeniem demonstracji, a nie zaleceniem podręcznika.

Na podstawie źródeł należy krótko uzasadnić wybór metody oraz wskazać jedną alternatywę i powód jej odrzucenia. Czat może pomóc dobrać słowa kluczowe i wyjaśnić metodę, ale podane publikacje, wzory i wnioski należy sprawdzić w oryginalnych źródłach.

## Warunki porównania

Przed uruchomieniem obliczeń należy zapisać w `docs/experiment.md`:

| Element | Co należy ustalić? |
|---|---|
| Pytanie i wymaganie projektu | Jaką decyzję ma wspierać wynik? |
| Dane | Plik i jego wersja, zakres, liczba obserwacji oraz jednostka obserwacji |
| Wariant bazowy i metoda | Konkretna reguła działania każdego wariantu |
| Parametry i założenia | Np. okno 3 dni, próg alarmu, liczba stanowisk, czas symulacji |
| Miara i kierunek poprawy | Np. MAE w kWh — mniej oznacza lepiej |
| Kryterium praktyczne | Jaka poprawa ma znaczenie dla użytkownika i jaki koszt jest dopuszczalny? |
| Warunki oceny | Podział danych, wspólne scenariusze albo liczba powtórzeń pomiaru |
| Próba wrażliwości | Jeden parametr lub warunek i jego druga wartość |
| Odtworzenie | Polecenie lub kroki uruchomienia; przy losowaniu także ziarna generatora |

**Próba wrażliwości** oznacza sprawdzenie, czy wniosek utrzymuje się po zmianie jednego założenia, np. skróceniu odstępów między przyjściami klientów. **Ziarno generatora** ustala początek sekwencji pseudolosowej, dzięki czemu można odtworzyć losowanie w tym samym środowisku. **Rozrzut wyników** pokazuje różnice między powtórzeniami; na początek należy podać minimum i maksimum obok średniej. Samo powtarzanie identycznego, nielosowego obliczenia sprawdza odtwarzalność, ale nie niepewność wyniku.

Przykładowy zapis dla demonstracji prognozowania:

| Element | Przykład wypełnienia |
|---|---|
| Pytanie i wymaganie | Czy średnia z trzech dni poprawia prognozę liczby zgłoszeń potrzebną do planowania obsady? |
| Dane | `examples/lab4/data/popyt.csv`, 12 dni syntetycznych; wersję wskazuje commit repozytorium |
| Warianty | Ostatnia znana wartość oraz średnia z trzech poprzednich dni |
| Ocena | Prognozy jednodniowe dla dni 9–12; po każdym dniu aktualizacja historii; MAE w zgłoszeniach |
| Kryterium praktyczne | Na potrzeby ćwiczenia: spadek MAE o co najmniej 0,5 zgłoszenia bez dodatkowego źródła danych; w projekcie próg należy uzgodnić z potrzebą użytkownika |
| Wrażliwość | Zmiana okna z 3 na 5 dni przy tych samych dniach oceny |
| Ograniczenie | Cztery oceniane dni syntetyczne sprawdzają procedurę, nie potwierdzają skuteczności biznesowej |
| Odtworzenie | Polecenia z części „Porównanie prognoz”; bez losowania |

Należy zastosować reguły właściwe dla wybranej ścieżki:

- **Model analityczny lub ekonometryczny:** przy ocenie przewidywania należy oddzielić dane do dopasowania od danych do oceny. Dla szeregu czasowego trzeba zachować kolejność czasu. Parametry przekształceń zależne od danych, np. średnią do uzupełnienia braków, należy wyznaczać wyłącznie na części dostępnej przed oceną. Trzeba sprawdzić założenia wybranego modelu.
- **Symulacja:** oba warianty należy uruchomić dla tych samych danych wejściowych i porównywalnego okresu. Trzeba zapisać początkowy stan systemu i sposób obsługi spraw niezakończonych na końcu symulacji. Jeśli występuje losowanie, należy użyć tej samej listy ziaren dla obu wariantów i wykonać kilka powtórzeń, zapisując każdy wynik oraz ich rozrzut.
- **Eksperyment pomiarowy:** należy zmienić jeden wybrany czynnik przy zachowaniu pozostałych warunków. Pomiar trzeba powtórzyć, zapisać sprzęt i obciążenie oraz uwzględnić rozgrzewkę i pamięć podręczną, jeśli mają znaczenie. Kolejność wariantów warto zmieniać między powtórzeniami. Należy porównać także poprawność wyniku, nie tylko szybkość.

Dla przykładowej prognozy można użyć **MAE**, czyli średniej z wartości bezwzględnych różnic między wynikiem rzeczywistym a prognozą. Błędy 2, 0 i 4 zgłoszenia dają MAE równe 2 zgłoszenia. Miara ma jednostkę prognozowanej wielkości; niższa wartość oznacza mniejszy błąd.

## Przebieg zajęć — 90 minut

### 1. Pytanie i podział pracy — 0–10 min

Należy:

1. otworzyć wymagania projektu i wyniki Lab 3;
2. wybrać jedno pytanie, wariant bazowy oraz metodę do porównania;
3. wskazać próbkę i miarę oceny;
4. podzielić pracę: implementacja wariantów, sprawdzenie źródeł i założeń, kontrola obliczeń, zapis i interpretacja wyników.

Każda osoba powinna mieć własny rezultat widoczny w repozytorium. Należy uzgodnić format danych i wyników oraz kolejność edycji dokumentacji. Przy równoległej pracy nad kodem należy używać osobnych plików.

### 2. Źródła i warunki porównania — 10–25 min

Należy zweryfikować przygotowane źródła i uzupełnić tabelę warunków w `docs/experiment.md`. Przed obejrzeniem wyników trzeba ustalić parametry obu wariantów, miarę i kryterium praktyczne. Jeżeli próbka nie wystarcza do wiarygodnej oceny, należy zapisać to ograniczenie i wykonać próbę działania procedury.

### 3. Uruchomienie przykładu — 25–35 min

Należy uruchomić jeden przygotowany przykład: prognozowanie, regresję albo kolejkę. Trzeba odszukać dane wejściowe, obie reguły i wynik zbiorczy oraz sprawdzić jeden wynik ręcznie według wskazówek pod kodem. Nie należy wykonywać kolejno wszystkich demonstracji.

### 4. Porównanie na danych projektu — 35–65 min

Należy:

1. dostosować przygotowany kod obu wariantów lub zapisać ich konfiguracje w wybranym narzędziu;
2. uruchomić je zgodnie z ustalonymi warunkami;
3. zapisać wyniki jednostkowe w `results/lab4/observations.csv`, np. datę, wynik rzeczywisty i obie prognozy albo numer powtórzenia, wariant i czas wykonania;
4. obliczyć wspólną miarę i zapisać porównanie w `results/lab4/comparison.csv`;
5. sprawdzić liczebność ocenianych przypadków, braki i zgodność jednostek.

Należy ograniczyć pierwsze porównanie do jednej miary i jednego prostego wariantu alternatywnego. Jeśli rzeczywiste dane nie pozwalają go wykonać, trzeba zastosować opisaną wcześniej próbkę syntetyczną i wskazać brakujące dane; samo uruchomienie niezmienionej demonstracji nie zastępuje pracy nad projektem.

### 5. Próba wrażliwości i interpretacja — 65–80 min

Należy zmienić jeden wcześniej wskazany parametr lub warunek, np. okno 3 dni na 5 dni albo natężenie napływu spraw. Trzeba zapisać dodatkowy wynik osobno i sprawdzić, czy wniosek o wyborze metody się zmienia.

Przed ponownym uruchomieniem należy zmienić katalog wyjściowy na `results/lab4/sensitivity/`, aby zachować podstawowe pliki `results/lab4/comparison.csv` i `results/lab4/observations.csv`. Wyniki próby należy zapisać jako `results/lab4/sensitivity/comparison.csv` i `results/lab4/sensitivity/observations.csv`, a zmieniony parametr opisać w `docs/experiment.md`. W demonstracjach należy zachować tę samą zasadę wewnątrz `examples/lab4/results/`.

Jeżeli po obejrzeniu wyników zmieniane są parametry modelu, oceniane dane służą już do doboru metody. Nie należy przedstawiać tak uzyskanego najlepszego wyniku jako niezależnej oceny końcowej. Należy zaplanować sprawdzenie na innym okresie lub osobnym zbiorze.

### 6. Odtworzenie i zapis — 80–90 min

Inna osoba z zespołu powinna ponownie uruchomić porównanie według instrukcji w `README.md`. Należy porównać wyniki dla tej samej próbki, parametrów i ziaren losowania. W `docs/experiment.md` trzeba zapisać wniosek, ograniczenia i wynik odtworzenia, a następnie wykonać commity własnych rezultatów.

## Przydatne narzędzia

Należy dobrać narzędzie do metody; można pozostać przy środowisku używanym w Lab 3.

| Narzędzie | Do czego wykorzystać? | Co zapisać? |
|---|---|---|
| Python w VS Code lub Jupyter | obliczenia, porównanie reguł, wykresy, powtarzalne eksperymenty | skrypt lub notebook, zależności i wyniki |
| DataGrip i SQL | agregacje, reguły progowe, porównania na danych w bazie | zapytania, sposób odtworzenia tabel i eksport wyników |
| statsmodels | model regresyjny, oszacowanie współczynników i diagnostyka | kod, opis zmiennych, diagnostyka i wyniki |
| SimPy | symulacja kolejek, obsługi i współdzielonych zasobów | model, parametry scenariuszy i wyniki powtórzeń |

### Porównanie prognoz (Python)

Poniższe dane są syntetyczne. Jedna obserwacja oznacza dzień, a `zgloszenia` — liczbę zgłoszeń z tego dnia. Należy zapisać próbkę jako `examples/lab4/data/popyt.csv`:

```csv
data,zgloszenia
2026-10-01,10
2026-10-02,12
2026-10-03,11
2026-10-04,13
2026-10-05,12
2026-10-06,14
2026-10-07,13
2026-10-08,15
2026-10-09,14
2026-10-10,16
2026-10-11,15
2026-10-12,17
```

Należy porównać prognozę na jeden następny dzień: ostatnią znaną wartość oraz średnią z trzech poprzednich dni. Pierwsze osiem dni stanowi początkową historię, a ostatnie cztery — okres oceny. Po ocenie prognozy dla danego dnia jego rzeczywista wartość staje się dostępna do prognozowania następnego dnia. Nie jest to prognoza czterech dni naraz.

Należy zapisać poniższy kod jako `examples/lab4/compare_forecasts.py`. Wystarcza Python 3; skrypt korzysta wyłącznie z biblioteki standardowej.

```python
import argparse
import csv
import math
from datetime import date
from pathlib import Path
from statistics import mean

parser = argparse.ArgumentParser()
parser.add_argument("input", type=Path)
parser.add_argument("output", type=Path, help="katalog wyników")
parser.add_argument("--window", type=int, default=3)
parser.add_argument("--start", type=int, default=8, help="liczba dni początkowej historii")
args = parser.parse_args()

with args.input.open(encoding="utf-8-sig", newline="") as stream:
    rows = list(csv.DictReader(stream))
dates = [date.fromisoformat(row["data"]) for row in rows]
values = [float(row["zgloszenia"]) for row in rows]

if not 1 <= args.window <= args.start < len(rows):
    parser.error("Wymagane: 1 <= window <= start < liczba obserwacji")
if any((b - a).days != 1 for a, b in zip(dates, dates[1:])):
    parser.error("Daty muszą być kolejnymi dniami, bez powtórzeń")
if not all(math.isfinite(v) and v >= 0 and v.is_integer() for v in values):
    parser.error("Liczby zgłoszeń muszą być nieujemnymi liczbami całkowitymi")

observations = []
for i in range(args.start, len(rows)):
    baseline = values[i - 1]
    method = mean(values[i - args.window:i])
    observations.append({
        "data": dates[i].isoformat(),
        "rzeczywiste": values[i],
        "bazowy": baseline,
        "srednia": method,
        "blad_bazowy": abs(values[i] - baseline),
        "blad_srednia": abs(values[i] - method),
    })

comparison = []
for variant, column, window in [
    ("ostatnia_wartosc", "blad_bazowy", 1),
    ("srednia_ruchoma", "blad_srednia", args.window),
]:
    comparison.append({
        "wariant": variant,
        "okno": window,
        "start": args.start,
        "n": len(observations),
        "mae": mean(row[column] for row in observations),
        "jednostka": "zgloszenia",
    })

args.output.mkdir(parents=True, exist_ok=True)
for name, records in [("observations.csv", observations), ("comparison.csv", comparison)]:
    destination = args.output / name
    if destination.resolve() == args.input.resolve():
        parser.error("Wynik nie może nadpisać pliku wejściowego")
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

for result in comparison:
    print(f"{result['wariant']}: MAE={result['mae']:.3f}, n={result['n']}")
```

W terminalu katalogu repozytorium należy wykonać:

```powershell
python examples/lab4/compare_forecasts.py examples/lab4/data/popyt.csv examples/lab4/results/okno3 --window 3
python examples/lab4/compare_forecasts.py examples/lab4/data/popyt.csv examples/lab4/results/okno5 --window 5
```

Dla okna 3 oczekiwane wyniki to:

| Wariant | Liczba ocenianych dni | MAE [zgłoszenia] |
|---|---:|---:|
| Ostatnia znana wartość | 4 | 1,5 |
| Średnia z trzech poprzednich dni | 4 | 1,0 |

Dla 9 października należy ręcznie sprawdzić prognozy: wariant bazowy daje 15, a średnia z 6–8 października wynosi 14. Rzeczywista liczba zgłoszeń to 14, więc błędy wynoszą odpowiednio 1 i 0.

**Ćwiczenie:** należy porównać wyniki dla okien 3 i 5 oraz wskazać, czy ranking metod się zmienił. Następnie trzeba wyjaśnić, dlaczego średnia obejmująca również prognozowany dzień byłaby nieuczciwym porównaniem. Cztery dni syntetyczne wystarczają do sprawdzenia rachunków, ale nie do potwierdzenia skuteczności prognozy w rzeczywistym procesie.

### Zapis obliczeń i wyników (Jupyter)

Jeżeli wybrano notebook, należy utworzyć komórki: opis pytania, wczytanie danych, parametry, wariant bazowy, metoda, ocena i eksport wyników. Komórkę można wykonać przez `Shift+Enter`. Przed oddaniem należy zrestartować sesję obliczeniową i wykonać wszystkie komórki od początku. Trzeba sprawdzić, czy wynik nie zależy od zmiennych utworzonych w poprzedniej sesji. Opis interfejsu i uruchamiania: [dokumentacja Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

![Interfejs Jupyter Notebook z komórką kodu, menu i paskiem narzędzi](https://user-images.githubusercontent.com/591645/229563988-8e3a4d04-6f31-4411-9a6b-9b9b045bc55e.png)

*Rzeczywisty zrzut z dokumentacji Jupyter Notebook. Należy odszukać komórkę kodu, przycisk uruchomienia i menu Kernel służące do zarządzania sesją obliczeniową. Układ może się różnić między wersjami; obraz jest ładowany z zewnętrznego źródła.*

Przy przenoszeniu demonstracji do notebooka należy zastąpić obsługę argumentów terminala komórką z jawnymi parametrami: ścieżką wejściową, katalogiem wyników, oknem i początkiem oceny. Ścieżki trzeba określić względem katalogu roboczego notebooka i opisać w instrukcji uruchomienia.

### Porównanie reguł na tabelach (DataGrip)

Należy wykorzystać połączenie i sposób importu opisane w [Lab 3](../lab3/#3-praca-z-bazą-danych-i-sql-datagrip). Własne zapytania należy zapisać w `scripts/compare_methods.sql`.

1. Utworzyć wspólny zbiór przypadków ocenianych przez oba warianty.
2. Obliczyć wynik obu reguł i błąd lub koszt dla każdego przypadku.
3. Sprawdzić, czy oba warianty obejmują te same identyfikatory i czy brakujące wartości nie zostały pominięte tylko w jednym z nich.
4. Wyeksportować wyniki jednostkowe do `observations.csv`, a agregację do `comparison.csv` w `results/lab4/`.

Przy porównaniu czasu zapytań należy sprawdzić zgodność zwracanych danych, wykonać kilka pomiarów w tych samych warunkach i zapisać każdy czas. Plan wykonania zapytania nie jest pomiarem czasu.

**Przykład w SQLite:** należy zaimportować demonstracyjny `popyt.csv` do tabeli `demo_popyt`, z kolumną `data` jako tekstem ISO `RRRR-MM-DD`, a `zgloszenia` jako liczbą całkowitą. Następnie należy zapisać zapytanie jako `examples/lab4/compare_forecasts.sql` i wykonać je w konsoli DataGrip:

```sql
WITH prognozy AS (
    SELECT data, zgloszenia,
           ROW_NUMBER() OVER (ORDER BY data) AS nr,
           LAG(zgloszenia) OVER (ORDER BY data) AS bazowy,
           AVG(zgloszenia) OVER (
               ORDER BY data ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING
           ) AS srednia
    FROM demo_popyt
)
SELECT data, zgloszenia, bazowy, srednia,
       ABS(zgloszenia - bazowy) AS blad_bazowy,
       ABS(zgloszenia - srednia) AS blad_srednia
FROM prognozy
WHERE nr > 8
ORDER BY data;
```

Zapytanie powinno zwrócić cztery dni, z błędami wariantu bazowego `1, 2, 1, 2` oraz średniej `0, 2, 0, 2`. Aby uzyskać podsumowanie, należy zachować część `WITH`, a końcowy `SELECT` zastąpić zapytaniem `SELECT COUNT(*) AS n, AVG(ABS(zgloszenia - bazowy)) AS mae_bazowy, AVG(ABS(zgloszenia - srednia)) AS mae_srednia FROM prognozy WHERE nr > 8;`. Oczekiwany wynik to `4; 1,5; 1,0`. Obie wersje należy zachować jako osobne zapytania w pliku. Wyniki demonstracji należy eksportować do `examples/lab4/results/sql/`.

**Ćwiczenie:** należy zmienić `3 PRECEDING` na `5 PRECEDING`, bez zmiany ocenianych dni. Trzeba wyjaśnić, dlaczego okno kończy się na `1 PRECEDING`, a nie `CURRENT ROW`. Okno obejmuje wiersze, nie dni kalendarzowe: przed użyciem na własnych danych należy sprawdzić ciągłość dat, unikalność dni i brak pustych wartości. Funkcja `AVG` pomija wartości `NULL`, co bez kontroli zmieniłoby liczbę obserwacji w średniej.

### Modelowanie zależności (statsmodels)

Należy sprawdzić, czy liczba pozycji zamówienia pozwala oszacować koszt jego obsługi lepiej niż jednakowy koszt dla wszystkich zamówień. **Zmienna objaśniana** to przewidywany koszt, a **zmienna objaśniająca** to znana wcześniej liczba pozycji. Regresja liniowa dopasowuje zależność `koszt = stała + współczynnik × liczba pozycji`. **Reszta** to rzeczywisty koszt minus wartość dopasowana dla obserwacji uczącej; dla nowych zamówień należy oceniać błędy prognoz.

W używanym środowisku Pythona należy wykonać `python -m pip install pandas statsmodels`. Należy zapisać poniższy kod jako `examples/lab4/compare_costs.py` i uruchomić go poleceniem `python examples/lab4/compare_costs.py`. Dane są syntetyczne; pierwsze sześć zamówień służy do dopasowania, a kolejne trzy do oceny.

```python
from pathlib import Path
import pandas as pd
import statsmodels.api as sm

data = pd.DataFrame({
    "id": range(1, 10),
    "pozycje": [1, 2, 3, 4, 5, 6, 2, 4, 6],
    "koszt": [12, 16, 16, 20, 20, 24, 15, 19, 23],
})
train, test = data.iloc[:6].copy(), data.iloc[6:].copy()
x_train = sm.add_constant(train[["pozycje"]], has_constant="add")
x_test = sm.add_constant(test[["pozycje"]], has_constant="add")
model = sm.OLS(train["koszt"], x_train).fit()
test["bazowy"] = train["koszt"].mean()
test["regresja"] = model.predict(x_test)
train["dopasowany"] = model.fittedvalues
train["reszta"] = model.resid
comparison = []
for variant in ["bazowy", "regresja"]:
    test[f"blad_{variant}"] = (test["koszt"] - test[variant]).abs()
    comparison.append({"wariant": variant, "n": len(test),
                       "mae_PLN": test[f"blad_{variant}"].mean()})
out = Path("examples/lab4/results/koszty")
out.mkdir(parents=True, exist_ok=True)
test.to_csv(out / "observations.csv", index=False)
train.to_csv(out / "diagnostics.csv", index=False)
pd.DataFrame(comparison).to_csv(out / "comparison.csv", index=False)
print(model.params.round(3).to_string())
print(pd.DataFrame(comparison).round(3).to_string(index=False))
```

Oczekiwane wyniki to stała około 10,4 PLN, współczynnik około 2,171 PLN na pozycję oraz MAE około 3,000 PLN dla wariantu bazowego i 0,257 PLN dla regresji. Dla zamówienia z dwiema pozycjami należy ręcznie obliczyć prognozę `10,4 + 2,1714286 × 2 ≈ 14,743 PLN` i błąd względem 15 PLN. Współczynnik opisuje dopasowanie w tej próbce, a nie udowodniony wpływ dodania pozycji na koszt.

Należy otworzyć `diagnostics.csv` i porównać `reszta` z `pozycje` oraz `dopasowany`. Dla sześciu obserwacji reszty wynoszą w przybliżeniu −0,57; 1,26; −0,91; 0,91; −1,26; 0,57 PLN. W większej próbce warto wykonać wykres punktowy reszt względem wartości dopasowanych: łuk może wskazywać nieliniowość, a rosnąca szerokość pasma — zmienność błędu zależną od kosztu. To kontrola wstępna, nie potwierdzenie wszystkich założeń. Trzeba również sprawdzić, czy kolejne wiersze nie są powiązanymi pomiarami tego samego zamówienia. Sześć rekordów nie wystarcza do wiarygodnej diagnostyki ani wnioskowania statystycznego. Opis dopasowania i dostępnych wyników zawiera [dokumentacja statsmodels](https://www.statsmodels.org/stable/regression.html).

**Ćwiczenie:** należy zmienić koszt wyłącznie pierwszego zamówienia uczącego z 12 na 22 PLN i ponowić obliczenia, zapisując wynik w innym katalogu. Trzeba sprawdzić zmianę MAE obu wariantów i wpływ pojedynczej obserwacji na współczynniki. Nie należy usuwać niewygodnej obserwacji tylko dlatego, że pogarsza dopasowanie.

### Porównanie scenariuszy obsługi (SimPy)

Należy porównać czas oczekiwania czterech spraw przy jednym i dwóch stanowiskach. Przyjęto syntetyczne chwile przyjścia: 0, 2, 4 i 6 minut, obsługę każdej sprawy przez 5 minut oraz kolejkę według kolejności przyjścia. System początkowo jest pusty, a obliczenia kończą się po obsłużeniu wszystkich spraw. Nie występuje losowanie, więc ziarno nie jest potrzebne.

Należy wykonać `python -m pip install simpy`, zapisać kod jako `examples/lab4/compare_queues.py` i uruchomić `python examples/lab4/compare_queues.py`.

```python
import csv
from pathlib import Path
from statistics import mean
import simpy

arrivals = [0, 2, 4, 6]  # minuty od początku obserwacji
service_times = [5, 5, 5, 5]
assert len(arrivals) == len(service_times) and len(arrivals) > 0
assert arrivals == sorted(arrivals) and all(t >= 0 for t in arrivals)
assert all(t > 0 for t in service_times)

def run(capacity):
    env = simpy.Environment()
    desks = simpy.Resource(env, capacity=capacity)
    records = []

    def case(number, arrival, duration):
        yield env.timeout(arrival)
        with desks.request() as request:
            yield request
            start = env.now
            yield env.timeout(duration)
            records.append({"stanowiska": capacity, "id": number,
                            "przyjscie": arrival, "start": start,
                            "koniec": env.now, "czekanie_min": start - arrival})

    for number, (arrival, duration) in enumerate(zip(arrivals, service_times), 1):
        env.process(case(number, arrival, duration))
    env.run()
    assert len(records) == len(arrivals)
    assert all(row["czekanie_min"] >= 0 for row in records)
    return records

observations, comparison = [], []
for capacity in [1, 2]:
    rows = run(capacity)
    observations.extend(rows)
    waits = [row["czekanie_min"] for row in rows]
    comparison.append({"stanowiska": capacity, "n": len(rows),
                       "srednia_min": mean(waits), "maksimum_min": max(waits)})
out = Path("examples/lab4/results/kolejka")
out.mkdir(parents=True, exist_ok=True)
for name, rows in [("observations.csv", observations), ("comparison.csv", comparison)]:
    with (out / name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
for row in comparison:
    print(row)
```

`Environment` przechowuje czas symulacji, `Resource` reprezentuje stanowiska, a `request()` powoduje oczekiwanie na wolne miejsce. `timeout()` przesuwa dany proces do następnego zdarzenia, nie zatrzymując pozostałych spraw. Mechanizm kolejki opisano w [samouczku SimPy o zasobach](https://simpy.readthedocs.io/en/latest/simpy_intro/shared_resources.html).

Należy porównać `observations.csv` i `comparison.csv` z oczekiwanym wynikiem:

| Stanowiska | Oczekiwanie spraw 1–4 [min] | Średnia [min] | Maksimum [min] |
|---|---|---:|---:|
| 1 | 0; 3; 6; 9 | 4,5 | 9 |
| 2 | 0; 0; 1; 1 | 0,5 | 1 |

Dla trzeciej sprawy przy dwóch stanowiskach należy sprawdzić ręcznie: przyjście w minucie 4, zwolnienie pierwszego stanowiska w minucie 5, oczekiwanie 1 minuta. **Ćwiczenie:** należy zmienić przyjścia na `[0, 1, 2, 3]`, zachować czasy obsługi i zapisać wyniki w osobnym katalogu. Trzeba porównać oba warianty ponownie. Następnie należy wskazać, jaki koszt dodatkowej obsady należałoby poznać przed rekomendacją drugiego stanowiska. Mniejsza kolejka sama nie oznacza opłacalności.

W projekcie należy zastąpić obie listy czasami wynikającymi z danych lub jawnie uzasadnionych założeń. Trzeba sprawdzić jednostki, kolejność przyjść, przerwy w pracy i różnice czasu obsługi. Jeżeli model zostanie rozszerzony o losowanie, należy najpierw wygenerować wspólny scenariusz wejściowy dla obu wariantów, a następnie powtórzyć porównanie dla ustalonej listy ziaren. Nie należy utożsamiać czterech spraw demonstracyjnych z reprezentatywnym dniem pracy.

### Dostosowanie przykładu do danych projektu

Należy wybrać jeden wiersz i zapisać odpowiedniki pól w `docs/experiment.md` przed zmianą kodu. Demonstrację trzeba pozostawić w `examples/lab4/`, a wersję projektową zapisać w `scripts/` lub notebooku projektu.

| Ścieżka | Co zastąpić? | Co ustalić przed uruchomieniem? |
|---|---|---|
| Prognozowanie | `data`, `zgloszenia` i jednostkę wyniku | Stały odstęp obserwacji, początek oceny, dostępność historii. Dla kWh należy dopuścić wartości ułamkowe zamiast kontroli liczby całkowitej; nie wolno bez sprawdzenia usuwać kontroli braków i skończoności wartości. |
| Regresja | Ramkę syntetyczną przez odczyt własnego pliku; `pozycje` przez cechę znaną przed wynikiem; `koszt` przez cel | Podział danych właściwy dla projektu, np. wcześniejsze/późniejsze okresy albo rozłączne grupy klientów. Nie należy kopiować podziału 6/3 ani dopuszczać tych samych spraw do obu części. |
| Symulacja | Przyjścia, czasy obsługi, liczbę stanowisk | Początek obserwacji, jednostkę czasu, stan początkowy, regułę obsługi i koszt zasobów. Należy opisać, które wartości zmierzono, a które założono. |

Nie należy ograniczać dostosowania do zmiany nazwy pliku. Wyniki własnego projektu trzeba zapisywać w `results/lab4/`, a próbę wrażliwości w osobnym podkatalogu. W przypadku problemu niepasującego do przykładów można porównać dwie proste reguły SQL lub konfiguracje istniejącego rozwiązania, zachowując wspólną miarę i te same przypadki oceny.

### Wsparcie pracy przez agenta AI

Agent może pomóc zaimplementować oba warianty, sprawdzić wzór miary i znaleźć błąd w obliczeniach. Należy przekazać mu dozwoloną próbkę, znaczenie pól i ustalone warunki porównania, np.:

> Przygotuj porównanie [wariant bazowy] i [metoda] na pliku [ścieżka]. Jedna obserwacja oznacza [...], a miarą jest [...]. Zachowaj ustalony podział danych i parametry [...]. Zapisz wyniki jednostkowe i zbiorcze. Wskaż, gdzie może wystąpić wykorzystanie informacji niedostępnej w chwili podejmowania decyzji. Nie zmieniaj parametrów po obejrzeniu wyników bez wyraźnego oznaczenia nowego eksperymentu.

Należy samodzielnie sprawdzić co najmniej jeden wynik jednostkowy i obliczenie miary. W dokumentacji trzeba opisać, do czego użyto agenta i jak sprawdzono jego wynik.

## Interpretacja wyniku

W `docs/experiment.md` należy zapisać porównanie:

| Wariant i parametry | Dane lub scenariusz | Liczba przypadków / powtórzeń | Miara, jednostka i wynik | Koszt lub ograniczenie |
|---|---|---:|---|---|
| Bazowy: ... | ... | ... | ... | ... |
| Metoda: ... | ... | ... | ... | ... |
| Próba wrażliwości: ... | ... | ... | ... | ... |

Następnie należy odpowiedzieć:

1. Który wariant uzyskał lepszy wynik i o ile? Czy różnica spełnia ustalone kryterium praktyczne?
2. Czy poprawa uzasadnia koszt, złożoność albo dodatkowe dane?
3. Czy zmiana parametru lub warunku zmieniła wniosek?
4. Którego wniosku nie można wyciągnąć z tej próby i czego brakuje do jego sprawdzenia?

Należy odróżniać obserwowaną zależność od wpływu przyczynowego. Przykładowo mniejsze zużycie energii w cieplejszym tygodniu nie dowodzi skuteczności nowego sterowania. W symulacji zmniejszenie kolejki po dodaniu stanowiska nie potwierdza jeszcze, że korzyść pokryje koszt jego utrzymania. Można pozostawić wariant bazowy lub zapisać, że dostępne wyniki nie pozwalają rozstrzygnąć wyboru.

## Zadania samodzielne

1. Sformułować jedno pytanie powiązane z wymaganiem projektu i zweryfikować dwa źródła uzasadniające dobór metody.
2. Zapisać wariant bazowy, wybraną metodę, parametry, miarę i warunki porównania w `docs/experiment.md`.
3. Uruchomić oba warianty na wspólnych przypadkach lub w porównywalnych warunkach; zapisać procedurę oraz wyniki jednostkowe i zbiorcze.
4. Sprawdzić ręcznie przynajmniej jeden wynik i obliczenie miary; przy powtórzeniach opisać także rozrzut wyników.
5. Wykonać jedną próbę wrażliwości i zapisać wyniki w `results/lab4/sensitivity/`, bez nadpisywania wyników podstawowych; udokumentować zmieniony parametr.
6. Uzasadnić wybór wariantu albo brak rozstrzygnięcia oraz zapisać ograniczenia.
7. Odtworzyć porównanie według `README.md` i zapisać wynik sprawdzenia. Wykonać commit własnego rezultatu.

## Rezultat do zapisania

- `docs/experiment.md`: pytanie, wymaganie, źródła, uzasadnienie metody, warunki, porównanie i ograniczenia;
- procedura uruchamiająca wariant bazowy i wybraną metodę;
- `results/lab4/`: wyniki jednostkowe, porównanie i osobny wynik próby wrażliwości;
- zaktualizowany `README.md`: środowisko, zależności, dane wejściowe, parametry i sposób odtworzenia;
- widoczny w historii repozytorium wkład każdego członka zespołu.

## Materiały pomocnicze

- Hyndman i Athanasopoulos, [Forecasting: Principles and Practice — proste prognozy i ocena błędu](https://otexts.com/fpp3/toolbox.html): punkt wyjścia dla projektów prognostycznych.
- [NIST/SEMATECH — planowanie eksperymentów](https://www.itl.nist.gov/div898/handbook/pri/section1/pri11.htm): ustalanie czynników, warunków i mierzonych rezultatów.
- [scikit-learn — typowe błędy i wyciek informacji](https://scikit-learn.org/stable/common_pitfalls.html): kontrola podziału danych i przekształceń zależnych od próby.
