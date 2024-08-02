from machine import Pin, SoftI2C
import ssd1306
# ESP32 Pin assignment


class Oled:
    def __init__(self) -> None:
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        oled_width = 128
        oled_height = 64
        self.oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
        self.page1_resources = []
        self.page2_resources = []
        self.menu_options = []
        self.selected_option = 1

    def reset_display(self):
        self.oled.fill(0)
        self.menu_options = []

    def show_display(self):
        self.oled.show()

    def display_menu(self):
        self.reset_display()
        self.menu_options = [0, 1, 2]
        self.oled.text("1. Rzut kostka", 0, 0)
        self.oled.text('2. Statystyki', 0, 10)
        self.oled.text('3. Koniec tury', 0, 20)
        self.show_display()

    def display_dice_result(self, dices):
        self.reset_display()
        i = 1
        x = 1
        y = -9
        self.menu_options = [0, 1]
        for dice in dices:
            if i % 2 == 1:
                x = 1
                y += 10
            else:
                x = 64
            self.oled.text(f'{i}. {dice}', x, y)
            i += 1
        sum_of_dices = sum(dices)
        y += 10
        self.oled.text(f'Sum: {sum_of_dices}', 45, y)
        self.oled.text('Roll again?', 0, y+10)
        self.show_display()

    def display_list_of_players(self, players):
        self.reset_display()
        i = 0
        self.menu_options = []
        for player in players:
            self.menu_options.append(i)
            self.oled.text(f'{i+1}.{player.get_name()}', 0, 10*i)
            i += 1
        self.show_display()

    def display_player_resources(self, player, selected=False):
        player_resources = player.get_resources()
        self.reset_display()
        i = 0
        resources = []
        self.menu_options = range(len(player_resources))
        for resource_name in player_resources:
            resources.append((resource_name, player_resources[resource_name]))
        if len(player_resources) > 5:
            first_resources = resources[:5]
            second_resources = resources[5:]
            self.page2_resources = second_resources
            self.page1_resources = first_resources
            self.oled.text("Show more", 90, 30)
        else:
            first_resources = resources

        for resource_name, resource in first_resources:
            if i == self.selected_option and selected == True:
                self.oled.text(f'{resource.get_name()}:   {resource.get_value()}', 0, 10*i)
            else:
                self.oled.text(f'{resource.get_name()}: {resource.get_value()}', 0, 10*i)
            i += 1
        self.oled.text(player.get_name(), 0, 55)
        self.show_display()

    def move_cursor(self, joystick_direction):
        # yyy nie wiem jakie wartosci zwraca joystick w ktora strone
        if (joystick_direction == "up" and self.selected_option > 0):
            self.selected_option -= 1
        elif (joystick_direction == "down" and self.selected_option < len(self.menu_options) - 1):
            self.selected_option += 1
        self.oled.text("|", 110, self.selected_option*10)
        self.oled.show()
