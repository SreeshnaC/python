class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(self.cpu)
        print(self.ram)
Com1=Computer('i5',16)
Com1.config()
Com2=Computer('i7',18)
Com2.config()
