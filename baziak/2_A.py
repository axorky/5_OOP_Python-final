class lamprow:
    def __init__(self):
        self._state = "00000000"
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        if len(value) == 8:
            self._state = value
        else:
            self._state = "00000000"
    def show(self):
        display = ""
        for ch in self._state:
            if ch == "0":
                display += "-"
            else:
                display += "*"
        print(display)
lamps = lamprow()
lamps.show()
lamps.state = "10101010"
print(lamps.state)
lamps.show()