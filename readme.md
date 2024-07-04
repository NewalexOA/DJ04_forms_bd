### [Описание на русском языке](#русский) 
### [Description in English](#english) 

---

## <a name="русский"></a>Описание на русском языке

### Описание
Этот проект выполнен в рамках задания на создание веб-приложения на Django. Проект называется `movie_project` и включает в себя приложение `films`.

### Задание:
"Создайте проект с именем `movie_project` и приложение в нем `films`. Создайте модель (таблицу) в которой будет поле для названия фильма, поле для описания фильма и поле для отзыва.

Создайте две HTML страницы, на одной из которых нужно заполнить 3 поля и отправить эту информацию в базу данных, а на второй будет публиковаться информация, которую вы записали в базу данных."

### Шаги выполнения:

1. **Создание проекта и приложения**:
   - Создан Django проект `movie_project`.
   - В проекте создано приложение `films`.

2. **Создание модели**:
   - В приложении `films` создана модель `Film` с полями для названия фильма, описания и отзыва.

3. **Настройка форм**:
   - Создана форма `FilmForm` для ввода данных о фильме.

4. **Создание представлений (views)**:
   - Созданы представления для добавления нового фильма (`add_film`) и для отображения списка фильмов (`film_list`).

5. **Настройка шаблонов**:
   - Созданы два HTML шаблона: 
     - `add_film.html` для заполнения и отправки формы.
     - `film_list.html` для отображения списка добавленных фильмов.

6. **Настройка маршрутов (URLs)**:
   - Настроены URL маршруты для доступа к страницам добавления фильма и списка фильмов.

7. **Обработка ошибок**:
   - В шаблонах добавлена обработка ошибок для отображения сообщений в случае некорректного заполнения формы и отсутствия отзывов.

### Как запустить:
1. Выполните миграции базы данных.
2. Запустите сервер разработки Django.
3. Перейдите на страницу добавления фильма и добавьте новый фильм.
4. Перейдите на страницу списка фильмов, чтобы увидеть добавленные фильмы.

---

## <a name="english"></a>Description in English

### Description
This project is carried out as part of an assignment to create a Django web application. The project is named `movie_project` and includes the `films` application.

### Assignment:
"Create a project named `movie_project` and an application within it named `films`. Create a model (table) with fields for the film title, film description, and film review.

Create two HTML pages: one where you can fill out 3 fields and submit this information to the database, and another one where the information recorded in the database will be published."

### Steps completed:

1. **Project and application creation**:
   - Created the Django project `movie_project`.
   - Created the `films` application within the project.

2. **Model creation**:
   - Created the `Film` model in the `films` application with fields for the film's title, description, and review.

3. **Form setup**:
   - Created the `FilmForm` form for entering film data.

4. **Views creation**:
   - Created views for adding a new film (`add_film`) and for displaying the list of films (`film_list`).

5. **Template setup**:
   - Created two HTML templates:
     - `add_film.html` for filling out and submitting the form.
     - `film_list.html` for displaying the list of added films.

6. **URL routing setup**:
   - Configured URL routes to access the film addition and film list pages.

7. **Error handling**:
   - Added error handling in templates to display messages in case of incorrect form submission and absence of reviews.

### How to run:
1. Apply database migrations.
2. Start the Django development server.
3. Navigate to the film addition page and add a new film.
4. Navigate to the film list page to see the added films.
