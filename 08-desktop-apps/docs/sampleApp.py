import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class WidgetExample(BoxLayout):

    counter = 0
    label_text = StringProperty(str(counter))
    
    def do_state(self, widget):
        print("do_state starts")
        if widget.state == "normal":
            widget.text = "OFF"
        else:
            widget.text = "ON"

    def do_click(self):
        self.counter += 1
        self.label_text = str(self.counter)
    

class SampleApp(App):
    pass

 
def main():
    app = SampleApp()
    app.run()

if __name__ == "__main__":
    main()
