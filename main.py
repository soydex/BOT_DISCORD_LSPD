import discord, random, time,os
from dotenv import load_dotenv
import secu, outils
from discord.ext import commands
from discord.commands import Option
import asyncio




while True :
    load_dotenv()
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())
    token = os.getenv("DISCORD_TOKEN")

    @bot.event
    async def on_ready():
        print(f"{str(bot.user.name)}")
        print(f"{int(bot.latency*100)} ping")
        await bot.change_presence(activity=discord.Streaming(name="Version 2.2.5", url="https://www.twitch.tv/soydex_"))
                
    @bot.command()
    async def send_message(ctx, *, message):
        await ctx.send(message)            
                
    @bot.event
    async def on_member_join(member):
        if member.guild_permissions.administrator:
            await member.ban(reason="Antiraid: utilisateur avec permissions administrateur")

    @bot.slash_command(guild_ids=[1053908434262704148], description="Voir les agents qui n'ont pas cochés la présence")
    @commands.has_role(1053908434476617867)
    async def react(
            ctx: discord.ApplicationContext,
            message_id: Option(str, "Choisissez un message :"),
        
        ):
            try:
                message = await ctx.fetch_message(message_id)
            except discord.NotFound:
                await ctx.respond("Message introuvable.")
                return
            reacted_users = set()
            for reaction in message.reactions:
                async for user in reaction.users():
                    reacted_users.add(user)
            role = discord.utils.get(ctx.guild.roles, name="Los Santos Police Department")
            role_name = "Los Santos Police Department"

            if not role:
                await ctx.respond(f"Le rôle {role_name} n'a pas été trouvé sur ce serveur.")
                return
            role_members = set([member for member in role.members])
            users_without_reaction = role_members - reacted_users
            sorted_users_without_reaction = sorted(users_without_reaction, key=lambda user: user.display_name)
            user_list = '\n'.join([user.mention for user in sorted_users_without_reaction])
            await ctx.respond(f"Utilisateurs sans réaction dans le rôle {role_name} :\n{user_list}")

    @bot.slash_command(guild_ids=[1053908434262704148], description="Changer le nom d'un salon intervention")
    async def intervention(
        ctx: discord.ApplicationContext,
        type: Option(str, "Choisissez le type d'intervention :")
        ):
        await ctx.defer()
        channel = ctx.channel
        if channel.category and channel.category.id == 1053908435806212110:
            await channel.edit(name=type)
            await ctx.respond(f"Nom du salon changé en {type}.")
        else:
            await ctx.respond(f"Vous ne pouvez pas changer le nom de ce channel.")

    @bot.slash_command(guild_ids=[1053908434262704148],description = "Voir les agents qui ont cochés la présence")
    @commands.has_role('Los Santos Police Department')
    async def presence(
        ctx: discord.ApplicationContext,
        message_id: Option(str, "Choisissez un message :"),

    ):
        message = await ctx.fetch_message(message_id)
        reactions = message.reactions
        result_message = ''
        for reaction in reactions:
            user_mentions = ''
            async for user in reaction.users():
                member = message.guild.get_member(user.id)
                if member is not None:
                    user_mentions += f'@{member.display_name} '
            result_message += f'{reaction.emoji}: {user_mentions}\n'
        await ctx.respond(result_message)

    @bot.slash_command(guild_ids=[950740696208392202], description="Sélectionner un autre recruteur LSPD")
    @commands.has_permissions(manage_messages=True)
    async def reroll(ctx: discord.ApplicationContext):
        role = ctx.guild.get_role(950752511856377927)

        if role is not None:
            members_with_role = [member for member in ctx.guild.members if role in member.roles]

            if members_with_role:
                random_member = random.choice(members_with_role)
                mention = random_member.mention
                d = random_member.display_name
                message = "Votre candidature va être traitée par" f" {mention}."
        await ctx.respond(message)
        channel = ctx.channel
        await channel.edit(name=f"rc {d[0:2]}")   

    @bot.slash_command(guild_ids=[1053908434262704148], description="Nouveau Rookie")
    @commands.has_permissions(manage_roles=True)
    async def rookie(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un agent :")
        ):
        await ctx.defer()
        role_ids=outils.role_ids

        roles = {key: ctx.guild.get_role(role_id) for key, role_id in role_ids.items()}

        if any(role in member.roles for role in roles.values()):
            await member.remove_roles(*roles.values())
            await ctx.respond(f"Rôles retirés à {member.mention}.", ephemeral=True)
        else:
            await member.add_roles(*roles.values())   
            await ctx.respond(f"Rôles ajoutés à {member.mention}.", ephemeral=True)

    @bot.user_command(name="hi")
    async def hi(ctx, user: discord.Member):
        await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        channel_mapping = {
            1102389154731536454: outils.tig,
            1102388422519300166: outils.cellules,
            1053908436418568313: outils.absent,
            1102388506371838093: outils.verif,
            1102389670396051486: outils.avocat,
            1053908436145946643: outils.altf4,
            1102388928033595454: outils.bracelet,
            1102388007862030356: outils.autorisation,
            1053908435109957691: outils.mdt,
            1152937736588775494: outils.trello,
            1053908436607324213: outils.justice
        }

        channel_id = message.channel.id
        if channel_id in channel_mapping:
            channel = bot.get_channel(channel_id)
            async for msg in channel.history(limit=200):
                if msg.author == bot.user:
                    await msg.delete()
            await channel.send(channel_mapping[channel_id])

        await bot.process_commands(message)

        if message.channel.id != 1102390705902596246:
            return
        if message.author.id == 527482340847386625:  # soydex
            return
        if message.author.id == 787640172698533918:  # bryan
            return
        has_media = message.attachments or any(embed.type == "video" or embed.type == "image" for embed in message.embeds)
        has_link = any(url in message.content for url in message.content.split() if url.startswith("http"))

        if has_media or has_link:
            await bot.process_commands(message)
        else:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, seuls les messages avec des vidéos, des images ou des liens sont autorisés.", delete_after=5)


    @bot.slash_command(guild_ids=[1053908434262704148], description="Licenciement d'un agent LSPD")
    @commands.has_permissions(manage_roles=True)
    async def licenciement(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Agent à qui vous retirez les rôles ?"),
    ):
        await ctx.defer()
        channel_ids = [1152937736588775494, 1053908435109957691]
        value = None
        value2 = None
        for channel_id in channel_ids:
            channel = bot.get_channel(channel_id)
            async for message in channel.history(limit=None):
                if message.author == member and "@" in message.content and "<" not in message.content:
                    if channel_id == 1152937736588775494:
                        value = message.content
                    elif channel_id == 1053908435109957691:
                        value2 = message.content

        for role in member.roles:
            if role.name != '@everyone':
                await member.remove_roles(role)
        if value is None:
            value = "Aucun Compte Trello trouvé."
        if value2 is None:
            value2 = "Aucun Compte MDT trouvé."
        channel = bot.get_channel(1070395118420496466)
        await channel.send(f"**Agent {member.mention} n'a plus ses rôles.**\n\n**Adresse Trello :** {value}\n\n**Adresse MDT :** {value2}\n\n*Merci de réagir sous ce message une fois que les comptes ont été retirés ☑️.*")
        await member.edit(nick=None)
        await ctx.respond(f"https://discord.com/channels/1053908434262704148/1070395118420496466")

    @bot.slash_command(guild_ids=[1053908434262704148], description="Voir le compte Trello d'un agent")
    @commands.has_role('Los Santos Police Department')
    async def trello(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un agent :")
    ):
        await ctx.defer()
        channel_id1 = [1102389260146983033]
        found_messages = False        

        for channel_id in channel_id1:
            channel = bot.get_channel(channel_id)
            async for message in channel.history(limit=None):
                if message.author == member and "@" in message.content and "<" not in message.content:
                    found_messages = True
                    await ctx.respond(f"Adresse Mail Trello : {message.content}")
                    return
        
        if not found_messages:
            await ctx.respond(f"Aucun compte trouvé pour l'utilisateur {member.mention}.")
    
    @bot.slash_command(guild_ids=[950740696208392202], description="Blacklist un candidat")
    @commands.has_role(950740696229355565)
    async def blacklist(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un candidat ?"),
        motif: Option(str, "Motif du refus ?"),
        ):

        channel = bot.get_channel(961733191952130128)
        await channel.send(f"- Agent en charge : {ctx.author.mention}\n"
                            f"\n"
                            f"- Motif : {motif}\n"
                            f"\n"
                            f"- ID : {member.id} \n"
                            f"\n"
                            f"- Discord : {member.mention}\n")
        await ctx.respond(f"Enregistrement fait ✅",ephemeral = True)



    @bot.slash_command(guild_ids=[950740696208392202], description="Refuser un candidat")
    @commands.has_role(950740696229355565)
    async def refuser(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un candidat ?"),
        temps: Option(int, "Temps du refus ?(en jours)"),
        motif: Option(str, "Motif du refus ?"),
        ):
        role_id = 950811799228391474

        role = ctx.guild.get_role(role_id)  
        channel = bot.get_channel(954362421500334100)
        await channel.send(f"- Agent en charge : {ctx.author.mention}\n"
                            f"\n"
                            f"- Refus temporaire : {temps}\n"
                            f"\n"
                            f"- Motif : {motif}\n"
                            f"\n"
                            f"- ID : {member.id} \n"
                            f"\n"
                            f"- Discord : {member.mention}\n")
        await member.add_roles(role)
        await ctx.respond(f"Le rôle {role.name} a été ajouté à {member.mention} pendant {temps} jours.")
        calc = temps * 604800
        await asyncio.sleep(calc)
        await member.remove_roles(role)

    @bot.slash_command(guild_ids=[950740696208392202], description="Accepter un candidat")
    @commands.has_role(950740696229355565)
    async def accepter(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un candidat ?"),
        temps: Option(int, "Temps du refus ?(en jours)"),
        ):
        role_id = 950811441814970408

        role = ctx.guild.get_role(role_id)  
        await member.add_roles(role)
        await ctx.respond(f"Le rôle {role.name} a été ajouté à {member.mention} pendant {temps} jours.")
        calc = temps * 604800
        await asyncio.sleep(calc)
        await member.remove_roles(role)

    @bot.slash_command(guild_ids=[1053908434262704148], description="Voir le compte MDT d'un agent")
    @commands.has_role('Los Santos Police Department')
    async def mdt(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un agent :")
    ):
        await ctx.defer()
        channel_id2 = [1053908435109957691]
        found_messages = False        

        for channel_id in channel_id2:
            channel = bot.get_channel(channel_id)
            async for message in channel.history(limit=None):
                if message.author == member and "@" in message.content and "<" not in message.content:
                    found_messages = True
                    msg = message.content
                    await ctx.respond(f"Adresse Mail MDT : {msg}")
                    return
        if not found_messages:
            await ctx.respond(f"Aucun compte trouvé pour l'utilisateur {member.mention}.")

    @bot.slash_command(guild_ids=[1145793700459466963], description="Créer une catégorie pour un groupe")
    @commands.has_permissions(manage_roles=True)
    async def groupe(
        ctx: discord.ApplicationContext,
        name: Option(str, "Nom du groupe ?")
    ):
        await ctx.defer()
        category = await ctx.guild.create_category(name)

        if category.name == name:
            channel_names = ["📌╏localisation", "🧍╏membres", "🚗╏véhicules", "📁╏dossiers", "📋╏informations", "📷╏photos-preuves"]
            for channel_name in channel_names:
                channel = await ctx.guild.create_text_channel(channel_name, category=category)
                role = ctx.guild.get_role(1145793700497207298)
                if role:
                    await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
                    await channel.set_permissions(role, read_messages=True, send_messages=True)
                else:
                    await ctx.send("Le rôle spécifié n'a pas été trouvé.")
                    await ctx.respond(f"Le rôle spécifié n'a pas été trouvé.", ephemeral=True)

            await ctx.respond(f"Catégorie {name} créée.")
        else:
            await ctx.respond(f"Erreur.", ephemeral=True)

    @bot.slash_command(guild_ids=[988485924063162378], description="Créer une catégorie pour un groupe")
    @commands.has_permissions(manage_roles=True)
    async def groupe(
        ctx: discord.ApplicationContext,
        name: Option(str, "Nom du groupe ?")
    ):
        await ctx.defer()
        category = await ctx.guild.create_category(name)

        if category.name == name:
            channel_names = ["📌╏localisation", "🧍╏membres", "🚗╏véhicules", "📁╏dossiers", "📋╏informations", "📷╏photos-preuves"]
            for channel_name in channel_names:
                channel = await ctx.guild.create_text_channel(channel_name, category=category)
                role = ctx.guild.get_role(988486798319714355)
                if role:
                    await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
                    await channel.set_permissions(role, read_messages=True, send_messages=True)
                else:
                    await ctx.send("Le rôle spécifié n'a pas été trouvé.")
                    await ctx.respond(f"Le rôle spécifié n'a pas été trouvé.", ephemeral=True)

            await ctx.respond(f"Catégorie {name} créée.")
        else:
            await ctx.respond(f"Erreur.", ephemeral=True)

    @bot.slash_command(guild_ids=[1053908434262704148], description="Ajouter ou retirer le rôle absent")
    @commands.has_permissions(manage_roles=True)
    async def absent(
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Choisissez un agent :")
        ):
        await ctx.defer()
        role = ctx.guild.get_role(1053908434497585161)  
        if member == ctx.author:
            await ctx.respond(f"Vous ne pouvez pas vous ajouter le rôle vous même")
        else: 
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.respond(f"Rôle retiré à {member.mention}.")
            else:
                await member.add_roles(role)
                await ctx.respond(f"Rôle ajouté à {member.mention}.")

                              
    @bot.event
    async def on_application_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("Vous n'avez pas les permissions nécessaires pour exécuter cette commande.", ephemeral=True)
        elif isinstance(error, commands.MissingRole):
            await ctx.respond("Vous n'avez pas les rôles requis pour exécuter cette commande.", ephemeral=True)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.respond("Commande introuvable.", ephemeral=True)
        elif isinstance(error, commands.DisabledCommand):
            await ctx.respond("Cette commande est désactivée.", ephemeral=True)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.respond("Cette commande est en cours de refroidissement. Veuillez réessayer ultérieurement.", ephemeral=True)
        else:
            await ctx.respond("Une erreur s'est produite lors de l'exécution de la commande.", ephemeral=True)

    @bot.event
    async def on_guild_channel_create(channel):
        if channel.category and channel.category.id == 950740697684799514:
            role_id_to_mention = 950752511856377927
            message = "Votre candidature va être traitée par"
            
            role = channel.guild.get_role(role_id_to_mention)

            if role is not None:
                members_with_role = [member for member in channel.guild.members if role in member.roles]

                if members_with_role:
                    random_member = random.choice(members_with_role)

                    mention = random_member.mention
                    d = random_member.display_name
                    message += f" {mention}."
            time.sleep(2)
            await channel.send(message)
            await channel.send(outils.rc)
            await channel.edit(name=f"rc {d[0:2]}")   
        if channel.category and channel.category.id == 1053908435806212110:
            time.sleep(2)
            await channel.send(outils.leadterrain)

    @bot.event
    async def on_member_update(before, after):
        if before.id == 527482340847386625 and before.roles != after.roles:
            user = await bot.fetch_user(527482340847386625)
            if user:
                await user.send(f"Une mise à jour a été effectuée sur {user.mention}.")

                
        allowed_role_ids = [1053908434287861828, 1053908434287861827, 1095806160906494043, 1053908434287861826, 1053908434287861824]
        async for entry in after.guild.audit_logs(limit=1):
            log_channel = await bot.fetch_user(527482340847386625)
            if before.roles != after.roles:
                role_removed = None

                for role in before.roles:
                    if role not in after.roles:
                        role_removed = role
                        break
                        
                if role_removed:
                    if role.id in allowed_role_ids:
                        log_channel = await bot.fetch_user(527482340847386625)

                        if log_channel:
                            message = f"L'agent {before.mention} n'a plus le rôle {role_removed}. Le rôle a été retiré par {entry.user.mention}."
                            await log_channel.send(message)


    bot.run(token)