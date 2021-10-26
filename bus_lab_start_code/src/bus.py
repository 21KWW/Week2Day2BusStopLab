class Bus:
    def __init__(self, init_route, init_destination):
        self.route_number = init_route
        self.destination = init_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def pick_up(self, person):
        self.passengers.append(person)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        self.passengers.extend(bus_stop.queue)
        bus_stop.clear()
