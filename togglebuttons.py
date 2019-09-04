import gi
import random
import time

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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

        for j in range(36):

            button = Gtk.ToggleButton(label="")
            Gtk.Window.set_size_request(button,50,50)
            buttons.append(button)

            if(j<6):
                grid.add(buttons[j])
            elif(j%6==0):
                grid.attach_next_to(buttons[j], buttons[j-6], Gtk.PositionType.BOTTOM, 1, 1)
            else:
                grid.attach_next_to(buttons[j], buttons[j-1], Gtk.PositionType.RIGHT, 1, 1)
            
            a = random.randint(0,len(labels)-1) 
            number = labels[a]
            button.connect("toggled", self.on_button_toggled, str(number), counter1, countername1)
            labels.remove(number)

    def updateGUI(self): #eventlerin devam etmesi(paralel calisma) icin tanimlanan fonksiyon
        while (Gtk.events_pending()):
            Gtk.main_iteration()
    
    def wait(self, sec): #sleep suresini bolup eszamanli olarak programin calismaya devam etmesini saglar
        for i in range(10):
            time.sleep(sec/10.0)
            self.updateGUI()

    def on_button_toggled(self, Button, name, counter, countername):
            
        if Button.get_active():
            Button.set_label(name)
            print(name)
            counter.append(Button)
            countername.append(name)
            if(len(counter)%2==0):
                self.wait(0.5) #0.5 saniye bekle
                self.change(counter, countername)
        else:
             Button.set_label("")
         
        #import pdb
        #pdb.set_trace()

    def change(self, array, labelarray):
        if(labelarray[-2]==labelarray[-1]):
            array[-1].set_label("ok")
            array[-2].set_label("ok")
        else:
            array[-2].set_active(False)
            array[-1].set_active(False)
        
win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
