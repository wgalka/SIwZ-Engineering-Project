# Weryfikator repozytorium

## Cel

Skrypt `verify_repository.py` służy do wstępnego sprawdzenia, czy repozytorium zespołu zawiera wymagane artefakty oraz czy każdy członek zespołu ma widoczny wkład w historię pracy.

## Uruchomienie

Wystarczy podać link do repozytorium i etap, który ma zostać sprawdzony:

```powershell
python tools/verify_repository.py --repo https://github.com/zespol/projekt --lab lab6
```

Jeżeli w repozytorium znajduje się poprawny plik `.course/members.json`, loginy członków zostaną odczytane automatycznie. Listę można również podać ręcznie:

```powershell
python tools/verify_repository.py --repo https://github.com/zespol/projekt --students anna123,jan456 --lab lab6
```

Dla repozytoriów prywatnych należy ustawić zmienną `GITHUB_TOKEN` albo przekazać token parametrem. Token nie powinien być zapisywany w repozytorium ani w dokumentacji projektu.

## Co sprawdza skrypt?

W zależności od wybranego laboratorium skrypt sprawdza:

- dostępność repozytorium;
- `README.md`, `.course/members.json` i wymagane pliki dokumentacji;
- Issues i Pull Requesty;
- obecność workflow GitHub Actions;
- commity i Pull Requesty przypisane do członków zespołu;
- wynik w formacie tekstowym albo JSON.

Skrypt jest pierwszą wersją weryfikatora. Dostęp do tablic GitHub Projects wymaga później dodatkowego uwierzytelnienia przez GitHub API. Do tego czasu należy wymagać zapisania linku do tablicy i krótkiego dowodu w `docs/evidence.md`.

## Zasady oceniania wkładu

Weryfikator nie powinien uznawać liczby linii kodu za miarę wkładu. Za rezultat można uznać również test, przygotowanie danych, diagram, dokumentację, workflow, analizę wyników albo decyzję architektoniczną. Każdy rezultat powinien mieć właściciela, Issue lub Pull Request oraz ślad w historii repozytorium.
