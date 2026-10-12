# Weryfikator repozytorium

## Cel

Skrypt `verify_repository.py` służy do wstępnego sprawdzenia, czy repozytorium zespołu zawiera wymagane artefakty oraz czy każdy członek zespołu ma widoczny wkład w historię pracy.

## Uruchomienie

Wystarczy podać link do repozytorium i etap, który ma zostać sprawdzony:

```powershell
python tools/verify_repository.py --repo https://github.com/zespol/projekt --lab lab6
```

Loginy członków zespołu należy przekazać weryfikatorowi osobno. Nie trzeba dodawać do publicznego repozytorium plików technicznych przeznaczonych dla bota. Listę można podać parametrem:

```powershell
python tools/verify_repository.py --repo https://github.com/zespol/projekt --students anna123,jan456 --lab lab6
```

Dla repozytoriów prywatnych należy ustawić zmienną `GITHUB_TOKEN` albo przekazać token parametrem. Token nie powinien być zapisywany w repozytorium ani w dokumentacji projektu.

## Co sprawdza skrypt?

W zależności od wybranego laboratorium skrypt sprawdza:

- dostępność repozytorium;
- `README.md` i wymagane pliki dokumentacji;
- Issues i Pull Requesty;
- obecność workflow GitHub Actions;
- commity i Pull Requesty przypisane do członków zespołu;
- wynik w formacie tekstowym albo JSON.

Skrypt jest pierwszą wersją weryfikatora. Sprawdza przede wszystkim pliki, historię commitów i podstawowe elementy repozytorium dostępne przez GitHub API.

Dla Lab 2 skrypt sprawdza, czy repozytorium jest publiczne oraz czy zawiera `README.md`, `docs/problem.md`, `docs/data.md` i katalog `data/` z plikiem `sample.*`. Po przekazaniu loginów parametrem `--students` skrypt sprawdza również, czy każdy członek zespołu ma co najmniej jeden commit.

## Zasady oceniania wkładu

Weryfikator nie powinien uznawać liczby linii kodu za miarę wkładu. Za rezultat można uznać również test, przygotowanie danych, diagram, dokumentację, workflow, analizę wyników albo decyzję projektową. Każdy rezultat powinien mieć właściciela i ślad w historii repozytorium. W laboratoriach, w których wymagane są Issues lub Pull Requesty, należy powiązać z nimi odpowiedni rezultat.
