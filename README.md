# BOT Discord LSPD

Conçu pour la faction LSPD du serveur GTA RP FIVE M | Flashworld en 2023.
Ce projet est un bot Discord conçu pour gérer diverses fonctionnalités liées à un serveur Discord de type "Los Santos Police Department" (LSPD). Le bot est développé en Python en utilisant la bibliothèque `discord.py`.

## Fonctionnalités principales

### 1. Gestion des utilisateurs
- **Antiraid** : Bannit automatiquement les utilisateurs qui rejoignent le serveur avec des permissions administratives.
- **Gestion des rôles** :
  - Ajout ou suppression de rôles spécifiques (ex. : rôle "Absent").
  - Gestion des rôles pour les "Rookies".
  - Licenciement d'un agent avec suppression de ses rôles et récupération de ses comptes Trello et MDT.
- **Blacklist et refus de candidats** :
  - Blacklist un candidat avec un motif.
  - Refuse temporairement un candidat avec un rôle spécifique et une durée définie.
  - Accepte un candidat avec un rôle temporaire.

### 2. Gestion des salons
- **Renommage des salons** : Permet de changer le nom d'un salon d'intervention.
- **Création de catégories** : Crée des catégories avec des salons spécifiques pour des groupes, avec des permissions configurées.

### 3. Gestion des présences
- **Vérification des présences** :
  - Liste les utilisateurs d'un rôle qui n'ont pas réagi à un message.
  - Liste les utilisateurs ayant réagi à un message.

### 4. Gestion des messages
- **Envoi de messages** : Commande pour envoyer un message dans un salon.
- **Modération des messages** :
  - Supprime les messages ne contenant pas de médias ou de liens dans certains salons.
  - Supprime les anciens messages du bot dans des salons spécifiques et envoie un modèle prédéfini.

### 5. Commandes slash
Le bot utilise des commandes slash pour une interaction plus intuitive. Voici quelques exemples :
- `/react` : Vérifie les utilisateurs sans réaction sur un message.
- `/intervention` : Change le nom d'un salon d'intervention.
- `/presence` : Liste les utilisateurs ayant réagi à un message.
- `/rookie` : Ajoute ou retire les rôles d'un rookie.
- `/licenciement` : Gère le licenciement d'un agent.
- `/trello` et `/mdt` : Récupère les comptes Trello ou MDT d'un utilisateur.
- `/groupe` : Crée une catégorie pour un groupe avec des salons spécifiques.
- `/absent` : Ajoute ou retire le rôle "Absent" à un utilisateur.

### 6. Notifications et logs
- Envoie des notifications privées à un utilisateur spécifique lors de mises à jour de rôles.
- Log des suppressions de rôles importants dans les audits du serveur.

## Fichiers du projet

### `main.py`
Le fichier principal qui contient la logique du bot, y compris les événements, les commandes et les interactions avec Discord.

### `secu.py`
Contient le token du bot. **Ce fichier est ignoré par Git grâce au `.gitignore` pour des raisons de sécurité.**

### `outils.py`
Fournit des modèles de messages et des identifiants de rôles utilisés dans le bot.

### `backup.py`
Un fichier supplémentaire qui semble contenir une version alternative ou de sauvegarde du bot.

### `version.csv`
Un fichier vide, probablement destiné à contenir des informations sur les versions du bot.

### `.gitignore`
Empêche le fichier `secu.py` d'être suivi par Git pour protéger le token du bot.

## Ce que vous avez fait

1. **Développement des fonctionnalités** :
   - Création de commandes pour gérer les rôles, les présences, les salons et les utilisateurs.
   - Implémentation de modèles de messages pour différents scénarios (ex. : absence, intervention, etc.).
   - Gestion des permissions et des rôles pour sécuriser les commandes.

2. **Sécurisation** :
   - Stockage du token dans un fichier séparé (`secu.py`) et ajout de ce fichier au `.gitignore`.

3. **Automatisation** :
   - Suppression automatique des messages non conformes dans certains salons.
   - Envoi automatique de modèles de messages dans des salons spécifiques.

4. **Utilisation avancée de Discord** :
   - Intégration des commandes slash pour une meilleure expérience utilisateur.
   - Utilisation des logs d'audit pour surveiller les modifications de rôles.

5. **Organisation du code** :
   - Séparation des responsabilités dans différents fichiers (`main.py`, `outils.py`, etc.).
   - Utilisation de dictionnaires pour mapper les salons à leurs modèles de messages.

## Dépendances

Les dépendances nécessaires pour exécuter ce projet sont listées dans le fichier `requirements.txt` :

- `discord.py==2.3.2`
- `py-cord==2.4.1`
- `asyncio`
- `python-dotenv`
- `os`

## Comment exécuter le bot

1. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
2. Lancez le fichier principal :
   ```bash
   python main.py
   ```