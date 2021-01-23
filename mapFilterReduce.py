from functools import reduce

lista = [1,3,-1,15,9]

listaDobles = map(lambda x: x*2, lista)
print(list(listaDobles))

listaPares = filter(lambda x: x % 2 == 0, lista)
print(list(listaPares))

listaMultiploTres = filter(lambda x: x % 3 == 0, lista)

print(list(listaMultiploTres))

def doble(x):
    return x+x

listaDobles2 = map(doble,lista)
print(list(listaDobles2))

def esPar(x):
    return x % 2 == 0

listaPares2 = filter(esPar,lista)
print(list(listaPares2))

sumatorio = reduce(lambda x, y: x + y, lista)
print(sumatorio)

suma100 = reduce(lambda x, y: x + y, range(101))
print(suma100)

sumatorioDobles = reduce(lambda x, y: x + y*2, lista)
print(sumatorioDobles)
#ojo el primer dato (1) no lo multiplica por 2, solo los datos que coje la y