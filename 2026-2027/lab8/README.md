---
title: "Laboratorium 8: Prezentacja rezultatów projektu"
permalink: /2026-2027/lab8/
---

# Laboratorium 8: Prezentacja rezultatów projektu

**Specjalność: Systemy informatyczne w zarządzaniu**

## Cel zajęć

Na tym etapie należy przygotować raport końcowy i przedstawić działanie projektu, uzasadnienie decyzji oraz wyniki oceny. Trzeba wskazać dokładną wersję rozwiązania i indywidualny wkład członków zespołu. Prezentacja powinna pokazać, jak rozwiązanie wspiera konkretną decyzję użytkownika, a nie tylko jakie technologie wykorzystano.

## Przygotowanie przed zajęciami

Należy przygotować zintegrowaną wersję z Lab 6, wyniki testów z Lab 7, dokumentację i dozwoloną próbkę demonstracyjną. Przed wystąpieniem trzeba sprawdzić pełny scenariusz na komputerze używanym do pokazu oraz przygotować lokalny wariant awaryjny.

Należy uzgodnić z prowadzącym limit wystąpienia i sposób przekazania materiałów. Poniższy podział 90 minut dotyczy przygotowania i prób; kolejność oraz czas prezentacji końcowych zależą od harmonogramu grupy. Osiem instrukcji odpowiada blokom tematycznym sylabusa, nie oznacza ośmiu jednakowych spotkań wyczerpujących cały wymiar 20 godzin zajęć projektowych.

## Rezultat pracy

```text
docs/
├── report.md             # raport końcowy z odnośnikami do istniejących dowodów
└── presentation.md       # scenariusz demonstracji, pytania i wynik próby
presentation/
├── slides.pdf            # czytelny eksport prezentacji
└── slides.pptx           # lub inny edytowalny format; jeśli używane są slajdy
README.md                 # punkt wejścia do uruchomienia i dokumentacji
```

Należy zachować format odpowiedni do narzędzia. Jeśli prezentacja jest przygotowana w usłudze internetowej, trzeba sprawdzić uprawnienia odbiorcy i zapisać eksport, który można otworzyć bez konta autora. Nie należy publikować karty projektu, prywatnych danych ani sekretów. Do raportu wystarczą bezpieczne przykłady i odnośniki do publicznych rezultatów pracy.

## Przebieg zajęć — przygotowanie i próba, 90 minut

### 1. Wybór wersji i kontrola gotowości — 0–15 min

Należy sprawdzić stan repozytorium, uruchomić testy i główny przepływ. Trzeba ustalić, który commit będzie prezentowany, oraz spisać błędy wpływające na demonstrację. Jeśli błąd uniemożliwia główną operację, należy go naprawić lub jawnie ograniczyć zakres pokazu; nie wolno przedstawiać zrzutu ekranu jako działającej aplikacji.

Każda osoba powinna odpowiadać za konkretny rezultat przygotowania: raport, weryfikację wydania, scenariusz, materiały wizualne lub kontrolę dowodów. Każda powinna również umieć wyjaśnić własny wkład w projekt.

### 2. Raport końcowy — 15–35 min

Należy uzupełnić `docs/report.md` według struktury poniżej. Nie trzeba przepisywać całej dokumentacji z poprzednich zajęć. Trzeba krótko podsumować wynik i wskazać pliki, testy oraz pomiary potwierdzające najważniejsze stwierdzenia.

### 3. Demonstracja i materiały — 35–55 min

Należy przygotować pokaz jednej ważnej operacji: wejście, wykonanie, wynik i interpretacja. Trzeba dobrać jeden diagram oraz jedną tabelę lub wykres, które pomagają wyjaśnić decyzje. Nie należy umieszczać na slajdach całego README ani zrzutów kodu z nieczytelną czcionką.

### 4. Próba z pomiarem czasu — 55–75 min

Należy przeprowadzić próbę przed inną osobą lub zespołem, z limitem uzgodnionym na zajęciach. Obserwator powinien zanotować: czas, niezrozumiałe pojęcie, stwierdzenie bez dowodu i jedno pytanie dotyczące ograniczeń. Trzeba przećwiczyć przekazanie głosu oraz odszukanie pliku z dowodem.

### 5. Poprawki i wydanie — 75–90 min

Należy poprawić najsłabszy fragment raportu lub wystąpienia, powtórzyć potrzebne sprawdzenia i oznaczyć gotową wersję. Trzeba potwierdzić, że README, raport, wyniki testów i prezentacja odnoszą się do tego samego stanu projektu. Po zmianie kodu nie należy używać starego raportu testów jako dowodu nowej wersji.

## Przygotowanie raportu końcowego

W `docs/report.md` należy zastosować poniższe rozdziały. Długość powinna wynikać z potrzeb wyjaśnienia projektu, nie z wypełniania określonej liczby stron.

| Rozdział | Co zapisać? | Gdzie szukać dowodu? |
|---|---|---|
| Problem i użytkownik | Jaką decyzję lub czynność usprawniono? | `docs/problem.md` |
| Zakres wykonany | Co rzeczywiście działa, a czego nie zrealizowano? | główny przepływ i otwarte Issues |
| Dane | Pochodzenie, jednostka obserwacji, dostęp, jakość i ograniczenia | `docs/data.md`, `docs/processing.md` |
| Metoda i architektura | Powód wyboru, wariant bazowy, kompromisy | `docs/experiment.md`, `docs/architecture.md`, ADR |
| Wyniki i ocena | Miary, dane, wersja, statusy wymagań | `docs/tests.md`, wyniki Lab 4 i Lab 7 |
| Użycie i odtworzenie | Jak uruchomić dokładnie prezentowaną wersję? | README, instrukcja użytkowa, tag |
| Ograniczenia i rozwój | Czego wynik nie potwierdza? Jaki jest najważniejszy dalszy krok? | niezweryfikowane założenia i błędy |
| Wkład zespołu i źródła | Rezultaty poszczególnych osób, wykorzystane materiały i wsparcie AI | Issue, PR, commity, literatura |

**Przykład poprawnego wniosku:** „Na czterech syntetycznych dniach średnia z trzech dni uzyskała MAE 1,0 zamiast 1,5 zgłoszenia. Potwierdza to działanie procedury porównawczej, ale nie skuteczność planowania obsady w rzeczywistej organizacji”.

**Przykład wymagający poprawy:** „System zmniejsza koszty obsługi o 30%”, jeśli nie zmierzono kosztów ani skutków wdrożenia. Należy zastąpić go wynikiem, który rzeczywiście uzyskano, i opisać brakujące sprawdzenie.

Wkład należy opisać przez rezultat, nie przez liczbę commitów. Przykładowy zapis: „Walidacja braków w imporcie — PR #18; test odrzucenia pustej próbki — plik testu; sprawdzenie integracji — wynik uruchomienia”. Nie należy tworzyć dodatkowej publicznej listy danych osobowych; sposób identyfikacji osób na potrzeby oceny należy uzgodnić z prowadzącym.

## Audyt gotowości projektu

Przed oznaczeniem wersji należy sprawdzić poniższe elementy i zapisać w `docs/report.md` brakujące dowody lub ograniczenia. Nie trzeba tworzyć kopii istniejących plików; wystarczą odnośniki. „Nie dotyczy” wymaga uzasadnienia, np. brak CI z opisanym lokalnym sprawdzeniem.

| Etap | Co sprawdzić? | Dowód / miejsce |
|---|---|---|
| Lab 1 — karta | Czy końcowy zakres odpowiada problemowi i czy wyjaśniono zmiany? | karta przekazana prywatnie; bez jej kopii i prywatnego linku w repo |
| Lab 2–3 — dane | Pochodzenie, prawo użycia, słownik, kontrola jakości i odtworzenie przetwarzania | `docs/data.md`, `docs/processing.md`, dozwolona próbka i skrypt |
| Lab 4 — metoda | Wariant bazowy, parametry, wspólne warunki oceny i ograniczenia | `docs/experiment.md`, wyniki porównania |
| Lab 5 — projekt | Zgodność diagramów i kontraktów z implementacją | `docs/architecture.md`, diagramy i ADR |
| Lab 6 — realizacja | Działający główny przepływ i zintegrowane zmiany | kod, README, PR i `docs/implementation.md` |
| Lab 7 — ocena | Wykonane testy, miara całego przepływu, otwarte błędy | `docs/tests.md`, wyniki, CI lub udokumentowane polecenie lokalne |
| Wydanie | Czy oznaczono dokładnie sprawdzoną wersję? | tag/commit i wynik odtworzenia |
| Lab 8 — przekazanie | Spójny raport, prezentacja, demonstracja i wkład | `docs/report.md`, `docs/presentation.md`, materiały oraz PR |

Nie należy ukrywać brakującego elementu przez oznaczenie go jako ukończonego. Trzeba wskazać jego wpływ na użyteczność lub możliwość oceny projektu.

## Przydatne narzędzia

| Narzędzie | Co wykonać? | Co sprawdzić? |
|---|---|---|
| Markdown / podgląd repozytorium | raport z odnośnikami | działające linki i czytelne tabele |
| Git i GitHub Releases | oznaczenie prezentowanej wersji | tag wskazuje sprawdzony commit |
| PowerPoint / LibreOffice Impress / Google Slides | slajdy i eksport PDF | czytelność na ekranie, brak prywatnych danych |
| Tryb prezentera i timer | próba wystąpienia | czas, kolejność, przejście do demonstracji |
| Środowisko projektu | rzeczywisty pokaz | wejście, wynik, jednostki i zachowanie przy błędzie |

Nie trzeba używać wszystkich narzędzi. Wykres powinien pochodzić z zapisanych wyników, a zrzut ekranu — z rzeczywistego działania aplikacji. Nie należy zastępować dowodów grafiką wygenerowaną przez AI.

### Oznaczenie sprawdzonej wersji (Git / GitHub Releases)

**Tag** nadaje nazwę konkretnemu stanowi repozytorium. **Release** pozwala dodatkowo dołączyć opis wydania i pliki. Przed oznaczeniem należy zakończyć integrację i sprawdzić czysty stan pracy:

```bash
git status
git rev-parse HEAD
git log -1 --oneline
```

Należy porównać identyfikator commita z wersją wskazaną w wynikach kontroli. Po sprawdzeniu można utworzyć nowy tag; poniższa nazwa jest przykładowa i musi być wolna:

```bash
git tag -a v1.0.0 -m "Wersja do prezentacji projektu"
git push origin v1.0.0
```

Nie należy przesuwać już udostępnionego taga na poprawioną wersję. Dla zmiany wymagającej ponownej oceny trzeba utworzyć kolejny tag i powtórzyć sprawdzenia. Przed wysłaniem taga należy upewnić się, że jego commit jest też dostępny w zdalnym repozytorium zespołu.

Na GitHubie należy otworzyć **Releases → Draft a new release**, wskazać istniejący tag i dodać: zakres działający, polecenie uruchomienia, odnośnik do raportu oraz znane ograniczenia. Następnie trzeba sprawdzić załączniki i opublikować wydanie. Szczegóły opisano w [dokumentacji GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

**Ćwiczenie:** inna osoba powinna pobrać wydanie do nowego katalogu, wykonać README i sprawdzić główny wynik. Nie należy używać lokalnych plików autora, których nie ma w wydaniu i nie opisano sposobu ich uzyskania. Baza danych lub zewnętrzne API nie są automatycznie dołączane do taga.

### Sprawdzenie historii wkładu (Git)

W lokalnym repozytorium należy wykonać:

```bash
git shortlog -sn --all
git log --all --author="Nazwisko" --stat
```

Filtr `Nazwisko` należy zastąpić rzeczywistą nazwą autora zapisaną w commitach; nie musi być ona taka sama jak login GitHub. Pierwsze polecenie grupuje liczbę commitów według autorów, drugie pokazuje ich zmiany plików. `--all` obejmuje lokalnie dostępne referencje, również gałęzie niescalone — nie jest dowodem, że zmiana znalazła się w wydaniu.

Aby sprawdzić historię osiągalną z prezentowanej wersji, należy użyć jej taga zamiast `--all`, np. `git log v1.0.0 --author="Nazwisko" --stat`. Do obejrzenia konkretnej zmiany służy `git show IDENTYFIKATOR`, po zastąpieniu identyfikatora skrótem commita. W przypadku squash merge, pracy w parze lub różnych nazw autora należy dodatkowo sprawdzić PR, przeglądy i opis współautorstwa.

**Ćwiczenie:** każda osoba powinna wskazać jeden własny rezultat, powiązany PR/commit i dowód działania w wersji prezentowanej. Liczba commitów i zmienionych linii nie jest oceną jakości ani wielkości wkładu. Nie należy publikować surowego eksportu historii z adresami e-mail tylko na potrzeby tej kontroli.

### Ułożenie demonstracji i slajdów

Należy rozpocząć od problemu użytkownika. Poniższy układ jest przykładem próby siedmiominutowej; trzeba dostosować go do limitu podanego przez prowadzącego.

| Czas | Treść | Co pokazać? |
|---|---|---|
| 0:00–1:00 | Problem i użytkownik | konkretna decyzja oraz wymaganie |
| 1:00–3:00 | Działający przepływ | wejście → uruchomienie → wynik |
| 3:00–4:00 | Dane, metoda i architektura | pochodzenie danych i jeden czytelny diagram |
| 4:00–5:30 | Ocena | wynik testów i porównanie z wariantem bazowym |
| 5:30–6:30 | Ograniczenia | jeden ważny brak i jego wpływ |
| 6:30–7:00 | Wkład i dalszy krok | rezultaty zespołu i uzasadniony priorytet |

Należy przygotować niewielką liczbę slajdów, każdy z jednym głównym komunikatem. W tabeli wyników trzeba podać jednostki, liczebność próby i warunki. Na wykresie należy opisać osie i nie obcinać skali w sposób sugerujący większą różnicę.

Można wykorzystać poniższy układ siedmiu slajdów. Jest to alternatywa organizacyjna wobec powyższej kolejności, nie dodatkowe siedem części wystąpienia. Po wyborze układu należy ponownie zmierzyć czas całego pokazu, łącznie z demonstracją; slajd nie musi zajmować pełnej minuty.

| Slajd | Główne pytanie | Materiał do pokazania |
|---|---|---|
| 1. Problem i zespół | Komu i w jakiej decyzji pomaga rozwiązanie? | jedno wymaganie, tytuł i oznaczenie zespołu zgodne z zasadami prywatności |
| 2. Dane | Skąd pochodzą i na ile można im ufać? | źródło, zakres, jednostka obserwacji i ważny brak |
| 3. Metoda i wariant bazowy | Co porównano i z jakim wynikiem? | jedna tabela miar z jednostką i liczebnością próby |
| 4. Architektura | Jak dane stają się wynikiem? | uproszczony przepływ z Lab 5 i jedna istotna decyzja ADR |
| 5. Działanie i testy | Czy rozwiązanie działa zgodnie z wymaganiem? | przejście do demonstracji, następnie najważniejsze testy i status wymagania |
| 6. Wnioski i ograniczenia | Czego wynik nie potwierdza i co warto zrobić dalej? | jeden wniosek, ograniczenie i uzasadniony priorytet |
| 7. Wkład | Jakie rezultaty przygotowały poszczególne osoby? | krótkie powiązanie rezultatów z PR, testem lub dokumentacją |

W wersji sześcioslajdowej można połączyć wkład z wnioskami, jeśli pozostaje czytelny. Nie należy zastępować demonstracji na slajdzie 5 samą listą funkcji.

W edytorze prezentacji należy wyeksportować PDF, otworzyć go poza edytorem i obejrzeć każdą stronę w rozmiarze zbliżonym do pokazu. Trzeba sprawdzić, czy diagramy, liczby i etykiety są czytelne. W trybie prezentera należy oddzielić notatki od widoku publicznego; przed udostępnieniem ekranu trzeba zamknąć prywatne dokumenty i wyłączyć powiadomienia.

W `docs/presentation.md` należy zapisać scenariusz demonstracji:

```markdown
## Demonstracja
Wersja: tag i identyfikator commita.
Wejście: dozwolona próbka i parametry.
Uruchomienie: dokładne polecenie lub kolejne działania w interfejsie.
Oczekiwany wynik: wartość/plik/ekran z jednostką i znaczeniem.
Przypadek błędny: bezpieczna kopia wejścia i oczekiwany komunikat.
Wariant awaryjny: zapisany wynik tej samej wersji, jawnie oznaczony jako nagranie lub zrzut.
## Próba
Zmierzony czas:
Niezrozumiały fragment:
Pytanie wymagające lepszego dowodu:
Wprowadzona poprawka:
```

Nie należy wykonywać operacji mogących zmienić rzeczywiste urządzenia, dane lub konta użytkowników tylko na potrzeby pokazu. Dla sterowania sprzętem można zademonstrować symulację albo tryb bez wykonania polecenia i wyraźnie to zaznaczyć.

### Przygotowanie slajdów z Markdownu (Marp — opcjonalnie)

Zamiast edytora prezentacji można użyć rozszerzenia **Marp for VS Code** (`marp-team.marp-vscode`) w lokalnym VS Code. Należy utworzyć `presentation/slides.md`, np.:

```markdown
---
marp: true
theme: default
paginate: true
---

# Prognoza zgłoszeń
Cel: wsparcie planowania obsady na następny dzień.

---

# Wynik demonstracji
| Wariant | MAE [zgłoszenia] |
|---|---:|
| Ostatnia wartość | 1,5 |
| Średnia z 3 dni | 1,0 |

Próba: 4 dni syntetyczne. Wynik nie potwierdza skuteczności wdrożenia.
```

Początkowy blok ustawia prezentację, a kolejne `---` rozdziela slajdy. Należy otworzyć podgląd Markdown, uzupełnić wybrany układ sześciu–siedmiu slajdów i zastąpić dane demonstracyjne własnymi wynikami. Diagram można dołączyć jako obraz zapisany w repozytorium, ze ścieżką względem `slides.md`.

Z palety poleceń należy wybrać **Marp: Export Slide Deck**, wskazać PDF i zapisać `presentation/slides.pdf`. Eksport wymaga obsługiwanej lokalnej przeglądarki; wymagania i ograniczenia opisuje [dokumentacja rozszerzenia](https://github.com/marp-team/marp-vscode#export-slide-deck-to-html-pdf-pptx-and-image-). Należy otworzyć PDF poza VS Code i sprawdzić podział, obrazy i czytelność tabel. Źródłem edytowalnym pozostaje `slides.md`; nie trzeba dodatkowo tworzyć PPTX.

### Przygotowanie odpowiedzi i dyskusji

W parze należy przećwiczyć odpowiedzi, każdorazowo wskazując plik, wynik lub decyzję:

1. Dlaczego te dane nadają się do problemu, a czego w nich brakuje?
2. Dlaczego wybrano tę metodę, a nie wariant bazowy?
3. Jak sprawdzono poprawność wyniku i jaki przypadek może nadal zawieść?
4. Która decyzja architektoniczna była kompromisem?
5. Jak koszt, prywatność albo możliwość utrzymania wpływają na zastosowanie?
6. Jaki konkretny rezultat przygotowała każda osoba?
7. Co należałoby sprawdzić przed rzeczywistym wdrożeniem?

Nie należy deklarować związku przyczynowego na podstawie samej korelacji ani skuteczności produkcyjnej na podstawie próbki syntetycznej. Jeżeli czegoś nie sprawdzono, trzeba wskazać brakującą weryfikację zamiast zgadywać.

## Zadania samodzielne

1. Przygotować raport końcowy z dowodami wyników i odnośnikami do istniejącej dokumentacji.
2. Zweryfikować zgodność kodu, danych, diagramów, wyników testów i instrukcji.
3. Oznaczyć sprawdzoną wersję tagiem lub wydaniem i potwierdzić jej odtworzenie.
4. Przygotować demonstrację oraz jawnie opisany wariant awaryjny.
5. Przygotować materiały wizualne i sprawdzić ich eksport.
6. Przeprowadzić próbę z pomiarem czasu, zebrać uwagi i poprawić co najmniej jeden fragment.
7. Przedstawić projekt, odpowiedzieć na pytania oraz wskazać indywidualne rezultaty.
8. Po dyskusji zapisać uzgodnione poprawki jako zadania; zmiany kodu oznaczyć nową wersją po sprawdzeniu.

## Rezultat do zapisania

- `docs/report.md`: raport końcowy;
- `docs/presentation.md`: scenariusz, wynik próby i pytania;
- materiały prezentacyjne w formacie możliwym do odczytu przez odbiorcę;
- tag lub release wskazujący sprawdzoną wersję oraz instrukcja odtworzenia;
- dowody indywidualnego wkładu, ograniczenia i uzgodnione dalsze zadania.

Należy przekazać prowadzącemu link do repozytorium oraz dokładny tag lub identyfikator wersji użytej w prezentacji, zgodnie z ustalonym sposobem oddania.
