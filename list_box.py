#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyListBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "ListBox")

        list_box = Gtk.ListBox()
        self.add(list_box)

        row = Gtk.ListBoxRow()
        row.add(Gtk.Button(label = "button1"))

        list_box.add(row)

        row = Gtk.ListBoxRow()
        row.add(Gtk.Button(label = "button2"))

        list_box.add(row)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

MyListBoxWindow()
Gtk.main()
