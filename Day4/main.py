import re


def txtToList():
    with open("Day4/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def numerosIguais(lista1, lista2):
    count = 0
    for numero in lista1:
        if numero in lista2:
            count += 1
    return count


def part1(lista):
    games = []
    for i in range(len(lista)):
        game = {}
        lista[i] = re.split(r"[|:]", lista[i])
        for j in range(len(lista[i])):
            lista[i][j] = lista[i][j].split(" ")
            if "" in lista[i][j]:
                while "" in lista[i][j]:
                    lista[i][j].remove("")
            game[j] = lista[i][j]
        games.append(game)
    pontos = 0
    for i in range(len(games)):
        qtdGanhadores = numerosIguais(games[i][1], games[i][2])
        if qtdGanhadores > 1:
            pontos += 2 ** (qtdGanhadores - 1)
        else:
            pontos += qtdGanhadores
    print(pontos)


def part2(lista):
    games = []
    for i in range(len(lista)):
        game = {}
        lista[i] = re.split(r"[|:]", lista[i])
        for j in range(len(lista[i])):
            lista[i][j] = lista[i][j].split(" ")
            if "" in lista[i][j]:
                while "" in lista[i][j]:
                    lista[i][j].remove("")
            game[j] = lista[i][j]
            game["qtd"] = 1
        games.append(game)
    for i in range(len(games)):
        qtdGanhadores = numerosIguais(games[i][1], games[i][2])
        for j in range(games[i]["qtd"]):
            if qtdGanhadores > 0:
                for n in range(1, qtdGanhadores + 1):
                    games[i + n]["qtd"] += 1
    total = 0
    for i in range(len(games)):
        total += games[i]["qtd"]
    print(total)


# part1(txtToList())

# part2(
#     [
#         " Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
#     ]
# )

# part2(txtToList())
