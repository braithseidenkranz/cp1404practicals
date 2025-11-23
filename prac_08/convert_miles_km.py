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
        value = self.get_valid_miles()

        value += change
        self.root.ids.input_miles.text = str(value)

        self.handle_convert()

    def handle_convert(self):
        miles = self.get_valid_miles()

        km = miles * MILES_TO_KM
        self.output_km = f"{km}"

    def get_valid_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesKmApp().run()