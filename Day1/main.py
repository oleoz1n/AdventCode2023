def txtToList():
    with open('Day1/input.txt') as f:
        return f.readlines()

def part1(lista):
    numeros = []
    for i in range(len(lista)):
        primeiroAchado = False
        for n in lista[i]:
            try:
                if n.isdigit() and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = n
                    ultimo = n
                elif n.isdigit():
                    ultimo = n
            except:
                continue
        numeros.append(int(primeiro+ultimo))
    print(sum(numeros))

def part2(lista):
    numeros = []
    for i in range(len(lista)):
        primeiroAchado = False
        for n in range(len(lista[i])):
            try:
                if lista[i][n].isdigit() and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = lista[i][n]
                    ultimo = lista[i][n]
                    
                elif lista[i][n] == 'o' and lista[i][n+1] == 'n' and lista[i][n+2] == 'e' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '1'
                    ultimo = '1'
                
                elif lista[i][n] == 't' and lista[i][n+1] == 'w' and lista[i][n+2] == 'o' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '2'
                    ultimo = '2'
                    
                elif lista[i][n] == 't' and lista[i][n+1] == 'h' and lista[i][n+2] == 'r' and lista[i][n+3] == 'e' and lista[i][n+4] == 'e' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '3'
                    ultimo = '3'
                    
                elif lista[i][n] == 'f' and lista[i][n+1] == 'o' and lista[i][n+2] == 'u' and lista[i][n+3] == 'r' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '4'
                    ultimo = '4'
                    
                elif lista[i][n] == 'f' and lista[i][n+1] == 'i' and lista[i][n+2] == 'v' and lista[i][n+3] == 'e' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '5'
                    ultimo = '5'
                    
                elif lista[i][n] == 's' and lista[i][n+1] == 'i' and lista[i][n+2] == 'x' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '6'
                    ultimo = '6'
                
                elif lista[i][n] == 's' and lista[i][n+1] == 'e' and lista[i][n+2] == 'v' and lista[i][n+3] == 'e' and lista[i][n+4] == 'n' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '7'
                    ultimo = '7'
                
                elif lista[i][n] == 'e' and lista[i][n+1] == 'i' and lista[i][n+2] == 'g' and lista[i][n+3] == 'h' and lista[i][n+4] == 't' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '8'
                    ultimo = '8'
                    
                elif lista[i][n] == 'n' and lista[i][n+1] == 'i' and lista[i][n+2] == 'n' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '9'
                    ultimo = '9'
                    
                elif lista[i][n] == 'z' and lista[i][n+1] == 'e' and lista[i][n+2] == 'r' and lista[i][n+3] == 'o' and not primeiroAchado:
                    primeiroAchado = True
                    primeiro = '0'
                    ultimo = '0'
                    
                elif lista[i][n].isdigit():
                    ultimo = lista[i][n]
                    
                elif lista[i][n] == 'o' and lista[i][n+1] == 'n' and lista[i][n+2] == 'e':
                    ultimo = '1'
                
                elif lista[i][n] == 't' and lista[i][n+1] == 'w' and lista[i][n+2] == 'o':
                    ultimo = '2'
                    
                elif lista[i][n] == 't' and lista[i][n+1] == 'h' and lista[i][n+2] == 'r' and lista[i][n+3] == 'e' and lista[i][n+4] == 'e':
                    ultimo = '3'
                    
                elif lista[i][n] == 'f' and lista[i][n+1] == 'o' and lista[i][n+2] == 'u' and lista[i][n+3] == 'r':
                    ultimo = '4'
                    
                elif lista[i][n] == 'f' and lista[i][n+1] == 'i' and lista[i][n+2] == 'v' and lista[i][n+3] == 'e':
                    ultimo = '5'
                    
                elif lista[i][n] == 's' and lista[i][n+1] == 'i' and lista[i][n+2] == 'x':
                    ultimo = '6'
                
                elif lista[i][n] == 's' and lista[i][n+1] == 'e' and lista[i][n+2] == 'v' and lista[i][n+3] == 'e' and lista[i][n+4] == 'n':
                    ultimo = '7'
                
                elif lista[i][n] == 'e' and lista[i][n+1] == 'i' and lista[i][n+2] == 'g' and lista[i][n+3] == 'h' and lista[i][n+4] == 't':
                    ultimo = '8'
                    
                elif lista[i][n] == 'n' and lista[i][n+1] == 'i' and lista[i][n+2] == 'n':
                    ultimo = '9'
                    
                elif lista[i][n] == 'z' and lista[i][n+1] == 'e' and lista[i][n+2] == 'r' and lista[i][n+3] == 'o':
                    ultimo = '0'
            except:
                continue
        numeros.append(int(primeiro+ultimo))
    print(sum(numeros))
    
part2(txtToList())