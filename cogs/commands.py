import nextcord
from nextcord.ext import commands


# commands_class
class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ping_command
    @nextcord.slash_command(description="Check ping.")
    async def ping(self, interction: nextcord.Interaction):
        await interction.response.send_message("Pong! {0}".format(round(self.bot.latency, 1)), ephemeral=True)

    # clear_command
    @nextcord.slash_command(description="Clear messages.")
    @commands.has_permissions(administrator=True)
    async def clear(self, interaction: nextcord.Interaction, amount: int):
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Deleted {len(deleted)} message(s)", ephemeral=True)

    # help_command
    @nextcord.slash_command(description="Help command.")
    async def help(self, interaction: nextcord.Interaction):
        emb = nextcord.Embed(title="Commands:", description="Use slash commands.", colour=nextcord.Colour.green())
        emb.add_field(name="ping", value="Check ping.")
        emb.add_field(name="youtube", value="Me and my friend")
        emb.add_field(name="hay", value="Call to server")
        emb.set_footer(text=interaction.user.name, icon_url=interaction.user.avatar)

        await interaction.response.send_message(embed=emb, ephemeral=True)

    # hay_command
    @nextcord.slash_command(description="Call to server.")
    async def hay(self, interaction: nextcord.Interaction, user: nextcord.Member):
        await user.send(f'Hay, {user.name}, go to the server, {interaction.user.name} is calling you.')
        await interaction.response.send_message("Message sent.", ephemeral=True)

    # yt_command
    @nextcord.slash_command(description="Me and my friend.")
    async def yt(self, interaction: nextcord.Interaction):
        emb = nextcord.Embed(title='Youtube:', colour=nextcord.Colour.dark_red())
        emb.fields(name='Kreanch', value='https://www.youtube.com/channel/UCl23wjjD8qtpKvgoeFW5Llw%27')
        emb.add_field(name='RedShadow', value='https://www.youtube.com/channel/UCveu0AvhcRdgMWkLzTJMgkQ%27')
        emb.set_footer(text=interaction.user.name, icon_url=interaction.user.avatar)

        await interaction.response.send_message(embed=emb, ephemeral=True)

    # avatar_command
    @nextcord.slash_command(description="Get avatar.")
    async def avatar(self, interaction: nextcord.Interaction, user: nextcord.User):
        await interaction.response.send_message(user.avatar, ephemeral=False)


def setup(bot):
    bot.add_cog(Commands(bot))
