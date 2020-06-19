from efficient_apriori import apriori
import re
class Apriori :
    def __init__(self):
        self.known_transactions =[
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

    def get_rules(self):
        itemsets, rules = apriori(self.known_transactions, min_support=0.1, min_confidence=1)
        antecedents = []
        consequents = []
        for i in range(0, len(rules)):
            rule = rules[i]
            antecedent = re.search('{(.+?)}', str(rule))
            consequent = re.search('-> {(.+?)}', str(rule))
            antecedents.append(antecedent.group(1).split(", "))
            consequents.append(consequent.group(1).split(", "))
        return antecedents, consequents

    def get_known_transactions(self):
        return self.known_transactions
