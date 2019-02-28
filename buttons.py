import gi
import random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Toggle Buttons")

        grid = Gtk.Grid()
        self.set_border_width(100)
        self.add(grid)


        buttons=[]
        labels=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]

#creating 36 buttons and assigning them a random number between 1-18

        for button in range(36):
            j=button

            button=Gtk.ToggleButton(label="")
            Gtk.Window.set_size_request(button,50,50)
            buttons.append(button)
           
            a=random.randint(0,len(labels)-1)
            number=labels[a]
            button.connect("toggled",self.on_button_toggled,str(number))
            labels.remove(number)

#locating buttons

            if(j<6):
                grid.add(buttons[j])
            elif(j%6==0):
                grid.attach_next_to(buttons[j], buttons[j-6], Gtk.PositionType.BOTTOM, 1,1)
            else:
                grid.attach_next_to(buttons[j], buttons[j-1], Gtk.PositionType.RIGHT,1,1)


    def on_button_toggled(self, Button, name):
        if Button.get_active():
            Button.set_label(name)
        else:
            Button.set_label("")




win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
