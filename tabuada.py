print('Gerador de Tabuada\n')

tabuada = int(input('Qual número você deseja ver a tabuada? '))
incremento = 0

while incremento >= 0 and incremento < 10:
    incremento += 1
    print(f'{tabuada} x {incremento} = {tabuada*incremento}')