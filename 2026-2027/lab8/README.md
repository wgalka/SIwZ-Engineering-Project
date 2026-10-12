# Laboratorium 8: Eksperymenty, testowanie i ocena wyników

## Cel zajęć

Na tych zajęciach należy sprawdzić poprawność działania rozwiązania, przeprowadzić eksperymenty i ocenić, czy projekt spełnia kryteria zapisane wcześniej. Sam fakt, że aplikacja się uruchamia, nie jest jeszcze dowodem poprawności ani użyteczności.

Po zajęciach każdy zespół powinien:

- mieć plan testów obejmujący poprawne i błędne przypadki;
- posiadać testy najważniejszego przepływu;
- mieć wynik eksperymentu opisany parametrami i miarami;
- umieć wskazać ograniczenia oraz źródła błędów;
- mieć udokumentowany przynajmniej jeden problem i jego poprawkę.

## Wynik trzeba zmierzyć

Zdefiniować, co oznacza dobry wynik dla danego projektu. Może to być poprawność odpowiedzi, czas działania, kompletność danych, liczba obsłużonych przypadków, jakość klasyfikacji albo inna miara związana z problemem użytkownika.

Oddzielić test od eksperymentu. Test odpowiada na pytanie, czy określone zachowanie jest poprawne. Eksperyment porównuje warianty albo bada wynik w określonych warunkach. W obu przypadkach zapisać dane wejściowe, parametry, oczekiwany lub zmierzony rezultat i sposób interpretacji.

### Pytania pomocnicze

1. Które wymagania z Lab 2 można sprawdzić automatycznie?
2. Co powinno się wydarzyć dla poprawnego, pustego i błędnego wejścia?
3. Jaką miarą ocenimy wynik głównego przepływu?
4. Czy porównanie wariantów jest wykonywane na tych samych danych?
5. Czy wynik można powtórzyć po ponownym uruchomieniu?
6. Jakie ograniczenia mogą zmienić interpretację wyniku?

## Przydatne narzędzia

Zrzuty demonstracyjne i opis pełnego przepływu znajdują się w [przewodniku po narzędziach](../narzedzia/README.md#zrzuty-demonstracyjne). Należy pokazać test poprawnego i błędnego przypadku, uruchomienie workflow oraz zapisanie problemu w Issue.

1. **pytest, JUnit lub narzędzie wybrane przez zespół** - przygotować test poprawnego przypadku, test błędu i test danych granicznych.
2. **GitHub Actions** - uruchamiać testy po każdym Pull Requeście i pokazać, jak awaria blokuje połączenie zmiany.
3. **Jupyter i matplotlib albo inne narzędzie analityczne** - przygotować powtarzalny eksperyment, tabelę wyników i wykres.
4. **Postman lub Insomnia** - sprawdzić API, jeśli projekt udostępnia endpointy.
5. **GitHub Issues** - zapisać problem, kroki odtworzenia, oczekiwany rezultat, poprawkę i potwierdzenie rozwiązania.

Podczas pokazu przygotować jeden test, celowo doprowadzić do jego niepowodzenia, zapisać problem w Issue, wprowadzić poprawkę i uruchomić kontrolę ponownie. Następnie pokazać eksperyment z dwoma wariantami i wyjaśnić, co oznacza jego wynik.

## Zadania samodzielne

1. Przygotować plan testów obejmujący co najmniej pięć przypadków, w tym przypadki poprawne, błędne i graniczne.
2. Napisać testy dla najważniejszej funkcji lub przepływu.
3. Przeprowadzić eksperyment porównujący co najmniej dwa warianty rozwiązania albo dwie metody.
4. Zmierzyć wynik według kryteriów ustalonych w Lab 2 lub Lab 3.
5. Zapisać dane, parametry, wynik i sposób jego interpretacji.
6. Opisać ograniczenia eksperymentu i możliwe źródła błędów.
7. Zarejestrować co najmniej jeden problem w GitHub Issues i zamknąć go po poprawce oraz ponownym teście.
8. Zapisać plan testów i wyniki w `docs/tests.md`, a link do Issue, Pull Requesta i workflow umieścić w `docs/evidence.md`.

Każdy członek zespołu powinien odpowiadać za konkretny element walidacji: test, dane testowe, eksperyment, wykres, analizę ograniczeń albo poprawkę. Rezultat powinien być widoczny w repozytorium lub w historii pracy.

## Rezultat do zapisania

- plan i zestaw testów;
- wyniki eksperymentów z parametrami;
- miary, wykresy albo tabele wyników;
- interpretacja wyników i ograniczeń;
- Issue opisujące problem oraz poprawkę;
- automatyczna kontrola uruchamiana w repozytorium.

## Zasady interpretacji

Nie przedstawiać pojedynczego wyniku jako dowodu ogólnej skuteczności rozwiązania. Zaznaczyć, na jakich danych i w jakich warunkach wykonano pomiar oraz czego wynik nie potwierdza.
