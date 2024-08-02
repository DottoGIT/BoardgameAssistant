"""Joystick module"""
from machine import Pin, ADC

class Joystick:
    """Joystick class"""
    def __init__(self, xpin, ypin, sens=150):
        self.x_int = ADC(Pin(xpin))
        self.x_int.atten(ADC.ATTN_11DB)
        self.y_int = ADC(Pin(ypin))
        self.y_int.atten(ADC.ATTN_11DB)
        self.ready = True  # zeby przycisk trwal jedna klatke
        self.sens = sens
        self.state = ''

    def get_input(self):  # stan - w ktora strone jest przesuniety
        """Return the state (direction) of the joystick"""
        sta = ''
        mid = 1820  # srodek joysticka, czyli int zwracany w pozycji domyslnej

        if self.y_int.read() > mid + self.sens:
            sta = 'up'
        elif self.y_int.read() < mid - self.sens:
            sta = 'down'
        elif self.x_int.read() > mid + self.sens:
            sta = 'right'
        elif self.x_int.read() < mid - self.sens:
            sta = 'left'
        else:
            sta = ''

        if self.ready and sta != '':
            self.ready = False
        elif not self.ready:
            if sta == '':
                self.ready = True
            sta = ''
        self.state = sta
