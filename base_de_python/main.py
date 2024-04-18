
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0 :
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
        
            age_int = int(age_str) 

        except ValueError:
            print("Erreur: Vous devez rentrer un nombre pour l'age")
    
    return age_int 

def demander_nom():

    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom? ")
    return reponse_nom

def afficher_informations_personne(nom,age,taille = 0):
    print("")    
    print("Vous vous appelez " + nom + ",vous avez " + str(age) + " ans")
 
    if age > 60:
        print("Vous etes senior")
    elif age == 17:
        print("Vous etes presque Majeur")
    elif age >= 12 and age < 18:
        print("Vous etes  adolescent")
    elif age == 1 or age == 2:
        print("Vous etes un bébé")
    elif age < 10:
        print("Vous etes enfant")
    elif age == 18:
        print("Tous juste Majeur : Félicitation")
    elif age >= 18:
        print("Vous etes Majeur")
    else:
        print("Vous etes Mineur")

    if not taille == 0:
        print("Votre taille : " + str(taille) + "m")

#nom1 = demander_nom()
#nom2 = demander_nom()

#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

#afficher_informations_personne(nom1,age1)
#afficher_informations_personne(nom2,age2)

NB_PERSONNES = 3

for i in range(0, NB_PERSONNES):
    nom = "personne " + str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom,age,1.60)