#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def on_button_clicked(widget):
    print("Clicked Here")

window = Gtk.Window()
window.set_title("Hello World")
button = Gtk.Button(label = "Click Here")
window.add(button)
button.connect("clicked", on_button_clicked)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
