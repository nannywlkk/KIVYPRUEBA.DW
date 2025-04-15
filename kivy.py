from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDToolbar

class ContadorApp(MDApp):
    def build(self):
        self.contador = 0  

        screen = Screen()

        main_layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        toolbar = MDToolbar(title="Contador KivyMD")
        toolbar.pos_hint = {"top": 1}
        main_layout.add_widget(toolbar)

        self.label = MDLabel(
            text=str(self.contador),
            halign="center",
            font_style="H3"
        )
        main_layout.add_widget(self.label)

        btn_layout = MDBoxLayout(spacing=20, padding=10, size_hint=(1, None), height=50)
        btn_menos = MDRaisedButton(text="-", on_release=self.decrementar)
        btn_mas = MDRaisedButton(text="+", on_release=self.incrementar)

        btn_layout.add_widget(btn_menos)
        btn_layout.add_widget(btn_mas)

        main_layout.add_widget(btn_layout)
        screen.add_widget(main_layout)

        return screen

    def incrementar(self, instance):
        self.contador += 1
        self.label.text = str(self.contador)

    def decrementar(self, instance):
        self.contador -= 1
        self.label.text = str(self.contador)

ContadorApp().run()
