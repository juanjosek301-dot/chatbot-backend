from fastapi import FastAPI

app = FastAPI(title="Chatbot institucional")


@app.get("/")
def hello_world():
    return {"message": "Hola mundo desde el backend del chatbot institucional"}
