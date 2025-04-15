from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar

class ContadorApp(MDApp):
    def build(self):
        self.contador = 0

        layout = MDBoxLayout(orientation="vertical", spacing=20, padding=20)

        toolbar = MDTopAppBar(title="Contador KivyMD")
        layout.add_widget(toolbar)


        self.label = MDLabel(
            int(self.contador),    
            halign="center",
            font_style="H3"
        )
        layout.add_widget(self.label)


        btn_layout = MDBoxLayout(spacing=20)
        btn_mas = MDRaisedButton(text="+", on_release=self.incrementar)
        btn_menos = MDRaisedButton(text="-", on_release=self.reducir)
        btn_layout.add_widget(btn_menos)
        btn_layout.add_widget(btn_mas)

        layout.add_widget(btn_layout)

        screen = Screen()
        screen.add_widget(layout)
        return screen

    def incrementar(self, instance):
        self.contador += 1
        self.label.text = str(self.contador)

    def reducir(self, instance):
        self.contador -= 1
        self.label.text = str(self.contador)

ContadorApp().run()