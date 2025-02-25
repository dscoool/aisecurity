# webhook: 
# https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV

import requests
headers = {
	"Content-Type": "application/json"
}

json_data = {
	"embeds": [{
		"title": f"제목",
		"description": f"글 내용",
		"url": f"메세지 글을 누르면 이동할 URL",
		"thumbnail": {
			"url": f"이미지 URL"
		}
	}]
}

requests.post("https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV", headers=headers, data=json.dumps(json_data))
