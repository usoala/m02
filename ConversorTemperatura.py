class Termometro():
    def __init__(self):
        self.__unidadM = "C"
        self.__temperatura = 0
        
    def __conversor(self, temperatura, unidad):
        if unidad == "C":
            return "{:.0f}ºF".format(temperatura * 9/5 + 32)
        elif unidad =="F":
            return "{:.2f}ºC".format(round((temperatura-32) *5/9,2))
        else:
            return "unidad incorrecta"
        
    def __str__(self):
        return "{}º{}".format(self.__temperatura, self.__unidadM)
        
    def uniM(self,uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM =="C":
               self.__unidadM = uniM
               
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM=None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura,self.__unidadM)
        
t = Termometro()

t.uniM("C")
t.temp(0)
print(t.mide())
print(t.mide("F"))
t.uniM("F")
t.temp(32)
print(t.mide())
print(t.mide("C"))