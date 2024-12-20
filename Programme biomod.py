import matplotlib.pyplot as plt
import math




figure, axes = plt.subplots()


axes.set_title('Nombre de bactéries fécales vivantes')
axes.set_xlabel('Jour du traitement')
axes.set_ylabel('Nombre de bactéries vivantes/g (log10)')
#Les axes du graphique en ligne et le graphique sont nommés


for souris in range (0,96) :    #On doit avoir une courbe pour chaque souris


  fINPUT = open('data_real.csv', 'r')
  fFécal = open('sortie fécal', 'w')
  fCécal = open('sortie cécal', 'w')
  fIleal = open('sortie ileal', 'w')
  #Le fichier contenant les données de l'expérience est ouvert et les fichiers de sortie (qui contiendront les données nécessaires aux 3 graphiques sont crées
  fFécal.close()
  fCécal.close()
  fIleal.close()
  #Afin de ne pas avoir trop de fichiers ouverts en même temps, les fichiers de sortie sont refermés


  ligne = fINPUT.readline()    #Lecture de la première ligne du fichier d'entrée
  liste = []   #Création de la liste qui contiendra les différents éléments du fichier d'entrée
  xgraphligne = []     #Création de la liste qui contiendra les données de l'axe des abscisses
  ygraphligne = []     #Création de la liste qui contiendra les données de l'axe des ordonnées




  while ligne != '':   #Cette boucle est effectuée tant que la ligne n'est pas vide, donc tant qu'il reste des lignes non-lues à notre fichier d'entrée
      ligne = fINPUT.readline()
      ligne = ligne.replace('\n', '') # On retire le retour à la ligne
      liste = ligne.split(';')     #Création d'une liste où les différents éléments sont les données du fichier d'entrée, la séparation se faisant au niveau du ";"




      if len(liste) != 11:  #Si la liste a moins d'éléments que le ficher a de colonnes, on sort de la boucle (ça nous évite d'avoir une liste vide à la fin)
          break


      listeSortie = []
      listeSortie2 = []
      listeSortie3= []
      #Création des 3 listes de sortie


      localisation = str(liste[2])     #Permet de différencier fécal, cécal et iléal pour faire nos 3 graphiques


      if localisation == 'fecal':  # On ne prend que les fécales
          fFécal = open('sortie fécal', 'a')   #On réouvre notre premier fichier de sortie en mode "ajout"
          listeSortie = [liste[4]] +[liste[5]] + [liste[7]] + [liste[8]]  # On ne réécrit que les listes "fécales"
          résultat = ';'.join(listeSortie)  # On assemble les termes de ces listes pour refaire un csv
          lS = résultat.split(';') #On recrée une liste
          fFécal.write(résultat + '\n')  # On écrit ces listes dans le fichier de sortie en ajoutant le retour à la ligne




      elif localisation == 'cecal' :   #On ne prend que les cécales
          fCécal = open('sortie cécal', 'a')
          listeSortie2 = [liste[4]] +[liste[5]] + [liste[7]] + [liste[8]]
          résultat2 = ';'.join(listeSortie2)  # On assemble les termes de ces listes pour refaire un csv
          fCécal.write(résultat2 + '\n')  # On écrit ces listes dans le fichier de sortie en ajoutant le retour à la ligne
          fCécal.close()   #Comme on en a pas besoin tout de suite, on le referme




      else :
          fIleal = open('sortie ileal', 'a')   #Il ne reste plus que les iléales
          listeSortie3 = [liste[4]] + [liste[5]] + [liste[7]] + [liste[8]]
          résultat3 = ';'.join(listeSortie3)  # On assemble les termes de ces listes pour refaire un csv
          fIleal.write(résultat3 + '\n')  # On écrit ces listes dans le fichier de sortie en ajoutant le retour à la ligne
          fIleal.close()   #Comme on en a pas besoin tout de suite, on le referme




      sourisID = int(lS[0].replace('ABX', ''))     #On supprime le terme 'ABX' de l'identifiant des souris afin de n'avoir que leur numéro


      Jour = float(lS[2])
      BactériesFécales = math.log10(float(lS[3]))  #On traite la valeur du tableau pour qu'elle ait la forme attendue (logarithmique)






      if sourisID==souris :    #Si l'identifiant de la souris correspond au numéro d'itération, on crée la courbe
          xgraphligne.append(Jour)
          ygraphligne.append(BactériesFécales)
          #On ajoute dans les listes créées prcedemment, les données nécessaires à la création du graph


      axes.plot(xgraphligne, ygraphligne)  #Détermination des axes abscisses et ordonnées
      fFécal.close()   #Fermeture du premier fichier de sortie




figure.savefig('Nombre de bactéries fécales vivantes chez les 2 groupes de souris en fonction du jour de traitement', dpi=400)
#Sauvegarde du premier graphique en tant que fichier image




fINPUT.close()      #Fermeture du fichier d'entrée




figure, axes = plt.subplots()   #Initialisation d'un nouveau graphique


axes.set_title('Nombre de bactéries cécales vivantes')
axes.set_ylabel('Nombre de bactéries vivantes/g (log10)')
#On nomme le graphique et l'axe


fCécal = open('sortie cécal', 'r')  #On réouvre le fichier créé précedemment cette fois en lecture seule
ligneCécal= fCécal  #Création de la variable
ygraphvioloncécalABX = []
ygraphvioloncécalPlacebo = []
#Création des listes qui accueilleront les 2 catégories de souris


while ligneCécal != '':
  ligneCécal = fCécal.readline()
  ligneCécal = ligneCécal.replace('\n', '')  # On retire le retour à la ligne
  listeCécal = ligneCécal.split(';')


  if len(listeCécal) != 4:  #On n'a plus que 4 colonnes dans ce fichier
      break


  BactériesCécales = math.log10(float(listeCécal[3]))


  if listeCécal[1] == 'ABX':  #Si les souris sont ABX, on ajoute leur nb de bactéries dans la liste pour les souris ABX
      ygraphvioloncécalABX.append(BactériesCécales)
  else:
      ygraphvioloncécalPlacebo.append(BactériesCécales)  #Sinon, on l'ajoute dans la liste pour les souris placebo


axes.violinplot([ygraphvioloncécalABX, ygraphvioloncécalPlacebo])   #Création du type de graphique




figure.savefig('Violon cécal', dpi = 400)
#Sauvegarde en tant que fichier image du 2e graphique


figure, axes = plt.subplots()   #Initialisation du 3e graphique




axes.set_title('Nombre de bactéries iléales vivantes')
axes.set_ylabel('Nombre de bactéries vivantes/g (log10)')




fIléal = open('sortie ileal', 'r')
ligneIléal= fIléal
ygraphviolonIléalABX = []
ygraphviolonIléalPlacebo = []




while ligneIléal != '':
  ligneIléal = fIléal.readline()
  ligneIléal = ligneIléal.replace('\n', '')  # On retire le retour à la ligne
  listeIléal = ligneIléal.split(';')


  if len(listeIléal) != 4:  # Le nombre de colonnes
      break




  BactériesIléales = math.log10(float(listeIléal[3]))




  if listeIléal[1] == 'ABX':  # Si les souris sont ABX, on ajoute leur nb de bactéries dans la liste pour les souris ABX
      ygraphviolonIléalABX.append(BactériesIléales)
  else:
      ygraphviolonIléalPlacebo.append(BactériesIléales)  # Sinon, on l'ajoute dans la liste pour les souris placebo




axes.violinplot([ygraphviolonIléalABX, ygraphviolonIléalPlacebo])




figure.savefig('Violon iléal', dpi = 400)
