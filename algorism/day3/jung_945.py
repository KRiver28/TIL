animation = {
    "Pokemon":"Pikachu",
    "Digimon":"Agumon",
    "Yugioh" : "Black Magician"
}

word = input()

print(animation.get(word,"I don't know"))