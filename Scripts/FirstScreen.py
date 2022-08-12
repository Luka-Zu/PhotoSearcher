from kivy.uix.screenmanager import *
import wikipedia
import requests


class FirstScreen(Screen):

    def search(self):
        # Get user query from text input
        query = self.manager.current_screen.ids.user_query.text

        # Get wikipedia page and first image URL
        page = wikipedia.page(query)
        image_link = page.images[0]

        print(image_link)

        # Download the Image

        req = requests.get(image_link, stream=True)

        with open("G.jpg", 'wb') as file:

            file.write(req.content)

        self.manager.current_screen.ids.img.source = 'G.jpg'
