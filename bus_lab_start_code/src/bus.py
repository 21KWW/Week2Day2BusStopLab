class Bus:
    def __init__(self):
        route_num = 22
        destination = "Ocean Terminal"
        passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.extend(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    