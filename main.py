from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.core.window import Window

#Window.clearcolor = (1, 1, 1, 1)

class ListScreen(Screen):
    pass
class NotesScreen(Screen):
    pass
class NoteScreen(Screen):
    pass
class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file("note.kv")

class NoteApp(App):
    def change_screen(self, screen_name):
        tr = NoTransition()
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = screen_name
    def create_list(self):
        self.gl.add_widget(Button())
    def setup(self):
        self.list = self.root.ids["list_screen"]
        self.gl = self.list.ids["gl"]
    def build(self):
        self.setup()
        return GUI

if __name__ == '__main__':
    NoteApp().run()
