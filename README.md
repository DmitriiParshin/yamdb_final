![yamdb_workflow](https://github.com/DmitriiParshin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# yamdb_final
**REST API** для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Произведению может быть присвоен жанр. Новые жанры может создавать только администратор.
Читатели оставляют к произведениям текстовые отзывы, и выставляют рейтинг (оценку в диапазоне от одного до десяти).
Из множества оценок автоматически высчитывается средняя оценка произведения.
* Аутентификация по JWT-токену
* Поддерживает методы GET, POST, PUT, PATCH, DELETE
* Предоставляет данные в формате JSON
* Создан в команде из трёх человек с использованием Git в рамках учебного курса Яндекс.Практикум.
## Стэк технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- библиотека django-filter - фильтрация запросов
- база данных - Postgresql
- HTTP-сервер - Nginx
- Для запуска проекта используется Docker
- система управления версиями - Git
## Алгоритм регистрации пользователей
- Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами *email* и *username* на эндпоинт /api/v1/auth/signup/.
- **YaMDB** отправляет письмо с кодом подтверждения (*confirmation_code*) на адрес *email*.
- Пользователь отправляет POST-запрос с параметрами *username* и *confirmation_code* на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
- При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).
## Пользовательские роли
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** (*user*) — может, как и **Аноним**, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- **Модератор** (*moderator*) — те же права, что и у А**утентифицированного пользователя** плюс право удалять любые отзывы и комментарии.
- **Администратор** (*admin*) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Суперюзер Django** — обладает правами администратора (*admin*)
## Ресурсы API YaMDb
- Ресурс AUTH: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).
- Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
- Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
______________________________________________________________________
## Как запустить проект:
1. Клонируйте репозиторий с проектом и перейдите в каталог с ним:
```
git clone https://github.com/DmitriiParshin/infra_sp2
cd infra_sp2
```
2. Создайте файл .env и заполните его как показано на примере:
```
touch .env
```
>_SECRET_KEY=YOUR_SECRET_KEY  
DB_ENGINE=YOUR_DB_ENGINE  
DB_NAME=YOUR_DB_NAME  
POSTGRES_USER=YOUR_POSTGRES_USER  
POSTGRES_PASSWORD=YOUR_POSTGRES_PASSWORD  
DB_HOST=YOUR_DB_HOST  
DB_PORT=YOUR_DB_PORT_  

3. Выполните команду для создания образов и запуска в контейнере приложения, сервера и базы данных
```
docker-compose up -d --build
```
4. Создайте и выполните миграции:
```
docker-compose exec web python manage.py makemigrations reviews users
docker-compose exec web python manage.py migrate
```
5. Создайте суперпользователя и соберите статику:
```
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```
__________________________________
_Ваш проект запустился на http://localhost/  
Полная документация доступна по адресу http://localhost/redoc/  
Админка для проверки и наполнения БД http://localhost/admin/_