from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class ProductSearchApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.search_input = TextInput(hint_text="Search products")
        layout.add_widget(self.search_input)
        search_button = Button(text="Search")
        search_button.bind(on_press=self.search_products)
        layout.add_widget(search_button)
        self.results_label = Label(text="")
        layout.add_widget(self.results_label)
        return layout

    def search_products(self, instance):
        query = self.search_input.text
        response = requests.get(f"http://localhost:5000/search?query={query}")
        results = response.json()
        self.results_label.text = "\n".join([product["name"] for product in results])

if _name_ == "_main_":
    ProductSearchApp().run()
