#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyGridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Grid")

        grid = Gtk.Grid()

        button1 = Gtk.Button(label = "Button 1")
        button2 = Gtk.Button(label = "Button 2")
        button3 = Gtk.Button(label = "Button 3")
        button4 = Gtk.Button(label = "Button 4")
        button5 = Gtk.Button(label = "Button 5")
        button6 = Gtk.Button(label = "Button 6")

        grid.add(button1)
        grid.add(button2)
        grid.add(button4)
        grid.attach(button3, 0, 1, 2, 1)

        self.add(grid)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

MyGridWindow()
Gtk.main()
