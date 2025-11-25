from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class CounterApp(App):
    def build(self):
        self.count = 0
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Count: 0", font_size=30)
        layout.add_widget(self.label)

        button = Button(text="Increment", font_size=24)
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)

        return layout
    def increment_counter(self, instance):
        self.count += 1
        self.label.text = f"Count: {self.count}"

if __name__ == "__main__":
    CounterApp().run()