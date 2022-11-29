from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider



class MainApp(App):

    def build(self):
        root = Widget()
        root.add_widget(
            Slider(
                min=0,
                max=100,
                value=25,
                step=1,
                size=(450, 32),
                value_track=True,
                value_track_color=[0.2, 0.8, 0.4, 1],
            )
        )
        return root
                

if __name__ == '__main__':
    app = MainApp(title="Ejemplo de slider") 
    app.run()
