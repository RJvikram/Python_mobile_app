from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        btn = MDRectangleFlatButton(text='Hello', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn)

        return screen


DemoApp().run()
