
from MeowerBot import Bot, __version__
from MeowerBot.commands import command
from os import environ as env


bot = Bot(debug=True, prefix="/")

@command()
def test(ctx, *args):
	ctx.send_msg(" ".join(args) + "\n mb.py " + __version__)

bot.run(env['username'], env['password'])

