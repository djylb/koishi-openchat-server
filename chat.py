from revChatGPT.V1 import Chatbot
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

HOST = "0.0.0.0"
PORT = 8006

chatbot = Chatbot(config={
  "email": "<your email>",
  "password": "your password"
})

class ChatRequest(BaseModel):
  prompt: str

@app.get("/ping")
def ping():
  return {"message": "pong"}

@app.post("/chat")
async def chatGPT(request: ChatRequest):
  prompt = request.prompt
  print(prompt)
  if prompt == "__clear__":
    chatbot.reset()
    return {"message": "OK"}
  answer = ""
  try:
    for data in chatbot.ask(
      prompt,
      conversation_id=chatbot.config.get("conversation"),
      parent_id=chatbot.config.get("parent_id"),
    ):
      #print(data["message"], end="", flush = True)
      answer = data["message"]
    print(data["message"])
    print()
  except:
    answer = "ERROR"
    pass
  return {"message": answer}

if __name__ == "__main__":
  uvicorn.run(app, host=HOST, port=PORT)

