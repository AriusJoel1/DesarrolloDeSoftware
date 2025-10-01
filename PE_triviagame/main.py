# main.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from trivia import Question  # Importamos tu clase Question

app = FastAPI()

# Base de datos en memoria
questions_db = []

# Modelo Pydantic para validar datos que llegan por la API
class QuestionModel(BaseModel):
    description: str
    options: List[str]
    correct_answer: str

@app.post("/questions/", status_code=status.HTTP_201_CREATED)
def create_question(question: QuestionModel):
    # Verificamos que la respuesta correcta esté dentro de las opciones
    if question.correct_answer not in question.options:
        raise HTTPException(
            status_code=400,
            detail="La respuesta correcta debe estar entre las opciones"
        )

    q = Question(
        description=question.description,
        options=question.options,
        correct_answer=question.correct_answer
    )
    questions_db.append(q)
    return {"message": "Pregunta creada"}

@app.get("/questions/")
def get_all_questions():
    # Convertimos preguntas a un formato serializable
    return [
        {
            "description": q.description,
            "options": q.options,
            "correct_answer": q.correct_answer
        }
        for q in questions_db
    ]
