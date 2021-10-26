class Bus:
    def __init__(self, init_route, init_destination):
        self.route_number = init_route
        self.destination = init_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.extend(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def pick_up(self, person):
        self.passengers.append(person)

    