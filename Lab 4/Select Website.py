import webbrowser
import random

websites = ["www.facebook.com","www.google.com","www.amazon.com","www.w3schools.com"]

url = random.choice(websites)

webbrowser.open(url)