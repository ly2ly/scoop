Module de gestion des cooperatives agricoles CI

Je fais un briefing rapide:<br></br>
L'objective est de creer un module de gestion des cooperatives agricoles alors l'idee comme l'a dit est d'integrer et d'adapter <br></br>
a Odoo. Les taches à faire:<br></br>
* ajouter les bolean isplanteur et isdelegue dans la fiche partenaire<br></br>
* dans le cas du planteur integrer la fichier xls Base de données qui est la base des planteurs<br></br>
* creer une table + vue mandat avec les champs date, delegué, fonds, nbre emballages, emballage, unité de mesure emballages<br></br>
explication: dans les cooperatives, de l'argent est remis à une categorie de commercial (les delegués) qui vont acheter <br></br>
des produits directement aux planteurs et il leur est preté des emballages pour le transport. <br></br>
Ces fonds sont suivi comptablement avec un compte financier de type tiers. Alors l'operation de remise de fonds doit permettre d'augmenter le debit du compte lié au partenaire.<br></br>
Sur la fiche partenaire, avec un bouton intelligent, on doit pouvoir savoir le niveau du compte du delegué ainsi que le nombre d'emballage en sa possession.<br></br>
pour La table + vue des mandat, vous avez un exemple dans le fichier gestion 2016 pour la partie MANDAT.<br></br>
Sur la fiche partenaire, avec un bouton intelligent, on doit pouvoir savoir le niveau du compte du delegué ainsi que le nombre d'emballage en sa possession.<br></br>
pour La table + vue des mandat, vous avez un exemple dans le fichier gestion 2016 pour la partie MANDAT.<br></br>
<br></br>
* Creer une table + vue suivi de pesage qui equivaut à des fiches d'entrée d'articles et d'emballage en stock<br></br>
explication: les cooperatives achetent des produits avec les delegués et planteurs.<br></br>
la valeur des produits livrées (article) est defini en fonction du prix d'achat unitaires par la quantité d'unité de mesure et<br></br>
cette valeur est enregistré au credit du compte partenaire lié au partenaire (delegué ou planteurs). la table recupere aussi <br></br>
la quantité d'emballage utilisé qui dans le cas d'un delegué viendra diminuer la quantité d'emballage qui lui avait ete remis.<br></br>
un taux de commission par defaut peut etre affecté à un delegué (dans sa fiche partenaire). Il permettra de determiner la valeur<br></br>
de sa commission du le prix de vente. Cette valeur viendra en augmentation du credit de son compte.<br></br>
L'ensemble des ces infos sont enregistré dans le document FICHE DE SUIVI PESAGE.<br></br><br></br>
TO DO: <br></br>
* Gestion des emprunts planteurs<br></br>
* Gestion et planification des chargements de produits.<br></br><br></br>


Taches To DO<br></br>
Richmond: fiche partenaire<br></br>
Elias: suivi du pesage et du mandat delegué<br></br>