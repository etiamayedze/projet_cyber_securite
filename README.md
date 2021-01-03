# projet_cyber_securite
Une application remplie de vulnérabilité pour mettre en exergue les surfaces d'attaque

#Qu'est ce que fait le projet?
Ce projet est un projet troué de la gestion de prise de rendez-vous des animaux chez un médecin vétérinaire
On peut donc y gérer un medecin, un parent, un animal-patient et un rendez-vous

#Les outils de réalisation
Ce projet a été fait en python avec le framework Django sur une base de données PostgreSQL

#Les objectifs de sécurité

-La confidentialité (4,5/5): 
Les informations doivent être disponibles aux seules personnes ayant les droits necessaires.
Dans notre cas par exemple, la liste des animaux-patients ne doit être que visible pour les personnes qui en ont le droit. 

-L'intégrité (5/5):
Les données attendues doivent être celles reçues, sans aucune altération possible.

-La disponibilité (4/5):
Le système doit être dans un état de fonctionnement optimal et répondre aux requêtes des utilisateurs en temps voulu et de manière rapide.
Dans notre cas par exemple, une demande de rendez-vous doit pouvoir être possible aux heures prévues.

-La traçabilité (2/5):
Toute trace de toute activité doit pouvoir être enregistrée. Dans notre cas, Django implémente très bien cela avec son module d'administration donc nous nous y attarderons pas 

#Pour lancer les conteneurs
Placez vous à la racine du dossier app_cybersecu et lancer la commande docker-compose up
La bonne version de python, de django et de postgresql sera installée vous permettant de lancer le projet dans votre navigateur

#Pour lancer le projet
Allez dans votre navigateur et tapez l'adresse localhost:8000/accueil

