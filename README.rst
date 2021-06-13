.. role:: shell(code)
   :language: shell

Разработка
==========

Быстрые команды
---------------
* :shell:`make` Отобразить список доступных команд
* :shell:`make devenv` Создать и настроить виртуальное окружение для разработки
* :shell:`make lint` Проверить синтаксис и стиль кода с помощью `pylama`_
* :shell:`make clean` Удалить файлы, созданные модулем `distutils`_

.. _pylama: https://github.com/klen/pylama
.. _distutils: https://docs.python.org/3/library/distutils.html
.. _source distribution: https://packaging.python.org/glossary/

Как подготовить окружение для разработки?
-----------------------------------------
.. code-block:: shell

    make devenv
    source env/bin/activate
    analyzer-recsys

Структура проекта взята из статьи для `практического руководства`_ по разработке бэкенд-сервисов на Python (на основе `вступительного испытания`_ в `Школу бэкенд-разработки Яндекса`_ в 2019 году).

.. _практического руководства: https://habr.com/ru/company/yandex/blog/499534/