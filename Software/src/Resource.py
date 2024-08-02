class Resource():
    """
    Klasa trzymająca podstawowe informacje o zasobie w grze
    """
    def __init__(self, name, start_value, min_value, max_value, current_value=None):
        if not name:
            raise ValueError("Nazwa surowca nie może być pusta")
        if not min_value < max_value:
            raise ValueError("Nieprawidłowy zakres wartości surowca")
        if not min_value <= start_value <= max_value:
            raise ValueError("Wartość początkowa surowca jest poza przedziałem")
        self.name = name
        self.value = start_value if not current_value else current_value
        self.start_value = start_value
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f"{self.name}:{self.value} [{self.min_value};{self.max_value}]"

    def add_amount(self, amount):
        """
        changes the resource's value by a given amount
        will set to max_value or min_value if new_value is out of range
        will be triggedred when an "add" command is received
        """
        new_value = amount + self.value
        if new_value >= self.min_value and new_value <= self.max_value:
            self.value += amount
        elif new_value < self.min_value:
            self.value = self.min_value
        else:
            self.value = self._max_value

    def set_amount(self, amount):
        """
        sets the resource's value to a given amount
        """
        if amount >= self.min_value and amount <= self.max_value:
            self.value = amount
        elif amount < self.min_value:
            self.value = self.min_value
        else:
            self.value = self.max_value