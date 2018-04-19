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

Entretien KASSI SCOOP 22112017

* Charge
- Gestion et suivi prefinancement des planteurs (pret planteurs)
	Suivi des operations
	Analyse du compte planteurs
	Edition des documents de caisse
	Paiement des prets
	Remboursement des prets

- Gestion des pisteurs
	Chaque pisteur est rattaché à une zone
	chaque planteur de la zone est rattaché à un pisteur
	(chaque planteur est aussi rattaché à une zone)
	il doit etre possible de faire des reaffectations de pisteurs (pouvoir suivre l'historique des affectations d'un pisteur??)
	
* Gestion des commissions chez les cooperants, les pisteurs et les cooperatives
- Pisteurs
	suivi de l'historique des prix de matieres premieres
	un fond est remis au pisteur pour l'achat de ses matieres premiere (a credit?)
	une commission est convenue entre la cooperative et les pisteurs (cette commission peut etre une commission variable et definir au poids)
	un fond peut etre remis au pisteur pour aller acheter les matieres premieres chez les planteurs
	un pisteur peut utiliser ses fonds propres pour acheter les matieres premieres chez les paysans
	au retour du pisteur un solde de son compte est effectué et ses commissions lui sont payé
		
** Document a fourni au conseil cafe cacao et a remplir en ligne (cas des cooperatives cacao)
	
	Commission des cooperants, cooperateurs et planteurs
		le prix des commission est decidé par AG
		il peut avoir des commissions ou pas
		les commissions sont calculées sur le volume des ressources envoyées (ressources ou production collecté au Kg)
		les commissions peuvent etre versées à tout moment mais de maniere generale cela se fait apres chaque campagne
		il est necessaire de pouvoir suivre en valeur et en quantité les volumes versés par les planteurs, leur situation et les commissions versées
		il faut pouvoir affecter chaque operation du systeme à une campagne grande, officiel ou des campagnes intermediaires
	Commission cooperative
		definition: difference entre le prix export et le prix bord champs (prix chez les planteurs)
		il represente le chiffre d'affaires des cooperatives et il est utilisé pour:
			le paiement des commissions
			les frais generaux
			les autres charges
			le solde est reversé au planteur (voir commission planteur)
		le client final (usinier ou exportateur) peut rembourser un fond (11 f/kg par exemple) qui sera reversé à la cooperative
		en fonction de ce qu'elle lui a envoyé. Les prix de ces remboursement sont defini par le conseil cafe cacao en fonction d'un
		bareme de distance. Ce mantant n'est pas toujours versée.

* Stock
- Magasin general (possibilité de multi entrepots)
	Matieres premieres
	Emballages sacs
	pouvoir suivre sortie de stocks de sacs chez les pisteurs et les planteurs
	pouvoir suivre retour de stocks de sacs chez les pisteurs et les planteurs
	en absence d'identification des sacs proposer un etiquetage code barre ou alphanumerique
- Entrees en stocks
	pisteurs ramene de la production emballé dans les sacs
	planteurs ramene de la production emballé dans les sacs
- Sorties de stocks
	Livraison chez le client export ou local
	Deplacement dans un autre entrepot
	
* Transport
- Identification des voyages
	tonnage, 
	transport, 
	date, 
	identification chauffeur, 
	identification vehicule, 
	identification prestataire
- Document de connestement demandé et livré par le client pour chaque voyages
Gestion de la caisse
Gestion des fournisseurs
