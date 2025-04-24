# webhook: 
import requests

headers = {
    "Content-Type": "application/json"
}
json_data = {
    "content": "디스코드 봇으로 보내는 메시지입니다: 안녕하세요?"
}
requests.post("https://discordapp.com/api/webhooks/**", headers=headers, json=json_data)
