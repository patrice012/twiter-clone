# this is just a twitter app simulation build with other technologies

## INSTALLATION

- create a virtual environnement using `python -m venv envir_name`
- activate your environnement `source envir_name/bin/activate` in UNIX base OS
- `cd envir_name` (optional)
- clone the repository `git clone https://...`
- install all dependecies packages `pip install -r requirements/base.txt`
- install others packages if need `test.txt use for testing`
- create `.env` file in the root of the project directory and put all your environnement variables inside (like `secret_key`, `Data Base information` ...)
- install postgress SQL `pip install posgressql` (optinal)
- create postgress database (optional)
- make migration `python manage.py makemigrations && python manage.py migrate`
- create superuser account `python manage.py createsuperuser`
- run django server `puthon manage.py runserver`
-go to `localhost:880` or `192.0.0.1` and enjoy the app
