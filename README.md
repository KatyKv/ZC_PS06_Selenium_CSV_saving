# Проект: Парсинг данных с сохранением в CSV

## Описание проекта
Учебный проект по парсингу данных с сайтов с использованием Selenium и Scrapy. Полученные данные сохраняются в файлы CSV, а также выводятся в консоль.

## Структура проекта
```
ZC_PS06_parsing_CSV_saving/
|
├── divanpars/               # Парсинг товаров с сайта divan.ru
│   ├── divanpars/
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   ├── divansecondpars.py  # Парсер для раздела "Декор"
│   │   │   ├── div_decor.csv       # Файл с сохраненными данными
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   ├── scrapy.cfg
│
├── hh_selenium.csv          # Файл с вакансиями с hh.ru
├── hh_selenium.py           # Парсер вакансий с hh.ru на Selenium
├── requirements.txt         # Список зависимостей проекта
├── .gitignore               # Файл исключений для Git
```

## Используемые технологии
- Python
- Scrapy
- Selenium
- CSV

## Запуск парсеров

### Парсинг вакансий с hh.ru (Selenium)
```sh
python hh_selenium.py
```
Данные сохраняются в `hh_selenium.csv`.

### Парсинг раздела "Декор" с divan.ru (Scrapy)
```sh
cd divanpars
tscrapy crawl divansecondpars
```
Данные сохраняются в `div_decor.csv`.

## Установка зависимостей
Перед запуском установите необходимые библиотеки:
```sh
pip install -r requirements.txt
```

