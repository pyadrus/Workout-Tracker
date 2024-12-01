from typing import List

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()  # Создание приложения FastAPI.

# Подключение шаблонов и статических файлов.
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

name_user = "Шварц"  # Имя пользователя (в дальнейшем предполагается загрузка из базы данных).


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Отображение стартовой страницы с приветствием пользователя.

    :param request: Объект запроса.
    :return: HTML-страница с приветствием.
    """
    return templates.TemplateResponse("index.html", {"request": request, "name_user": name_user})


@app.get("/types_of_exercises/{day}", response_class=HTMLResponse)
async def types_of_exercises(request: Request, day: str):
    """
    Страница выбора упражнений на основе выбранного дня.

    :param request: Объект запроса.
    :param day: Выбранный день недели.
    :return: HTML-страница с вариантами упражнений.
    """
    return templates.TemplateResponse("types_of_exercises.html", {"request": request, "day": day})


@app.get("/exercise/{day}/{exercise1}", response_class=HTMLResponse)
async def get_exercise(request: Request, day: str, exercise1: str):
    """
    Страница ввода данных о подходах (GET-запрос).

    :param request: Объект запроса.
    :param day: Выбранный день недели.
    :param exercise1: Выбранное упражнение.
    :return: HTML-страница для ввода данных о подходах.
    """
    return templates.TemplateResponse("exercise.html", {"request": request, "day": day, "exercise1": exercise1})


@app.post("/exercise/{day}/{exercise1}", response_class=HTMLResponse)
async def post_exercise(request: Request, day: str, exercise1: str, sets: int = Form(...), ):
    """
    Обработка данных о подходах (POST-запрос).

    :param request: Объект запроса.
    :param day: Выбранный день недели.
    :param exercise1: Выбранное упражнение.
    :param sets: Количество подходов.
    :return: HTML-страница с результатами.
    """
    return templates.TemplateResponse(
        "workout_calculation.html",
        {"request": request, "sets": sets, "day": day, "exercise1": exercise1},
    )


@app.post("/workout_calculation", response_class=HTMLResponse)
async def workout_data(request: Request, weights: List[float] = Form(...), reps: List[int] = Form(...), ):
    """
    Расчет общего веса на основе данных о подходах.

    :param request: Объект запроса.
    :param weights: Список весов для каждого подхода.
    :param reps: Список повторений для каждого подхода.
    :return: HTML-страница с итоговым результатом расчета.
    """
    total_weight = sum(weight * rep for weight, rep in zip(weights, reps))

    return templates.TemplateResponse("workout_result.html", {"request": request, "total_weight": total_weight})
