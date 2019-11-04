import discord
from discord.ext import commands


class client(commands.Bot):

    def __init__(self, command_prefix='$', *args, **kwargs):
        super().__init__(command_prefix, *args, **kwargs)
        self.prefixes = command_prefix
        self.command_prefix = self.prefixes 
        self.case_insensitive = True
        self.welcome_message = None
        self.on_ready_message = None
        self.presence_message = None
        self.reactions = []
        self.roles_for_reactions = []
        self.reaction_for_role_channel = None

    # ===================================Build in react for roles=========================
    # Seems to only work when passed custom emoji names from the server, tried using the default :frowning: emoji and the name of it is not 'frowning' so it never registered to add a role
    # It did not pass 'if payload.emoji.name in self.reactions' because it looked for '? ??' (literal name of :frowning:) when it should've looked for 'frowning' (what got added to self.reactions)
    
    # Can be set as the channel's ID or the channel's name, it gets checked in on_raw_reaction_add
    def set_reaction_for_role_channel(self, channel):
        self.reaction_for_role_channel = channel
    
    def add_reaction_for_role(self, reaction_name, role_name):
        self.reactions.append(reaction_name)
        self.roles_for_reactions.append(role_name)

    async def on_raw_reaction_add(self, payload):
        # Only tries to add a role if self.reactions/self.roles_for_reactions is bigger than zero, meaning that add_reaction_for_role has been called once
        # self.reaction_for_role_channel must be set before this can work so we check if set_reaction_for_role_channel has been called
        if len(self.reactions) > 0 and not self.reaction_for_role_channel is None:
            guild = self.get_guild(payload.guild_id)
            # Checks if the channel that was reacted in is set as the channel we want to look for reactions
            if payload.channel_id == self.reaction_for_role_channel or self.get_channel(payload.channel_id).name == self.reaction_for_role_channel:
                member = discord.utils.get(guild.members, name=self.get_user(payload.user_id).name)
            else:
                return
            if payload.emoji.name in self.reactions:
                role = discord.utils.get(guild.roles, name=self.roles_for_reactions[self.reactions.index(payload.emoji.name)])
                await member.add_roles(role)
    async def on_raw_reaction_remove(self, payload):
        if len(self.reactions) > 0 and not self.reaction_for_role_channel is None:
            guild = self.get_guild(payload.guild_id)
            if payload.channel_id == self.reaction_for_role_channel or self.get_channel(payload.channel_id).name == self.reaction_for_role_channel:
                member = discord.utils.get(guild.members, name=self.get_user(payload.user_id).name)
            else:
                return
            if payload.emoji.name in self.reactions:
                role = discord.utils.get(guild.roles, name=self.roles_for_reactions[self.reactions.index(payload.emoji.name)])
                await member.remove_roles(role)

    # ==================================Using Prefixes=================================
    def get_prefixes(self):
        return self.prefixes

    # takes a list of strings or just a single string
    def set_prefixes(self, prefixes):
        self.command_prefix = prefixes
    
    # ======================================Change Presence==================================
    # Presence gets set in on_ready
    def set_presence(self, presence):
        self.presence_message = presence

    # =====================================Welcome Message====================================
    async def on_member_join(self, member):
        if not self.welcome_message is None:
            if isinstance(self.welcome_message, discord.Embed):
                await member.send(embed=self.welcome_message)
            else:
                await member.send(self.welcome_message)

    def get_welcome_message(self):
        return self.welcome_message

    # can be set as a discord.Embed object or just as a string, it gets handled in on_member_join
    def set_welcome_message(self, message):
        self.welcome_message = message

    # =========================Shows that the bot has connected=================================

    async def on_ready(self):
        print(self.on_ready_message)
        if not self.presence_message is None:
            await self.change_presence(activity=discord.Game(name=self.presence_message))
        
        # Seems to be that it will only return the user when inside an async function
        # print(self.user)

    def get_on_ready_message(self):
        return self.on_ready_message

    def set_on_ready_message(self, message):
        self.on_ready_message = message
    # ===========================================Statistics==============================================
    @staticmethod
    def get_role_counts(guild):
        role_dict = {}
        for role in guild.roles:
            for member in guild.members:
                if role in member.roles:
                    if role.name in role_dict:
                        role_dict[role.name] += 1
                    else:
                        role_dict[role.name] = 1
        return role_dict
    
    @staticmethod
    def get_player_join_dates(guild):
        dates_dict = {}
        for member in guild.members:
            dates_dict[member.name] = member.joined_at
        return dates_dict


    # ========================================Generic Command Error======================================
    @staticmethod
    async def on_command_error(ctx, error):
        await ctx.author.send('```Error: ' + str(error) + '```')
