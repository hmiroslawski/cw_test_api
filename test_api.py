import subprocess
import json

# Endpointy do testowania wraz z oczekiwanymi kluczami
endpoints = {
    "https://jsonplaceholder.typicode.com/posts": ["userId", "id", "title"],
    "https://jsonplaceholder.typicode.com/comments": ["postId", "id", "name", "email", "body"],
    "https://jsonplaceholder.typicode.com/albums": ["userId", "id", "title"]
}


# Funkcja do testowania endpointu
def test_endpoint(url, expected_keys):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    response = result.stdout.decode('utf-8')

    try:
        data = json.loads(response)
        if isinstance(data, list) and data:
            first_item = data[0]
            keys = first_item.keys()
            if all(key in keys for key in expected_keys):
                return "PASSED"
            else:
                return f"FAILED: Missing expected keys. Expected keys: {expected_keys}. Found keys: {list(keys)}"
        else:
            return "FAILED: No data returned"
    except json.JSONDecodeError:
        return "FAILED: Invalid JSON"


# Testowanie wszystkich endpointów
for i, (endpoint, keys) in enumerate(endpoints.items(), start=1):
    result = test_endpoint(endpoint, keys)
    print(f"Test {i}: {result}")
