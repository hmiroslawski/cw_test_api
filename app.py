# plik app.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        a, b = map(int, sys.argv[1:3])
        print(add(a, b))
    else:
        print("Usage: python app.py num1 num2")
