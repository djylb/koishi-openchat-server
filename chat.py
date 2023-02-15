from revChatGPT.V1 import Chatbot
from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()

HOST = "0.0.0.0"
PORT = 8006

chatbot = Chatbot(config={
    "email": "<your email>",
    "password": "your password"
})


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.post("/chat")
async def chatGPT(body: dict = Body(...)):
    prompt = body["prompt"]
    print("User: " + prompt)
    print("Chatbot: ", end="")
    try:
        if prompt == "!reset":
            chatbot.reset_chat()
            print("OK")
            return {"message": "OK"}
        answer = ""
        for data in chatbot.ask(
            prompt,
            conversation_id=chatbot.config.get("conversation"),
            parent_id=chatbot.config.get("parent_id"),
        ):
            message = data["message"][len(answer):]
            print(message, end="", flush=True)
            answer = data["message"]
        print()
    except:
        answer = "ERROR"
        pass
    return {"message": answer}

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
