Проект для тестовых упражнений.  
Файл с переменным окружением доступен намеренно для тестов.  

**Запуск**  
docker-compose up -d

**Первоначальные действия**
*Инициализируем базу*  
docker-compose exec web python manage.py migrate  

*Создаем суперпользователя*  
docker-compose exec web python manage.py createsuperuser  

**API**  
*Авторизация*  
http://127.0.0.1:8000/api/v1/rest-auth/login/  
