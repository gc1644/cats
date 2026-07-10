help:
	@echo "Commands:"
	@echo " make password	Generate a password"
	@echo " make random-cat	Pick a random cat name"

password:
	python3 password.py

random-cat:
	python3 random_cat.py

clean:
	@echo "Nothing to clean... yet."

check:
	python3 -m py_compile password.py
	python3 -m py_compile random_cat.py
