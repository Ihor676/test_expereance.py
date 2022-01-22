class Buffer:
    def __init__(self):
        self.buffer = []
        self.five = []

    def add(self, *a):
        self.buffer.extend(a)
        while self.buffer:
            if len(self.buffer) >= 5:
                self.five = self.buffer[0:5]
                del self.buffer[0:5]
                self.get_current_part()
            elif len(self.buffer) < 5:
                break

    def get_current_part(self):
        print(sum(self.five))
        self.five = []


if __name__ == '__main__':
    x = Buffer()
    x.add(5, 5, 5, 5, 5, 6, 6)
    x.add(6, 6, 6, 7, 7)
    x.add(7, 7, 7)
    x.add(10, 5, 7, 8, 12, 45, 78, 83, 32, 35, 778)
    x.add(12, 15, 56, 13.56)
