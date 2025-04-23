import pytest
from trivia import Question, Quiz



def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert question.is_correct("4")

def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    assert not question.is_correct("2")


def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    quiz.add_question(question)
    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1

def run_quiz():
    print("¡Bienvenido al juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    
    quiz = Quiz()

    # Cargar 10 preguntas en español
    preguntas = [
        ("¿Cuánto es 2 + 2?", ["1", "2", "3", "4"], "4"),
        ("¿Cuál es la capital de Francia?", ["Londres", "Berlín", "París", "Madrid"], "París"),
        ("¿Qué planeta es conocido como el planeta rojo?", ["Tierra", "Marte", "Venus", "Júpiter"], "Marte"),
        ("¿Quién escribió 'Hamlet'?", ["Shakespeare", "Cervantes", "Tolstói", "Homero"], "Shakespeare"),
        ("¿Cuánto es 5 * 6?", ["30", "20", "25", "40"], "30"),
        ("¿Cuál es el punto de ebullición del agua (°C)?", ["50", "100", "80", "120"], "100"),
        ("¿Qué gas absorben las plantas?", ["Oxígeno", "Hidrógeno", "Dióxido de carbono", "Nitrógeno"], "Dióxido de carbono"),
        ("¿Cuál es el océano más grande?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "Pacífico"),
        ("¿Cuál es la raíz cuadrada de 81?", ["9", "8", "7", "6"], "9"),
        ("¿Quién pintó la Mona Lisa?", ["Picasso", "Van Gogh", "Da Vinci", "Rembrandt"], "Da Vinci"),
    ]

    for desc, opciones, correcta in preguntas:
        quiz.add_question(Question(desc, opciones, correcta))

    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        if question:
            print(f"\nPregunta {quiz.current_question_index}: {question.description}")
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer_input = input("Tu respuesta (número): ")

            try:
                answer_index = int(answer_input) - 1
                if 0 <= answer_index < len(question.options):
                    answer_text = question.options[answer_index]
                    if quiz.answer_question(question, answer_text):
                        print("¡Correcto!")
                    else:
                        print(f"Incorrecto. La respuesta correcta era: {question.correct_answer}")
                else:
                    print("Número fuera de rango. Pregunta omitida.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")
        else:
            break

    print("\nJuego terminado.")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")


run_quiz()