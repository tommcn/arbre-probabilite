import json


with open("tree.json") as f:
    data = json.load(f)

def main():
    printChilds(data, 0)

def printChilds(parent, profondeur):
    for i in range(profondeur):
        print("\t", end="")
    if parent != None:
        for key in parent:
            print(key, "-", parent[key]["chance"])
            if parent[key]["enfants"] != {}:
                printChilds(parent[key]["enfants"], profondeur+1)
            elif len(parent[key]["enfants"]) == 1:
                check = parent["key"] 
                while (len(find_key(data, check)) == 1):
                    profondeur -= 1
                    check = find_key(data, check)
                printChilds(parent["key"], profondeur)
            else:
                printChilds(parent[key]["enfants"], profondeur)


def find_key(d, value):
    for k,v in d.items():
        if isinstance(v, dict):
            p = find_key(v, value)
            if p:
                return [k] + p
        elif v == value:
            return [k]

if __name__ == "__main__":
    main()