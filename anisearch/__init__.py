from .anisearch import AniSearch


async def setup(bot):
    cog = AniSearch(bot)
    await bot.add_cog(cog)
