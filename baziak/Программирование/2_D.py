class LampRow:
    def __init__(self, count=8):
        self._count = count
        self._state_int = 0
    @property
    def state(self):
        result = ""
        temp = self._state_int
        for _ in range(self._count):
            result = str(temp % 10) + result
            temp //= 10
        return result
    @state.setter
    def state(self, value):
        if len(value) == self._count and all(c in '012' for c in value):
            self._state_int = int(value)
        else:
            self._state_int = 0
    def show(self):
        state_str = self.state
        display = ''
        for c in state_str:
            if c == '0':
                display += '-'
            elif c == '1':
                display += '*'
            elif c == '2':
                display += 'o'
        print(display)

lamps = LampRow(6)
lamps.show()
lamps.state = "102102"
print(lamps.state)
lamps.show()
lamps.state = "10201010"
print(lamps.state)
lamps.show()
