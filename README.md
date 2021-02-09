1- PROJET_CYBER_SECURITE
Une application remplie de vulnérabilité pour mettre en exergue les surfaces d'attaque



2- QU'EST CE QUE FAIT LE PROJET?
Ce projet est un projet troué de la gestion de prise de rendez-vous des animaux chez un médecin vétérinaire
On peut donc y gérer un medecin, un parent, un animal-patient et un rendez-vous



3- LES OUTILS DE RÉALISATION
Ce projet a été fait en python avec le framework Django sur une base de données PostgreSQL



4- LES OBJECTIFS DE SÉCURITÉ
-La confidentialité (4,5/5): 
Les informations doivent être disponibles aux seules personnes ayant les droits necessaires.
Dans notre cas par exemple, la liste des animaux-patients et leurs informations ne doivent être visibles que pour les personnes qui en ont le droit. 
La fuite de données personnelles à des personnes malveillantes comme des kinappeurs peut mettre en danger la vie des patients.

-L'intégrité (5/5):
Les données attendues doivent être celles reçues, sans aucune altération possible.
On ne devrait pas par exemple se tromper de date de rendez-vous pour un patient pouvant créer des mécontentements au niveau des parents et mettre en péril l'image de la clinique.

-La disponibilité (4/5):
Le système doit être dans un état de fonctionnement optimal et répondre aux requêtes des utilisateurs en temps voulu et de manière rapide.
Dans notre cas par exemple, une demande de rendez-vous doit pouvoir être possible aux heures prévues et on doit pouvoir consulter n'importe quelle information à la demande.

-La traçabilité (2/5):
Toute trace de toute activité doit pouvoir être enregistrée.
La traçabilité n'est pas prioritaire dans notre système. Les droits et les autorisations sont bien distribués pour réduire les manipulations frauduleuses.



5- FONCTIONALITES DE SECURITE MIS EN PLACE
Vous trouverez dans le dossier app_cybersecu un fichier pdf "cybersécurité" listant les différentes fonctionnalités de sécurité mises en place


5- POUR LANCER LES CONTENEURS
Placez vous à la racine du dossier app_cybersecu et lancer la commande docker-compose up
La bonne version de python, de django et de postgresql sera installée vous permettant de lancer le projet dans votre navigateur

Après avoir lancé les conteneurs il faudra lancer les commandes de migration pour créer la BD.
Pour cela, ouvrez une autre fenêtre shell pendant que les conteneurs tournent et exécutez les commandes suivantes:

docker exec -it django bash (pour ouvrir le bash django)

python manage.py migrate (pour appliquer les migrations)



6- POUR LANCER LE PROJET
Allez dans votre navigateur et tapez l'adresse localhost:8000,

