{{cookiecutter.project_name}}

==============================

{{cookiecutter.description}}

В проекте используется {{cookiecutter.python_version}}

Структура проекта
------------

    ├── README.md               <- Общее описание проекта	
    |        
    ├── data                    <- Данные. Сырые выборки и датасеты, появляющиеся в процессе разработки
    |                        
    ├── models                  <- Обученные и сериализованные файлы моделей
    |             
    ├── notebooks               <- Jupyter Notebooks
    |              
    ├── requirements.txt   	    <- Файл с описанием окружения модели, в нем указываются необходимые для работы модели библиотеки. Сгенерировать файл можно командой `pip freeze > requirements.txt`
    └── src                     <- Скрипты, используемые в проекте
        └── __init__.py

--------
**Процес запуска проекта**

{{cookiecutter.description_project_run}}
