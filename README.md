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
1. Uruchom reguły Makefile:
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
