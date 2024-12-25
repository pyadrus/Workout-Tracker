# **Проект "StrongTrack_Bot"**

"Workout Tracker" — это веб-приложение для учета тренировок. Пользователь может выбрать день недели, указать количество
подходов, вес и количество повторений, после чего приложение рассчитает общий поднятый вес за тренировку.

## **Функционал проекта:**

- **Выбор дня недели**: Пользователь выбирает день, для которого будет добавлена тренировка.
- **Ввод данных о тренировке**: Пользователь вводит количество подходов, вес и количество повторений для каждого
  подхода.
- **Расчет общего веса**: Приложение рассчитывает суммарный поднятый вес за тренировку.
- **Отображение результата**: Итоговый результат отображается в удобном формате.

---

## **Установка и запуск:**

### 1. Клонирование репозитория:

```bash
git clone https://github.com/username/workout-tracker.git cd workout-tracker
```

### 2. Установка зависимостей:

Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows
```

Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

### 3. Запуск приложения:

```bash
uvicorn main:app
```

После запуска приложение будет доступно по адресу: `http://127.0.0.1:5000/`.

---

## **Использование:**

1. **Главная страница**: Выберите день недели, нажав на соответствующую кнопку.
2. **Ввод данных**: Укажите количество подходов и нажмите "Далее".
3. **Заполнение подходов**: Введите вес и количество повторений для каждого подхода.
4. **Расчет веса**: Нажмите "Рассчитать", чтобы увидеть общий поднятый вес.

---

## **Файловая структура:**
```csharp
workout-tracker/
├── bot/
│   ├── data/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── administration_panel.py
│   │   ├── feedback.py
│   │   ├── launch_bot.py
│   │   ├── personal_acount.py
│   │   └── registration_user.py
│   ├── keyboards/
│   │   ├── __init__.py
│   │   └── keyboards.py
│   ├── messages/
│   │   ├── text_admin_panel.json
│   │   ├── text_authorized_user_greeting.json
│   │   ├── text_description.json
│   │   ├── text_hello_welcome.json
│   │   ├── text_input_height_error.json
│   │   ├── text_input_height.json
│   │   ├── text_input_name.json
│   │   ├── text_input_training_experience.json
│   │   ├── text_input_weight_error.json
│   │   ├── text_input_weight.json
│   │   └── text_sending_message.json
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py
│   └── run_bot.py
├── WebApp/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── images/
│   │   │   └── avatar.jpg
│   ├── templates/
│   │   ├── basic_exercises/
│   │   ├── day_of_the_week/
│   └── main.py
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
├── sqlite3.db
├── TODO.md
```

```csharp

workout-tracker/
├── static/
│   └── css/
│       └── styles.css            # Стили для всех страниц
├── templates/
│   ├── index.html                # Главная страница
│   ├── exercise.html             # Страница ввода данных
│   ├── workout_calculation.html  # Страница расчета тренировки
│   └── workout_result.html       # Страница с результатом
├── app.py                        # Основной файл приложения Flask
└── README.md                     # Документация проекта
```

---

## **Технологии:**

- **Python**
- **Fastapi** — для создания веб-приложения.
- **HTML/CSS** — для отображения страниц и стилизации.

---

## **Возможности для улучшения:**

- Добавление возможности сохранять результаты тренировок.
- Расширение функционала для просмотра статистики по дням.
- Поддержка авторизации пользователей.

Установка бота

1. установить зависимости requirements.txt
2. создать файл .env и туда записать переменную TOKEN="токен вашего бота" и ADMIN_ID=id_вашего телеграмма - чтобы работало админка и BASE_SITE=url_вашего_сайта
