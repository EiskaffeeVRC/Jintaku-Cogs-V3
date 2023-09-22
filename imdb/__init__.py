from .imdb import Imdb


async def setup(bot):
    await bot.add_cog(Imdb())
