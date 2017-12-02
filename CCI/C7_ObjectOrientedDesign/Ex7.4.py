import datetime
from queue import deque

class ParkingLot():
    def __init__(self, size, rate):
        self.lots = []
        self.rate = rate

        for i in range(size):
            self.lots.append(Park(i))
        self.availble = deque(self.lots)

    def park(self, car):
        park = self.available.popleft()
        park.park(car)

    def leave(self, car):
        park = car.get_park()
        time = park.leave()
        charge = math.ceil(time) * self.rate
        self.available.append(park)
        return charge

class Car():
    def __init__(self):
        self.park_index = None

    def get_park(self):
        return self.park_index

    def set_park(self, index):
        self.park_index = index

class Park():
    def __init__(self, index):
        self.is_available = True
        self.index = index

    def park(self, car):
        self.is_available = False
        car.set_park(self.index)
        self.start_time = datetime.datetime.now()

    def leave(self):
        self.is_available = True
        return datetime.datetime.now() - self.start_time
