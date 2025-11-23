from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Braith", "Arabella", "Julius", "Alice"]

    def build(self):
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

        return self.root

DynamicLabelsApp().run()