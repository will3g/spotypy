# API em DJANGO para músicas - Spotypy

## Para rodar o projeto 

- python manage.py runserver

## Método POST

- curl -X POST http://127.0.0.1:8000/musics/ -H 'content-type: application/json' -d '{"title": "É isso ai", "seconds": 305, "album": "é isso"}'

## Método GET

- curl -X GET http://127.0.0.1:8000/musics/ -H 'Aceppt: application/json'