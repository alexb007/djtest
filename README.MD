#DJTEST

###Подготовить DOCKER
Для инициализации docker контейнеров требуется выполнить:

```
sudo ./scripts/first_start.sh
```

Запустить проект:
```
sudo docker-compose up -d project nginx
```

URL приложения: http://<server_url>:8000


#Документация по API

##Endpoint Application

`http://localhost:8000/api/applications/`

##Создание:

Метод: `POST`

Url: `http://localhost:8000/api/applications/`

Параметры:

``
    "name" 
``
название для нового приложения

Ответ: 
```
{
    "id": 1,
    "name": "Application name",
    "api_key": "4bf92d86f85479d26f9a15d1333bde181aebcfe37cfbcfa961c97171892b7ed2",
    "created": "2020-04-22T14:35:57.869039Z",
    "updated": "2020-04-22T14:35:57.869113Z"
}
```

##Изменение
Метод: `PUT`

Url: `http://localhost:8000/api/applications/<app_id>/`

Параметры:

``
    "name" 
``
название для нового приложения

Ответ: 
```
{
    "id": 1,
    "name": "Application name",
    "api_key": "4bf92d86f85479d26f9a15d1333bde181aebcfe37cfbcfa961c97171892b7ed2",
    "created": "2020-04-22T14:35:57.869039Z",
    "updated": "2020-04-22T14:35:57.869113Z"
}
```

##Генерировать новый ключь API
Метод: `POST`

Url: `http://localhost:8000/api/applications/<app_id>/refresh_apikey/`

Ответ: 
```
{
    "API_KEY": "4c9fe4450ee460d963abb1668c242a35118bffcde4f04d0a18a6e16b7ff4c43e"
}
```


##Endpoint Test

`http://localhost:8000/api/test/`

Метод: `GET`

Параметры:

`api_key` Ключ апи от приложения
