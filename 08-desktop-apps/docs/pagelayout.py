from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class MyPageLayout(PageLayout):

    def print_hola(self):
        print("hola") 

class PageLayoutApp(App):
    
    def build(self):
        return MyPageLayout()
 
if __name__=="__main__":
  app = PageLayoutApp()
  app.run()