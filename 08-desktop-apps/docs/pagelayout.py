from kivy.app import App
from kivy.uix.pagelayout import PageLayout
 

class PageLayoutApp(App):
    def build(self):
        return PageLayout()
 
if __name__=="__main__":
  app = PageLayoutApp()
  app.run()