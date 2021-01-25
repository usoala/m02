class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU,GUAU")
        else:
            print("guau,guau")
            
    def ladrar2(self,c):
        if self.peso >= 8:
            print("GUAU,GUAU",c)
        else:
            print("guau,guau",c)
            
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
        
salchicho = Perro("Salchicho",3,12)
lola = Perro("Lola",8,1.5)
miko = Perro("Miko",8,3)

#print(lola)
#salchicho.ladrar()
#miko.ladrar2("dame comida")

class PerroAsistencia(Perro):
    
    def __init__(self, n, e, p, a):
        Perro. __init__(self, n, e, p)
        self.amo = a
        self.__trabajando = False
        
    def __str__(self):
        return "Perro de Asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayuda a su dueño {}".format(self.nombre,self.amo))
        
    def ladrar(self):
        if self.trabajando:
            print("shhh, no puedo ladrar")
        else:
            Perro.ladrar(self)

    def trabajando(self,valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
        
rantanplan = PerroAsistencia("Ran Tan Plan",4,8,"Lucky Luke")     

#print(rantanplan)
#rantanplan.ladrar()
#rantanplan.pasear()
#rantanplan._trabajando = True
#rantanplan.ladrar()

#print(rantanplan._PerroAsistencia__trabajando)
#print(rantanplan.trabajando())

class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def __str__(self):
        return "Dog {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
        
    def ladrar(self):
        if self.peso == None:
            print("soy un fantasma")
        elif self.peso >= 8:
            print("GUAU,GUAU")
        else:
            print("guau,guau")
            
#blacky = Dog()
#print(blacky)
#blacky.ladrar()
#blacky.nombre="Blacky"
#blacky.edad = 5
#blacky.peso = 4
#print(blacky)
#blacky.ladrar()
