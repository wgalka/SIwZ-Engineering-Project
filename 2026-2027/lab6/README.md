---
title: "Laboratorium 6: Realizacja projektu"
permalink: /2026-2027/lab6/
---

# Laboratorium 6: Realizacja projektu

**Specjalność: Systemy informatyczne w zarządzaniu**

## Cel zajęć

Na tych zajęciach należy połączyć przygotowane dane, wybraną metodę i interfejs w jeden działający przepływ projektu. Należy wykorzystać kod z Lab 3–4 i projekt techniczny z Lab 5. Rezultatem ma być uruchamialna wersja, a nie wyłącznie tablica zadań ani niezintegrowane fragmenty kodu.

> 💡 **MVP** oznacza w tym przedmiocie pierwszą minimalną, ale działającą wersję projektu, która realizuje jeden najważniejszy przepływ użytkownika od wejścia do wyniku. Interfejsem może być także polecenie terminala lub notebook, jeżeli odpowiada potrzebom użytkownika.

## Przygotowanie przed zajęciami

Należy przygotować aktualne repozytorium, działające środowisko, dozwoloną próbkę danych oraz wynik porównania metod. Trzeba sprawdzić, czy każda osoba ma uprawnienia do pracy na własnej gałęzi i czy kod analizy daje się uruchomić.

Należy ustalić główną gałąź repozytorium: `main` albo `master`. Przykłady poleceń poniżej zakładają `main`; trzeba zastąpić tę nazwę, jeśli projekt korzysta z innej gałęzi. W Pythonie należy używać środowiska wirtualnego projektu opisanego w Lab 4.

## Rezultat pracy

Należy rozszerzać istniejącą strukturę, bez zmiany nazw katalogów tylko po to, aby dopasować je do przykładu:

```text
README.md                 # instalacja, uruchomienie, dane, oczekiwany wynik
src/ lub scripts/         # zintegrowany kod własnego projektu
tests/                    # istniejące i nowe kontrole
docs/implementation.md    # stan przepływu, ograniczenia i wyniki integracji
requirements.txt          # dla Pythona; odpowiednik w innej technologii
.env.example              # tylko jeśli projekt używa zmiennych środowiskowych
examples/lab6/            # demonstracja, nie kod własnego rozwiązania
```

W `docs/implementation.md` należy zapisać polecenie głównego przepływu, sprawdzoną wersję kodu, wynik uruchomienia oraz znane ograniczenia. Istniejące opisy wymagań i danych należy linkować, nie kopiować.

## Przebieg zajęć — 90 minut

### 1. Zakres i zadania — 0–15 min

Należy wybrać UC-01 lub inny główny przypadek z Lab 5. Trzeba ustalić jeden widoczny wynik oraz podzielić pracę na zadania z właścicielem i kryterium odbioru.

| Zadanie | Mierzalny rezultat | Sposób sprawdzenia |
|---|---|---|
| Wczytanie i kontrola danych | Funkcja zgodna z ustalonym kontraktem | Poprawna próbka przyjęta, brak kolumny odrzucony |
| Podłączenie metody | Wynik obliczony z rzeczywistych danych wejściowych | Zgodność z ręcznym wynikiem z Lab 4 |
| Interfejs i eksport | Jedno polecenie lub działająca operacja w aplikacji | Wynik z jednostką i parametrami zapisany w uzgodnionym miejscu |
| Integracja i dokumentacja | Instrukcja oraz sprawdzenie pełnego przepływu | Uruchomienie przez osobę inną niż autor integracji |

Role trzeba dostosować do liczebności zespołu. Nie należy tworzyć zadania „robić backend”; trzeba wskazać konkretną funkcję lub zachowanie. Współpraca nad jednym zadaniem jest dopuszczalna, ale każda osoba powinna umieć wskazać własny rezultat.

### 2. Uzgodnienie połączeń — 15–25 min

Należy zapisać nazwy funkcji lub endpointów, format wejść i wyjść oraz sposób zgłaszania błędów. Trzeba uzgodnić małą wspólną próbkę i oczekiwany wynik. Przykład: moduł danych zwraca listę dziennych liczebności, analiza przyjmuje listę i okno, a interfejs zapisuje prognozę razem z jednostką.

Przed równoległą edycją należy rozdzielić pliki. Jeżeli istniejący skrypt łączy wszystko w jednym miejscu, można wydzielić funkcję analityczną i osobną funkcję uruchomieniową. Nie należy przebudowywać całej aplikacji bez potrzeby.

### 3. Implementacja i sprawdzenie zmian — 25–60 min

Każda osoba powinna wykonać ustalone zadanie na swojej gałęzi, sprawdzić poprawne wejście i co najmniej jeden błąd oraz otworzyć Pull Request. Należy połączyć istniejące moduły; niewielkie funkcje można przygotować na podstawie demonstracji poniżej.

Trzeba obsłużyć brak danych, niepoprawny format i niemożność zapisu wyniku. Nie należy zastępować błędu pustym raportem ani fikcyjną wartością. Komunikat powinien wskazywać przyczynę, bez ujawniania sekretów i danych osobowych.

### 4. Przegląd i integracja — 60–80 min

Inna osoba powinna sprawdzić różnicę w Pull Requeście i uruchomić opisany przypadek. Należy scalać zależne zmiany w uzgodnionej kolejności, a po scaleniu ponownie uruchomić cały przepływ. Samo działanie modułu na gałęzi autora nie potwierdza integracji.

Jeżeli pojawi się konflikt, trzeba wspólnie ustalić docelowe zachowanie. Nie należy automatycznie wybierać całej wersji „ours” albo „theirs”, ponieważ można w ten sposób zgubić poprawki innej osoby.

### 5. Odtworzenie i podsumowanie — 80–90 min

Osoba nieodpowiedzialna za główną implementację powinna uruchomić projekt według `README.md`. Należy zapisać wynik, poprawić brakujące kroki i zaznaczyć w Issues rzeczywisty stan zadań. Niedziałające elementy trzeba pozostawić jako otwarte zadania z opisem blokady.

Po zajęciach należy dokończyć uzgodniony zakres w pracy własnej. Na zajęciach należy doprowadzić do działania jedną operację, a nie próbować ukończyć całego rozbudowanego systemu.

## Przydatne narzędzia

| Narzędzie | Do czego użyć? | Co sprawdzić? |
|---|---|---|
| GitHub Issues i Pull Requests | podział pracy, przegląd i scalanie | kryteria odbioru oraz działanie zmiany |
| VS Code lub IDE projektu | uruchomienie, debugowanie, odczyt błędu | wartości na granicy modułów |
| Terminal i menedżer zależności | powtarzalne środowisko i polecenia | instalacja zgodna z README |
| Bruno / Postman, jeśli projekt ma API | kontrola rzeczywistej odpowiedzi | kod odpowiedzi, pola i przypadek błędny |

Nie trzeba przenosić projektu do Pythona ani dodawać API tylko dlatego, że pojawia się w przewodniku.

Należy wybrać jeden interfejs: CLI do pracy wsadowej, FastAPI do komunikacji między systemami albo Streamlit do interakcji z użytkownikiem. Zapis SQLite jest niezależną opcją przechowywania danych. Nie trzeba łączyć wszystkich wariantów. Dodatkowe pakiety należy instalować w aktywnym środowisku wirtualnym i zapisać ich sprawdzone wersje w zależnościach projektu.

### Przejście od zadania do scalonej zmiany (GitHub / Git)

W **Issues → New issue** należy opisać konkretne zachowanie. Przykład:

```markdown
## Cel
Obsłużyć zbyt krótką historię danych w operacji prognozowania.
## Kryteria odbioru
- Dla 2 obserwacji i okna 3 pojawia się czytelny komunikat.
- Nie powstaje nowy plik prognozy.
- Poprawna próbka nadal daje oczekiwany wynik.
## Zakres
Walidacja, test i opis komunikatu; bez zmiany metody prognozowania.
```

Należy przypisać wykonawcę. Przed utworzeniem gałęzi trzeba zakończyć lub bezpiecznie zachować dotychczasową pracę i sprawdzić `git status`. Przy czystym stanie można wykonać:

```bash
git switch main
git pull --ff-only
git switch -c feature/forecast-validation
```

Po implementacji należy sprawdzić `git diff`, dodać wyłącznie pliki zadania i obejrzeć przygotowany commit. Poniższe ścieżki są przykładowe — należy zastąpić je własnymi:

```bash
git add src/forecast.py tests/test_forecast.py
git diff --cached
git commit -m "Validate forecast history"
git push -u origin feature/forecast-validation
```

Na GitHubie należy wybrać **Compare & pull request**, sprawdzić gałąź docelową i opisać sposób uruchomienia oraz wynik kontroli. Do opisu można dodać `Closes #12`, jeśli 12 jest numerem rzeczywiście realizowanego Issue. Następnie należy poprosić członka zespołu o przegląd. Procedurę opisuje [dokumentacja Pull Requestów](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).

Przegląd powinien odpowiedzieć na trzy pytania: czy zachowanie spełnia kryteria, czy błąd jest obsłużony i czy kod nie zawiera sekretów ani niepotrzebnych plików. Zamknięcie PR bez scalenia nie oznacza integracji rozwiązania. Po scaleniu należy zaktualizować lokalną główną gałąź przez `git pull --ff-only`. Jeśli polecenie odmawia aktualizacji, trzeba sprawdzić rozbieżności; nie należy używać wymuszonego pushowania jako naprawy.

### Odłożenie niedokończonej pracy przed aktualizacją (Git)

Jeśli aktualizację gałęzi blokują niezacommitowane zmiany, należy najpierw wykonać `git status` i `git diff`. Zakończoną część pracy można zapisać w commicie. Niedokończone zmiany można odłożyć lokalnie:

```bash
git stash push -u -m "Praca przed aktualizacja galezi"
git stash list
git status
git pull --ff-only
git stash apply 'stash@{0}'
```

Procedura zakłada brak trwającego konfliktu oraz skonfigurowaną gałąź zdalną. `-u` obejmuje także pliki nieśledzone, ale nie ignorowane; przed odłożeniem trzeba sprawdzić ich zawartość. Stash nie jest kopią wysłaną na GitHub. Jeśli `pull` zgłosi rozbieżność gałęzi, należy ją wyjaśnić przed dalszą pracą, zamiast wymuszać aktualizację.

Po `apply` trzeba sprawdzić pliki i testy. Jeśli pojawi się konflikt, należy rozwiązać go według kolejnej procedury, ale bez `git merge --continue`: przywrócenie stash nie jest scalaniem gałęzi. Dopiero po potwierdzeniu odzyskania pracy można usunąć właściwy wpis przez `git stash drop 'stash@{0}'`, wcześniej ponownie sprawdzając `git stash list`. Numer wpisu może się zmienić po utworzeniu kolejnego stash. `git stash pop` łączy przywrócenie z usunięciem wpisu po sukcesie; wariant `apply` pozwala najpierw zweryfikować wynik.

### Rozwiązanie konfliktu przy scalaniu (Git / VS Code)

Procedurę należy wykonać na własnej gałęzi zadania z czystym stanem pracy, nie na gałęzi innej osoby. Aby włączyć zmiany z głównej gałęzi do zadania, należy wykonać:

```bash
git status
git fetch origin
git merge origin/main
```

Jeśli repozytorium używa `master`, trzeba zmienić nazwę gałęzi. Przy konflikcie należy ponownie wykonać `git status` i otworzyć wskazany plik w VS Code. Przykładowy konflikt opisu kontraktu może wyglądać tak:

```text
    <<<<<<< HEAD
    Przy braku historii należy wyświetlić komunikat błędu.
    =======
    Niepoprawna historia nie może utworzyć pliku wynikowego.
    >>>>>>> origin/main
```

`HEAD` oznacza tutaj własną gałąź zadania, a druga część — dołączaną wersję z `origin/main`. Należy odczytać obie intencje i uzgodnić wynik, np. „Przy niepoprawnej historii należy wyświetlić komunikat błędu i nie tworzyć pliku wynikowego”. Trzeba usunąć znaczniki konfliktu i zachować poprawną składnię pliku. W kodzie samo użycie **Accept Both Changes** może utworzyć niedziałający program.

Po edycji wszystkich konfliktów należy sprawdzić różnice, wykonać testy, a następnie wskazać konkretne rozwiązane pliki:

```bash
git diff --check
git add docs/architecture.md
git diff --cached
git status
git merge --continue
```

Ścieżkę należy zastąpić rzeczywistym plikiem konfliktu. Polecenie końcowe może otworzyć edytor wiadomości commita. Po scaleniu trzeba ponownie uruchomić przepływ i wysłać gałąź zadania zwykłym `git push`. Jeśli nie można uzgodnić rozwiązania, należy zachować potrzebne nowe poprawki osobno i przerwać bieżące scalanie przez `git merge --abort`; nie używać `reset --hard` ani wymuszonego pushowania.

### Sprawdzenie gotowości zmiany do przeglądu

**Definition of Done** to wspólne kryteria uznania zadania za ukończone. Przed PR należy sprawdzić poniższe punkty; wymaganie niezwiązane z zadaniem można oznaczyć „nie dotyczy” z uzasadnieniem.

| Kontrola | Dowód przed PR |
|---|---|
| Zadanie i zakres | powiązane Issue, wskazane kryteria odbioru |
| Poprawne i błędne wejście | polecenie/test i oczekiwany wynik |
| Integracja | zgodność z kontraktem, kontrola głównego przepływu |
| Bezpieczny diff | brak kluczy, prywatnych danych, `.venv`, `__pycache__` i przypadkowych plików |
| Odtwarzalność | aktualne zależności, konfiguracja i README |
| Przegląd | osoba przeglądająca i opis ograniczeń; przed scaleniem rozwiązane uwagi |

Checklista nie zastępuje sprawdzenia kodu i nie oznacza obowiązku dopisywania testów niezwiązanych ze zmianą.

### Połączenie obliczenia z interfejsem (Python)

Demonstracja rozwija średnią z Lab 4 do polecenia przyjmującego JSON. Należy zapisać kod jako `examples/lab6/forecast.py`. Wystarcza standardowa biblioteka Pythona.

```python
import argparse
import json
import math
from pathlib import Path
from statistics import mean

def forecast(history, window):
    if type(window) is not int or window <= 0:
        raise ValueError("Okno musi być dodatnią liczbą całkowitą")
    if not isinstance(history, list) or len(history) < window:
        raise ValueError("Historia musi być listą o długości co najmniej równej oknu")
    if any(type(x) not in (int, float) or not math.isfinite(x) or x < 0 for x in history):
        raise ValueError("Historia wymaga skończonych, nieujemnych liczb")
    return mean(history[-window:])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--window", type=int, default=3)
    args = parser.parse_args()
    try:
        if args.input.resolve() == args.output.resolve():
            raise ValueError("Wynik nie może nadpisać wejścia")
        if args.output.exists():
            raise ValueError("Plik wyniku już istnieje; należy wybrać nową nazwę")
        history = json.loads(args.input.read_text(encoding="utf-8-sig"))
        value = forecast(history, args.window)
        result = {"forecast": value, "unit": "zgloszenia/dzien",
                  "method": "moving_average", "window": args.window}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
        print(f"Prognoza: {value:.2f} {result['unit']}")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Błąd: {error}\n")

if __name__ == "__main__":
    main()
```

Należy utworzyć `examples/lab6/history.json` z zawartością `[12, 14, 13, 15]`, a następnie uruchomić:

```powershell
python examples/lab6/forecast.py examples/lab6/history.json examples/lab6/results/run-01.json --window 3
```

Oczekiwany wynik to `Prognoza: 14.00 zgloszenia/dzien`, ponieważ średnia z 14, 13 i 15 wynosi 14. Należy otworzyć zapisany JSON i sprawdzić metodę, jednostkę i okno. Ponowne uruchomienie z tą samą ścieżką wyjściową celowo kończy się błędem; dla kolejnej próby trzeba wybrać nową nazwę pliku.

**Ćwiczenie:** należy użyć `--window 5` i nowego pliku `run-bad.json`. Program powinien zgłosić zbyt krótką historię i nie utworzyć wyniku. Następnie trzeba sprawdzić brak pliku wejściowego. Własna wersja powinna korzystać z przygotowanych danych projektu, uwzględniać daty i identyfikację wejścia — demonstracja pomija je dla pokazania samego połączenia modułów.

Kod nie zabezpiecza przed każdym błędem infrastruktury, np. przerwaniem procesu w trakcie zapisu. Jeśli zapis musi być atomowy, należy zaprojektować plik tymczasowy i zatwierdzenie dopiero po poprawnym zakończeniu.

### Udostępnienie obliczenia przez API (FastAPI — opcjonalnie)

Należy zachować `examples/lab6/forecast.py` z poprzedniego przykładu. W aktywnym środowisku należy wykonać `python -m pip install fastapi uvicorn`, a poniższy kod zapisać jako `examples/lab6/server.py`. Polecenia należy uruchamiać z katalogu głównego repozytorium.

```python
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from examples.lab6.forecast import forecast

app = FastAPI(title="Prognoza zgłoszeń")

class ForecastInput(BaseModel):
    model_config = ConfigDict(strict=True, allow_inf_nan=False, extra="forbid")
    history: list[float]
    window: int = Field(gt=0)

@app.exception_handler(RequestValidationError)
async def invalid_request(request: Request, exc: RequestValidationError):
    malformed = any(error["type"] == "json_invalid" for error in exc.errors())
    return JSONResponse(status_code=400 if malformed else 422,
                        content={"error": "invalid_json" if malformed else "invalid_history"})

@app.post("/api/forecast")
def calculate(body: ForecastInput):
    try:
        value = forecast(body.history, body.window)
    except (ValueError, OverflowError):
        return JSONResponse(status_code=422, content={"error": "invalid_history"})
    return {"forecast": value, "unit": "zgloszenia/dzien", "window": body.window}
```

Należy uruchomić lokalny serwer:

```powershell
python -m uvicorn examples.lab6.server:app --host 127.0.0.1 --port 8000
```

W przeglądarce należy otworzyć `http://127.0.0.1:8000/docs`, rozwinąć **POST /api/forecast**, wybrać **Try it out**, wpisać `{"history":[12,14,13,15],"window":3}` i nacisnąć **Execute**. Oczekiwany kod to 200, a prognoza wynosi 14,0. Swagger UI pokazuje schemat i pozwala wysyłać żądania; nie zastępuje automatycznych testów ani interfejsu dla odbiorcy biznesowego.

**Ćwiczenie:** należy wysłać za krótką historię i oczekiwać 422 z `invalid_history`. W Postmanie trzeba wysłać niepoprawny JSON `{"history":` i sprawdzić 400 z `invalid_json`. Własny handler jest potrzebny, ponieważ domyślna odpowiedź walidacyjna FastAPI ma inny format; mechanizm opisuje [dokumentacja obsługi błędów](https://fastapi.tiangolo.com/tutorial/handling-errors/).

Usługa nie zapisuje danych, nie ma uwierzytelniania ani limitów ruchu. Należy używać jej lokalnie na dozwolonych próbkach; nie publikować tego przykładu jako gotowej usługi produkcyjnej. Serwer należy zatrzymać przez `Ctrl+C`.

### Przygotowanie interaktywnego widoku (Streamlit — opcjonalnie)

Dla użytkownika wybierającego parametry analizy można zamiast API lub CLI przygotować lokalny dashboard. Należy wykonać `python -m pip install streamlit` i zapisać poniższy kod jako `examples/lab6/dashboard.py`. Obliczenie nadal wykorzystuje funkcję `forecast`, nie jej skopiowaną wersję.

```python
import json
import streamlit as st
from examples.lab6.forecast import forecast

st.title("Prognoza zgłoszeń")
st.caption("Dane demonstracyjne; kolejne obserwacje oznaczają dni.")
text = st.text_area("Historia jako lista JSON", "[12, 14, 13, 15]")
window = st.slider("Okno średniej", min_value=1, max_value=10, value=3)
try:
    history = json.loads(text)
    value = forecast(history, window)
except (ValueError, OverflowError) as error:
    st.error(f"Nie można obliczyć prognozy: {error}")
else:
    st.line_chart(history)
    st.metric("Prognoza [zgłoszenia/dzień]", f"{value:.1f}")
```

Należy wykonać `python -m streamlit run examples/lab6/dashboard.py --server.address 127.0.0.1` i otworzyć adres podany w terminalu, zwykle `http://127.0.0.1:8501`. Dla okna 3 oczekiwana wartość to 14,0; po zmianie na 1 — 15,0. Okno 5 powinno wyświetlić komunikat błędu bez prognozy. Oś pozioma przykładowego wykresu to indeks obserwacji, nie data — w projekcie trzeba użyć rzeczywistych dat i oznaczyć jednostki.

Zmiana kontrolki powoduje ponowne wykonanie skryptu. Nie należy umieszczać w takim przepływie bezwarunkowego zapisu do bazy lub wywołania sterującego urządzeniem. Dla operacji z efektem ubocznym trzeba zaprojektować jawne zatwierdzenie i ochronę przed powtórzeniem. **Ćwiczenie:** należy sprawdzić pustą listę i tekst zamiast liczby, a następnie dostosować wejście do danych projektu. Wyniki na ekranie należy porównać z CLI dla tych samych danych i parametrów.

### Zapisanie tego samego wyniku w bazie (Python / SQLite)

Ten wariant zastępuje zapis JSON dla zespołów pracujących z bazą; nie trzeba realizować obu ścieżek. Należy utworzyć w DataGrip demonstracyjną bazę `examples/lab6/results/forecast.db` i wykonać w niej `schema.sql` z Lab 5. Trzeba zachować tabele `run` i `forecast` bez zmian. Następnie należy zapisać poniższy kod jako `examples/lab6/save_forecast.py`, obok wcześniejszego `forecast.py`.

```python
from contextlib import closing
from datetime import date
import json
from pathlib import Path
import sqlite3
from forecast import forecast

def save_forecast(db_path, history, window, target_date, data_version):
    value = forecast(history, window)
    date.fromisoformat(target_date)
    if not isinstance(data_version, str) or not data_version.strip():
        raise ValueError("Wymagana wersja danych")
    # mode=rw: brak bazy ma być błędem, a nie utworzeniem pustego pliku.
    uri = Path(db_path).resolve().as_uri() + "?mode=rw"
    with closing(sqlite3.connect(uri, uri=True)) as db:
        db.execute("PRAGMA foreign_keys = ON")
        with db:
            cursor = db.execute(
                "INSERT INTO run(data_version, method, window) VALUES (?, ?, ?)",
                (data_version, "moving_average", window),
            )
            run_id = cursor.lastrowid
            db.execute(
                "INSERT INTO forecast(run_id, target_date, value) VALUES (?, ?, ?)",
                (run_id, target_date, value),
            )
        return run_id

if __name__ == "__main__":
    history = json.loads(Path("examples/lab6/history.json").read_text(encoding="utf-8-sig"))
    run_id = save_forecast("examples/lab6/results/forecast.db", history, 3,
                           "2026-10-10", "demo-history-v1")
    print(f"Zapisano uruchomienie {run_id}")
```

Należy wykonać `python examples/lab6/save_forecast.py` z katalogu repozytorium, a w DataGrip uruchomić:

```sql
SELECT r.id, r.data_version, r.method, f.target_date, f.value
FROM run r JOIN forecast f ON f.run_id = r.id
ORDER BY r.id DESC LIMIT 1;
```

Dla historii `[12,14,13,15]` oczekiwany wynik ma wersję `demo-history-v1`, datę `2026-10-10` i wartość `14.0`. Identyfikator zależy od wcześniejszych zapisów. W tej demonstracji jednostka jest stała: zgłoszenia/dzień; dla różnych miar należy zaprojektować jej zapis. Każde uruchomienie tworzy nowy rekord — procedura nie zapewnia deduplikacji ponowionych żądań API.

Parametry `?` oddzielają wartości od tekstu SQL; nie należy składać zapytań z wejścia użytkownika za pomocą f-stringów. Blok `with db` zatwierdza oba zapisy razem albo wycofuje je po wyjątku; `closing` dodatkowo zamyka połączenie. Zasady te opisano w [dokumentacji sqlite3](https://docs.python.org/3/library/sqlite3.html). Warstwa interfejsu powinna zamienić błąd bazy na czytelny komunikat, bez potwierdzania zapisu.

**Ćwiczenie:** na demonstracyjnej bazie należy podać niepoprawną datę i potwierdzić brak nowego `run`. Aby sprawdzić wycofanie już rozpoczętej transakcji, można na osobnej kopii skryptu celowo użyć nieistniejącego `run_id` w drugim `INSERT`. Po błędzie FK liczba rekordów `run` powinna pozostać niezmieniona. Nie należy pozostawiać tej zmiany w kodzie projektu.

### Oddzielenie wyniku od diagnostyki (logging)

`print()` nadaje się do wyniku dla użytkownika. Komunikaty diagnostyczne należy kierować przez `logging`, domyślnie na standardowe wyjście błędów (`stderr`), aby nie mieszały się z JSON-em lub CSV na `stdout`.

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)
logger.info("Rozpoczęto obliczenia")
logger.warning("Użyto lokalnej kopii danych; źródło jest niedostępne")
# W bloku obsługującym rzeczywisty błąd:
# logger.error("Nie zapisano wyniku analizy")
```

`INFO` opisuje przebieg, `WARNING` sytuację wymagającą uwagi, a `ERROR` nieudaną operację. Ostrzeżenie należy emitować tylko wtedy, gdy opisana sytuacja rzeczywiście wystąpiła. Nie należy logować tokenów, pełnych żądań z danymi osobowymi ani zawartości prywatnych plików. Log błędu nie zastępuje niezerowego kodu wyjścia programu lub właściwej odpowiedzi HTTP.

### Znalezienie błędu na granicy modułów (IDE)

Należy ustawić punkt przerwania przed wywołaniem funkcji obliczeniowej i uruchomić program w debuggerze z tymi samymi argumentami co w terminalu. Trzeba odczytać typ danych, liczbę obserwacji i parametr metody, a następnie przejść do funkcji. Dla powyższej próbki lista ma 4 elementy, a okno wynosi 3.

**Ćwiczenie:** na kopii wejścia należy zmienić jedną liczbę na tekst `"brak"`. Trzeba odszukać walidację odrzucającą rekord, zamiast usuwać ją w celu „uruchomienia” programu. Jeżeli aplikacja korzysta z API, analogicznie należy sprawdzić ciało odpowiedzi w Bruno/Postmanie przed przekazaniem go do obliczeń.

### Oddzielenie konfiguracji od kodu

Jeżeli projekt potrzebuje klucza API, należy pobierać go ze zmiennej środowiskowej, np. `os.environ["API_TOKEN"]`, a nie wpisywać w kod. Plik `.env` sam nie jest automatycznie wczytywany przez Pythona; wymaga jawnego mechanizmu w aplikacji lub środowisku.

W `.env.example` należy umieścić tylko nazwy i puste wartości, np. `API_TOKEN=`. W `.gitignore` trzeba uwzględnić `.env` i katalog środowiska wirtualnego. Nie należy ignorować wszystkich wyników, jeżeli są wymaganym dowodem działania projektu. Sekret już zapisany w historii wymaga unieważnienia u dostawcy — samo dodanie go do `.gitignore` nie usuwa ujawnienia.

Administrator repozytorium powinien sprawdzić w **Settings → Code security** dostępność secret scanning i **Push protection** oraz włączyć ochronę, jeśli pozwalają na to ustawienia konta lub organizacji. Aktualną ścieżkę opisuje [dokumentacja GitHub](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/prevent-future-leaks/enable-push-protection). Mechanizm rozpoznaje obsługiwane typy sekretów; nie gwarantuje wykrycia dowolnego hasła lub danych osobowych. Nie należy testować go przez wysyłanie prawdziwego klucza ani obchodzić blokady, aby oddać zadanie. Po wykryciu rzeczywistego sekretu trzeba go unieważnić i usunąć z przygotowywanych commitów.

### Kontrolowane wykorzystanie agenta AI

Można zlecić agentowi małą zmianę z konkretnym kontraktem, np.:

> Dostosuj funkcję do kontraktu z docs/architecture.md. Zachowaj metodę z docs/experiment.md. Obsłuż pustą i zbyt krótką historię, bez zwracania fikcyjnego zera. Nie dodawaj nowych usług ani zależności bez uzasadnienia. Wskaż sposób sprawdzenia zmiany.

Należy obejrzeć diff, wykonać poprawny i błędny przypadek oraz opisać wynik przeglądu. Odpowiedzialność za zachowanie programu pozostaje po stronie zespołu.

## Zadania samodzielne

1. Wybrać jeden główny przepływ i utworzyć zadania z kryteriami odbioru oraz właścicielami.
2. Połączyć wejście, obliczenie i wynik zgodnie z kontraktami z Lab 5.
3. Obsłużyć brak wejścia, niepoprawne dane i błąd zapisu; sprawdzić każdy przypadek.
4. Przeprowadzić zmiany przez gałęzie i Pull Requesty z przeglądem innej osoby.
5. Uruchomić całość po scaleniu, nie tylko poszczególne moduły.
6. Uzupełnić README i odtworzyć działanie na komputerze innego członka zespołu.
7. Zapisać stan implementacji i pozostałe zadania; wskazać rezultat każdej osoby przez Issue/PR.

Optymalizację należy podejmować po wskazaniu rzeczywistego problemu. Przed i po zmianie trzeba sprawdzić ten sam wynik na tej samej próbce. Nie należy wymieniać biblioteki lub wprowadzać cache tylko dla zwiększenia liczby wykorzystanych technologii.

## Rezultat do zapisania

- działający główny przepływ własnego projektu z obsługą błędów;
- README z zależnościami, konfiguracją, poleceniem i oczekiwanym wynikiem;
- `docs/implementation.md` z wynikiem integracji oraz ograniczeniami;
- scalone i sprawdzone zmiany, powiązane z zadaniami;
- mierzalny wkład każdej osoby w kodzie, testach, integracji lub dokumentacji.
