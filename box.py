#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Box Window")
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        box.pack_start(Gtk.Button(label = "Button 1", margin_left = 5, margin_right = 5, margin_top = 5), True, True, 0)
        box.pack_start(Gtk.Button(label = "Button 2", margin_left = 5, margin_right = 5, margin_bottom = 5), True, True, 0)
        self.add(box)

window = MyBoxWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

