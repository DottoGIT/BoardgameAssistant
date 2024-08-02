from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PySide2.QtCore import QTimer
from ui_MainWindow import Ui_MainWindow
from ApplicationManager import ApplicationManager
from DebugWindow import DebugWindow
from Template import Template
from Dice import Dice
from Resource import Resource
import sys


class MainWindow(QMainWindow):
    """
    Klasa która zarządza działaniem aplikacji okienkowej
    """

    def __init__(self, app_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # Variables used in layouts

        self.currently_shown_player_stats = 0  # ZRESETOWAĆ TE ZMEINNĄ ZAWSZE JAK ODPALAMY\WCZYTUJEMY NOWĄ GRĘ

        # Usefull Functions

        def load_template_list():
            templates = app_manager.saved_tamplates
            self.ui.TemplatesList.clear()
            for temp in templates:
                item = QListWidgetItem(temp.name)
                self.ui.TemplatesList.addItem(item)

        def load_saves_list():
            saves = app_manager.saved_games
            self.ui.SavesList.clear()
            for save in saves:
                item = QListWidgetItem(save.date)
                self.ui.SavesList.addItem(item)

        def load_command_logs():
            logs = app_manager.current_game.command_log[::-1]
            self.ui.CommandLogs.clear()
            for log in logs:
                item = QListWidgetItem(log)
                self.ui.CommandLogs.addItem(item)

        def show_pop_up_window(text, title="Błąd"):
            msg = QMessageBox()
            msg.setWindowTitle(title)
            msg.setText(text)
            msg.exec_()

        # Main loop

        def Update():
            app_manager.update()
            if app_manager.value_changed:
                Game_Update_Values()
                app_manager.value_changed = False

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: Update())
        self.timer.start(1)  # Ta liczba w środku to milisekundy co ile ma się wykonywać Update

        # Main Menu Layout

        def BtnStartGame_Function():
            load_template_list()
            self.ui.stackedWidget.setCurrentIndex(1)

        def BtnLoadGame_Function():
            load_saves_list()
            self.ui.stackedWidget.setCurrentIndex(4)

        def BtnCreateTemplate_Function():
            self.ui.TempCreation_name.setText("")
            self.ui.stackedWidget.setCurrentIndex(3)

        self.ui.BtnStartGame.clicked.connect(BtnStartGame_Function)
        self.ui.BtnLoadGame.clicked.connect(BtnLoadGame_Function)
        self.ui.BtnCreateTemplate.clicked.connect(BtnCreateTemplate_Function)

        # Create Template Layout

        def BtnCreate_CreateTemplate_Function():
            if Can_create_template():
                temp_name = self.ui.TempCreation_name.toPlainText()
                temp_resources = create_resources()
                temp_dice = create_dice()
                createdTemplate = Template(temp_name, temp_resources, temp_dice)
                app_manager.add_template(createdTemplate)
                self.ui.stackedWidget.setCurrentIndex(0)

        def BtnReturn_CreateTemplate_Function():
            self.ui.stackedWidget.setCurrentIndex(0)

        def TxtEdit_on_value_change_numberOfResources():
            ''' This function hides And shows Resource textBoxes depending on given value in "number_of_resources" '''
            if self.ui.number_of_resources.toPlainText() != "":
                if not self.ui.number_of_resources.toPlainText().isnumeric() \
                    or int(self.ui.number_of_resources.toPlainText()) < 0 or int(self.ui.number_of_resources.toPlainText()) > 10:
                    show_pop_up_window("Należy podać liczbę z przedziału 0-10")
                    return
            how_many_to_show = 0 if self.ui.number_of_resources.toPlainText() == "" else int(self.ui.number_of_resources.toPlainText())
            # Hide elements
            for res in range(10, how_many_to_show, -1):
                eval(f"self.ui.res{res}_name.setVisible(False)", {"self": self})
                eval(f"self.ui.res{res}_min.setVisible(False)", {"self": self})
                eval(f"self.ui.res{res}_max.setVisible(False)", {"self": self})
                eval(f"self.ui.res{res}_curr.setVisible(False)", {"self": self})
                for element in range(1, 5):
                    eval(f"self.ui.res{res}_l{element}.setVisible(False)", {"self": self})
                    eval(f"self.ui.res{res}_l{element}.setVisible(False)", {"self": self})
            # Show elements
            for res in range(1, how_many_to_show + 1):
                eval(f"self.ui.res{res}_name.setVisible(True)", {"self": self})
                eval(f"self.ui.res{res}_min.setVisible(True)", {"self": self})
                eval(f"self.ui.res{res}_max.setVisible(True)", {"self": self})
                eval(f"self.ui.res{res}_curr.setVisible(True)", {"self": self})
                for element in range(1, 5):
                    eval(f"self.ui.res{res}_l{element}.setVisible(True)", {"self": self})
                    eval(f"self.ui.res{res}_l{element}.setVisible(True)", {"self": self})

        def Dice_settings_set_active():
            if int(self.ui.dice_checkBox.checkState()) == 0:
                self.ui.dice_l1.setEnabled(False)
                self.ui.dice_l2.setEnabled(False)
                self.ui.dice_walls.setEnabled(False)
                self.ui.dice_throws.setEnabled(False)
            else:
                self.ui.dice_l1.setEnabled(True)
                self.ui.dice_l2.setEnabled(True)
                self.ui.dice_walls.setEnabled(True)
                self.ui.dice_throws.setEnabled(True)

        def Can_create_template():
            if not self.ui.TempCreation_name.toPlainText():
                show_pop_up_window("Należy wpisać nazwę szablonu!")
                return False
            if app_manager.check_if_template_exists(self.ui.TempCreation_name.toPlainText()):
                show_pop_up_window("Nazwa szablonu jest zajęta!")
                return False
            if int(self.ui.dice_checkBox.checkState()) == 2 and (not self.ui.dice_throws.toPlainText().isnumeric() or not self.ui.dice_throws.toPlainText().isnumeric()):
                show_pop_up_window("Ustawienia kostek są niepoprawne!")
                return False
            if check_if_resource_names_are_repeating():
                show_pop_up_window("Nazwy zasobów się powtarzają!")
                return False
            if not self.ui.number_of_resources.toPlainText():
                show_pop_up_window("Należy podać liczbę zasobów!")
                return False
            for index in range(1, 11):
                if eval(f"self.ui.res{index}_l1.isVisible()", {"self": self}) and (not eval(f"self.ui.res{index}_curr.toPlainText().isnumeric()",{"self":self}) or not eval(f"self.ui.res{index}_min.toPlainText().isnumeric()",{"self":self}) or not eval(f"self.ui.res{index}_max.toPlainText().isnumeric()",{"self":self}) or not eval(f"self.ui.res{index}_name.toPlainText()",{"self":self})):
                    show_pop_up_window(f"Nie wszystkie pola są uzupełnione: Zasób {index}")
                    return False
            return True

        def create_dice():
            if int(self.ui.dice_checkBox.checkState()) == 0:
                return None
            else:
                walls = int(self.ui.dice_walls.toPlainText())
                throws = int(self.ui.dice_throws.toPlainText())
                return Dice(walls, throws)

        def check_if_resource_names_are_repeating():
            resource_names = []
            for index in range(1, int(self.ui.number_of_resources.toPlainText())+1):
                resource_names.append(eval(f"self.ui.res{index}_name.toPlainText()", {"self": self}))
            name_dict = {}
            for name in resource_names:
                name_dict[name] = name_dict.get(name, 0) + 1
                if name_dict[name] > 1:
                    return True
            return False

        def create_resources():
            resources = []
            for index in range(1, int(self.ui.number_of_resources.toPlainText())+1):
                name = eval(f"self.ui.res{index}_name.toPlainText()", {"self": self})
                min = eval(f"int(self.ui.res{index}_min.toPlainText())", {"self": self})
                max = eval(f"int(self.ui.res{index}_max.toPlainText())", {"self": self})
                default = eval(f"int(self.ui.res{index}_curr.toPlainText())", {"self": self})
                resources.append(Resource(name, default, min, max))
            return resources

        self.ui.number_of_resources.setText("0")
        self.ui.BtnCreate_CreateTemplate.clicked.connect(BtnCreate_CreateTemplate_Function)
        self.ui.BtnReturn_CreateTemplate.clicked.connect(BtnReturn_CreateTemplate_Function)
        self.ui.number_of_resources.textChanged.connect(TxtEdit_on_value_change_numberOfResources)
        self.ui.dice_checkBox.stateChanged.connect(Dice_settings_set_active)

        Dice_settings_set_active()
        TxtEdit_on_value_change_numberOfResources()

        # Chose Template Layout

        def BtnReturn_ChoseTemplate_Function():
            self.ui.stackedWidget.setCurrentIndex(0)

        def BtnStart_ChoseTemplate_Function():
            """ Starts new game if possible """
            if Can_start_game():
                plr_names = get_player_names()
                template_name = self.ui.TemplatesList.currentItem().text()
                app_manager.start_new_game(plr_names, template_name)
                self.currently_shown_player_stats = 0
                Game_hide_unused_resources()
                Game_Update_Values()
                self.ui.stackedWidget.setCurrentIndex(2)

        def Btn_Delete_ChoseTemplaye_Function():
            if not self.ui.TemplatesList.currentItem():
                show_pop_up_window("Należy wybrać szablon")
                return
            app_manager.delete_template(self.ui.TemplatesList.currentItem().text())
            load_template_list()

        def Check_if_player_names_are_repeating():
            """ Sprawdza czy dwoch graczy nazywa sie tak samo """
            name_dict = {}
            for name in get_player_names():
                name_dict[name] = name_dict.get(name, 0) + 1
                if name_dict[name] > 1:
                    return True
            return False

        def TxtEdit_on_value_change_numberOfPlayers():
            ''' This function hides And shows Players textBoxes depending on given value in "num_of_players" '''
            if self.ui.num_of_players.toPlainText() != "":
                if not self.ui.num_of_players.toPlainText().isnumeric() \
                    or int(self.ui.num_of_players.toPlainText()) < 0 or int(self.ui.num_of_players.toPlainText()) > 10:
                    show_pop_up_window("Należy podać liczbę z przedziału 0-10")
                    return
            how_many_to_show = 0 if self.ui.num_of_players.toPlainText() == "" else int(self.ui.num_of_players.toPlainText())
            # Hide elements
            for plr in range(10, how_many_to_show, -1):
                eval(f"self.ui.g{plr}_l.setVisible(False)", {"self": self})
                eval(f"self.ui.name_{plr}.setVisible(False)", {"self": self})
            # Show elements
            for plr in range(1, how_many_to_show + 1):
                eval(f"self.ui.g{plr}_l.setVisible(True)", {"self": self})
                eval(f"self.ui.name_{plr}.setVisible(True)", {"self": self})

        def Can_start_game():
            if not self.ui.TemplatesList.currentItem():
                show_pop_up_window("Należy wybrać szablon")
                return False
            # checks for player names
            if Check_if_player_names_are_repeating():
                show_pop_up_window("Nazwy graczy nie mogą się powtarzać")
                return False
            for index in range(1, 11):
                if eval(f"self.ui.g{index}_l.isVisible()", {"self": self}) and not eval(f"self.ui.name_{index}.toPlainText()",{"self":self}):
                    show_pop_up_window(f"Nie wszystkie pola są uzupełnione: Gracz {index}")
                    return False
            return True

        def get_player_names():
            names = []
            for index in range(1, int(self.ui.num_of_players.toPlainText())+1):
                names.append(eval(f"self.ui.name_{index}.toPlainText()", {"self": self}))
            return names

        self.ui.BtnReturn_ChoseTemplate.clicked.connect(BtnReturn_ChoseTemplate_Function)
        self.ui.BtnStart_ChoseTemplate.clicked.connect(BtnStart_ChoseTemplate_Function)
        self.ui.BtnDelete_ChoseTemplate.clicked.connect(Btn_Delete_ChoseTemplaye_Function)
        self.ui.num_of_players.textChanged.connect(TxtEdit_on_value_change_numberOfPlayers)

        TxtEdit_on_value_change_numberOfPlayers()

        # In Game Layout

        def Game_Update_Values():
            load_command_logs()
            plr = app_manager.current_game.players[self.currently_shown_player_stats]
            self.ui.g_curr_plr.setText(plr.name)
            index = 1
            for res in plr.resources:
                eval(f"self.ui.g_res{index}.setText('{res.name}')", {"self": self})
                eval(f"self.ui.g_v_res{index}.setText('{res.value}')", {"self": self})
                index += 1

        def Game_hide_unused_resources():
            how_many_to_show = len(app_manager.current_game.template.resources)
            # Hide elements
            for plr in range(10, how_many_to_show, -1):
                eval(f"self.ui.g_res{plr}.setVisible(False)", {"self": self})
                eval(f"self.ui.g_v_res{plr}.setVisible(False)", {"self": self})
            # Show elements
            for plr in range(1, how_many_to_show + 1):
                eval(f"self.ui.g_res{plr}.setVisible(True)", {"self": self})
                eval(f"self.ui.g_v_res{plr}.setVisible(True)", {"self": self})

        def BtnNext():
            self.currently_shown_player_stats += 1
            if self.currently_shown_player_stats > len(app_manager.current_game.players)-1:
                self.currently_shown_player_stats = 0
            Game_Update_Values()

        def BtnPrevious():
            self.currently_shown_player_stats -= 1
            if self.currently_shown_player_stats < 0:
                self.currently_shown_player_stats = len(app_manager.current_game.players)-1
            Game_Update_Values()

        def BtnSave_inGame_Function():
            # proste rozwiązanie, można zmienić
            app_manager.save_game()

        def BtnReturn_InGame_Function():
            self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.BtnSave_inGame.clicked.connect(BtnSave_inGame_Function)
        self.ui.BtnReturn_InGame.clicked.connect(BtnReturn_InGame_Function)
        self.ui.g_next.clicked.connect(BtnNext)
        self.ui.g_previous.clicked.connect(BtnPrevious)

        # Load game

        def BtnReturn_LoadGame_Function():
            self.ui.stackedWidget.setCurrentIndex(0)

        def BtnDelete_Chosen_Save_Function():
            if not self.ui.SavesList.currentItem():
                show_pop_up_window("Należy wybrać zapis")
                return
            app_manager.delete_game(self.ui.SavesList.currentItem().text())
            load_saves_list()

        def BtnStart_Chosen_game_Funcion():
            self.currently_shown_player_stats = 0
            game_name = self.ui.SavesList.currentItem().text()
            app_manager.load_game(game_name)
            Game_hide_unused_resources()
            Game_Update_Values()
            self.ui.stackedWidget.setCurrentIndex(2)

        self.ui.BtnDelete_Chosen_Save.clicked.connect(BtnDelete_Chosen_Save_Function)
        self.ui.BtnReturn_LoadGame.clicked.connect(BtnReturn_LoadGame_Function)
        self.ui.BtnStart_Chosen_Game.clicked.connect(BtnStart_Chosen_game_Funcion)


def main(argv):
    app = QApplication(argv)
    app_manag = ApplicationManager()
    window = MainWindow(app_manag)
    debug_window = DebugWindow(app_manag)
    app_manag.init_app_window(window)
    window.show()
    debug_window.show()
    return app.exec_()


if __name__ == "__main__":
    main(sys.argv)
