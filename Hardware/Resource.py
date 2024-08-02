class Resource():
    def __init__(self, name, start_value, min_value, max_value):
        if not name:
            raise ValueError("Nazwa surowca nie może być pusta")
        if not min_value < max_value:
            raise ValueError("Nieprawidłowy zakres wartości surowca")
        if not min_value <= start_value <= max_value:
            raise ValueError("Wartość początkowa surowca jest poza przedziałem")
        self._name = name
        self._value = start_value
        self._start_value = start_value
        self._min_value = min_value
        self._max_value = max_value

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_min_value(self):
        return self._min_value

    def get_max_value(self):
        return self._max_value

    def get_start_value(self):
        return self._start_value

    def add_amount(self, amount):
        """
        changes the resource's value by a given amount
        will set to max_value or min_value if new_value is out of range
        will be triggedred when an "add" command is received
        """
        new_value = amount + self._value
        if new_value >= self._min_value and new_value <= self._max_value:
            self._value += amount
            return amount
        elif new_value < self._min_value:
            self._value = self._min_value
            return 0
        else:
            self._value = self._max_value
            return 0

    def set_amount(self, amount):
        """
        sets the resource's value to a given amount
        """
        if amount >= self._min_value and amount <= self._max_value:
            self._value = amount
        elif amount < self._min_value:
            self._value = self._min_value
        else:
            self._value = self._max_value