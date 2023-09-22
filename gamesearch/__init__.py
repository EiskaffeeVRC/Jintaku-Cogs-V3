from .gamesearch import Gamesearch


async def setup(bot):
    await bot.add_cog(Gamesearch())
