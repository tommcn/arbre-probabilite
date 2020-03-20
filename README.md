# probabilite

Visualition d'un arbre de probabilite a partir d'un fichier JSON

## Format JSON

Chaque issue est constitué ainsi:  
```JSON
"nom": {
    "chance": 0-1,
    "enfants": {
        ...
    } 
}
```
`nom` est le nom qui va être montré à l'écran, il ne doit pas contenir d'espaces. `chance` doit être suivi d'une valeur entre 0 et 1 inclus. `enfants` est une liste d'issues qui dependent de la premiere issue.

### Example  

```JSON
{
    "nombre-pair": {
        "chance": 0.5,
        "enfants": {
            "voiture": {
                "chance": 0.6,
                "enfants": {}
            }, 
            "bille": {
                "chance": 0.4, 
                "enfants": {
                    "rouge": {
                        "chance": 1, 
                        "enfants": {}
                    }
                }
            }
        }
    },
    "nombre-impair": {
        "chance": 0.5,
        "enfants": {
            "voiture": {
                "chance": 0.6,
                "enfants": {
                    "bleu": {
                        "chance": 0.1, 
                        "enfants": {}
                    }, 
                    "vert": {
                        "chance": 0.9,
                        "enfants": {}
                    }
                }
            }, 
            "bille": {
                "chance": 0.4, 
                "enfants": {
                    "rouge": {
                        "chance": 1, 
                        "enfants": {}
                    }
                }
            }
        }
    }
}
```
Ici, les conditions de depart sont `nombre-pair` et `nombre-impair`, qui ont tous les deux comme enfants voiture et billes.

Pour commencer le serveur: `python3 application.py`. Vous verrez l'arbre des probabilités et en appuyant sur les cases vous verrez la probabilité que l'évenement se passe.

https://drive.google.com/file/d/1xnjhiDhvnmW9L2eqnMtryGj2SVXnQQw-/preview
