#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MySearchWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Hello World")
        search_entry = Gtk.SearchEntry()
        self.add(search_entry)

window = MySearchWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

