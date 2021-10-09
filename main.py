from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # if data["type"] in ["message_new", "message_event"]:
    return "ok"
