To create the Backend:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Change the config file app/config.py to insert your own MySQL configurations.

Insert the SQL dumps to the MySQL database.

To run pytest properly an empty __init__.py file must be created inside tests directory.
For testing:

```
cd .../tests
pytest -v
```
