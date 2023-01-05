from os import environ as env

from MeowerBot import Bot, __version__

bot = Bot(debug=True)


def login(*_, **__):
    print("login CB")
    bot.send_msg("TESTING!!!!!!!! O_O", to="home")
    bot.send_msg("MeowerBot.py " + __version__, to="home")


def msg(msg, *args, **_):
    print("msg CB")
    if msg.user.username == "Discord":
        bot.send_msg("TEEEEEST", to="livechat")


bot.callback(login, cbid="login")
bot.callback(msg, cbid="message")

bot.run(env["username"], env["password"])
