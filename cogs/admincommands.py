import discord, json
from discord.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open('db/emojis.json', 'r') as f:
            self.emojis = json.load(f)

    async def cog_check(self, ctx):
        if not await self.bot.is_owner(ctx.author):
            await ctx.reply('You need to be the owner of this bot to run this command.')
            return False
        else:
            return True

    @commands.command(name='load', brief='Loads a cog')
    async def load(self, ctx, extension):
        await ctx.message.add_reaction(self.emojis['loading'])
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'\'cogs.{extension}\' loaded successfully!')
        await ctx.message.remove_reaction(self.emojis['loading'], self.bot.user)

    @commands.command(name='unload', brief='Unloads a cog')
    async def unload(self, ctx, extension):
        await ctx.message.add_reaction(self.emojis['loading'])
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'\'cogs.{extension}\' unloaded successfully!')
        await ctx.message.remove_reaction(self.emojis['loading'], self.bot.user)

    @commands.command(name='reload', brief='Reloads a cog')
    async def reload(self, ctx, extension):
        await ctx.message.add_reaction(self.emojis['loading'])
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'\'cogs.{extension}\' reloaded successfully!')
        await ctx.message.remove_reaction(self.emojis['loading'], self.bot.user)

    @commands.command(name='restart', brief='Restarts the bot')
    async def restart(self, ctx):
        await ctx.message.delete()
        await self.bot.close()

def setup(bot):
    bot.add_cog(AdminCommands(bot))
