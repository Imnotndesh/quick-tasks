import gi
gi.require_version("Gtk","4.0")
gi.require_version("Gdk","4.0")

from gi.repository import Gtk,Gdk
builder = Gtk.Builder()

def styling_resource():
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path("./resources/Window/notesApp.css")
    Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    builder.add_from_file("./resources/Window/notesapp.ui")


def itemStyling(application_window,add_task_button,tasks_lists_container):

    application_window.set_css_classes(['appMainWindow'])
    add_task_button.set_css_classes(['addTaskButton'])
    tasks_lists_container.set_css_classes(['tasksContainer'])