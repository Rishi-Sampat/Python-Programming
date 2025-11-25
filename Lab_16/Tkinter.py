import tkinter as tk
def say_hello():
    print("Hello, Tkinter!")
root = tk.Tk()
btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack()
root.mainloop()


from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text='Click Me', on_press=lambda x: print("Hello, Kivy!"))
    
MyApp().run()