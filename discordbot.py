from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('【/team チーム数】

例：/team 3
→ 3チーム作成

・指定した数のチームを作成

・メンバー数が同じになるように作成

・チーム数を指定しなくても実行可。デフォルトで"2"を指定



【/group メンバー数】

例：/group 3
→ 1チーム3人になるようにチーム作成

・指定したメンバー数でチームを作成

・メンバー数を指定しない場合、デフォルトとして"1"を指定')


bot.run(token)
