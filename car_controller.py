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
    
    # Part 5: Para mas maangas ang output natin mamaya at hindi lang number, gumawa ako ng custom display dashboard. Ipapakita nito yung kotse natin, ano ginagawa, at yung bilis.
    def display_speedometer(self, action_message):
        print(f"| {action_message.upper()} | 🏎️  {self.__year_model} {self.__make} | Current Speed: {self.__speed} km/h")

        # Part 6: Start na ng road test! Gagawa tayo ng kotse natin (isang 2025 Mustang) tapos aapakan natin ang gas nang limang beses gamit ang for loop.
def test_car_program():
    print("\n[ STARTING CAR ENGINE... ]\n")
    
    my_sports_car = Car("2025", "Ford Mustang")
    
    print("--- 🟢 ACCELERATING PHASE ---")
    for loop_count in range(5):
        my_sports_car.accelerate()
        my_sports_car.display_speedometer("Accelerating")

        # Part 7: Tapos na ang joyride, kailangan na pumreno dahil may humps. Apak sa brake limang beses hanggang sa huminto, tapos i-run na natin ang buong script!
    print("\n--- 🔴 BRAKING PHASE ---")
    for loop_count in range(5):
        my_sports_car.brake()
        my_sports_car.display_speedometer("Braking     ")
        

if __name__ == "__main__":
    test_car_program()