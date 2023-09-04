import sys
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.drulum.shopping_list_generator")
        GLib.set_application_name("Shopping List Generator")

    def do_activate(self) -> None:
        window = Gtk.ApplicationWindow(application=self, title="Shopping List Generator")
        window.present()


if __name__ == '__main__':
    app = MyApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
