class Player():
    def __init__(self, name, resources={}):
        if not name:
            raise ValueError("Gracz musi mieć imie")
        if not resources:
            raise ValueError("Gracz musi mieć zasoby")
        self._name = name
        self._my_resources = resources

    def get_name(self):
        return self._name

    def get_resources(self):
        return self._my_resources

    def get_resource(self, resource: str):
        """
        Returns a specific resource
        """
        return self._my_resources[resource]

    def add_resource(self, resource: str, amount: int):
        self._my_resources[resource].add_amount(amount)

    def set_resource(self, resource: str, amount: int):
        self._my_resources[resource].set_amount(amount)
