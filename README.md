# Automatyzacja testów API z wykorzystaniem curl

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