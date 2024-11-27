from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exercise')
def exercise():
    return render_template('exercise.html')


@app.route('/workout_data', methods=['POST'])
def workout_data():
    sets = int(request.form['sets'])
    workout_data = []

    # Собираем данные о подходах
    for i in range(sets):
        workout_data.append({
            'weight': 0,  # Изначально вес 0
            'reps': 0     # Изначально повторений 0
        })

    # Передаем данные о подходах на страницу для расчета
    return render_template('workout_calculation.html', workout_data=workout_data)

@app.route('/calculate_workout', methods=['POST'])
def calculate_workout():
    workout_data = request.form.getlist('workoutData')
    total_weight = sum([float(data.split(',')[0]) * int(data.split(',')[1]) for data in workout_data])

    return f'Общий поднятый вес: {total_weight} кг'

if __name__ == '__main__':
    app.run(debug=True)
