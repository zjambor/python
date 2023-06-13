import time

class Vehicle:
    def change_direction(self, left, on):
        pass

    def turn(self, left):
        self.change_direction(left, True)
        time.sleep(0.25)
        self.change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(self, left, stop):
        print("tracks: ", left, stop)

    def change_direction(self, left, on):
        self.control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(self, left, on):
        print("wheeled: ", left, on)

    def change_direction(self, left, on):
        self.turn_front_wheels(left, on)

track = TrackedVehicle()
track.change_direction("Left", True)

wheeled = WheeledVehicle()
wheeled.change_direction("Right", True)
