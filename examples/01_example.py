import qsbot

# This would be the code for a basic bot that will welcome members to the server, display a presence,
# and give/remove a role from members when they react/remove reaction with a certain emoji in a specific channel

# Creates the client. Keep in mind this is a sub class of discord.ext.commands.Bot
client = qsbot.client()

# Sets the welcome message to a basic message. This will be sent to every new member when they join the server
client.set_welcome_message('Welcome!')

# This only gets printed to console, but it is a good indication if the bot has actually connected
client.set_on_ready_message('Connected to server.')

# Sets the bots presence to Bot stuff
client.set_presence('Bot stuff')

# Sets the channel that you can react for roles in, it is set by the channel name here
client.set_reaction_for_role_channel('rolereact')

# Links the reaction :HS: to the role Hearthstone
client.add_reaction_for_role('HS', 'Hearthstone')

# Runs the bot
client.run('DISCORD_TOKEN')

