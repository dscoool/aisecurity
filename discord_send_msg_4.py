# webhook: 
# https://discordapp.com/api/webhooks/1344086029489143910/RBic3z8_q7itigPhxaYrJQQlOBjy04d7dciJMUug3kUCt8LIHBftfQ-_FeBvpOwLYVWV
import requests 

headers = {
    "Content-Type": "application/json"
}
json_data = {
	"embeds": [{
		"title": f"[⭐️]이스트소프트_디스코드봇",
		"description": f"디스코드봇에 메시지 보내기",
		"url": f"https://github.com/dscoool/aisecurity/blob/main/discord_send_msg.py",
		"thumbnail": {
			"url": f"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx1kkiO_HhVWIXL-RBDOLDzNVjHvcDNxl11swe-mvGzbpHQdYYDzye3_Y&usqp=CAE&s"
		}
	}]
}

requests.post("https://discordapp.com/api/webhooks/1354231049768402955/LVFBX8RltSgawfA9_n8quVqHfDZyGt-OhuvTt_5n-KT8WSc0OXqPncHfpJf7E7RQ-s2I", 
              headers=headers, json=json_data)
