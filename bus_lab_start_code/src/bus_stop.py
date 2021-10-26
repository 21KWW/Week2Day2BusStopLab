class BusStop:
    def __init__(self, init_name):
        self.name = init_name
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person):
        self.queue.append(person)

    def clear(self):
        self.queue.clear()

    