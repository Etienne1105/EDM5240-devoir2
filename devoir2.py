#coding: utf-8

#ici, je dis à python d'importer le module "csv", ce qui
#va lui permettre de lire le fichier grants.csv
import csv

#ici, je créer une varible qui va correspondre à mon fichier
#pour ne pas avoir à réécrire le nom du fichier chaque fois
fichier = "grants.csv"

#Je code ici une variable qui va ouvrir le fichier (encore une fois,
#c'est plus facile ensuite si je dois réouvrir le fichier)
f1 = open(fichier)

#Ici, j'utilise une fonction du module "CSV" que j'ai importé
#plus tot pour lire le fichier csv.
lignes = csv.reader(f1)


#Ici, j'ai créer une boucle que j'ai appelé "JOLY." Ce que je dis à
#python, c'est qu'a chaque fois qu'il rencontre les mots "Fonds du Canada pour les périodiques"
#Dans l'élément 18 du tableau du fichier csv (qui contient l'emplacement ou le nom du programme se trouve)
#de m'imprimer la ligne correspondante. J'ai trouvé la méthode "if in" sur le forum de stack overflow.

for joly in lignes:

	#Suivant une méthode que j'ai lu sur stack overflow, j'ai créer une variable qui correspond à la
	#case ou se trouvent les dates de chaque subvention.
	date = joly[13] 
	
	if "Fonds du Canada pour les périodiques" in joly[17]:

		#Je dis ici a python de m'imprimer chaque ligne, et juste avant, je lui demande de
		#me faire une colonne qui contient seulement les 4 premiers caractères de
		#des éléments de la variable date. (Ce sont les 4 premiers qui déterminent l'année.)
		print(date[:4],joly)


