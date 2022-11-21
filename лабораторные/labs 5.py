class Rocket():
    def __init__(self, total_weight, amount_of_fuel, engine_status):      
        self.total_weight = total_weight
        self.amount_of_fuel = amount_of_fuel
        self.engine_status = engine_status
    def spend_fuel(self, count):              
        self.amount_of_fuel -= count           
        self.total_weight -= count             
        if self.amount_of_fuel <= 0:
            self.amount_of_fuel = 0
            self.engine_status = False
            return False
        elif self.amount_of_fuel > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                       
        return f'Кол-во топлива: {self.amount_of_fuel}'
    def get_total_weight(self):                                     
        return f'Общая масса: {self.total_weight}'
    def get_is_engine_running(self):                                
        return f'Состояние двигателя: {self.engine_status}'

def main():
    Roketa = Rocket(100000, 60000, True)
    while Roketa.amount_of_fuel > 0:
        Roketa.spend_fuel(6000)
        print(Roketa.get_fuel_level(), end='; ')
        print(Roketa.get_total_weight(), end='; ')
        print(Roketa.get_is_engine_running())
main()