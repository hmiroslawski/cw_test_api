# Zadanie 1 - Automatyzacja testów API z wykorzystaniem curl

## Opis
Skrypt w Pythonie, który automatycznie testuje różne endpointy API przy użyciu `curl`. Skrypt wysyła żądania HTTP do publicznego API JSONPlaceholder i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON).

## Użycie
1. Upewnij się, że masz zainstalowany Python oraz `curl`.
2. Uruchom skrypt:
    ```sh
    python test_api.py
    ```

## Wyniki
Skrypt wyświetla wyniki sprawdzeń w czytelny sposób, np.:
```
Test 1: PASSED
Test 2: PASSED
Test 3: PASSED
```


# Zadanie 2 - Automatyzacja procesów z wykorzystaniem Makefile

## Opis
Plik Makefile, który zautomatyzuje procesy testowania i uruchamiania aplikacji w Pythonie. Makefile zawiera reguły dla instalacji zależności, uruchamiania testów jednostkowych oraz uruchamiania aplikacji.

## Użycie
1. Zainstaluj MSYS2 z [oficjalnej strony MSYS2](https://www.msys2.org/) i otwórz go.
2. Zainstaluj narzędzie `make`:
    ```sh
    pacman -Syu
    pacman -S make
    ```
3. Dodaj MSYS2 do zmiennej PATH, aby `make` było dostępne w Git Bash.
4. Przejdź do katalogu projektu:
    ```sh
    cd /path/to/your/project
    ```
5. Utwórz plik Makefile i dodaj do niego odpowiednie reguły:
    ```sh
    nano Makefile
    ```

6. Skopiuj poniższy kod do pliku Makefile:
    ```makefile
    # Reguła do instalacji zależności
    install:
        pip install -r requirements.txt

    # Reguła do uruchamiania testów jednostkowych
    test:
        python -m unittest test_app.py

    # Reguła do uruchamiania aplikacji
    run:
        python app.py 2 3
    ```

7. Zapisz zmiany i zamknij edytor.

8. Uruchom reguły Makefile:
    - Instalacja zależności:
        ```sh
        make install
        ```
    - Uruchamianie testów jednostkowych:
        ```sh
        make test
        ```
    - Uruchamianie aplikacji:
        ```sh
        make run
        ```

## Pliki
- `app.py`: Główna aplikacja.
- `test_app.py`: Testy jednostkowe dla aplikacji.
- `Makefile`: Definicje reguł do automatyzacji procesów.
- `requirements.txt`: Lista zależności.
