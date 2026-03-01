class lamprow:
    def __init__(self, count=8):
        self.count = count
        self._state = "0" * count
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        if len(value) == self.count and all(ch in "012" for ch in value):
            self._state = value
        else:
            self._state = "0" * self.count
    def show(self):
        display = ""
        for ch in self._state:
            if ch == "0":
                display += "-"
            elif ch == "1":
                display += "*"
            else:
                display += "o"
        print(display)
lamps = lamprow(9)
lamps.show()
lamps.state = "102102102"
print(lamps.state)
lamps.show()
lamps.state = "10201010"
print(lamps.state)