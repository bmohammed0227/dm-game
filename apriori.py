import re
from random import choice, randint

from efficient_apriori import apriori


# compte le nombre d'element communs entre deux tableaux
def count(tab1, tab2):
    count = 0
    for i in range(0, len(tab1)):
        for j in range(0, len(tab2)):
            if tab1[i] == tab2[j] :
                count+=1
    return count

# fonction qui retourne l'indice du tableau qui contient le plus d'elements communs
def search_index(tab1, tab2):
    index = randint(0, len(tab1)-1)
    nbr_common_elements = 0
    for i in range(0, len(tab1)):
        nbr = count(tab1[i], tab2)
        if(nbr > nbr_common_elements) :
            nbr_common_elements = nbr
            index = i
    return index

# fonction qui retourne le choix de l'algorithme apriori
def choice_apriori():
    global known_objects
    global choices
    global antecedents
    global consequents
    index = search_index(antecedents, known_objects)
    choice = search_index(choices, consequents[index])
    return choice


objects = ['biscuit','fish','mushroom','burger',
           'fruits','pistachio','cheese','honey',
           'pizza','chicken','icecream','shrimp',
           'chocolate','meat','soda','croissant',
           'medicine','sweets','egg','milk',
           'vegetables']

known_transactions =[
('chocolate','milk','croissant'),
('pizza','burger','icecream'),
('icecream','soda','pistachio'),
('pistachio','chocolate','honey'),
('fish','shrimp','sweets'),
('mushroom','medicine'),
('fruits','chicken','cheese','meat'),
('burger','icecream','pizza'),
('biscuit','milk','egg'),
('sweets','shrimp','fish'),
('chocolate','honey','pistachio'),
('medicine','mushroom'),
('pizza','burger','icecream'),
('biscuit','milk','egg'),
('honey','pistachio','chocolate'),
('croissant','chocolate','milk'),
('mushroom','medicine'),
('chocolate','milk','croissant')
]


unknown_transactions = [
('milk','chocolate','croissant'),
('burger','pizza','icecream'),
('soda','icecream','pistachio'),
('chocolate','pistachio','honey'),
('shrimp','fish','sweets'),
('mushroom','medicine'),
('cheese','chicken','fruits','meat'),
('icecream','burger','pizza'),
('milk','biscuit','egg'),
('shrimp','sweets','fish'),
('honey','chocolate','pistachio'),
('medicine','mushroom'),
('burger','pizza','icecream'),
('milk','biscuit','egg'),
('pistachio','honey','chocolate'),
('chocolate','croissant','milk'),
('medicine','mushroom'),
('milk','chocolate','croissant')
]


itemsets, rules = apriori(known_transactions, min_support=0.1, min_confidence=1)
antecedents = []
consequents = []
print("Règles extraites :")
print("____________________")
for i in range(0, len(rules)):
    rule = rules[i]
    antecedent = re.search('{(.+?)}', str(rule))
    consequent = re.search('-> {(.+?)}', str(rule))
    antecedents.append(antecedent.group(1).split(", "))
    consequents.append(consequent.group(1).split(", "))
    print(antecedents[i],"->",consequents[i])
print("____________________")

#on déroule les achats connues
for id_known_transaction in range(0,len(known_transactions)):
    print("Le client (apparence",randint(0,3),") est rentré")
    print("Le client a acheté : ", known_transactions[id_known_transaction])
    print()

print("___________________________________________")
print("             Début du jeu :")
print("___________________________________________")

enchainement_player = False
enchainement_algo = False
score_player = 0
score_algo = 0
#on devine les nouveaux achats
for id_unknown_transaction in range(0,len(unknown_transactions)):
    print("Le client (apparence",randint(0,3),") est rentré")
    transaction = unknown_transactions[id_unknown_transaction]
    number_known_objects = randint(1,len(transaction))
    number_unknown_objects = len(transaction)-number_known_objects
    known_objects = []
    unknown_objects = []
    for i in range(0, len(transaction)):
        if(i<number_known_objects):
            known_objects.append(transaction[i])
        else:
            unknown_objects.append(transaction[i])

    print("Le client a acheté : ", known_objects)

    false_choice = []
    choices = []
    # on crée le vecteur des choix possible
    if(randint(0,10)<5):
        # on ajoute le bon choix d'abord
        choices.append(unknown_objects)
        right_choice_id = 0
        # puis on ajoute au hasard un autre choix
        false_choice.append(choice(objects))
        false_choice.append(choice(objects))
        choices.append(false_choice)
    else :
        # on ajoute au hasard un choix faux
        false_choice.append(choice(objects))
        false_choice.append(choice(objects))
        choices.append(false_choice)
        # puis on ajoute le bon choix
        choices.append(unknown_objects)
        right_choice_id = 1

    print("Devinez ce qu'il va acheté ensuite, entrer votre choix :")
    print("0 : ", choices[0])
    print("1 : ", choices[1])

    player_choice = int(input())
    old_score_player = score_player

    if(player_choice == right_choice_id) :
        print("c'est juste ! ",end='')
        if(enchainement_player == True):
            score_player *= 2
        else :
            score_player += 20
    else :
        print("faux !",end='')
    if(old_score_player==score_player) :
        enchainement_player = False
    else :
        enchainement_player = True

    print("votre score :", score_player)
    print("- - - - - ")
    # L'algo devine la liste d'achats
    algo_choice = choice_apriori()
    print("algo choice : ", algo_choice)
    print("L'algo a choisi : ", choices[algo_choice])
    old_score_algo = score_algo
    if(algo_choice == right_choice_id):
        print("c'est juste ! ",end='')
        if(enchainement_algo == True):
            score_algo *= 2
        else :
            score_algo += 20
    else :
        print("faux !",end='')
    if(old_score_algo==score_algo):
        enchainement_algo = False
    else :
        enchainement_algo = True

    print("Le score de l'algo :", score_algo)
    print("____________________\n")
