from os import system
import json

class Option:
    def __init__(self, name, chance):
        self.name = name
        self.chance = chance
        self.enfants = []
        self.parent = None
    
    def __str__(self):
        return f"{self.name} -- {self.chance}"
    def __repr__(self):
        return f"{self.name} -- {self.chance}"

def main():
    system("clear")
    tree = {}
    other_tree = []
    nb_epreuves = convertInt(input("Nombre d'epreuves: "))
    
    for i in range(nb_epreuves):
        other_tree.append([])
        if i == 0: #premiere fois
            issues = convertInt(input(f"Nombre d'issues pour l'epreuve #{i+1}: "))
            for j in range(issues):
                issue = input(f"Issue #{j+1}: ")
                chance = convertFloat(input(f"Chance de l'issue #{j+1}: "))
                add = Option(issue, chance)
                other_tree[i].append(add)
        else:
            for count, j in enumerate(other_tree[i-1]):
                issues = convertInt(input(f"Nombre d'issues pour l'epreuve #{i+1}, dependant de '{other_tree[i-1][count]}': "))
                for k in range(issues):
                    issue = input(f"Issue #{k+1}, dependant de '{other_tree[i-1][count]}': ")
                    chance = convertFloat(input(f"Chance de l'issue #{k+1}, dependant de '{other_tree[i-1][count]}': "))
                    add = Option(issue, chance)
                    add.parent = other_tree[i-1][count]
                    other_tree[i-1][count].enfants.append(add)
                    other_tree[i].append(add)
    
    print(other_tree)
    for i in other_tree[0]:
        tree[i.name] = {}
        tree[i.name]["chance"] = i.chance
        tree[i.name]["enfants"] = createDictFromChilds(i)

    printDict(tree)


        
    
def createDictFromChilds(d):
    temp = {}
    if not len(d.enfants) == 0:
        for i in d.enfants:
            temp[i.name] = {}
            temp[i.name]["chance"] = i.chance
            temp[i.name]["enfants"] = createDictFromChilds(i)
        return temp
    else:
        return {}
    

    


def convertInt(val):
    try:
        return int(val)
    except ValueError:
        print("Erreur")
        exit(1)

def convertFloat(val):
    try:
        return float(val)
    except ValueError:
        print("Erreur")
        exit(1)

def printDict(d):
    nice = json.dumps(d, indent=4)
    print(nice)
    with open("tree.json", "w+") as f:
        f.write(nice)




if __name__ == "__main__":
    main()