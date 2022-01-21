class DigitalCounter:
    counter = 0

    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.counter = min

    def overflow(self):
        if self.counter < self.max:
            self.counter += 1
            return f"Счетчик увеличен до {self.counter}."
        else:
            return "Значение счетчика вне допустимого диапазона!"
        pass

    def show_counter_value(self):
        return f"Значение счетчика:\n{self.counter}"

    def reset_to_minimum(self):
        self.counter = self.min
        return "Значение счетчика сведено к минимуму."


if __name__ == '__main__':
    c = DigitalCounter(2, 5)
    print(c.show_counter_value())
    print(c.overflow())
    print(c.overflow())
    print(c.overflow())
    print(c.overflow())
    print(c.overflow())
    # Смотрим значение счетчика
    print(c.show_counter_value())
    # Сброс до минимума
    c.reset_to_minimum()
    # Значение счетчика после сброса
    print(c.show_counter_value())
