from operator import truediv


class Samochod:
    #definicja klasy
    def __init__(self, marka, model):
        self.marka= marka
        self.model= model
        self.predkosc= 0

    def uruchom_silnik(self):
        print("silnik zostal uruchomiony")
        self.wlaczony_silnik = True

    def przyspiesz(self, wartosc):
        self.predkosc += wartosc

moj_samochod= Samochod("Toyota", "yaris")

moj_samochod_2= Samochod.__init__(any, "Toyota", "Yaris")

moj_samochod.uruchom_silnik()
moj_samochod.przyspiesz(30)

moj_samochod_2= Samochod("BMW", "M3")
print(moj_samochod_2.predkosc)