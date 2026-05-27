# Part 1: Gawa ulit tayo ng blueprint, ngayon naman para sa Car. Set up na natin yung constructor kung saan ilalagay natin yung year model at make. Siyempre, nakaparada muna kaya zero ang speed.
class Car:
    def __init__(self, car_year_model, car_make):
        self.__year_model = car_year_model
        self.__make = car_make
        self.__speed = 0

        # Part 2: Kailangan nating umarangkada! Ito yung accelerate method natin. Kada tapak sa silinyador, dagdag 5 sa speed natin. Vroom vroom!
    def accelerate(self):
        self.__speed += 5