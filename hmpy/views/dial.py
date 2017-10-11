from hmpy.views.view import View
from PyQt5.QtWidgets import QDial


class DialView(View):

    def __init__(self, value=None, min_value=0, max_value=100, notches_visible=True):
        """Initialize the DialView QWidget

        :param value: value of the dial.
        :param min_value: The minimum value.
        :param max_value: The maximum value.
        :param notches_visible: show/hide notches"""
        super().__init__()

        self.dial = QDial(self)
        self.dial.setMinimum(min_value)
        self.dial.setMaximum(max_value)

        if value is None:
            value = min_value

        self.dial.setValue(value)
        self.dial.setNotchTarget(self.width()/130.0)
        self.dial.setNotchesVisible(notches_visible)
        self.dial.setNotchesVisible(True)

    def set_on_value_changed(self, callback):
        self.dial.valueChanged.connect(callback)

    @property
    def value(self):
        return self.dial.value()

    @value.setter
    def value(self, value):
        self.dial.setValue(value)

    @property
    def min_value(self):
        return self.dial.minimum()

    @min_value.setter
    def min_value(self, value):
        self.dial.setMinimum(value)

    @property
    def max_value(self):
        return self.dial.maximum()

    @max_value.setter
    def max_value(self, value):
        self.dial.setMaximum(value)
