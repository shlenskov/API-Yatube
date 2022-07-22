Проект, по адресу  `http://127.0.0.1:8000/redoc/`  будет доступна документация для API  **Yatube**. В документации описано, как должен работать API. Документация представлена в формате  **Redoc**.

Есть распространённый способ проектирования, согласно которому сначала составляют документацию, а потом, основываясь на ней как на техническом задании, пишут программную часть API. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git

```

```
cd kittygram

```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

```

```
source env/bin/activate

```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

```

```
pip install -r requirements.txt

```

Выполнить миграции:

```
python3 manage.py migrate

```

Запустить проект:

```
python3 manage.py runserver
```
-   **Примеры**. Некоторые примеры запросов к API.

GET ... api/v1/posts/

{

   "count": 123,
    
 "next": "[http://api.example.org/accounts/?offset=400&limit=100](http://api.example.org/accounts/?offset=400&limit=100)",
    
 "previous": "[http://api.example.org/accounts/?offset=200&limit=100](http://api.example.org/accounts/?offset=200&limit=100)",
    
 "results": [
    
       {}
        
    
    ]