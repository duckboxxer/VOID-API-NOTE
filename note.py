import requests

response = requests.post("https://api.voids.top/quote", json={
  "username": "abcdef...",
  "display_name": "Nickname",
  "text": "Example message",
  "avatar": "https://cdn.discordapp.com/avatars/1338293216826622005/5a5df301f628b135b305ca31457d3a97.png?size=1024",
  "color": True
})
print(response.status_code)
print(response.json())
