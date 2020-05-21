#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Hello World")
        button = Gtk.Button(label = "Click Here")
        self.add(button)
        button.connect("clicked", self.on_button_clicked)
        self.set_resizable(False)
    def on_button_clicked(self, widget):
        print("Clicked Here")

window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

