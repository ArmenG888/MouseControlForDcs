import sys
from tkinter import *
import keyboard,pyautogui,time
import vgamepad as vg

from PySide2 import QtCore,QtWidgets


from ui_mouseControl import Ui_MainWindow


class main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()
        self.setWindowTitle('Mouse Control For Dcs')

    def close(self):
        quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())

# gamepad = vg.VX360Gamepad()
# gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
# gamepad.update()
# time.sleep(0.5)


# offset_x, offset_y = pyautogui.position()
# while True:
#     x, y = pyautogui.position()
#     x = max(-1, min(1, (x-offset_x)/100))
#     y = max(-1, min(1, (y-offset_y)/100))
#     print(x,y)
#     gamepad.right_joystick_float(x_value_float=x, y_value_float=y)
#     gamepad.update()
#     time.sleep(0.01)
#     if keyboard.is_pressed('`'):
#         offset_x, offset_y = pyautogui.position()


