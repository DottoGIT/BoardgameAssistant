from random import randint

class Dice():
    """ Klasa odpowiedzialna za zwracanie wyniku rzutu """
    def __init__(self, walls, throws):
        self.throws = throws
        self.walls = walls

    def generate_result(self):
        """ Zwraca rzuty w postaci listy """
        results = []
        for throw in range(self.throws):
            results.append(randint(1, self.walls))
        return results

    def __str__(self):
        return f"d{self.walls}x{self.throws}"