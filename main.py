import fastapi

app = fastapi.FastAPI()

whatever = 'Random Value'

@app.get('/')
def home():
    return {'message': whatever}
