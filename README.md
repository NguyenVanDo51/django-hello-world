## set requirement package
```bash
pip freeze > requirements.txt
```

## install all python modules and packages listed in the requirements.txt file
```bash
pip install -r .\requirements.txt
```

## migrations models in a app
```bash
python .\manage.py makemigrations youtube
```
## Running Locally

```bash
python manage.py runserver
```

Your Django application is now available at `http://localhost:8000`.

## DB
https://console.neon.tech/app/projects/tiny-scene-990279/tables?