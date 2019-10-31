import qsbot
import discord

# Creates a small bot that welcomes users with an embedded message

# Initialize the client
client = qsbot.client()

# Create an embed object and add a field to it.
embed = discord.Embed()
embed.add_field(name='Welcome!', value='Welcome to the server! Feel free to look around and make yourself at home.')
embed.add_field(name='Feedback', value='If you have any questions, comments or concerns be sure to let us know!')

# Set the welcome message to be the embed object
client.set_welcome_message(embed)

# Runs the bot
client.run('DISCORD TOKEN')
