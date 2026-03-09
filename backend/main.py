from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import sqlite3

from workout_agent import generate_workout
from nutrition_agent import generate_meal_plan
from aromi_agent import aromi_chat
from models import UserProfile

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():
    return {"message": "ArogyaMitra Backend Running"}


# Workout Plan API
@app.get("/generate-workout")
def workout(goal: str, minutes: int):

    plan = generate_workout(goal, minutes)

    return {
        "goal": goal,
        "minutes": minutes,
        "workout_plan": plan
    }


# Meal Plan API
@app.get("/generate-meal-plan")
def meal_plan(diet: str, calories: int):

    plan = generate_meal_plan(diet, calories)

    return {
        "diet": diet,
        "calories": calories,
        "meal_plan": plan
    }


# AROMI AI Coach Chat
@app.get("/aromi-chat")
def chat(message: str):

    reply = aromi_chat(message)

    return {
        "user_message": message,
        "aromi_response": reply
    }


# Create User Profile and Save to Database
@app.post("/create-profile")
def create_profile(user: UserProfile):

    conn = sqlite3.connect("arogyamitra.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        weight REAL,
        goal TEXT,
        workout_time INTEGER,
        diet TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO users (name, age, weight, goal, workout_time, diet) VALUES (?, ?, ?, ?, ?, ?)",
        (user.name, user.age, user.weight, user.goal, user.workout_time, user.diet)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Profile saved successfully",
        "user": user
    }