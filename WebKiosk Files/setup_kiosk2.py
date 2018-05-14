#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import time
import sys
import select

              
class Handler:
              
    def onDestroy(self, *args):
        Gtk.main_quit()
        exit
        
    def file_chosen(self, widget):
        
        filepath = fileChooser.get_filename()
        print(filepath)

        if filepath.endswith(".txt"):
            
            with open (filepath, "r") as myfile:
                data = myfile.readlines()
                if len(data) > 1:
                    switchString = data[0].replace('\n', '')
                    refreshString = data[1].replace('\n', '')
                    try:
                        spinbutton1.set_value(float(switchString))
                        spinbutton2.set_value(float(refreshString))
                        
                    except ValueError:
                        
                        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, "An error has occurred.")
                        dialog.format_secondary_text("The chosen file was not suitable for web kiosk.")
                        dialog.run()
                        print("ERROR dialog closed")
                        dialog.destroy()
                        fileChooser.unselect_all()
                        return False
                    
                    if len(data) > 2:
                        
                        for i in box.get_children():
                            box.remove(i)

                        for i in data[2:]:
                            newBox = Gtk.Box(spacing = 5)
                            my_entry = Gtk.Entry()
                            my_entry.set_text(i.replace('\n', ''))
                            my_label = Gtk.Label()
                            my_remove = Gtk.Button("X")
                            my_remove.connect("clicked", self.removebutton1_is_clicked)
                            my_label.set_text("URL:")
                            newBox.add(my_label)
                            newBox.add(my_entry)
                            newBox.add(my_remove)
                            box.add(newBox)
                            
                        window.show_all()
                else:
                    dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, "An error has occurred.")
                    dialog.format_secondary_text("The chosen file was not suitable for web kiosk.")
                    dialog.run()
                    print("ERROR dialog closed")
                    dialog.destroy()
                    fileChooser.unselect_all()

        else:
            dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, "An error has occurred, unfitting file.")
            dialog.format_secondary_text("Please choose a .txt file for the web kiosk.")
            dialog.run()
            print("ERROR dialog closed")
            dialog.destroy()
            fileChooser.unselect_all()
            
                    
    def file_chosen2(self, widget):

        with open("/home/pi/WebKiosk/.runMode.txt", "w") as myfile:
            print("1",file = myfile)
            
        filepath = fileChooser2.get_filename()
        print(filepath)
        filename = fileChooser2.get_file().get_basename()
        print(filename)
        split = os.path.splitext(filename)
        ending = split[1]
        filenoend = split[0]
        delay = spinbutton3.get_value()

        if ending == ".txt":
                print("")

        if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".avi") or filename.endswith(".wmv") or filename.endswith(".mpeg") or filename.endswith(".h264"):
            with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
                print('/home/pi/WebKiosk/singleVideoPlayer.sh ' + filepath, file = myfile)

            os.system('/home/pi/WebKiosk/kioskMode.sh')
            print('/home/pi/WebKiosk/singleVideoPlayer.sh ' + filepath)
            os.system('/home/pi/WebKiosk/singleVideoPlayer.sh ' + filepath)

        elif filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".tif") or filename.endswith(".pnm") or filename.endswith(".bmp") or filename.endswith(".gif") or filename.endswith(".xpm"):
            with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
                print('/home/pi/WebKiosk/imagePlayer.sh ' + str(int(delay)) + ' ' + filepath, file = myfile)

            os.system('/home/pi/WebKiosk/kioskMode.sh')
            print('/home/pi/WebKiosk/imagePlayer.sh ' + str(int(delay)) + ' ' + filepath)
            os.system('/home/pi/WebKiosk/imagePlayer.sh ' + str(int(delay)) + ' ' + filepath)

        elif filename.endswith(".odp") or filename.endswith(".ppt") or filename.endswith(".pptx"):
            with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
                print('/home/pi/WebKiosk/slidePlayer.sh ' + filepath + ' ' + filenoend + ' ' + str(int(delay)), file = myfile)

            os.system('/home/pi/WebKiosk/kioskMode.sh')
            print('/home/pi/WebKiosk/slidePlayer.sh ' + filepath + ' ' + filenoend + ' ' + str(int(delay)))
            os.system('/home/pi/WebKiosk/slidePlayer.sh ' + filepath + ' ' + filenoend + ' ' + str(int(delay)))

        else:
            window.popover2.set_relative_to(widget)
            window.popover2.show_all()
            window.popover2.popup()
                
    def presentation_chosen(self, button):

        filepath = fileChooser2.get_filename()
        filename = fileChooser2.get_file().get_basename()
        delay = spinbutton3.get_value()
        with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
            print('/home/pi/WebKiosk/slidePlayer.sh ' + filepath + ' ' + filename + ' ' + str(int(delay)), file = myfile)

        os.system('/home/pi/WebKiosk/kioskMode.sh')
        print('/home/pi/WebKiosk/slidePlayer.sh ' + filepath + ' ' + filename + ' ' + str(int(delay)))
        os.system('/home/pi/WebKiosk/slidePlayer.sh ' + filepath + ' '  + filename + ' ' + str(int(delay)))
        
    def video_chosen(self, button):

        filepath = fileChooser2.get_filename()
        with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
            print('/home/pi/WebKiosk/videoPlayer.sh ' + filepath, file = myfile)
            
        os.system('/home/pi/WebKiosk/kioskMode.sh')
        print('/home/pi/WebKiosk/videoPlayer.sh ' + filepath)
        os.system('/home/pi/WebKiosk/videoPlayer.sh ' + filepath)

    def cancel1_clicked(self, button):
        
        fileChooser2.unselect_all()
        window.popover2.hide()
        
    def folder_chosen(self, widget):
        
        with open("/home/pi/WebKiosk/.runMode.txt", "w") as myfile:
            print("1",file = myfile)
            
        direc = folderChooser.get_filename()
        delay = spinbutton3.get_value()
        isVideo = False
        isImage = False
        print(direc)
        for filename in os.listdir(direc):
            print(filename)
            if filename.endswith(".mp4") or filename.endswith(".mov") or filename.endswith(".avi") or filename.endswith(".wmv") or filename.endswith(".mpeg") or filename.endswith(".mkv") or filename.endswith(".h264"):
                isVideo = True
            elif filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".tif") or filename.endswith(".pnm") or filename.endswith(".bmp") or filename.endswith(".gif") or filename.endswith(".xpm"):
                isImage = True

        if isImage:
            
            print("imagescript")
            with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
                print('/home/pi/WebKiosk/imagePlayer.sh ' + str(int(delay)) + ' ' + direc, file = myfile)

            os.system('/home/pi/WebKiosk/kioskMode.sh')
            print('/home/pi/WebKiosk/imagePlayer.sh ' + str(int(delay)) + ' ' + direc)
            os.system('/home/pi/WebKiosk/imagePlayer.sh ' + str(int(delay)) + ' ' + direc)
            
        elif isVideo:
            
            print("videoscript")
            with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
                print('/home/pi/WebKiosk/videoPlayer.sh ' + direc, file = myfile)

            os.system('/home/pi/WebKiosk/kioskMode.sh')
            print('/home/pi/WebKiosk/videoPlayer.sh ' + direc)
            os.system('/home/pi/WebKiosk/videoPlayer.sh ' + direc)

        else:
            
            dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, "An error has occurred.")
            dialog.format_secondary_text("The chosen folder didn't contain image or video files.")
            dialog.run()
            print("ERROR dialog closed")
            dialog.destroy()
            folderChooser.unselect_all()
            

    def image_folder_chosen(self, button):
        with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
            print('/home/pi/WebKiosk/imagePlayer.sh ' + direc, file = myfile)

        os.system('/home/pi/WebKiosk/kioskMode.sh')
        print('/home/pi/WebKiosk/imagePlayer.sh ' + direc)
        os.system('/home/pi/WebKiosk/imagePlayer.sh ' + direc)

    def videos_folder_chosen(self, button):
        with open ("/home/pi/WebKiosk/.runCommand.txt", "w") as myfile:
            print('./videoPlayer.sh ' + direc, file = myfile)

        os.system('/home/pi/WebKiosk/kioskMode.sh')
        print('/home/pi/WebKiosk/videoPlayer.sh ' + direc)
        os.system('/home/pi/WebKiosk/videoPlayer.sh ' + direc)

    def cancel2_clicked(self, button):
        folderChooser.unselect_all()
        window.popover3.hide()
        
    def addbutton1_is_clicked(self, button):
        newBox = Gtk.Box(spacing = 5)
        my_entry = Gtk.Entry()
        my_label = Gtk.Label()
        my_remove = Gtk.Button("X")
        my_remove.connect("clicked", self.removebutton1_is_clicked)
        my_up = Gtk.Button()
        my_up.set_image(Gtk.Image.new_from_stock("gtk-go-up", 4))
        my_up.set_always_show_image(True)
        my_down = Gtk.Button()
        my_down.set_image(Gtk.Image.new_from_stock("gtk-go-down", 4))
        my_down.set_always_show_image(True)
        my_up.connect("clicked", self.upbutton1_is_clicked)
        my_down.connect("clicked", self.downbutton1_is_clicked)
        my_label.set_text("URL:")
        newBox.add(my_label)
        newBox.add(my_entry)
        newBox.add(my_remove)
        newBox.add(my_up)
        newBox.add(my_down)
        
        box.add(newBox)
        print(box)
        for n in box.get_children():
            print(n.get_children())
            print(n.get_children()[1].get_text())
        window.show_all()

    def removebutton1_is_clicked(self, button):
        parent = button.get_parent()
        print(parent.get_children())
        box.remove(parent)

    def upbutton1_is_clicked(self,button):
        parent = button.get_parent()
        grandparent = parent.get_parent()
        i = box.get_children().index(parent)
        if i > 0:
            grandparent.reorder_child(parent,i-1)

    def downbutton1_is_clicked(self, button):
        parent = button.get_parent()
        grandparent = parent.get_parent()
        i = box.get_children().index(parent)
        if i < len(grandparent.get_children())-1:
            grandparent.reorder_child(parent,i+1)
        

    def savefilebutton1_is_clicked(self, button):
        window.popover.set_relative_to(button)
        window.popover.show_all()
        window.popover.popup()

        
    def savebutton_is_clicked(self, widget):
        print(str(len(filenameEntry.get_text())))
        if len(filenameEntry.get_text()) > 0:

            filename = filenameEntry.get_text() + ".txt"
            with open(filename, "w") as text_file:
                print(spinbutton1.get_value(), file = text_file)
                print(spinbutton2.get_value(), file = text_file)
                for i in box.get_children():
                    print(i.get_children()[1].get_text(), file = text_file)
            window.popover.hide()

    def loadprevious_is_clicked(self, button):
        print(self)
        print(button)
        with open ("/home/pi/WebKiosk/Previous.txt", "r") as myfile:
            data=myfile.readlines()
            switchString = data[0].replace('\n', '')
            refreshString = data[1].replace('\n', '')

        spinbutton1.set_value(float(switchString))
        spinbutton2.set_value(float(refreshString))
        for i in box.get_children():
            box.remove(i)
        for i in data[2:]:
            newBox = Gtk.Box(spacing = 5)
            my_entry = Gtk.Entry()
            my_entry.set_text(i.replace('\n', ''))
            my_label = Gtk.Label()
            my_remove = Gtk.Button("X")
            my_remove.connect("clicked", self.removebutton1_is_clicked)
            my_label.set_text("URL:")
            my_up = Gtk.Button()
            my_up.set_image(Gtk.Image.new_from_stock("gtk-go-up", 4))
            my_up.set_always_show_image(True)
            my_down = Gtk.Button()
            my_down.set_image(Gtk.Image.new_from_stock("gtk-go-down", 4))
            my_down.set_always_show_image(True)
            my_up.connect("clicked", self.upbutton1_is_clicked)
            my_down.connect("clicked", self.downbutton1_is_clicked)
            newBox.add(my_label)
            newBox.add(my_entry)
            newBox.add(my_remove)
            newBox.add(my_up)
            newBox.add(my_down)
            box.add(newBox)
        window.show_all()
                

    def applybutton1_is_clicked(self, button):

        with open("/home/pi/WebKiosk/.runMode.txt", "w") as myfile:
            print("0",file = myfile)
        
        with open("/home/pi/WebKiosk/Previous.txt", "w") as text_file:
            print(spinbutton1.get_value(), file = text_file)
            print(spinbutton2.get_value(), file = text_file)
            for i in box.get_children():
                print(i.get_children()[1].get_text(), file = text_file)

        if len(box.get_children()) > 0:
            
            switchRate = int(spinbutton1.get_value())
            refreshRate = int(spinbutton2.get_value())
            for i in box.get_children():
                print(i.get_children()[1].get_text())
                websiteList.append(i.get_children()[1].get_text())

            window.destroy()
            Gtk.main_quit()

            os.system('/home/pi/WebKiosk/kioskMode.sh')
            os.system('export DISPLAY=:0')
            os.system('/home/pi/WebKiosk/xauth_root.sh')
            cycle = 0
            time.sleep(1)
            print("lets go")
            
            try:
                while True:
                    if cycle == 0:
                        print(websiteList)
                        for n in websiteList:
                            print('chromium-browser --incognito '+ n + '&')
                            os.system('chromium-browser --incognito '+ n + '&')
                            if cycle == 1:
                                os.system('xdotool key "F11" &')
                                os.system('/home/pi/WebKiosk/autorefresh-chromium.sh '+ str(refreshRate))
                            time.sleep(switchRate)
                            cycle += 1

                    else:
                        for n in range(0,len(websiteList)):
                            tabNumber = n + 1
                            os.system('xdotool key "ctrl+'+str(tabNumber)+'"')
                            time.sleep(switchRate)
                                
            except KeyboardInterrupt:
                exit

        else:

            dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, "An error has occurred.")
            dialog.format_secondary_text("No URL fields were defined.")
            dialog.run()
            print("ERROR dialog closed")
            dialog.destroy()
            fileChooser.unselect_all()
            return False
        
handler = Handler()
builder = Gtk.Builder()
builder.add_from_file("/home/pi/WebKiosk/webKioskUi.glade")
window = builder.get_object("window1")
box = builder.get_object("box")

#popover1
window.popover = Gtk.Popover()
vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
filenameEntry = Gtk.Entry()
hbox1.pack_start(filenameEntry, False, True, 10)
hbox1.pack_start(Gtk.Label(".txt"), False, True, 10)
hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
saveButton = Gtk.Button("Save")
saveButton.connect("clicked",handler.savebutton_is_clicked)
hbox2.pack_start(saveButton, False, True, 10)
vbox.pack_start(hbox1, False, True, 10)
vbox.pack_start(hbox2, False, True, 10)
vbox.set_border_width(5)
window.popover.add(vbox)
window.popover.set_position(Gtk.PositionType.BOTTOM)

#popover2
window.popover2 = Gtk.Popover()
vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
presentation = Gtk.Button("presentation")
presentation.connect("clicked", handler.presentation_chosen)
video = Gtk.Button("video")
video.connect("clicked", handler.video_chosen)
cancel1 = Gtk.Button("cancel")
cancel1.connect("clicked", handler.cancel1_clicked)
vbox2.pack_start(Gtk.Label("Unknown/missing file extension.\nOpen as:"), False, True, 10)
vbox2.pack_start(presentation, True, True, 5)
vbox2.pack_start(video, True, True, 5)
vbox2.pack_start(cancel1, False, False, 5)
vbox2.set_border_width(5)
window.popover2.add(vbox2)
window.popover2.set_position(Gtk.PositionType.BOTTOM)

#popover3
window.popover3 = Gtk.Popover()
vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
images = Gtk.Button("images")
images.connect("clicked", handler.image_folder_chosen)
videos = Gtk.Button("videos")
videos.connect("clicked", handler.videos_folder_chosen)
cancel2 = Gtk.Button("cancel")
cancel2.connect("clicked", handler.cancel2_clicked)
vbox3.pack_start(Gtk.Label("File extensions were missing, what files does the folder contain"), False, True, 10)
vbox3.pack_start(images, False, True, 10)
vbox3.pack_start(videos, False, True, 10)
vbox3.pack_start(cancel2, False, True, 10)
vbox3.set_border_width(5)
window.popover3.add(vbox3)
window.popover3.set_position(Gtk.PositionType.BOTTOM)

index = 1
websiteList = []

websites = []

builder.connect_signals(handler)

up = builder.get_object("image1")
down = builder.get_object("image2")

adjustment1 = Gtk.Adjustment(10,0,1000,1,1)
adjustment2 = Gtk.Adjustment(20,0,1000,1,1)
adjustment3 = Gtk.Adjustment(10,0,1000,1,1)

spinbutton1 = builder.get_object("spinbutton1")
spinbutton2 = builder.get_object("spinbutton2")
spinbutton3 = builder.get_object("spinbutton3")

spinbutton1.configure(adjustment1, 1, 0)
spinbutton2.configure(adjustment2, 1, 0)
spinbutton3.configure(adjustment3, 1, 0)


fileChooser = builder.get_object("filechoosebutton1")


fileChooser2 = builder.get_object("filechoosebutton2")


folderChooser = builder.get_object("folderchoosebutton1")
folderChooser.set_action(2)


def main():

    window.show_all()
    Gtk.main()

open("/home/pi/WebKiosk/.runMode.txt", "a+")
    
with open("/home/pi/WebKiosk/.runMode.txt", "r") as myfile:
    data = myfile.readlines()
    

if len(data) < 1:
    main()

else:
    
    print ("You have 10 seconds to press ENTER!")
    print("Pressing ENTER will interrupt Kiosk autostart and open the Setup.")

    i, o, e = select.select( [sys.stdin], [], [], 10 )

    if (i):
        
        os.system('xdotool getactivewindow windowminimize')
        main()
             
    else:
        
        print("Launching Kiosk Mode")
        time.sleep(1)
        os.system('xdotool getactivewindow windowminimize')
        if data[0].replace('\n','') == "0":
            with open ("/home/pi/WebKiosk/Previous.txt", "r") as myfile:
                data=myfile.readlines()
                switchRate = float(data[0].replace('\n', ''))
                refreshRate = float(data[1].replace('\n', ''))
            websiteList = []
            for n in data[2:]:
                websiteList.append(n.replace('\n', ''))
                
            os.system('/home/pi/WebKiosk/kioskMode.sh')
            os.system('/home/pi/WebKiosk/xauth_root.sh')
            os.system('export DISPLAY=:0')
            cycle = 0
            
            try:
                while True:
                    if cycle == 0:
                        print(websiteList)
                        for n in websiteList:
                            print('chromium-browser --incognito '+ n + '&')
                            os.system('chromium-browser --incognito '+ n + '&')
                            if cycle == 1:
                                os.system('xdotool key "F11" &')
                                os.system('/home/pi/WebKiosk/autorefresh-chromium.sh '+ str(refreshRate))
                            time.sleep(switchRate)
                            cycle += 1

                    else:
                        for n in range(0,len(websiteList)):
                            tabNumber = n + 1
                            os.system('xdotool key "ctrl+'+str(tabNumber)+'"')
                            time.sleep(switchRate)
                                
            except KeyboardInterrupt:
                exit

        else:
            with open ("/home/pi/WebKiosk/.runCommand.txt", "r") as myfile:
                data = myfile.readlines()
            command = data[0].replace('\n', '')
            print(command)
            os.system(command)
           

    
