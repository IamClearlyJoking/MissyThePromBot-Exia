import discord
from discord.ext import commands

class Normies:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        await self.bot.say('Pong!')


def setup(bot):
    bot.add_cog(Normies(bot))