from tkinter import *
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import pyvisa
from lecroydso import LeCroyDSO, LeCroyVISA

#initializations
rm = pyvisa.ResourceManager()
root = Tk()
logo = tk.PhotoImage(file = 'logo.gif')
fileName = 'Capture1'
file = 0

#conditionals
fileSelected = 0
fileSaved = 0
deviceSelected = 0
deviceTypeSelected = 0
TLSelected = 0
KSSelected = 0

#USB setups
deviceOption = tk.StringVar(root)
deviceOption.set("Select Devices")
usbOption = tk.StringVar(root)
usbOption.set("None")
selectedUSB = "None"

#device type setups
typeList = ('Keysight', 'Teledyne Lecroy')

#device type selection function: 

#USB selection functions: 

def capture():
    file = filedialog.asksaveasfile(defaultextension='.bmp',
                                    filetypes=[
                                        ("BMP File",".bmp"),
                                    ], mode = 'wb+')
    if file is None:
        return
    usb = rm.open_resource(usbOption.get())
    #file_name = "C:\\Users\\FZuo\\Desktop\\secondTry.bmp" #Make suere that the drive specified is available on your computer
    #usb.write("SAVE:IMAG\"C:/Temp.png\"")
    #usb.write('FileSystem:READFile \"C:/Temp.png\"')
    #usb.chunk_size = 20*1024*1024 #default value is 20*1024(20k bytes)
    #usb.timeout = 300000
    usb.write("HCSU DEV, BMP, PORT, NET, FORMAT, PORTRAIT, BCKG, WHITE; SCDP")
    #usb.write("SCDP")
    result_str = usb.read_raw()
    #f = open(file_name,'wb')
    file.write(result_str)
    file.flush()
    file.close()

def captureWindow():
#print select USB device
    captureWin = Toplevel()
    captureWin.title('Capture Window')
    captureWin.configure(bg='white')
    usbList = rm.list_resources()
    #imageFrame = tk.Frame(captureWin).grid(column = 0, row = 0)
    #tk.Label(imageFrame, bg='white', image = logo).grid(column = 0, row = 0)
    tk.Label(captureWin, text = 'Select Connected Oscilloscope:', font = 'Barlow', bg = 'white',).grid(column = 0, row = 2, sticky = tk.E)
    USBMenu = OptionMenu(captureWin, usbOption, *usbList).grid(column = 1, row = 2, sticky = tk.E)
#button = Button(root,text='File Save Location', font = 'Barlow', command=saveFile, width = 30).grid(column = 1, row = 4, sticky = tk.E)
    tk.Button(captureWin, text = "Capture", state = NORMAL, font = 'Barlow', command=capture, width = 30).grid(column = 1, row = 4, sticky = tk.E)
#location = Label(text='Unselected Location', font = 'Barlow', bg = 'white').grid(column = 2, row = 1)


#Prepare main Wndow
root.title('FAE Oscilloscope Capture Toolkit')
root.configure(bg='white')
tk.Label(root, text='Please connect Oscilloscope to Computer', font = 'Barlow', background = 'white').grid(column = 0, row = 1)
tk.Button(root, text="I'm Connected", font='Barlow', background = 'white', command = captureWindow).grid(column = 0, row = 2)
imageFrame = tk.Frame(root).grid(column = 0, row = 0)
tk.Label(imageFrame, bg='white', image = logo).grid(column = 0, row = 0)

#print select device type
#tk.Label(root, text = 'Select Device Type: ', font = 'Barlow', bg = 'white',).grid(column = 0, row = 1, sticky = tk.E)
#dviceMenu = OptionMenu(root, deviceOption, *typeList, command = deviceTypeSelect).grid(column = 1, row = 1, sticky = tk.E)


root.mainloop()



#def saveFile():
#    file = filedialog.asksaveasfile(defaultextension='.txt',
#                                    filetypes=[
#                                        ("BMP File",".txt"),
#                                        ("PNG File",".png"),
#                                        ("CSV File",".csv"),
#                                        ("All files", ".*"),
#                                    ])
#    if file is None:
#        return
#    # get the text
#    filetext = str(text.get(1.0,END))
#    file.write(filetext)
#    file.close()
