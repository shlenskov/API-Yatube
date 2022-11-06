Yatube - социальная сеть. Пользователи могут создать учетную запись, публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи.  

По адресу `http://127.0.0.1:8000/redoc/` доступна документация для API **Yatube**. В документации описано, как должен работать API. Документация представлена в формате **Redoc**.

### Как запустить проект:  
  
Клонировать репозиторий и перейти в него в командной строке:  
  
```  
git clone git@github.com:shlenskov/API-Yatube.git  
  
```  
  
```  
cd api_final_yatube  
  
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
pip install -r requirements.txt
  
```  
  
```  
  
python3 -m pip install --upgrade pip
```  
  
Выполнить миграции:  
  
```  
python3 manage.py migrate  
  
```  
  
Запустить проект:  
  
```  
python3 manage.py runserver  
```  
-   **Пример**. Пример запроса к API.  
  
POST .../api/v1/posts/  
  
{
  "text": "ваш текст",
  "group": 0
}
      
 Автор: Шленсков Владимир.
