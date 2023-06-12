import discord
from discord.ext import commands

class TicketView(discord.ui.View):
    def __init__(self, bot, category_id):
        super().__init__()
        self.bot = bot
        self.category_id = category_id

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.primary)
    async def create_ticket(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        channel = await interaction.guild.create_text_channel(name=f"ticket-{interaction.user.display_name}", category=self.category_id)
        await channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
        await interaction.user.send(f"Your ticket channel has been created: {channel.mention}")
        self.stop()

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.secondary)
    async def cancel_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(content="Ticket creation cancelled.", ephemeral=True)
        self.stop()

@bot.command()
async def open_ticket(ctx):
    category_id = 1234567890  # Replace with the ID of the category where the ticket channels will be created

    modal = TicketView(bot, category_id)
    await ctx.send("Click the button below to create a ticket.", view=modal)

bot.run("your_bot_token")
