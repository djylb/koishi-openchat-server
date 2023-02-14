from revChatGPT.V1 import Chatbot
import sys
import os
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import asyncio

#### 手动配置时删除以下代码
from dotenv import load_dotenv, find_dotenv

load_dotenv(verbose=True)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
####

app = FastAPI()

# 手动配置时删除下行代码，并取消下面的注释并修改配置文件
#chatbot = Chatbot(email=EMAIL, password=PASSWORD) # v2版本api
chatbot = Chatbot(config={
  "email": EMAIL,
  "password": PASSWORD
})

# 手动配置时取消注释,并按需求配置参数
''' 
HOST = "0.0.0.0"
PORT = 8006

chatbot = Chatbot(
    email="",
    password="",
    # paid=True,
    # proxy="http://127.0.0.1:7890",
)
'''

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
      print(data["message"], end="", flush = True)
      answer = answer + data["message"]
    print()
  except:
    answer = "ERROR"
    pass

  return {"message": answer}

if __name__ == "__main__":
  uvicorn.run(app, host=HOST, port=PORT)

