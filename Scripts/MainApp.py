from kivy.app import App

from Scripts.RootWidget import RootWidget


class MainApp(App):

    def build(self):
        return RootWidget()
