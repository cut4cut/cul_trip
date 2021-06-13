# Рекомендательная система для хакатона [moscityhack](https://moscityhack.innoagency.ru)

Описание
-----------------------------------------
Реализация рекомендательной системы на основе эмбеддингов описания событий (doc2vec). Эмбединги строились на датасете с описанием событий с конца 2017 года.

Запуск
-----------------------------------------
    make devenv
    source env/bin/activate
    analyzer-recsys

Быстрые команды
---------------
* `make` Отобразить список доступных команд
* `make devenv` Создать и настроить виртуальное окружение для разработки
* `make lint` Проверить синтаксис и стиль кода с помощью [`pylama`](https://github.com/klen/pylama)
* `make clean` Удалить файлы, созданные модулем [`distutils`](https://docs.python.org/3/library/distutils.html)

Repo Group
---------------
back_api:  [Konab/cul_trip_back](https://github.com/Konab/cul_trip_back)
ML:  [this project](https://github.com/cut4cut/cul_trip)
front_web:  [Tenutes/cul_trip_frontend](https://github.com/Tenutes/cul_trip_frontend)

Enjoy