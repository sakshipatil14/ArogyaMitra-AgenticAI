from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    weight: float
    goal: str
    workout_time: int
    diet: str