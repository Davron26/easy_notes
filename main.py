from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class ListScreen(Screen):
    pass
class NotesScreen(Screen):
    pass
class NoteScreen(Screen):
    pass

GUI = Builder.load_file("note.kv")

class NoteApp(App):
    def build(self):
        return GUI

if __name__ == '__main__':
    NoteApp().run()
