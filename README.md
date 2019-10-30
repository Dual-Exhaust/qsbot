# qsbot

An extension of the discord.py library that makes the initial creation of a bot's code much easier.

## Features

* Built in functions for easy 'react for role' setup.
* Set welcome message and discord presence.
* Set single or multiple prefixes for commands.
* Built in command error catch. (Probably will end up phasing this out or replacing it with something more practical)

## Install

Not yet on PyPI, I am waiting until this has more features before I add it there. You can still clone this repo and install from there though.

```
git clone https://github.com/Dual-Exhaust/qsbot

cd qsbot

pip install .
``` 

## qsbot.client

The commands.Bot class from discord.ext.commands is the super class to this one, so initializing is virtually the same.
Note that the default command prefix is set to '$' so you do not have to set one on initialization.

> client = qsbot.client(command_prefix='$', \*args, \*\*kwargs)

### Reaction for Roles

The logic behind adding and removing a reaction to add and remove a role is provided by default. You just have to pass what channel you want to listen to and specify what reactions give which roles.

#### set_reaction_for_role_channel

Used to set which channel that the bot will listen to for when users add reactions to gain roles in the server. This must be set before you can use add_reaction_for_role. The channel can be passed as a channel id or as a channel name.

> Usage: client.set_reaction_for_role_channel( <channel> )
  
#### add_reaction_for_role

Used to link what reactions give which roles. The first parameter is the reaction name and the second is the role name. These are case sensative and as far as I know only work with custom emojis at the moment.

> Usage: client.add_reaction_for_role( <reaction name>, <role name> )

### Prefixes

#### set_prefixes

Used to overwrite the default command prefix. This can be passed a single string or a list of strings to set a single or multiple prefixes respectively.

> Usage: client.set_prefixes( <prefixe(s)> )

#### get_prefixes

Used to return what the current prefixes are. Currently broken, and may also be a duplicate method of commands.Bot.get_prefix.

> Usage: client.get_prefixes()

### Presence

#### set_presence

Used to set the bots presence in discord. The parameter is a string. Custom statuses have not yet been looked at.

> Usage: client.set_presence( <presence> )

### Welcome Message

#### set_welcome_message

Sets the welcome message that is sent to the user when they join the server. If this is not set then the default behavior is to send no welcome message. The command can be passed a discord.Embed object or a regular string.

> Usage: client.set_welcome_message( <welcome message> )

#### get_welcome_message

Simply returns the set welcome message. Returns None if it has not been set.

> Usage: client.get_welcome_message()

### Command Error Behavior

#### on_command_error

A default command error is included; however, I may be leaning towards disabling it by default and making it have to be enabled. Sends the discord user the error that occured during calling a command. The default behavior is bound to change as this is impractical. 
