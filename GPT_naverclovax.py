# -*- coding: utf-8 -*-

import requests


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

        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                           headers=headers, json=completion_request, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    print(line.decode("utf-8"))


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

    print(preset_text)
    completion_executor.execute(request_data)
