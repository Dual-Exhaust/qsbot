# qsbot

An extension of the discord.py library that makes the initial creation of a bot's code much easier.

## Features

* Built in functions for easy 'react for role' setup
* Set welcome message and discord presence
* Set single or multiple prefixes for commands
* Built in command error catch (Probably will end up phasing this out or replacing it with something more practical)
* Generate starting code from the command line

## Roadmap

- [x] Basic examples
- [x] Command to install examples
- [x] Command to get basic starting code for bot creation
- [ ] Server statistics
- [ ] Cog support
- [ ] Easy load token

## Install

Not yet on PyPI, I am waiting until this has more features before I add it there, but if this gets some stars then I may consider adding it early. You can still clone this repo and install from there though.

```
git clone https://github.com/Dual-Exhaust/qsbot

cd qsbot

pip install .
``` 

### qs_install_examples

A command line function that creates a sub-directory containing the qsbot examples in the current working directory.

> Usage: qs_install_examples

### makebot

A command line function that generates code for you to start with.

> Usage: makebot

*Optional arguments*

* -F  | --filename : The name of the file generated. If not specified, it will be 'basic_bot.py' by default.
* -W  | --welcome  : The welcome message that your bot should send to new members. 
* -P  | --prefix   : The prefix that your bot should use, if not set it is '$' by default.
* -Pr | --presence : The discord presence of your bot.
* -R  | --react    : How many 'react for role' calls to generate.

## qsbot.client

The commands.Bot class from discord.ext.commands is the super class to this one, so initializing is virtually the same.
Note that the default command prefix is set to '$' so you do not have to set one on initialization.

> client = qsbot.client(command_prefix='$', \*args, \*\*kwargs)

### Reaction for Roles

The logic behind adding and removing a reaction to add and remove a role is provided by default. You just have to pass what channel you want to listen to and specify what reactions give which roles.

#### set_reaction_for_role_channel

Used to set which channel that the bot will listen to for when users add reactions to gain roles in the server. This must be set before you can use add_reaction_for_role. The channel can be passed as a channel id or as a channel name.

> Usage: client.set_reaction_for_role_channel( \<channel> )
  
#### add_reaction_for_role

Used to link what reactions give which roles. The first parameter is the reaction name and the second is the role name. These are case sensative and as far as I know only work with custom emojis at the moment.

> Usage: client.add_reaction_for_role( \<reaction name>, \<role name> )

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

> Usage: client.set_presence( \<presence> )

### Welcome Message

#### set_welcome_message

Sets the welcome message that is sent to the user when they join the server. If this is not set then the default behavior is to send no welcome message. The command can be passed a discord.Embed object or a regular string.

> Usage: client.set_welcome_message( \<welcome message> )

#### get_welcome_message

Simply returns the set welcome message. Returns None if it has not been set.

> Usage: client.get_welcome_message()

### On Ready

#### set_on_ready_message

Sets the message that gets printed to console when on_ready gets called.

> Usage: client.set_on_ready_message( \<message> )
  
#### get_on_ready_message

Returns the message that gets printed when on_ready triggers. Returns None if not set.

> Usage: client.get_on_ready_message()

#### on_ready

When this triggers, the on_ready_message is printed to console and if a presence has already been specified, then it gets set. It does trigger at some odd times though, read the [docs](https://discordpy.readthedocs.io/en/latest/api.html#discord.on_ready) for more info about it. 

### Command Error Behavior

#### on_command_error

A default command error is included; however, I may be leaning towards disabling it by default and making it have to be enabled. Sends the discord user the error that occured during calling a command. The default behavior is bound to change as this is impractical. 
