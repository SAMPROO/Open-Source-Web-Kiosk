#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import os
import time
              
class Handler:
              
    def onDestroy(self, *args):
        Gtk.main_quit()

    def addbutton1_is_clicked(self, button):
        newBox = Gtk.Box(spacing = 5)
        my_entry = Gtk.Entry()
        url_list.append(my_entry)
        my_label = Gtk.Label()
        my_remove = Gtk.Button("X")
        my_remove.connect("clicked", self.removebutton1_is_clicked)
        my_label.set_text("URL:")
        newBox.add(my_label)
        newBox.add(my_entry)
        newBox.add(my_remove)
        
        box.add(newBox)
        window.show_all()

    def removebutton1_is_clicked(self, button):
        parent = button.get_parent()
        print(parent.get_children())
        url_list.remove(parent.get_children()[1])
        box.remove(parent)
        

    def applybutton1_is_clicked(self, button):
        
        with open("Output.txt", "w") as text_file:
            print(spinbutton1.get_value(), file = text_file)
            print(spinbutton2.get_value(), file = text_file)
            for i in url_list:
                print(i.get_text(), file = text_file)
        Gtk.main_quit()
        window.destroy()
        with open ("Output.txt", "r") as myfile:
            data=myfile.readlines()
            refreshString = data[0].replace('\n', '')
            switchString = data[1].replace('\n', '')
            websites = data[2:]
            print(data)
            for i in websites:
                print(i)
                websiteList.append(i.replace('\n', ''))
            refreshRate = int(float(refreshString))
            switchRate = int(float(switchString))
            print(switchRate)
            websites = data[2:]
            print(websiteList)
            for n in websiteList:
                os.system('chromium-browser --incognito --kiosk '+n)
                #os.system('/home/pi/xauth_root.sh')
                #os.system('/home/pi/autorefresh-chromium.sh 5')
                time.sleep(switchRate)
        
    
        
index = 1
websiteList = []
refreshRate = 0
switchRate = 0
websites = []
builder = Gtk.Builder()
builder.add_from_file("webKioskUi.glade")
builder.connect_signals(Handler())

adjustment1 = Gtk.Adjustment(10,0,1000,1,1)
adjustment2 = Gtk.Adjustment(20,0,1000,1,1)

spinbutton1 = builder.get_object("spinbutton1")
spinbutton2 = builder.get_object("spinbutton2")

spinbutton1.configure(adjustment1, 1, 0)
spinbutton2.configure(adjustment2, 1, 0)

entry = builder.get_object("entry1")
url_list = [entry]

window = builder.get_object("window1")
box = builder.get_object("box")
window.show_all()

Gtk.main()
