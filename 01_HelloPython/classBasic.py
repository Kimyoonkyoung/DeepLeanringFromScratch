class Man:
    def __init__(self, name):
        self.name = name
        print("initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")


m = Man("kimyoonkyoung")
m.hello()
m.goodbye()
