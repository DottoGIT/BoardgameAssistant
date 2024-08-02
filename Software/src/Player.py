class Player():
    """
    Klasa tzymająca podstawowe informacje o graczu
    """
    def __init__(self, name, resources=None):
        if not name:
            raise ValueError("Gracz musi mieć imie")
        self.name = name
        self.resources = [] if not resources else resources

    def get_resource(self, resource: str):
        """
        Returns a specific resource
        """
        for res in self.resources:
            if res.name == resource:
                return res.value
        return None

    def get_resource_object(self, resource: str):
        for res in self.resources:
            if res.name == resource:
                return res
        return None

    def __str__(self):
        res_to_str = ""
        for res in self.resources:
            res_to_str += f"{res.name}:{res.value} \n"
        return f"{self.name}: \n[ \n{res_to_str}] "

    def add_resource(self, resource: str, amount: int):
        self.get_resource_object(resource).add_amount(amount)

    def set_resource(self, resource: str, amount: int):
        self.get_resource_object(resource).set_amount(amount)
#  to sie importuje w Hardware.game wiec jak cos zmienisz to mow
