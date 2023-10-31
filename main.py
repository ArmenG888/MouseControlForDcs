from tkinter import *
import keyboard,pyautogui,time
import vgamepad as vg



root = Tk() 
root.title("Mouse Control For DCS World")


title = Label(root, text="Mouse Control For DCS World",font=("Helvetica", 24))
title.grid(pady=20, padx=20) 

label = Label(root, text="Your Input:")
label.grid(row=1, column=0, padx=10, pady=10)  # placing it in the first row, first column

# Create an Entry widget for user input
entry = Entry(root)
entry.grid(row=1, column=0, padx=10, pady=10)  # placing it in the first row, second column


root.geometry("800x600")
mainloop() 


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


