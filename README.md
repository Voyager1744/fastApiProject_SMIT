# fastApiProject_SMIT
Тестовое задание от компании SMIT.Studio

Реализован REST API сервис по расчёту стоимости страхования в зависимости
от типа груза и объявленной стоимости (ОС).


Технологии, которые использованы при реализации тестового задания:
- FastApi - framework
- Tortoise ORM
- Postgresql
- Docker
- Docker-compose с докером для постгресса


## Требования

Перед началом развертывания убедитесь, что на вашей системе установлены следующие компоненты:

- Docker 
- Docker Compose 

## Установка и настройка

1. Клонируйте репозиторий проекта:

```shell
git clone https://github.com/Voyager1744/fastApiProject_SMIT.git
```

2. Перейдите в директорию проекта:

```shell
cd fastApiProject_SMIT
```

3. Запустите контейнеры с использованием Docker Compose:
```shell
docker-compose up -d
```

Дождитесь успешного развертывания контейнеров.

Документация будет доступна по адресу 0.0.0.0:8000/docs

Тарифы загружаются из файла tariffs.json

Пример запроса:
```
http://0.0.0.0:8000/api/v1/insurance/2020-07-01/Glass/1000
```

## Автор
Ушаков Дмитрий



