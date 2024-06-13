# Projet Marty

Bienvenue dans le projet Marty ! Ce projet a pour objectif de développer une application en Python avec PyQt6 pour piloter et gérer des robots Marty. Ce fichier README fournit une vue d'ensemble des fonctionnalités, de la structure du projet, et des instructions pour démarrer.

## Contexte

- **Outil de gestion de projet** : Utiliser un outil de gestion de projet associé à Git.
- **Gestion de version de code** : Utiliser Git pour la gestion de versions.
- **Technologies** : Python et PyQt6.
- **Accès pour les enseignants** : Fournir l’accès à la gestion de projet et au dépôt Git avant le 13 avril 2024 aux enseignants :
  - Quentin.Chassel@u-bourgogne.fr
  - Hermine.Chatoux@u-bourgogne.fr
  - Duncan.Luguern@u-bourgogne.fr
  - Meldrick.Reimmer@u-bourgogne.fr
- **Premiers livrables** : Un premier commit et le premier jet de la gestion de projet doivent être réalisés.

## Fonctionnalités

### 1ère Partie

- **Connexion/Déconnexion des robots** : Gérer la connexion et la déconnexion des robots Marty via le protocole de communication.
- **Interface graphique** :
  - **Pilotage du robot** : Avancer, reculer, tourner.
  - **Emotions** : Gérer le regard de Marty, danser, célébrer.
  - **Données capteurs** : Récupérer les données des capteurs (distance, obstacle, niveau de batterie, flux vidéo, capteur couleur).
  - **Pilotage par interface** : Piloter les déplacements du robot via des boutons sur l’interface et par les touches du clavier.
- **Groupes de 4 personnes** : 
  - **Pilotage par manette** : Utiliser une manette de jeux ou d'autres périphériques pour le pilotage et les animations (vibration/lumière) de la manette.
  - **Liste d'instructions** : Ajouter un onglet pour créer une liste d'instructions que Marty exécutera successivement.

### 2ème Partie

- **Gestion de deux robots** : Piloter deux robots en séquentiel, Marty1 commence toujours le premier.
- **Labyrinthe** : Utiliser des repères de couleur pour aller au centre du labyrinthe.
  - **Déplacement tour par tour** : Chaque robot avance l’un après l’autre.
  - **Lecture de QR code** : Lire les QR codes au sol via la caméra pour reconstituer une phrase mystère lors de la rencontre des robots au centre du labyrinthe.
  - **Célébration** : Les robots célèbrent leur rencontre.
  - **Chorégraphie synchronisée** : Synchroniser les robots pour une chorégraphie lors de leur rencontre.

## Structure du Projet

```plaintext
marty_project/
├── Application/
│   ├── Interface/
│       ├── main.py
│   │   ├── Class_MartyControlApp.py
│   │   ├── Class_MartyRobot.py
│   │   └── ...
│   ├── /
│   │   ├── marty.py
│   │   └── ...
│   ├── utils/
│   │   ├── communication.py
│   │   ├── sensors.py
│   │   └── ...
│   └── ...
├── tests/
│   ├── test_communication.py
│   ├── test_sensors.py
│   └── ...
├── docs/
│   ├── requirements.md
│   ├── design.md
│   └── ...
└──README.md
