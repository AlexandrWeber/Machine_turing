#utf-8

#import parser /// parser est un module qui exécute les boucles. à finaliser

# input du fichier et des chiffres
data=input("taper le fichier: ")
chiffres=input("taper les chiffres: ")

chiffres=chiffres.split()

# les listes pour la pile, le compteur d'instructions(compt) et le compteur d'instructions à l'intérieur de la boucle (compt_bouc)
adresse=[]
compt_bouc=0
compt=0
tete_pos=19

# la liste adresse concerve l'adresse du début et de la fin de chaque boucle tout en séparant le texte du fichier .split("\n") et en les mettant dans la liste
with open (data, 'r') as f:
	data_read=f.readlines()
	
	read_data="".join(data_read).split("\n")
	for z in read_data:
		compt_bouc+=1
		if z=="boucle:":
			adresse.append(compt_bouc)
		if z=="fin":
			adresse.append(compt_bouc)




# iniciation de la bande et de la tête de lecture
x=" "
bande=["\t\t", "0","0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0","0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
bande[19]="1"
tete=[x for e in range(0,len(bande))] 
tete.insert(0, "\t\t")
tete[tete_pos]="X"
#print de l'état inicial de la bande à chaque execution
print("".join(bande))
print("".join(tete))

 
# met les chiffres entrés par l'utilisateur sur la bande et les affiche. il y a 00 entre les deux chiffres
for i in range(19,20+int(chiffres[0])):
	bande[i]="1"
	
for c in range(22+int(chiffres[0]),22+int(chiffres[0])+int(chiffres[1])):
	bande[c]="1"

print("".join(bande))
print("".join(tete))

#partie execution. 
print("EXECUTION\n\n\n")




# on lit la liste avec les instructions et les exécute un par un. vu le nombre limité des instructions , il est possible de les énumérer
for d in read_data:
	compt+=1
	if d!="boucle":
		if d=="I":
			print("".join(bande))
			print("".join(tete))
		if d=="G":
			tete[tete_pos]=" " # la tête enlève le X
			tete_pos=tete_pos-1 # se positionne à gauche
			tete[tete_pos]="X" # écrit le X
		if d=="D":
			tete[tete_pos]=" " # la tête enlève le X
			tete_pos=tete_pos+1 # se positionne à droite
			tete[tete_pos]="X" # écrit le X
		
		if d=="1":
			bande[tete_pos]="1"
			tete[tete_pos]=" "
			tete_pos=tete_pos+1
			tete[tete_pos]="X"
			
		if d=="0":
			bande[tete_pos]="0"
			tete[tete_pos]=" "
			tete_pos=tete_pos+1
			tete[tete_pos]="X"
			
		if d=="si 1 fin":
			if bande[tete_pos]=="1":
				continue
				
		if d=="si 0 fin":
			if bande[tete_pos]=="0":
				continue
	"""	
	if d=="boucle:":
		while True:
			 
		parser.boucle(read_data, bande, tete, tete_pos, d, compt_bouc)
	"""
		
