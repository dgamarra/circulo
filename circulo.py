class Circulo:
    PI = 3.1416

    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return 2 * self.PI * self.radio

    def area(self):
        return self.PI * self.radio * self.radio


if __name__ == "__main__":
    instamcia_ciculo = Circulo(10)
    print(f"La circunferencia es: {instamcia_ciculo.circunferencia()}")
    print(f"El area es: {instamcia_ciculo.area()}")
