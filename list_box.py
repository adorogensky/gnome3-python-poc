#!/usr/bin/python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyListBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "ListBox")
        self.set_default_size(700, 100)

        list_box = Gtk.ListBox()
        self.add(list_box)

        row = Gtk.ListBoxRow()
        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        row.add(box)

        label = Gtk.Label(label = "Hello\nWorld")
        box.set_border_width(10)
        box.pack_start(label, True, False, 0)
        box.pack_start(Gtk.Button(label = "button1"), True, False, 0)
        list_box.add(row)

        row = Gtk.ListBoxRow()
        row.add(Gtk.Button(label = "button2"))

        list_box.add(row)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

MyListBoxWindow()
Gtk.main()
