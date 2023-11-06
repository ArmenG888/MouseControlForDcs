import keyboard,pyautogui,time,threading,sys
import vgamepad as vg
from PySide2 import QtCore,QtWidgets
from ui_mouseControl import Ui_MainWindow

gamepad = vg.VX360Gamepad()
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()

def convert(sens, key):
    offset_x, offset_y = pyautogui.position()
    while True:
        x, y = pyautogui.position()
        x = max(-1, min(1, (x-offset_x)/100*float(sens)))
        y = max(-1, min(1, (y-offset_y)/100*float(sens)))
        gamepad.right_joystick_float(x_value_float=x, y_value_float=-y)
        gamepad.update()
        time.sleep(0.01)
        if stop_thread:
            break
        if keyboard.is_pressed(key):
            offset_x, offset_y = pyautogui.position()

class main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.setWindowTitle('Mouse Control For Dcs')
        self.ui.startBtn.clicked.connect(self.start)       
        
    def start(self):
        global stop_thread 
        if self.ui.startBtn.text() == 'Stop':      
            stop_thread = True
            self.ui.startBtn.setText('Start')
        else:
            self.ui.startBtn.setText('Stop')
            stop_thread = False
            threading.Thread(target=convert, args=(self.ui.sens.text(),self.ui.key.text(),)).start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())
