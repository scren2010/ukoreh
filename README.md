<h1 align="center" >Install</h1> 

 - Устанавливаем окружение: python3.7 -m venv myvenv; source myvenv/bin/activate

 - Устанавливаем зависимости: pip install -r requirements.txt

 - Проводим миграции: ./manage.py migrate

 - Создать супер пользователя: ./manage.py createsuperuser

 - Запуск: ./manage.py runserver


<h3> Документация </h3>

- /schema/
- /docs/
- /swagger-docs/
 
<p>Авторизация через соц, сети.</p>

- Вход через google:
    /accounts/google/login/

- Вход через facebook:
    /accounts/facebook/login/

- Вход через odnoklassniki:
    /accounts/odnoklassniki/login/