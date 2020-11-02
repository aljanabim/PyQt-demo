#!/usr/bin/env python
import sys

import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from layout import Ui_MainWindow
import rospy


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.dummy = 0
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.edit_slider(init_val=1, min_val=-10, max_val=10)
        self.interactions()

    def interactions(self):
        '''
            Set up the connectivity between all the GUI elements that where generated in 
            the layout.py file.
        '''

        self.variance_slider.sliderMoved.connect(
            lambda val, dummy=None: self.slider_moved_handler(val, self.dummy))
        # Lambda was used here to demonstrate how a second argument can be passed to the
        # handler function

        self.variance_slider.sliderReleased.connect(
            self.slider_released_handler)

    def edit_slider(self, init_val, min_val, max_val):
        '''
            Edit the minimum and maximum values of the slider, along side the steps the slider takes
            per change

            See https://www.tutorialspoint.com/pyqt/pyqt_qslider_widget_signal.htm
        '''
        # Sets the value of the control programmatically
        self.variance_slider.setValue(init_val)
        # Update the text of the value according to the new initial value
        self.variance_label.setText(str(init_val))
        # Sets the lower bound of the slider
        self.variance_slider.setMinimum(min_val)
        # Sets the upper bound of the slider
        self.variance_slider.setMaximum(max_val)

    def slider_moved_handler(self, val, dummy):
        '''
            Takes the slider value and a dummy value and sets the label of the variance in the interface
            (This function runs whenever the value of the slider moves)
        '''
        self.variance_label.setText(str(val))

    def slider_released_handler(self):
        '''
            Gets the value of the slider upon its release and DOES THINGS WITH IT
        '''
        # The sliderReleased signal is emitted when the slider is released and it
        # doesn't return the value of the slider. Therefore we need to get the value first
        # read more here https://doc.qt.io/qt-5/qslider.html

        slider_value = self.variance_slider.value()
        print("I am about to call a rosservice with the following variance " + str(slider_value))


def Window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    Window()
