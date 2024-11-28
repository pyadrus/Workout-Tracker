from typing import List

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

name_user = "Шварц"  # Имя пользователя, в дальнейшем берется из базы данных


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Стартовая страница с выбором дня недели."""
    return templates.TemplateResponse("index.html", {"request": request, "name_user": name_user})


@app.get("/types_of_exercises/{day}", response_class=HTMLResponse)
async def types_of_exercises(request: Request, day: str):
    """Выбор упражнения с учетом выбранного дня."""
    return templates.TemplateResponse("types_of_exercises.html", {"request": request, "day": day})


@app.get("/exercise/{day}/{exercise1}", response_class=HTMLResponse)
async def get_exercise(request: Request, day: str, exercise1: str):
    """Страница ввода данных о подходах (GET запрос)."""
    return templates.TemplateResponse("exercise.html", {"request": request, "day": day, "exercise1": exercise1})


@app.post("/exercise/{day}/{exercise1}", response_class=HTMLResponse)
async def post_exercise(
    request: Request,
    day: str,
    exercise1: str,
    sets: int = Form(...),
):
    """Страница ввода данных о подходах (POST запрос)."""
    return templates.TemplateResponse(
        "workout_calculation.html",
        {"request": request, "sets": sets, "day": day, "exercise1": exercise1},
    )


@app.post("/workout_calculation", response_class=HTMLResponse)
async def workout_data(
    request: Request,
    sets: int = Form(...),
    weights: List[float] = Form(...),
    reps: List[int] = Form(...),
):
    """Получение данных о подходах и их расчет."""
    total_weight = sum(weight * rep for weight, rep in zip(weights, reps))

    return templates.TemplateResponse("workout_result.html", {"request": request, "total_weight": total_weight})
