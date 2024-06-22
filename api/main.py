from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def root():
    return {"messaginggg" : "Hello world"}
