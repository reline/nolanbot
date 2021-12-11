from discord.ext import commands

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == 'Donut':
            role = await self.create_role_ifne(payload.member.guild, 'testrole')
            if role not in payload.member.roles:
                await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.emoji.name == 'Donut':
            guild = self.bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            for role in member.roles:
                if role.name == 'testrole':
                    await member.remove_roles(role)

    async def create_role_ifne(self, guild, new_role):
        for role in guild.roles:
            if role.name == new_role:
                return role
        return await guild.create_role(name=new_role)

def setup(bot):
    bot.add_cog(ReactionRoles(bot))