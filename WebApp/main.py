from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")  # Подключаем статические файлы

templates = Jinja2Templates(directory="templates")  # Указываем директорию с шаблонами.


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Отображение стартовой страницы с приветствием пользователя.

    :param request: Объект запроса.
    :return: HTML-страница с приветствием.
    """
    return templates.TemplateResponse("index.html", {"request": request})  # Добавлен context.view_results


@app.get("/about_us")
async def about(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("about_us.html", {"request": request})


@app.get("/view_results")
async def view_results(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("view_results.html", {"request": request})


@app.get("/basic_exercises")
async def basic_exercises(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("basic_exercises.html", {"request": request})


@app.get("/contacts")
async def contacts(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("contacts.html", {"request": request})


@app.get("/exercise")
async def exercise(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("exercise.html", {"request": request})


@app.get("/my_details")
async def my_details(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("my_details.html", {"request": request})


@app.get("/nutrition")
async def nutrition(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("nutrition.html", {"request": request})


@app.get("/settings")
async def settings(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("settings.html", {"request": request})


@app.get("/types_of_exercises")
async def types_of_exercises(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("types_of_exercises.html", {"request": request})


@app.get("/view_results")
async def view_results(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("view_results.html", {"request": request})


@app.get("/view_workouts")
async def view_workouts(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("view_workouts.html", {"request": request})


@app.get("/workout_calculation")
async def view_workouts(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("workout_calculation.html", {"request": request})


@app.get("/workout_result")
async def workout_result(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("workout_result.html", {"request": request})


@app.get("/сreate_workouts")
async def create_workouts(request: Request):
    """
    Отображение страницы с информацией о проекте.
    :return: HTML-страница с информацией о проекте.
    """
    return templates.TemplateResponse("create_workouts.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
