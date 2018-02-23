### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#coding: utf-8

#ici, je dis à python d'importer le module "csv", ce qui
#va lui permettre de lire le fichier grants.csv
import csv

#ici, je créer une varible qui va correspondre à mon fichier
#pour ne pas avoir à réécrire le nom du fichier chaque fois

### Je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordinateur

fichier = "../grants.csv"

### J'ajoute un compteur pour vérifier le nombre de subventions que trouve ton code

n = 0

#Je code ici une variable qui va ouvrir le fichier (encore une fois,
#c'est plus facile ensuite si je dois réouvrir le fichier)
f1 = open(fichier)

#Ici, j'utilise une fonction du module "CSV" que j'ai importé
#plus tot pour lire le fichier csv.
lignes = csv.reader(f1)

### En fait, la boucle n'a pas de nom; c'est la variable dont tu te sers dans la boucle qui s'appelle «joly» (cool nom d'aileurs)

#Ici, j'ai créer une boucle que j'ai appelé "JOLY." Ce que je dis à
#python, c'est qu'a chaque fois qu'il rencontre les mots "Fonds du Canada pour les périodiques"
#Dans l'élément 18 du tableau du fichier csv (qui contient l'emplacement ou le nom du programme se trouve)
#de m'imprimer la ligne correspondante. J'ai trouvé la méthode "if in" sur le forum de stack overflow.

for joly in lignes:

	#Suivant une méthode que j'ai lu sur stack overflow, j'ai créer une variable qui correspond à la
	#case ou se trouvent les dates de chaque subvention.
	date = joly[13] 
	
	if "Fonds du Canada pour les périodiques" in joly[17]:

### J'augmente mon compteur de 1
		n += 1

### Excellente façon de trouver l'année

		#Je dis ici a python de m'imprimer chaque ligne, et juste avant, je lui demande de
		#me faire une colonne qui contient seulement les 4 premiers caractères de
		#des éléments de la variable date. (Ce sont les 4 premiers qui déterminent l'année.)

### J'ajoute ma variable «n» à ton «print»
		print(n,date[:4],joly)

### Très bon code!
### Il ne trouve cependant que 2494 subventions alors qu'il y en a 4608.
### Pour trouver celles qui manque, il faut simplement chercher une autre expression dans ton «if»:
### «if "Fonds du Canada pour les périodiques" in joly[17] or "FCP -" in joly[17]:»
### Cela te permet aussi de trouver les subventions identifiées uniquement par l'acronyme «FCP»