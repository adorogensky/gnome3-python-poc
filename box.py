#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyBoxWindow(Gtk.Window):

    new_buttons = []

    def __init__(self):
        Gtk.Window.__init__(self, title = "Box Window")
        
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)

        btn_add = Gtk.Button(
            label = "Add", 
            margin_top = 5,
            margin_left = 5, 
            margin_right = 5
        )

        btn_remove = Gtk.Button(
            label = "Remove", 
            margin_left = 5, 
            margin_right = 5,
            margin_bottom = 5
        )


        self.box.pack_start(btn_add, True, True, 0)
        self.box.pack_start(btn_remove, True, True, 0)

        self.add(self.box)
        
        btn_add.connect("clicked", self.add_new_button)
        btn_remove.connect("clicked", self.remove_added_button)

        self.show_all()
    def add_new_button(self, widget):
        new_button = Gtk.Button(
            label = "New Button",
            margin_left = 5,
            margin_right = 5,
            margin_bottom = 5
        )

        self.new_buttons.append(new_button)

        self.box.pack_start(
            new_button, True, True, 0
        )

        self.show_all()
        
    def remove_added_button(self, widget):
        if len(self.new_buttons) > 0:
            self.box.remove(self.new_buttons[0])
            self.show_all()
            self.new_buttons.remove(self.new_buttons[0])


window = MyBoxWindow()
window.connect("destroy", Gtk.main_quit)
Gtk.main()

