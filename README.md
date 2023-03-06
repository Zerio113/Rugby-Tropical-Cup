
# Exercice "Rugby"

![Logo](../../assets/rugby.svg)

👉 À réaliser après avoir lu le cours "Advanced 3"

## 📜 Situation

Depuis l'année 2022, le paysage du rugby s'est doté d'une nouvelle compétition : la **Rugby Tropical Cup**. Mettant en concurrence des équipes nationales dans un tournoi à élimination directe, sa première édition s'est déroulée avec succès dans son pays hôte, la Nouvelle-Zélande.


Pour la deuxième édition de 2023, le pays hôte sera le Japon, bénéficiant déjà d'une expertise suite à son accueil d'une précédente compétition internationale de Rugby. Plusieurs villes accueilleront les différents matchs. Cette fois-ci, les pays en compétition seront les suivants : Nouvelle-Zélande, Australie, Japon, Fidji, Samoa, Tonga, Afrique du Sud et Angleterre.

L'entreprise qui s'occupait de la billetterie pour la précédente édition ayant fait un travail remarquable, elle est appelée à nouveau pour éditer les billets correspondant aux commandes du site e-commerce.

Voici le calendrier des rencontres :

Date            | Match                  | Affiche
--------------- | ---------------------- | ---------------------
12 Juillet 2023 | Quart de finale A      | Angleterre vs Fidji
13 Juillet 2023 | Quart de finale B      | Japon vs Samoa
14 Juillet 2023 | Quart de finale C      | Australie vs Tonga
15 Juillet 2023 | Quart de finale D      | Nouvelle-Zélande vs Afrique du Sud
18 Juillet 2023 | Demi-finale            | Vainqueur Quart A vs Vainqueur Quart B
20 Juillet 2023 | Demi-finale            | Vainqueur Quart C vs Vainqueur Quart D
22 Juillet 2023 | Match pour la 3e place |
22 Juillet 2023 | Finale                 |

Pour ce qui est des billets, ils seront vendus selon 3 catégories, et avec plusieurs choix de devises pour faciliter l'achat à l'international : yen japonais (JPY), euro (EUR) et dollar néo-zélandais (NZD).

Catégorie            | Placement | Prix JPY | Prix EUR | Prix NZD
-------------------- | --------- | -------- | -------- | --------
Catégorie "Silver"   | Libre     | 5500 JPY | 40 EUR   | 65 NZD  
Catégorie "Gold"     | Attribué  | 6700 JPY | 50 EUR   | 80 NZD  
Catégorie "Platinum" | Attribué  | 8000 JPY | 60 EUR   | 95 NZD  

## 🏁 Objectifs

Vous êtes en charge de la génération des billets dans leur version française. Pour cela, l'entreprise qui s'occupe de la vente des billets en ligne vous a fourni plusieurs choses :

* Un export de leur base de données, avec 1 fichier JSON correspondant à 1 table
* L'image de fond à utiliser pour les billets

### Formatage des données

Vu que l'API permettant de récupérer ces informations en temps réel n'existe pas encore, on vous a fourni des extraits de la base de données sous forme de documents JSON, chaque fichier correspondant à une table :

* `stadiums.json` contient la liste des stades utilisés lors du tournoi
* `events.json` contient la liste des matchs
* `tickets.json` contient la liste des billets à éditer

Vous y retrouverez notamment les ID (clés étrangères) utilisés dans la base de données pour faire référence à d'autres tables. La valeur `event_id` présente sur un élément du fichier `tickets.json` fera donc référence à un match du fichier `events.json`, etc.

Pour identifier chaque ticket, utiliser un simple nombre qui s'auto-incrémente aurait été délicat car trop simple à deviner, facilitant ainsi la fraude aux faux billets. On utilise à la place des [**UUID**](https://fr.wikipedia.org/wiki/Universally_unique_identifier) quasi-uniques pour numéroter chaque billet, la base de donnée d'origine [(PostgreSQL)](https://www.postgresql.org/docs/current/datatype-uuid.html) s'occupant d'éviter l'insertion tout doublon.

### Écriture sur le billet

Votre tâche sera d'abord de lire les trois documents JSON, d'éventuellement ranger et recouper leurs données, puis il faudra ensuite boucler sur **chaque billet** pour écrire leurs informations et le QR Code sur l'image de fond, qui sera sauvegardée dans le dossier `tickets`.

Pour le texte à imprimer sur le billet, il faudra impérativement utiliser la police d'écriture de la charte graphique du tournoi, à savoir **Akshar**. Le nom des équipes devront être écrits en **noir** avec la police **"Akshar Bold"** ("Bold" étant une grosse épaisseur), et le reste des textes devront devront être écrits en **blanc** avec la police **"Akshar Medium"** ("Medium" étant une épaisseur moyenne). L'entreprise vous a fourni les fichiers à utiliser, dans le dossier `fonts`.

Vous partez de données formatées en anglais (sauf pour le nom des équipes) et il faudra donc prendre en compte cela. Les dates sont stockées au format [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601) avec l'heure correspondant au fuseau horaire [JST](https://fr.wikipedia.org/wiki/Heure_normale_du_Japon) observé au Japon, et correspondant à +9 heures par rapport à UTC. Sur le billet, la date devra être affichée au format "jour/mois/année" et l'heure du match au format "heures:minutes", grâce à l'usage de la [bibliothèque standard datetime](https://docs.python.org/fr/3/library/datetime.html). Si un billet n'a pas de place définie (valeur "free"), on devra écrire "Libre".

Le code-barres bidimensionnel de type **QR Code** a été choisi pour assurer un scan rapide des billets, qu'ils soient imprimés ou présentés sur un smartphone. Son contenu devra simplement correspondre à l'ID du billet.

Pour cela, on vous propose d'installer et d'utiliser la bibliothèque Python `qrcode` dont la documentation est sur [PyPI](https://pypi.org/project/qrcode/). Son usage n'est pas très complexe, mais on vous a fourni un exemple fonctionnel dans le fichier `test_qr.py`.

Enfin, l'entreprise d'impression vous a envoyé les positions x,y de chaque texte ainsi que celles du QR Code :

* 111, 340 : QR Code
* 877, 115 : Équipe domicile (1ere ligne)
* 877, 242 : Équipe extérieur (2nde ligne)
* 705, 375 : Nom du stade
* 1155, 375 : Ville du stade
* 705, 485 : Date de début du match
* 1155, 485 : Heure de début du match
* 650, 605 : Catégorie
* 845, 605 : Place
* 995, 605 : Prix du billet

## ⭕ Conditions de réussite

* ✔️ Chaque image générée correspond à un billet du fichier `tickets.json`
* ✔️ Toutes les informations du billet, du stade et du match sont écrites de façon lisible (format de date, devise...)
* ✔️ Le prix du billet est suivi d'un `$`, d'un `€` ou d'un `¥` selon la devise
* ✔️ Un billet sans place attribuée indique "Libre"

## ☝ Conseils

Faites attention, lors de l'écriture de votre code, à ne pas trop mélanger anglais et français, et à utiliser le bon lexique selon la langue : "billet" en français mais "ticket" en anglais, etc. Dans le cas présent, les données qui vous sont fournies sont en anglais, et il vaut mieux s'en tenir à l'anglais lorsque l'on travaille avec un partenaire international. (Vous pouvez garder les commentaires en français, ça reste un exercice !)
