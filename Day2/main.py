import re


def txtToList():
    with open("Day2/input.txt") as f:
        return f.readlines()


def part1(lista):
    games = []
    for i in range(len(lista)):
        game = re.split(r"[;,:]", lista[i])
        games.append(game)
    gamesValidos = []
    for i in range(len(games)):
        red = 0
        green = 0
        blue = 0
        for n in range(len(games[i])):
            if n == 0:
                valoresJogoAtual = ""
                for j in range(len(games[i][n])):
                    if games[i][n][j].isdigit():
                        valoresJogoAtual += games[i][n][j]
                jogoAtual = int(valoresJogoAtual)

            else:
                valoresValor = ""
                for j in range(len(games[i][n])):
                    if games[i][n][j].isdigit():
                        valoresValor += games[i][n][j]
                valor = int(valoresValor)
                if "red" in games[i][n]:
                    if valor > red:
                        red = valor
                elif "green" in games[i][n]:
                    if valor > green:
                        green = valor
                elif "blue" in games[i][n]:
                    if valor > blue:
                        blue = valor

        if red <= 12 and green <= 13 and blue <= 14:
            print("red:", red, "green:", green, "blue:", blue)
            gamesValidos.append(jogoAtual)

    print(gamesValidos)
    print(sum(gamesValidos))


def part2(lista):
    games = []
    for i in range(len(lista)):
        game = re.split(r"[;,:]", lista[i])
        games.append(game)
    gamesValidos = []
    for i in range(len(games)):
        red = 0
        green = 0
        blue = 0
        for n in range(len(games[i])):
            if n == 0:
                valoresJogoAtual = ""
                for j in range(len(games[i][n])):
                    if games[i][n][j].isdigit():
                        valoresJogoAtual += games[i][n][j]
                jogoAtual = int(valoresJogoAtual)

            else:
                valoresValor = ""
                for j in range(len(games[i][n])):
                    if games[i][n][j].isdigit():
                        valoresValor += games[i][n][j]
                valor = int(valoresValor)
                if "red" in games[i][n]:
                    if valor > red:
                        red = valor
                elif "green" in games[i][n]:
                    if valor > green:
                        green = valor
                elif "blue" in games[i][n]:
                    if valor > blue:
                        blue = valor

        print("red:", red, "green:", green, "blue:", blue)
        gamesValidos.append(red * green * blue)

    print(gamesValidos)
    print(sum(gamesValidos))


part2(txtToList())
