from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Стартовая страница"""
    return render_template('index.html')


@app.route('/exercise/<day>', methods=['GET', 'POST'])
def exercise(day):
    """Страница ввода тренировки"""
    if request.method == 'POST':
        sets = int(request.form['sets'])
        return render_template('workout_calculation.html', sets=sets, day=day)
    return render_template('exercise.html', day=day)


@app.route('/workout_calculation', methods=['POST'])
def workout_data():
    """Получение данных о подходах и их сохранение"""
    total_weight = 0
    # Получаем все веса и повторения из формы
    sets = int(request.form['sets'])  # Количество подходов
    for i in range(sets):
        weight = float(request.form[f'set[{i}][weight]'])  # Вес
        reps = int(request.form[f'set[{i}][reps]'])  # Повторения
        total_weight += weight * reps

    return render_template('workout_result.html', total_weight=total_weight)


if __name__ == '__main__':
    app.run(debug=True)
