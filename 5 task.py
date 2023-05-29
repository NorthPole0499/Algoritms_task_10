class ThreeStack:
    def __init__(self):
        self.data = [0, 0, 0]
        self.index = 1

    def get_1(self):
        num = self.data[0]
        if num != 0:
            self.data = self.data[1:]
            self.index -= 1
            return num
        else:
            return None

    def add_1(self, num):
        self.data = [num] + self.data
        self.index += 1

    def get_3(self):
        num = self.data[-1]
        if num != 0:
            self.data = self.data[:-1]
            return num
        else:
            return None

    def add_3(self, num):
        self.data.append(num)

    def get_2(self):
        num = self.data[self.index - 1]
        if num != 0:
            del self.data[self.index - 1]
            self.index -= 1
            return num
        else:
            return None

    def add_2(self, num):
        self.data.insert(self.index - 1, num)
        self.index += 1
