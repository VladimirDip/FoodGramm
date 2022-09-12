# foodgram-project
[![foodgram_workflow](https://github.com/vamotest/foodgram-project/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master)](https://github.com/vamotest/foodgram-project/actions/workflows/foodgram_workflow.yml)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)


# Index
- [Описание](#описание)
  - [Исходники](#исходники)
  - [HTML](#html)
  - [JavaScript](#javascript)
  - [Список ингредиентов](#список-ингредиентов)
  - [Рецепт](#рецепт)
  - [Ингредиент](#ингредиент)
  - [Сервисы и страницы проекта](#сервисы-и-страницы-проекта)
  - [Главная страница](#главная-страница)
  - [Страница рецепта](#страница-рецепта)
  - [Страница пользователя](#страница-пользователя)
  - [Подписка на авторов](#подписка-на-авторов)
  - [Список избранного](#список-избранного)
  - [Список покупок](#список-покупок)
  - [Фильтрация по тегам](#фильтрация-по-тегам)
  - [Регистрация и авторизация](#регистрация-и-авторизация)
  - [Что могут делать неавторизованные пользователи](#что-могут-делать-неавторизованные-пользователи)
  - [Что могут делать авторизованные пользователи](#что-могут-делать-авторизованные-пользователи)
  - [Что может делать администратор](#что-может-делать-администратор)
  - [Настройки админки](#настройки-админки)
  - [Технические требования и инфраструктура](#технические-требования-и-инфраструктура)

- [Чек-лист для проверки](#чек-лист-для-проверки)  
  - [Функциональность проекта](#функциональность-проекта)
  - [Для авторизованных пользователей](#для-авторизованных-пользователей)
  - [Для неавторизованных пользователей](#для-неавторизованных-пользователей)
  - [Администратор и админ-зона](#администратор-и-админ-зона)
  - [Инфраструктура](#инфраструктура)
  - [Оформление кода](#оформление-кода)


<br><br>
**[⬆ Back to Index](#index)**
## Описание
**foodgram** — онлайн-сервис, где пользователи смогут публиковать рецепты, 
подписываться на публикации других пользователей, добавлять понравившиеся р
ецепты в список «Избранное», а перед походом в магазин скачивать 
сводный список продуктов, необходимых для приготовления одного 
или нескольких выбранных блюд. 

<br><br>
**[⬆ Back to Index](#index)**
### Исходники
Студенты веб-факультета Яндекс.Практикума подготовили для вас HTML-шаблоны 
и JS-код, они сохранены в [данном](https://github.com/yandex-praktikum/foodgram-project) репозитории. 
Склонируйте его и делайте проект в нём.

<br><br>
**[⬆ Back to Index](#index)**
### HTML
[Макеты](https://www.figma.com/file/HHEJ68zF1bCa7Dx8ZsGxFh/Продуктовый-помощник-Final?node-id=0%3A), по которым свёрстаны шаблоны, можно посмотреть на Figma.com.

**Список шаблонов:**
* 1\. Главная страница проекта для неавторизованного пользователя.
* 2\. Главная страница проекта для авторизованного пользователя.
* 3\. Персональная страница пользователя (рецепты одного автора).
* 4\. Страницы для регистрации/авторизации/сброса пароля/изменения пароля.
* 5\. Страница рецепта для автора.
* 6\. Страница рецепта для авторизованного читателя.
* 7\. Страница рецепта для неавторизованного читателя.
* 8\. Страница создания рецепта.
* 9\. Страница редактирования/удаления рецепта.
* 10\. Страница подписок.
* 11\. Страница избранных рецептов.
* 12\. Страница списка покупок.
* 13\. Формы:
    * 13.1\. зарегистрироваться,
    * 13.2\. войти на сайт,
    * 13.3\. сбросить пароль,
    * 13.4\. изменить пароль.

<br><br>
**[⬆ Back to Index](#index)**
### JavaScript
При определённых действиях пользователя с веб-страницы 
будут отправляться запросы к бэкенду. Это делает внедрённый в страницу 
код JavaScript, язык сценариев, работающих на стороне клиента.

**JS будет отправлять запросы в таких случаях:**
* 1\. при добавлении рецепта в список избранного и удалении рецепта из списка;
* 2\. при добавлении рецепта в список покупок и удалении рецепта из списка;
* 3\. при подписке на автора и отмене подписки;
* 4\. при вводе названия ингредиента в форме создания рецепта: 
  на сервер отправляется введённый в поле фрагмент текста, 
  возвращаются найденные совпадения, которые выводятся в подсказки. 
  При выборе нужного ингредиента подставляются соответствующие 
  единицы измерения: «Яйца — шт», «Молоко — мл», «Сахар — г»;
* 5\. при изменении количества рецептов в «Списке покупок»: 
  в запросе отправляется ID добавленного/удалённого рецепта, 
  после успешного запроса в шапке сайта обновляется счётчик.

<br><br>
**[⬆ Back to Index](#index)**
### Список ингредиентов
Мы подготовили для вас небольшой [список ингредиентов](https://code.s3.yandex.net/backend-developer/learning-materials/ingredients.zip) с единицами измерения, 
чтобы вам не пришлось вручную заполнять базу. 


<br><br>
**[⬆ Back to Index](#index)**
### Рецепт

**Рецепт должен описываться такими полями:**
* 1\. Автор публикации (пользователь).
* 2\. Название.
* 3\. Картинка.
* 4\. Текстовое описание.
* 5\. Ингредиенты: продукты для приготовления блюда по рецепту. 
  Множественное поле, выбор из предустановленного списка, 
  с указанием количества и единицы измерения.
* 6\. Тег (можно установить несколько тегов на один рецепт, 
  выбор из предустановленных): завтрак, обед, ужин.
* 7\. Время приготовления в минутах.
* 8\. Slug (уникальная часть URL для рецепта) — по желанию.

Все поля обязательны для заполнения.

<br><br>
**[⬆ Back to Index](#index)**
### Ингредиент
Данные об ингредиентах должны храниться в нескольких связанных таблицах. 
В результате на стороне пользователя ингредиент 
должен описываться такими полями:
- Название.
- Количество.
- Единицы измерения.

Все поля обязательны для заполнения.

<br><br>
**[⬆ Back to Index](#index)**
### Сервисы и страницы проекта
Посмотрите HTML-шаблоны и [дизайн-макеты](https://clck.ru/TrMSi), 
это поможет лучше ориентироваться в описании.

<br><br>
**[⬆ Back to Index](#index)**
### Главная страница
Содержимое главной страницы — список рецептов, 
отсортированных по дате публикации (от новых к старым).

<br><br>
**[⬆ Back to Index](#index)**
### Страница рецепта
На странице — полное описание рецепта, возможность добавить рецепт 
в избранное и в список покупок, возможность подписаться на автора рецепта.

<br><br>
**[⬆ Back to Index](#index)**
### Страница пользователя
На странице — имя пользователя, все рецепты, опубликованные пользователем 
и возможность подписаться на пользователя.

<br><br>
**[⬆ Back to Index](#index)**
### Подписка на авторов
Подписка на публикации доступна только авторизованному пользователю. 
Страница подписок доступна только владельцу.

**Сценарий поведения пользователя:**
- Пользователь переходит на страницу другого пользователя или на страницу 
  рецепта и подписывается на публикации автора 
  кликом по кнопке «Подписаться на автора».
- Пользователь переходит на страницу «Мои подписки» и просматривает 
  список рецептов, опубликованных теми авторами, на которых он подписался. 
  Сортировка записей — по дате публикации (от новых к старым).
- При необходимости пользователь может отказаться от подписки на автора: 
  переходит на страницу автора или на страницу его рецепта 
  и нажимает «Отписаться от автора».

<br><br>
**[⬆ Back to Index](#index)**
### Список избранного
Работа со списком избранного доступна только авторизованному пользователю. 
Список избранного может просматривать только его владелец.

**Сценарий поведения пользователя:**
- Пользователь отмечает один или несколько рецептов кликом 
  по кнопке «Добавить в избранное».
- Пользователь переходит на страницу «Список избранного» и просматривает 
  персональный список избранных рецептов.
- При необходимости пользователь может удалить рецепт из избранного.

<br><br>
**[⬆ Back to Index](#index)**
### Список покупок
Работа со списком покупок доступна авторизованным пользователям. Список покупок может просматривать только его владелец.

**Сценарий поведения пользователя:**
- Пользователь отмечает один или несколько рецептов кликом 
  по кнопке «Добавить в покупки».
- Пользователь переходит на страницу `Список покупок`, там доступны 
  все добавленные в список рецепты. 
  Пользователь нажимает кнопку `Скачать список` и получает файл 
  с суммированным перечнем и количеством необходимых ингредиентов 
  для всех рецептов, сохранённых в «Списке покупок».

При необходимости пользователь может удалить рецепт из списка покупок.
Список покупок скачивается в формате `*.txt`.

При скачивании списка покупок ингредиенты в результирующем 
списке не должны дублироваться; 
если в двух рецептах есть сахар (в одном рецепте 5 г, в другом — 10 г), 
то в списке должен быть один пункт: *Сахар — 15 г.*

**В результате список покупок может выглядеть так:**
<details>
<summary>Список покупок</summary>
- Фарш (баранина и говядина) (г) — 600 <br>
- Сыр плавленый (г) — 200 <br>
- Лук репчатый (г) — 50 <br>
- Картофель (г) — 1000 <br>
- Молоко (мл) — 250 <br>
- Яйцо куриное (шт) — 5 <br>
- Соевый соус (ст. л.) — 8 <br>
- Сахар (г) — 230 <br>
- Растительное масло рафинированное (ст. л.) — 2 <br>
- Соль (по вкусу) — 4 <br>
- Перец черный (щепотка) — 3 <br>
</details>

**По желанию:** в список покупок можно вывести шапку и подвал (или что-то одно)
с информацией о вашем проекте.

**По желанию:** можно настроить проект так, чтобы сервис `Список покупок`
был доступен и неавторизованным пользователям. 

Работа с сессиями поможет решить эту задачу.
**Документация по работе с сессиями в Django:**
- [Описание](https://docs.djangoproject.com/en/3.1/topics/http/sessions/)
- [Примеры](https://docs.djangoproject.com/en/3.1/topics/http/sessions/#examples)

<br><br>
**[⬆ Back to Index](#index)**
### Фильтрация по тегам
При нажатии на название тега выводится список рецептов, отмеченных этим тегом. 
Фильтрация может проводится по нескольким тегам в комбинации «или»: 
если выбраны несколько тегов — в результате должны быть показаны рецепты, 
которые отмечены хотя бы одним из этих тегов.

При фильтрации на странице пользователя должны фильтроваться только рецепты 
выбранного пользователя. Такой же принцип должен соблюдаться 
при фильтрации списка избранного.


<br><br>
**[⬆ Back to Index](#index)**
### Регистрация и авторизация
В проекте должна быть доступна система регистрации и авторизации пользователей. 
Чтобы собрать весь код для управления пользователями 
воедино — создайте приложение `users`.

Обязательные поля для пользователя:
- Логин
- Пароль
- Email

Валидация email при регистрации — **по желанию**.

**Уровни доступа пользователей:**
- Гость (неавторизованный пользователь)
- Авторизованный пользователь
- Администратор

<br><br>
**[⬆ Back to Index](#index)**
### Что могут делать неавторизованные пользователи
- Создать аккаунт.
- Просматривать рецепты на главной.
- Просматривать отдельные страницы рецептов.
- Просматривать страницы пользователей.
- Фильтровать рецепты по тегам.

<br><br>
**[⬆ Back to Index](#index)**
### Что могут делать авторизованные пользователи
* 1\. Входить в систему под своим логином и паролем.
* 2\. Выходить из системы (разлогиниваться).
* 3\. Восстанавливать свой пароль.
* 4\. Менять свой пароль.
* 5\. Создавать/редактировать/удалять собственные рецепты.
* 6\. Просматривать рецепты на главной.
* 7\. Просматривать страницы пользователей.
* 8\. Просматривать отдельные страницы рецептов.
* 9\. Фильтровать рецепты по тегам.
* 10\. Работать с персональным списком избранного: добавлять/удалять `чужие` рецепты, 
  просматривать свою страницу избранных рецептов.
* 11\. Работать с персональным списком покупок: добавлять/удалять `любые` рецепты,
  выгружать файл с количеством необходимых ингредиентов 
  для рецептов из списка покупок.
* 12\. Подписываться на публикации авторов рецептов и отменять подписку,
  просматривать свою страницу подписок.

<br><br>
**[⬆ Back to Index](#index)**
### Что может делать администратор
Администратор обладает всеми правами авторизованного пользователя.

**Плюс к этому он может:**
- изменять пароль любого пользователя,
- создавать/блокировать/удалять аккаунты пользователей,
- редактировать/удалять `любые` рецепты,
- добавлять/удалять/редактировать ингредиенты.

<br><br>
**[⬆ Back to Index](#index)**
### Настройки админки
В интерфейс админ-зоны нужно вывести необходимые поля моделей 
и настроить фильтры.

**Модели:**
- Вывести все модели с возможностью редактирования и удаление записей.

**Модель пользователей:**
- Добавить фильтр списка по email и имени пользователя.

**Модель рецептов:**
- В списке рецептов вывести название и автора рецепта.
- Добавить фильтр по автору, названию рецепта, тегам.
- На странице рецепта вывести число добавлений этого рецепта в избранное.

**Модель ингредиентов:**
- В список вывести название ингредиента и единицы измерения.
- Добавить фильтр по названию.

<br><br>
**[⬆ Back to Index](#index)**
### Технические требования и инфраструктура
- Проект должен использовать базу данных PostgreSQL.
- В Django-проекте должен быть файл requirements.txt со всеми зависимостями.
- Проект нужно запустить в трёх контейнерах (nginx, PostgreSQL и Django) 
  через docker-compose на вашем сервере в Яндекс.Облаке. 
  Образ с проектом должен быть запушен на Docker Hub.

<br><br>
**[⬆ Back to Index](#index)**
## Чек-лист для проверки

<br><br>
**[⬆ Back to Index](#index)**
### Функциональность проекта
* 1\. Проект доступен по IP или доменному имени.
* 2\. Все сервисы и страницы доступны для пользователей в соответствии с их правами.
* 3\. Рецепты на всех страницах сортируются по дате публикации (новые — выше).
* 4\. Работает фильтрация по тегам, в том числе на странице избранного 
и на странице рецептов одного автора).
* 5\. Работает пагинатор (в том числе при фильтрации по тегам).
* 6\. Обрабатывается ошибка 404.


<br><br>
**[⬆ Back to Index](#index)**
### Для авторизованных пользователей
* 1\. Доступна главная страница.
* 2\. Доступна страница другого пользователя.
* 3\. Доступна страница отдельного рецепта.

* 4\. Доступна страница «Мои подписки».
    * 4.1\. Можно подписаться и отписаться на странице рецепта.
    * 4.2\. Можно подписаться и отписаться на странице автора.
    * 4.3\. При подписке рецепты автора добавляются на страницу «Мои подписки» 
      и удаляются оттуда при отказе от подписки.


* 5\. Доступна страница «Избранное».
    * 5.1\. На странице рецепта есть возможность добавить рецепт в список 
      избранного и удалить его оттуда.
    * 5.2\. На любой странице со списком рецептов есть возможность 
      добавить рецепт в список избранного и удалить его оттуда.

* 6\. Доступна страница «Список покупок».
    * 6.1\. На странице рецепта есть возможность добавить рецепт 
      в список покупок и удалить его оттуда.
    * 6.2\. На любой странице со списком рецептов есть возможность 
      добавить рецепт в список покупок и удалить его оттуда.
    * 6.3\. Есть возможность выгрузить файл txt с перечнем и количеством 
      необходимых продуктов для рецептов из «Списка покупок».
    * 6.4\. Ингредиенты в выгружаемом списке не повторяются, 
      корректно подсчитывается общее количество для каждого ингредиента.

* 7\. Доступна страница «Создать рецепт».
    * 7.1\. Есть возможность опубликовать свой рецепт.
    * 7.2\. Есть возможность отредактировать и сохранить изменения в своём рецепте.
    * 7.3\. Есть возможность удалить свой рецепт.  

* 8\. Доступна и работает форма изменения пароля.
* 9\. Доступна возможность выйти из системы (разлогиниться).

<br><br>
**[⬆ Back to Index](#index)**
### Для неавторизованных пользователей
* 1\. Доступна главная страница.
* 2\. Доступна страница отдельного рецепта.
* 3\. Доступна страница любого пользователя.
* 4\. Доступна и работает форма авторизации.
* 5\. Доступна и работает система восстановления пароля.
* 6\. Доступна и работает форма регистрации.

<br><br>
**[⬆ Back to Index](#index)**
### Администратор и админ-зона
* 1\. Все модели выведены в админ-зону.
* 2\. Для модели пользователей включена фильтрация по имени и email.
* 3\. Для модели рецептов включена фильтрация по названию.
* 4\. Для модели ингредиентов включена фильтрация по названию.

<br><br>
**[⬆ Back to Index](#index)**
### Инфраструктура
* 1\. Проект работает с СУБД PostgreSQL.



<br><br>
**[⬆ Back to Index](#index)**
### Оформление кода
Код соответствует PEP8.

<br><br>
