from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('exercise.html')

@app.route('/save_workout', methods=['POST'])
def save_workout():
    exercise = request.form['exercise']
    sets = request.form['sets']
    workout_data = json.loads(request.form['workoutData'])

    # Форматирование данных для записи
    workout_info = f"Упражнение: {exercise}\nКоличество подходов: {sets}\n\n"
    for idx, set_data in enumerate(workout_data, start=1):
        workout_info += f"Подход {idx}: Вес {set_data['weight']} кг, Повторений {set_data['reps']}\n"

    workout_info += "\n--------------------\n"

    # Запись в файл
    with open('workout_log.txt', 'a', encoding='utf-8') as f:
        f.write(workout_info)

    return "Данные успешно сохранены!"

if __name__ == '__main__':
    app.run(debug=True)
