# Reguła do instalacji zależności
install:
	pip install -r requirements.txt

# Reguła do uruchamiania testów jednostkowych
test:
	python -m unittest test_app.py

# Reguła do uruchamiania aplikacji
run:
	python app.py 2 3
