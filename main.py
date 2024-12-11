from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget

class InvestmentsManagerWindow(Widget):
    pass

class InvestmentsApp(App):
    def build(self):
        Window.maximize()
        return InvestmentsManagerWindow()
        

if __name__ == '__main__':
    InvestmentsApp().run()