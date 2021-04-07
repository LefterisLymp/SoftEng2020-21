Για την δημιουργία του Backend:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

Πρέπει να γίνει αλλαγή στο έγγραφο /app/config.py το οποίο περιέχει τα στοιχεία της mysql του user.

Πρέπει επίσης από τα sql dumps να βάλει ο χρήστης τα αντίστοιχα δεδομένα στη βάση MySQL

Για να τρέξει σωστά το pytest πρέπει να μπεί ένα κενό __init__ μέσα στο φάκελο tests
Για το testing στο Terminal: 
	cd .../tests
	pytest -v
