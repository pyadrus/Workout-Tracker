from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Стартовая страница с выбором дня недели"""
    return render_template('index.html')

@app.route('/types_of_exercises/<day>')
def types_of_exercises(day):
    """Выбор упражнения с учетом выбранного дня"""
    return render_template('types_of_exercises.html', day=day)

@app.route('/exercise/<day>/<exercise1>', methods=['GET', 'POST'])
def exercise(day, exercise1):
    """Страница ввода данных о подходах"""
    if request.method == 'POST':
        sets = int(request.form['sets'])
        return render_template('workout_calculation.html', sets=sets, day=day, exercise1=exercise1)
    return render_template('exercise.html', day=day, exercise1=exercise1)

@app.route('/workout_calculation', methods=['POST'])
def workout_data():
    """Получение данных о подходах и их расчет"""
    total_weight = 0
    sets = int(request.form['sets'])
    for i in range(sets):
        weight = float(request.form[f'set[{i}][weight]'])
        reps = int(request.form[f'set[{i}][reps]'])
        total_weight += weight * reps

    return render_template('workout_result.html', total_weight=total_weight)

if __name__ == '__main__':
    app.run(debug=True)
