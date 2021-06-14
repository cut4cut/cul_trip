# Рекомендательная система для хакатона [moscityhack](https://moscityhack.innoagency.ru)

Описание
-----------------------------------------
Реализация рекомендательной системы на основе эмбеддингов описания событий (doc2vec). Эмбединги строились на [датасете](https://data.mos.ru/opendata/2251) с описанием событий с конца 2017 года и на недавних событиях с [mos.ru/afisha](https://www.mos.ru/api/newsfeed/v4/frontend/json/ru/afisha).

В качестве лемматизатора был использован `pymystem3`, список стоп-слов русского языка из `nltk.corpus`. Для построение эмбедингов использовалась реализация из `gensim`. 

Рекомендательная система по выбранным записям из таблицы `events` выдаёт оценку соответствия двух событий между собой. Данная оценка записывается в таблицу `scores` для дальнейшего использования на backend.

Запуск
-----------------------------------------
1. Написать параметры доступа к БД в `.env` файле.
2. Создать виртуальное окружение.
```
make devenv
source env/bin/activate
```
3. Запустить.
```
analyzer-recsys
```

Быстрые команды
---------------
* `make` Отобразить список доступных команд
* `make devenv` Создать и настроить виртуальное окружение для разработки
* `make lint` Проверить синтаксис и стиль кода с помощью [`pylama`](https://github.com/klen/pylama)
* `make clean` Удалить файлы, созданные модулем [`distutils`](https://docs.python.org/3/library/distutils.html)

Repo Group
---------------
* back_api:  [Konab/cul_trip_back](https://github.com/Konab/cul_trip_back)
* ML:  [this project](https://github.com/cut4cut/cul_trip)
* front_web:  [Tenutes/cul_trip_frontend](https://github.com/Tenutes/cul_trip_frontend)

Enjoy ❤️