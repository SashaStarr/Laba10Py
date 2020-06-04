class Ship:
    number_ships = 0

    def __init__(self, name="Ferry", number_of_containers=120, water_capacity_in_Liters=2400, producer="USA",
                 lengt_in_meters=40, engine="E-32", weight_lifting_in_tons=250.0):
        self.name = name
        self.number_of_containers = number_of_containers
        self.water_capacity_in_Liters = water_capacity_in_Liters
        self.producer = producer
        self.lengt_in_meters = lengt_in_meters
        self.engine = engine
        self.weight_lifting_in_tons = weight_lifting_in_tons
        Ship.number_ships += 1

    def __del__(self):
        print("Deleted ship")

    def __str__(self):
        return ('(name:' + self.name
                + ', number of containers:' + str(self.number_of_containers)
                + ',  water capacity in Liters:' + str(self.water_capacity_in_Liters)
                + ', producer:' + self.producer
                + ", lengt in meters:" + str(self.lengt_in_meters)
                + ', engine' + self.engine
                + ', weight lifting in tons=' + str(self.weight_lifting_in_tons) + ')')

    @staticmethod
    def create_ship():
        return Ship.number_ships


def main():
    First = Ship("Boat", 1, 3, "default", 2, "-", 0.25)
    Second = Ship("Liner", 40, 500, "Italy", 50, "Ch-45", 250)
    Third = Ship("Сutter", 5, 10, "Spain", 2, "58-G", 1)

    print(First)
    print(Second)
    print(Third)

    print("Number of created ships", Ship.number_ships)


main()
