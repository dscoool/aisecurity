# webhook: 
# https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV
import requests

def send_discord_msg(webhook, msg):
    headers = {
    "Content-Type": "application/json"
    }
    json_data = {
        "content": msg
    }
    requests.post(wwebhook, headers=headers, json=json_data)

webhook = "https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV"
message = "디스코드 봇으로 보내는 메시지입니다: 안녕하세요?"
send_discord_msg(webhook, message)