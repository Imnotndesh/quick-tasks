#! ./guitasks/bin/python
# Imports
import sys
import gi
import styling,handlers
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk,Adw

# Setting default variables
global builder
builder = Gtk.Builder()
builder.add_from_file("./resources/Window/notesapp.ui")
styling.styling_resource()


class myApp(Adw.Application):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)
    def on_activate(self,app):
        # Getting items from ui file
        add_task_button = builder.get_object("addNoteButton")
        tasks_lists_container = builder.get_object("notesCont")
        self.task_display = builder.get_object("textBoxContent")

        # Connections logic
        tasks_lists_container.connect('row-activated',self.show_content)
        tasks_lists_container.set_activate_on_single_click(True)
        add_task_button.connect('clicked',self.add_note)


        # Fetching current tasks names
        tasks_names = ["this","that","those"]
        self.task_stuff = ["i contain this","i contain that","i contain those"]
        
        self.get_items(tasks_names,tasks_lists_container)
        
        # Window Actions
        application_Window = builder.get_object("mainWindow")
        application_Window.set_application(self)

        # Items passed to style
        styling.itemStyling(application_Window,add_task_button,tasks_lists_container)

        # Present windows
        application_Window.present()


    # Getting items from storage
    def get_items(self,tasks_names,tasks_lists_container):
        for items in tasks_names:
            taskItem = Gtk.ListBoxRow()
            noteText = Gtk.Label()
            noteText.set_text(items)
            taskItem.set_child(noteText)
            taskItem.set_css_classes(['taskItem'])
            tasks_lists_container.append(taskItem)

    # Show items in Text View
    def show_content(self,ListBox,ListBoxRow):
        this_index = ListBoxRow.get_index()
        this_task_content = self.task_stuff[this_index]
        self.task_display.set_text(this_task_content)

    def add_note(self,Button):
        print("Works")
app = myApp(application_id="com.amnotndesh.terminalTasks")
app.run(sys.argv)
