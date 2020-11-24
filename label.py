from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):

    def build(self):
        label = MDLabel(text='SystematixIndia.com', halign='center', theme_text_color='Custom',
                        text_color=(236 / 255.0, 98 / 255.0, 0 / 255.0, 1), font_style='H2')
        icone_label = MDIcon(icon='language-python', halign='center')
        return icone_label
        # return label


DemoApp().run()

# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
#
#
# class DemoApp(MDApp):
#     def build(self):
#         label = MDLabel(text='SystematixIndia.com..!')
#         return label
#
#
#
# DemoApp().run()