from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesKmApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        text = self.root.ids.input_miles.text

        try:
            value = float(text)
        except ValueError:
            value = 0

        value += change
        self.root.ids.input_miles.text = str(value)

        self.handle_convert()

    def handle_convert(self):
        text = self.root.ids.input_miles.text

        try:
            miles = float(text)
        except ValueError:
            miles = 0

        km = miles * MILES_TO_KM
        self.output_km = f"{km}"


MilesKmApp().run()