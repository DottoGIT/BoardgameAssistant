from Template import Template
from Resource import Resource
from Player import Player
from ApplicationManager import ApplicationManager
from pytest import raises

# APPLICATION_MANAGER TESTS


def test_ApplicationManager_Valid():
    app_manag = ApplicationManager([Template("test"), Template("test2")])
    assert app_manag.get_templates()[0].get_name() == "test"
    assert app_manag.get_templates()[1].get_name() == "test2"


def test_ApplicationManager_Add_Template():
    app_manag = ApplicationManager()
    assert len(app_manag.get_templates()) == 0
    app_manag.add_template(Template("1"))
    assert len(app_manag.get_templates()) == 1
    assert app_manag.get_templates()[0].get_name() == "1"


def test_ApplicationManager_Delete_Template():
    app_manag = ApplicationManager([Template("1"), Template("2"), Template("3")])
    assert len(app_manag.get_templates()) == 3
    app_manag.delete_template("2")
    assert len(app_manag.get_templates()) == 2
    assert app_manag.get_templates()[0].get_name() == "1"
    assert app_manag.get_templates()[1].get_name() == "3"


def test_ApplicationManager_Check_If_Template_Exists():
    app_manag = ApplicationManager([Template("1"), Template("2"), Template("3")])
    assert app_manag.check_if_template_exists("1") is True
    assert app_manag.check_if_template_exists("4") is False


def test_ApplicationManager_Delete_Template_Invalid():
    app_manag = ApplicationManager([Template("1"), Template("2"), Template("3")])
    with raises(ValueError):
        app_manag.delete_template("4")


# TEMPLATE TESTS


def test_Template_Valid():
    temp = Template("test")
    assert temp.get_name() == "test"
    assert temp.get_resources() == []
    temp2 = Template("test2", [Resource("drewno", 0, 0, 100), Resource("stal", 0, 0, 200)])
    assert temp2.get_name() == "test2"
    assert temp2.get_resources()[0].get_name() == "Drewno"
    assert temp2.get_resources()[1].get_name() == "Stal"


def test_Template_Invalid():
    with raises(ValueError):
        Template("")


# RESOURCE TESTS


def test_Resource_valid():
    resource = Resource("drewno", 0, 0, 100)
    assert resource.get_name() == "Drewno"
    assert resource.get_max_value() == 100
    assert resource.get_min_value() == 0
    assert resource.get_start_value() == 0
    assert resource.get_value() == 0


def test_Resource_invalid():
    with raises(ValueError):
        Resource("", 0, 0, 100)
    with raises(ValueError):
        Resource("drewno", 200, 0, 100)
    with raises(ValueError):
        Resource("drewno", 0, 100, 0)


# PLAYER TESTS


def test_Player_valid():
    plr = Player("dawid", [Resource("drewno", 0, 0, 100), Resource("stal", 0, 0, 100)])
    assert plr.get_name() == "Dawid"
    assert plr.get_resources()[0].get_name() == "Drewno"
    assert plr.get_resources()[1].get_name() == "Stal"


def test_Player_invalid():
    with raises(ValueError):
        Player("", [Resource("drewno", 0, 0, 100), Resource("stal", 0, 0, 100)])
