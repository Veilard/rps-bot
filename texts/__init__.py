import json

with open("texts/responses.json", "r", encoding='utf-8') as file:
    bot_replies = json.load(file)

win_replies = bot_replies["wins"]
lose_replies = bot_replies["loses"]
draw_replies = bot_replies["draws"]