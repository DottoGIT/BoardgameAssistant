class Template():
    """
    Klasa trzymająca informacje o szablonie stworzonym przez użytkownika
    """
    def __init__(self, name, resources, dice):
        if not name:
            raise ValueError("Template must have a name")
        self.name = name
        self.resources = resources
        self.dice = dice
        self.resource_amount = len(resources)

    def __str__(self):
        end_str = f"Nazwa: {self.name} Kość: {str(self.dice)} Zasoby: \n[ \n"
        for res in self.resources:
            end_str += str(res) + "\n"
        end_str += "]"
        return end_str
