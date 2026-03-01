class lamprow:
    def __init__(self, count=8):
        self.count = count
        self._state = "0" * count
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        if len(value) == self.count:
            self._state = value
        else:
            self._state = "0" * self.count
    def show(self):
        display = ""
        for ch in self._state:
            if ch == "0":
                display += "-"
            else:
                display += "*"
        print(display)
lamps = lamprow(6)
lamps.show()
lamps.state = "101010"
print(lamps.state)
lamps.show()
lamps.state = "10101010"
print(lamps.state)