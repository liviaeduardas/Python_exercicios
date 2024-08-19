# tabuada

i = 0
while True:
    n = int(input('Qual tabuada você deseja:'))
    if n < 0:
        break
    while i <= 10:
        print(f'{n} x {i} = {n * i}')
        i += 1
    i = 0
   
