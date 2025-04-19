import discord, random, time
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True    

bot = commands.Bot(command_prefix='%', intents=intents)
token = "MTExNDUxMjg5MjAzNzk2Mzg0Ng.GP-Ht4.sFm52oTV4dT3xNdqf7At_6dglu2KkObcjdHw7c"

@bot.event
async def on_ready():
    print('Central Office is ready')
    print(f"{int(bot.latency*100)} ping")

@bot.event
async def on_member_join(member):
    # Vérifie si le membre a des permissions administratives
    if member.guild_permissions.administrator:
        # Bannit le membre
        await member.ban(reason='Possède des permissions administratives')
        print(f'Banned {member.name} ({member.id})')

    @bot.event
    async def on_message(message):
            if message.author == bot.user:  
                return  
            if message.channel.id == 1102389154731536454:
                channel = bot.get_channel(1102389154731536454)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter :**\n\n"
                                "* Prénom :\n"
                                "* Nom :\n"
                                "* Nombre :\n"
                                "* Motif(s) :\n"
                                "* Présence d'avocat : Oui/Non\n"
                                "* Agent(s) présent(s) :")
            await bot.process_commands(message)
            if message.channel.id == 1102388422519300166:
                channel = bot.get_channel(1102388422519300166)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter :**\n\n"
                                "* Prénom :\n"
                                "* Nom :\n"
                                "* Heure d'entrée :\n"
                                "* Heure de sortie :\n"
                                "* Motif(s) :\n"
                                "* Type d'amende/UP : MIN1/MIN2/MIN3 - Nominale - MAX1/MAX2\n"
                                "* Présence d'avocat : Oui/Non\n"
                                "* Agent(s) présent(s) :")
            await bot.process_commands(message)
            if message.channel.id == 1053908436418568313:
                channel = bot.get_channel(1053908436418568313)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter :**\n\n"
                                "* https://discord.com/channels/1053908434262704148/1053908436418568313/1065846155679903774")
            await bot.process_commands(message)
            if message.channel.id == 1102388506371838093:
                channel = bot.get_channel(1102388506371838093)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter pour les ⁠🔎┃vérification-procédures**\n\n"
                                "Erreur(s) constatée(s) :\n"
                                "Modification à effectuer :\n"
                                "Lien du message :\n"
                                "Agent(s) en charge :\n\n"
                                "⏲️ Vous avez un délais de 12h00 pour corriger votre erreur ! (Ouvrir un https://discord.com/channels/1053908434262704148/1102389738620588213/1102390175314747462⁠)\n\n"
                                "        ")
            await bot.process_commands(message)
            if message.channel.id == 1102389670396051486:
                channel = bot.get_channel(1102389670396051486)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ Template à respecter pour un appel Avocat**\n\n"
                                "* Prénom Nom de l'individu :\n"
                                "* Chef D'accusation \n"
                                "* Agent en charge :\n"
                                "* Calculateur de peine (en screen)\n"
                                "   \n"
                                "Dès lors que l'appel a été effectué, l'avocat a 15 minutes pour se manifester. Au delà de ce délais impartis l'agent en charge finalisera sa procédure normalement → Recensement → Rapport d'arrestation → Mise en garde à vue.\n"
                                "*Pensez à bien ping le rôle @| Avocat à chaque message !*")
            await bot.process_commands(message)
            if message.channel.id == 1053908436145946643:
                channel = bot.get_channel(1053908436145946643)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter :**\n\n"
                                "* Contexte RP :\n"
                                " \n"
                                "* ID Unique :\n"
                                " \n"
                                "* Screen de la déconnexion :")
            await bot.process_commands(message)
            if message.channel.id == 1102388928033595454:
                channel = bot.get_channel(1102388928033595454)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter :**\n\n"
                                "* Prénom :\n"
                                "* Nom :\n"
                                "* ID Unique :\n"
                                "* Motif(s) :\n"
                                "* Agent(s) présent(s) :")
            await bot.process_commands(message)
            if message.channel.id == 1102388007862030356:
                channel = bot.get_channel(1102388007862030356)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter :**\n\n"
                                "* Agent :\n"
                                "* Autorisation :\n"
                                "* Durée :\n"
                                "* Motif(s) :\n"
                                "* Agent(s) en charges(s) :")
            await bot.process_commands(message)
            if message.channel.id == 1053908435109957691:
                channel = bot.get_channel(1053908435109957691)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter pour la demande d'accès au MDT :**\n\n"
                                "* Matricule :\n"
                                "* Nom :\n"
                                "* Prénom :\n"
                                "* E-mail :")
            await bot.process_commands(message)
            if message.channel.id == 1102389260146983033:
                channel = bot.get_channel(1102389260146983033)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter pour la demande d'accès au Trello :**\n\n"
                                "* Matricule | Prénom Nom | Adresse Mail Trello | Nom d'utilisateur Trello")
            await bot.process_commands(message)
            if message.channel.id == 1121329550433996870:
                channel = bot.get_channel(1121329550433996870)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter pour les rapports rookies**\n\n"
                                    "Rapport Rookie de *Matricule | Agent*\n"

                                    "Relation civiles :  /10\n"
                                    "Contrôle routiers : /10\n"
                                    "Terrain : /10\n"
                                    "Procédures : /10\n"
                                    "Conduite : /10\n"
                                    "Déontologie : /10\n"
                                    "Respect de la hiérarchie : /10\n"
                                    "Calls radio : /10\n"
                                    "\n"
                                    "Notes : /80\n"
                                    "\n"
                                    "Commentaire :\n"
                                    "Début de service :\n"
                                    "Fin de service :\n"
                                    "\n"
                                    "Rapport rédigé par:")
            await bot.process_commands(message)        
            if message.channel.id == 1121329527688273960:
                channel = bot.get_channel(1121329527688273960)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter pour les rapports d'arrestation**\n\n"

                                    "Nom :  \n"
                                    "Prénom : \n"
                                    "Charges retenues : \n"
                                    "Type de l’up: MIN 1 - MIN 2 - MIN 3 - Nominale - MAX 1 - MAX 2 : \n"
                                    "Temps : \n"
                                    "Type de l’amende: MIN 1 - MIN 2 - MIN 3 - Nominale - MAX 1 - MAX 2 : \n"
                                    "Montant de l’amende :\n"
                                    "Matériel saisi : ")
            await bot.process_commands(message) 
            if message.channel.id == 1121344371665682485:
                channel = bot.get_channel(1121344371665682485)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ TEMPLATE à respecter pour les recensements**\n\n"
                                    "Nom :  \n"
                                    "Prénom : \n"
                                    "Date de naissance : \n"
                                    "Taille : \n"
                                    "Numéro de téléphone : \n"
                                    "Couleur de cheveux : \n"
                                    "Couleur des yeux : \n"
                                    "Sexe : \n"
                                    "Permis ( Valide / Non valide ) :\n"              
                                    "PPA ( Valide / Non valide ) :\n"
                                    "Photo : ")
            await bot.process_commands(message)
            if message.channel.id == 1130482092858409060:
                channel = bot.get_channel(1130482092858409060)
                async for msg in channel.history(limit=200):
                    if msg.author == bot.user:
                        await msg.delete()
                await channel.send("### **➟ Template à respecter et a compléter au pied de la lettre :**\n\n"
                                    "Identité : \n"
                                    "Heure passage à Los Santos : \n"
                                    "Métier reconnu : \n"
                                    "Visa de Cayo : Oui/Non \n"
                                    "Photo Carte d'identité : \n"
                                    "Agent en charge : ")
            await bot.process_commands(message)

            mediachannel_id = 1102390705902596246
            WLid= 527482340847386625

            if message.author.bot:
                return

            elif message.channel.id != mediachannel_id:
                return

            elif message.author.id == WLid:
                return

            has_media = message.attachments or any(embed.type == "video" or embed.type == "image" for embed in message.embeds)
            has_link = any(url in message.content for url in message.content.split() if url.startswith("http"))

            if has_media or has_link:
                await bot.process_commands(message)
            else:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, seuls les messages avec des vidéos, des images ou des liens sont autorisés.", delete_after=5)


bot.run(token)