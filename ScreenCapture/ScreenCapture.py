###
# ScreenCapture:    A script that automatically selects a specified section on your screen and takes a screen capture of it.
#                   It then pastes it into a specified program/file.
#
# By:               Jose Flores
#
###

import pyautogui as py

py.hotkey('shiftleft', 'win','s')   # Keyboard shortcut to open up Snip & Sketch

py.sleep(0.5)                       # Gives the computer time (0.5s) to bring up Snip & Sketch interface.

py.moveTo(3858, 400)                # Moves the cursor to where i want it to start the screenCapture.
                                    # To find the coordinates that you need in order to be able to change my default coordinates,
                                    # use pyautogui.position() which will return the current position of your cursor.

py.mouseDown(button='left')         # Holds down the mouse's left button
py.dragTo(4749, 896,0.5)            # While holding down the left button, it drags the cursor to (X = 4729, Y = 896) in 0.5 seconds


# Snip & Sketch automatically adds the screen capture to our clip board.
# Here we'll just be pasting the copied screen capture. 
py.sleep(1)
py.click(989, 16)
py.sleep(0.5)
py.hotkey('ctrlleft', 'v')
