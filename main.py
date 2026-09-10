from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import requests

class CUgoldApp(App):
    def build(self):
        self.label = Label(text="CUgold 18 AUTO\nCLEAN DEFAULT\nLIVE...", font_size='20sp', markup=True, halign='center')
        Clock.schedule_interval(self.update, 4)
        self.update(0)
        return self.label
    def update(self, dt):
        try:
            p = requests.get("https://api.gold-api.com/price/XAU", timeout=5).json().get('price',0)
            self.label.text = f"[b][color=ffd700]CUgold 18 AUTO[/color][/b]\nXAUUSD ${p}\nBUY 2/18 Confirm\nSL -$3 TP +$9"
        except:
            self.label.text = "CUgold 18 AUTO\nConnecting..."
if __name__ == '__main__':
    CUgoldApp().run()
