#!usr/bin/python3 
#added counter button for number of trials

import gi
import random
import time

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

number_of_trial = 0

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Toggle Buttons")

        grid = Gtk.Grid()
        self.set_border_width(100)
        self.add(grid)

        labels = []
        for i in range(1,19):
            labels.append(i)
            labels.append(i)
        
        buttons = []
        counter1 = []
        countername1 = []
        
        counter_button = Gtk.Button("")
        Gtk.Window.set_size_request(counter_button,40,40)
   #     grid.attach(x, 0, 0, 1, 1)
        grid.add(counter_button)
    
        for j in range(36):

            button = Gtk.ToggleButton(label="")
            Gtk.Window.set_size_request(button,60,60)
            buttons.append(button)

            if(j<6):
                grid.add(buttons[j])
            elif(j%6==0):
                grid.attach_next_to(buttons[j], buttons[j-6], Gtk.PositionType.BOTTOM, 1, 1)
            else:
                grid.attach_next_to(buttons[j], buttons[j-1], Gtk.PositionType.RIGHT, 1, 1)
            
            a = random.randint(0,len(labels)-1) 
            number = labels[a]
            button.connect("toggled", self.on_button_toggled, str(number), counter1, countername1, counter_button)
            labels.remove(number)

    def updateGUI(self): #eventlerin devam etmesi(paralel calisma) icin tanimlanan fonksiyon
        while (Gtk.events_pending()):
            Gtk.main_iteration()
    
    def wait(self, sec): #sleep suresini bolup eszamanli olarak programin calismaya devam etmesini saglar
        for i in range(10):
            time.sleep(sec/10.0)
            self.updateGUI()

    def on_button_toggled(self, Button, name, counter, countername, counter_button):
            
        if Button.get_active():
            Button.set_label(name)
            print(name)
            #append counter/2
            counter.append(Button)
            countername.append(name)
            if(len(counter)%2==0):
                self.wait(0.5) #0.5 saniye bekle
                self.change(counter, countername, counter_button)
        else:
             Button.set_label("")
         
        #import pdb
        #pdb.set_trace()
    
    def change(self, array, labelarray, counter_button):
        
        global number_of_trial
        
        if(labelarray[-2]==labelarray[-1]):
            array[-1].set_sensitive(False)
            array[-2].set_sensitive(False)
        else:
            array[-2].set_active(False)
            array[-1].set_active(False)
            print("Number of trial:", number_of_trial)
            number_of_trial += 1
            counter_button.set_label(str(number_of_trial))
            
        
win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
