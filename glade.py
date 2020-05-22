#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def on_btnHelp_clicked(widget):
    print("May I Help You?")

builder = Gtk.Builder()
builder.add_from_file("glade.glade")
window = builder.get_object("window")
btnHelp = builder.get_object("btnHelp")
btnHelp.connect("clicked", on_btnHelp_clicked)
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()

