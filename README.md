BlijvenLeren
========

Dit is de een beschrijing voor het installeren van de Blijven Leren demo applicatie

Installatie
============

1. Installeer python, indien nog niet eerder gedaan
   ```
   Kan worden gedownload vanaf https://www.python.org/downloads/
   ```
1. Installeer postgres en maak een database aan, of configureer de app met een andere DB in wigo4it.settings.DATABASES
    ```
    - Postgres beschikbaar op https://www.postgresql.org/download/
      Installeer en maak database aan vanaf command line: createdb blijvenleren 
    - Log in PostgreSQL terminal van blijvenleren database: psql blijvenleren    
      > create user wigo4it with password 'now';
      > grant all privileges on database blijvenleven to wigo4it;
      > create schema wigo4it authorization wego4it;
      \q om PostgreSQL te verlaten
   ```
1. Maak een venv aan vanuit de root directory van het project
    ```
    python -m venv venv
    pip install -r requirements.txt
    ``` 
1. Creeer de tabellen in de database
    ```
    python manage.py migrate
    ```
1. Maak een superuser aan voor het admin en api scherm 
    ```
    python manage.py createsuperuser
    ```
1. Nu kan de server worden gestart:
    ```
    python manage.py runserver
    ```
1. Open een browser en navigeer naar
   ```
   127.0.0.1:8000/wigo4it/admin voor de admin pagina en log in met de superuser
   127.0.0.1:8000/wigo4it/api voor het testen van de api's
   127.0.0.1:8000/wigo4it/api/docs voor de documentatie van de api's
   ```
