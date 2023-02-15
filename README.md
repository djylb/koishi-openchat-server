# koishi-openchat-server

2023.2.14 更新 修复返回未知错误。
2023.2.16 更新 优化输出，优化体积，修复损坏的重置功能。

一个适用于 https://forum.koishi.xyz/t/topic/59 的后端API接口。

## 前提准备

- 搭建一个可以运行的koshi服务器
- 拥有一个openai的账号 https://platform.openai.com/account/api-keys
- 拥有一台服务器并拥有python环境（如果不需要在服务器在搭建可以不需要）

# **docker 搭建 server （推荐）By D-Jy**

```shell
# 下载项目源码
git clone https://github.com/D-Jy-lab/koishi-openchat-server.git

# 进入项目
cd koishi-openchat-server

# 修改chat.py文件，填入OpenAI账号
nano chat.py

# 编译容器
docker build -t duan2001/openchat .

# 运行容器
docker run -d --name=openchat --restart=always -p 8006:8006 duan2001/openchat

```

# 手动搭建

## 一、本地自建server

- 本地需要一个koishi的服务器

官方插件的地址 @42 [https://github.com/MirrorCY/openchat](https://github.com/MirrorCY/openchat)

只需下载chat.py 文件放入工作文件夹中
打开chat.py文件填入账号密码。

新建一个Python运行环境 venv

```python
virutalenv venv
souce venv/bin/activate
pip install --upgrade revChatGPT fastapi uvicorn
python chat.py
```


## 二、服务器自建server


```python
# 安装依赖
sudo apt update 
sudo apt ugrade 
sudo apt install git -y
pip3 install virtualenv

# 下载项目源码
git clone https://github.com/D-Jy-lab/koishi-openchat-server.git

# 进入项目
cd koishi-openchat-server

# 修改chat.py文件，填入OpenAI账号
nano chat.py

# 创建虚拟环境
virtualenv .venv

# 进入虚拟环境
source .venv/bin/activate

# 安装依赖
pip3 install -r requirments.txt

# 运行服务器
python3 chat.py

```
## Links

koishi-openchat-server
[https://github.com/houko/koishi-openchat-server](https://github.com/houko/koishi-openchat-server),

OpenChat
[https://github.com/MirrorCY/openchat](https://github.com/MirrorCY/openchat),

ChatGPT
[https://github.com/acheong08/ChatGPT](https://github.com/acheong08/ChatGPT),
