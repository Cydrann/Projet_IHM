Projet IHM 

Le sujet répond à la majorité des problématiques malgré quelques omissions comme les révoltes. 
Pour l'executer il faudra executer le fichier menu.py uniquement ! 
Hormais les fonctions de tkkinter je n'ai pas utilisé de fonctins necessitant un certain setup.

Cependant, il fonctionne plutôt bien :
Seul le bouton nouvelle_partie et Quitter fonctionnent pour le moment.
![image](https://github.com/user-attachments/assets/9bb9d9ef-c42b-4808-bfa7-2f600bd38482)

Chaque phase doit se faire en cliquant sur les boutons afin de pouvoir progresser à son rythme et ne pas être surpris par les fonctions executé automatiquement comme evenement_aléatoire de la phase 1
Chaque map est généré aléatoirement en respectant les consignes de distances entre chaque village.
Il y a également une sécurité, l'utilisateur ne peut pas sauter de phase elles doivent être réalisée dans l'ordre et donc chacune ne se réalisera que lorsque la précedente a été eu lieu.

![image](https://github.com/user-attachments/assets/14b14934-0394-47ba-a54b-61d720a8e27a)

On a une jauge d'actions réalisables, chaque action en consomme sauf "Rien faire" et se regenere à chaque fin de tour.

On commence par créer un village : Phase 2 -> Construire -> On choisit le terrain où on souhaite faire construire son village et il apparait.
Les villages ne peuvent être placés que dans zones spéciiques.

Ensuite il sera alors possible de réaliser diverses actions sur ce village.



Quelques anomalies sont à souligner :

- Il y a eu un bug sur le 1er village crée, on ne plus interagir avec lui.Il fonctionnait bien au début mais en continuant le projet j'ai du faire une mauvaise manipulation ça devrait pouvoir être fix assez rapidement avec un peu plus de temps.

- Le clic pour les villages laisse à désirer, en effet la zone pour cliquer sur le village n'est pas bien centré, il faut plus cliquer vers le coté bas-droit de l'image afin que ça fonctionne bien.

- La generation du fief ne peut se faire qu'une fois par execution après la génération de la map n'est pas celle souhaitée.


  La redirection de la sortie standard vers un widget vient de :
  https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget

  
