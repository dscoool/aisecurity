# -*- coding: utf-8 -*-

import requests
import json
import time

# 디스코드 설정
DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/**"
DISCORD_BOT_NAME = "[⭐️]이스트소프트_고양이챗봇"
DISCORD_BOT_URL = "https://github.com/dscoool/aisecurity/blob/main/discord_send_msg.py"
DISCORD_BOT_THUMBNAIL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx1kkiO_HhVWIXL-RBDOLDzNVjHvcDNxl11swe-mvGzbpHQdYYDzye3_Y&usqp=CAE&s"

def send_discord_message(title, description, url=None, thumbnail_url=None):
    """디스코드 웹훅을 사용하여 메시지를 보냅니다."""
    headers = {
        "Content-Type": "application/json"
    }
    embed = {
        "title": title,
        "description": description
    }
    if url:
        embed["url"] = url
    if thumbnail_url:
        embed["thumbnail"] = {"url": thumbnail_url}
    json_data = {
        "embeds": [embed]
    }
    response = requests.post(DISCORD_WEBHOOK_URL, headers=headers, json=json_data)
    if response.status_code != 204:
        print(f"디스코드 메시지 전송 실패: {response.status_code} - {response.text}")

class CompletionExecutor:
    def __init__(self, host, api_key, request_id):
        self._host = host
        self._api_key = api_key
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'Authorization': self._api_key,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }

        full_response = ""
        try:
            with requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                                 headers=headers, json=completion_request, stream=True) as r:
                for line in r.iter_lines():
                    if line:
                        decoded_line = line.decode("utf-8")
                        if decoded_line.startswith("data:"):
                            json_str = decoded_line[len("data:"):].strip()
                            try:
                                data = json.loads(json_str)
                                if 'result' in data and 'message' in data['result'] and 'content' in data['result']['message']:
                                    content = data['result']['message']['content']
                                    print(content, end="", flush=True)
                                    full_response += content
                            except json.JSONDecodeError as e:
                                print(f"JSON 디코딩 오류: {e} - {json_str}")
                        elif decoded_line == "event: end":
                            break
                        else:
                            print(f"기타 이벤트: {decoded_line}")
        except requests.exceptions.RequestException as e:
            print(f"API 요청 오류: {e}")
            return None
        return full_response

if __name__ == '__main__':
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='Bearer nv-d856ce9247a44479a3bd85a28ca04a6aelI7',
        request_id='a9a19e27c12a44afa177d30ad347f6c7'
    )

    preset_text = [{"role":"system","content":"- 캐릭터의 특성을 반영한 고양이 챗봇을 생성합니다.\n- 이모티콘을 사용해서 생동감을 더합니다.\n- '했다냥' 냥말투를 사용합니다.\n- 가장 친한 친구는 노란 고양이 '치즈'입니다.\n- 좋아하는 음식은 고등어캔입니다.\n"},{"role":"user","content":"안녕하세요? 클로바 챗봇입니다.\n\n"}]

    request_data = {
        'messages': preset_text,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 256,
        'temperature': 0.7,
        'repeatPenalty': 1.2,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 0
    }

    print("--- 네이버 챗봇 응답 시작 ---")
    naver_response = completion_executor.execute(request_data)
    print("\n--- 네이버 챗봇 응답 종료 ---")

    if naver_response:
        discord_message = f"**질문:** 안녕하세요? 클로바 챗봇입니다.\n\n**고양이 챗봇 응답:**\n{naver_response}"
        send_discord_message(
            title=DISCORD_BOT_NAME,
            description=discord_message,
            url=DISCORD_BOT_URL,
            thumbnail_url=DISCORD_BOT_THUMBNAIL
        )
        print("디스코드 메시지 전송 완료!")
    else:
        send_discord_message(
            title=f"[⚠️] {DISCORD_BOT_NAME}",
            description="네이버 챗봇 응답에 실패했습니다.",
            url=DISCORD_BOT_URL
        )
        print("네이버 챗봇 응답 실패 알림을 디스코드로 전송했습니다.")
