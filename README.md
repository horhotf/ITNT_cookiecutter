Шаблон для проектов ml

==============================

Упрощенный шаблон для проектов data science, разворачивается с помощью библиотеки cookiecutter

Структура проекта
------------

    ├── README.md               <- Общее описание проекта
    |        
    ├── {{cookiecutter.project_name}}   <- Директория со структурой проекта
    |   |        
    |   ├── data                    <- Данные. Сырые выборки и датасеты, появляющиеся в процессе разработки
    |   |
    |   ├── .gitignore               <- Список файлов, которые не нужно добавлять в git
    |   |
    |   ├── README.md               <- Общее описание проекта
    |   |                        
    |   ├── models                  <- Обученные и сериализованные файлы моделей
    |   |             
    |   ├── notebooks               <- Jupyter Notebooks
    |   |              
    |   ├── requirements.txt   	    <- Файл с описанием окружения модели, в нем указываются необходимые для работы модели библиотеки. Сгенерировать файл можно командой `pip freeze > requirements.txt`
    |   └── src                     <- Скрипты, используемые в проекте
    |      └── __init__.py
    |        
    └── cookiecutter.json           <- Параметры устанавлемые пользователем

--------
**Процес запуска шаблона**

Шаблон запрашивает 4 значения:

Название проекта ("project_name": "default_name") устанавливает название директории и записывает README

Описание проекта ("description") поставленная задача и метод решения, записывается в README

Сбособ запуска проекта("description_project_run") пишется для разработчиков, которые будут работать с проектом

Версия Python("python_version": "python3.7") для воспроизведения окружения
