import time


def txtToList():
    with open("Day3/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def part1(lista):
    posicoes = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if not lista[i][j].isdigit() and lista[i][j] != ".":
                for linha in range(-1, 2):
                    for coluna in range(-1, 2):
                        # print("i: ", i + linha, "j: ", j + linha)
                        if lista[i + linha][j + coluna].isdigit():
                            posicoes.append({"i": i + linha, "j": j + coluna})

    newPosicoes = []
    posicoesOrdenadas = sorted(posicoes, key=lambda x: x["j"])
    posicoes = sorted(posicoesOrdenadas, key=lambda x: x["i"])
    # print(posicoes)
    for i in range(1, len(posicoes)):
        current_position = posicoes[i]
        previous_position = posicoes[i - 1]

        if (
            previous_position["i"] == current_position["i"]
            and previous_position["j"] == current_position["j"]
            and i != len(posicoes) - 1
        ):
            pass
        elif (
            previous_position["i"] == current_position["i"]
            and previous_position["j"] + 1 == current_position["j"]
            and i != len(posicoes) - 1
        ):
            pass
        else:
            # print(current_position)
            newPosicoes.append(previous_position)
        if (
            i == len(posicoes) - 1
            and not (
                previous_position["i"] == current_position["i"]
                and previous_position["j"] == current_position["j"]
            )
            and not (
                previous_position["i"] == current_position["i"]
                and previous_position["j"] + 1 == current_position["j"]
            )
        ):
            newPosicoes.append(current_position)
    # print(newPosicoes)
    numerosValidos = []
    for i in range(len(newPosicoes)):
        coluna = newPosicoes[i]["j"]
        while True:
            if not lista[newPosicoes[i]["i"]][coluna].isdigit():
                primeiro = coluna + 1
                break
            if coluna == 0:
                primeiro = coluna
                break
            coluna -= 1
        coluna = newPosicoes[i]["j"]
        while True:
            if not lista[newPosicoes[i]["i"]][coluna].isdigit():
                ultimo = coluna - 1
                break
            if coluna == len(lista[newPosicoes[i]["i"]]) - 1:
                ultimo = coluna
                break
            coluna += 1
        valor = ""
        for n in range(primeiro, ultimo + 1):
            valor += str(lista[newPosicoes[i]["i"]][n])
        numerosValidos.append(int(valor))
    # print(numerosValidos)
    print(sum(numerosValidos))


# inicio = time.time()
# part1(txtToList())
# fim = time.time()
# print(fim - inicio)


def part2(lista):
    posicoes = []
    quadradoAdjacente = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == "*":
                for linha in range(-1, 2):
                    for coluna in range(-1, 2):
                        # print("i: ", i + linha, "j: ", j + linha)
                        if lista[i + linha][j + coluna].isdigit():
                            posicoes.append(
                                {
                                    "i": i + linha,
                                    "j": j + coluna,
                                    "qA": quadradoAdjacente,
                                }
                            )
                quadradoAdjacente += 1

    newPosicoes = []
    posicoesOrdenadas = sorted(posicoes, key=lambda x: x["j"])
    posicoes = sorted(posicoesOrdenadas, key=lambda x: x["i"])
    # print(posicoes)
    for i in range(1, len(posicoes)):
        current_position = posicoes[i]
        previous_position = posicoes[i - 1]

        if (
            previous_position["i"] == current_position["i"]
            and previous_position["j"] == current_position["j"]
            and i != len(posicoes) - 1
        ):
            pass
        elif (
            previous_position["i"] == current_position["i"]
            and previous_position["j"] + 1 == current_position["j"]
            and i != len(posicoes) - 1
        ):
            pass
        else:
            newPosicoes.append(previous_position)
        if (
            i == len(posicoes) - 1
            and not (
                previous_position["i"] == current_position["i"]
                and previous_position["j"] == current_position["j"]
            )
            and not (
                previous_position["i"] == current_position["i"]
                and previous_position["j"] + 1 == current_position["j"]
            )
        ):
            newPosicoes.append(current_position)
    print(newPosicoes)
    numerosValidos = {}
    for i in range(len(newPosicoes)):
        coluna = newPosicoes[i]["j"]
        while True:
            if not lista[newPosicoes[i]["i"]][coluna].isdigit():
                primeiro = coluna + 1
                break
            if coluna == 0:
                primeiro = coluna
                break
            coluna -= 1
        coluna = newPosicoes[i]["j"]
        while True:
            if not lista[newPosicoes[i]["i"]][coluna].isdigit():
                ultimo = coluna - 1
                break
            if coluna == len(lista[newPosicoes[i]["i"]]) - 1:
                ultimo = coluna
                break
            coluna += 1
        valor = ""
        for n in range(primeiro, ultimo + 1):
            valor += str(lista[newPosicoes[i]["i"]][n])

        if str(newPosicoes[i]["qA"]) not in numerosValidos:
            numerosValidos[str(newPosicoes[i]["qA"])] = [int(valor)]
        else:
            numerosValidos[str(newPosicoes[i]["qA"])].append(int(valor))

    print(numerosValidos)
    soma = 0
    for key in numerosValidos:
        if len(numerosValidos[key]) == 2:
            soma += numerosValidos[key][0] * numerosValidos[key][1]
    print(soma)


part2(txtToList())
