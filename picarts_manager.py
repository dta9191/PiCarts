import tkinter as tk
import os

unmountCart = "umount /dev/mmcblk0p1"
mountCart = "sudo mount /dev/mmcblk0p1 /media/dustin/256SD"
#os.system("mount /dev/sd(x) /mountpoint") 



#----------------------------------------------------------
window = tk.Tk()
#----------------------------------------------------------
# Greeting

greeting = tk.Label(text="PiCarts Manager",
    fg="white",
    bg="purple")

greeting.pack()
#----------------------------------------------------------
# loadSW

button_loadSW = tk.Button(
  text="Load SW",
  width=50,
  height=2,
  bg="blue",
  fg="white",
  )

button_loadSW.pack()

def loadSW_pressed(event):
    outputBox.insert(1.0, "Cart Software Loaded \n")
button_loadSW.bind("<Button-1>", loadSW_pressed)

#----------------------------------------------------------
#----------------------------------------------------------
# loadCart

button_loadCart = tk.Button(
  text="Load Cart",
  width=50,
  height=2,
  bg="green",
  fg="black",
  )

button_loadCart.pack()

def loadCart_pressed(event):
    os.system(mountCart)
    outputBox.insert(1.0, "Cart Loaded \n")
button_loadCart.bind("<Button-1>", loadCart_pressed)

#----------------------------------------------------------
# ejectCart

button_ejectCart = tk.Button(
  text="Eject Cart",
  width=50,
  height=2,
  bg="red",
  fg="black",
  )
button_ejectCart.pack()

def ejectCart_pressed(event):
    os.system(unmountCart)
    outputBox.insert(1.0, "Cart Safely Ejected \n")
button_ejectCart.bind("<Button-1>", ejectCart_pressed)
#----------------------------------------------------------
# backupCart

button_backupCart = tk.Button(
  text="Backup Cart",
  width=50,
  height=2,
  bg="white",
  fg="green",
  )

button_backupCart.pack()

def backupCart_pressed(event):
    outputBox.insert(1.0, "Cart Backup Initiated \n")
button_backupCart.bind("<Button-1>", backupCart_pressed)

#----------------------------------------------------------
# restoreCart
button_restoreCart = tk.Button(
  text="Restore Cart",
  width=50,
  height=2,
  bg="white",
  fg="blue",
  )

button_restoreCart.pack()

def restoreCart_pressed(event):
    outputBox.insert(1.0, "Cart Restore Completed \n")
button_restoreCart.bind("<Button-1>", restoreCart_pressed)

#----------------------------------------------------------
# lockCart

button_lockCart = tk.Button(
  text="Lock Cart",
  width=50,
  height=2,
  bg="black",
  fg="red",
  )

button_lockCart.pack()

def lockCart_pressed(event):
    outputBox.insert(1.0, "Cart Locked \n")
button_lockCart.bind("<Button-1>", lockCart_pressed)

#----------------------------------------------------------
# unlockCart Serial Connection

button_unlockCart = tk.Button(
  text="Unlock Cart",
  width=50,
  height=2,
  bg="black",
  fg="green",
  )

button_unlockCart.pack()

def unlockCart_pressed(event):
    outputBox.insert(1.0, "Cart Unlocked \n")
button_unlockCart.bind("<Button-1>", unlockCart_pressed)

#----------------------------------------------------------
# Debug Window
##Make text entry box. Retrieve with <.get(1, tk.END). Indexes: first is line, second is character.
outputBox = tk.Label(text="Actions")
outputBox.pack()
outputBox = tk.Text()
outputBox.pack()
#----------------------------------------------------------

window.mainloop()



