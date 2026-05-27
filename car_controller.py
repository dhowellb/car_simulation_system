# Part 1: Gawa ulit tayo ng blueprint, ngayon naman para sa Car. Set up na natin yung constructor kung saan ilalagay natin yung year model at make. Siyempre, nakaparada muna kaya zero ang speed.
class Car:
    def __init__(self, car_year_model, car_make):
        self.__year_model = car_year_model
        self.__make = car_make
        self.__speed = 0

        # Part 2: Kailangan nating umarangkada! Ito yung accelerate method natin. Kada tapak sa silinyador, dagdag 5 sa speed natin. Vroom vroom!
    def accelerate(self):
        self.__speed += 5

        # Part 3: Siyempre bawal puro harurot, baka mabangga. Gawa tayo ng preno. Kada apak sa brake, babawas ng 5 yung speed natin para iwas disgrasya.
    def brake(self):
        self.__speed -= 5

        # Part 4: Kailangan din natin ng speedometer para malaman kung nahuhuli na tayo sa speed limit. Eto yung getter natin para masilip yung current speed natin.
    def get_speed(self):
        return self.__speed