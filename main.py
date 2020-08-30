from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, NoTransition
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

Window.clearcolor = (1, 1, 1, 1)

class ListScreen(Screen):
    pass
class NotesScreen(Screen):
    pass
class NoteScreen(Screen):
    pass
class CreateList(Screen):
    pass
class ImageButton(ButtonBehavior, Image):
    pass

GUI = Builder.load_file("note.kv")

class NoteApp(App):
    def build(self):
        self.setup()
        return GUI
    def setup(self):
        self.list_screen = GUI.ids["list_screen"]
        self.create_list_screen = GUI.ids["create_list"]
        self.gl = self.list_screen.ids["gl"]
        self.text_input = self.create_list_screen.ids["text_input"]
        self.name_long = self.create_list_screen.ids["name_long"]
        self.test()
    def change_screen(self, screen_name):
        tr = NoTransition()
        screen_manager = GUI.ids["screen_manager"]
        screen_manager.transition = tr
        screen_manager.current = screen_name
    def create_list(self):
        if len(self.text_input.text) > 37:
            self.name_long.text = "Имя нового списка слишком длинное!!!"
        else:
            self.gl.add_widget(Button(size_hint_y=None, height=100, text=self.text_input.text))
            self.text_input.text = "Напишите имя сюда"
            self.name_long.text = ""
            self.change_screen("list_screen")
    def test(self):
        test = JsonStore('test.json')
        test.put('tito', name='Mathieu', org='kivy')


if __name__ == '__main__':
    NoteApp().run()
