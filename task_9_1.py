from time import sleep


class TrafficLight:
    def __init__(self):
        self._colour = ["green", "yellow", "red"]

    def running(self):
        print(f"{self._colour[0]}")
        sleep(7)
        print(f"{self._colour[1]}")
        sleep(3)
        print(f"{self._colour[2]}")
        sleep(9)


Tr_light = TrafficLight()
Tr_light.running()
