hola profe

El intento de usar KivyMD es correcto, pero falla al importar Screen (debería ser MDScreen o importarse desde kivy.uix.screenmanager) y al crear la etiqueta con MDLabel(int(self.contador)) en lugar de usar text=str(...). Corrige esas importaciones, usa el parámetro text= con un string, y renombrá tu script. Por ejemplo, a main.py o contador_app.py (¡nunca kivy.py!).
