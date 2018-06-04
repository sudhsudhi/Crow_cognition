'''
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.button import ButtonBehavior
from kivy.lang import Builder
from kivy.graphics import Triangle
from kivy.graphics import Color

Builder.load_string("""

<TwoColorsButton>:
    size_hint: None,None
    size: 250,250
    font_size: '26dp'  
    canvas.before:
        Color:
            rgba:0.5,0,0,1
        Triangle:
            points: [0,0, 0,root.size[1], root.size[0],0] 
        Color:
            rgba:0,0,0.5,1 
        Triangle:
            points: [0,root.size[1],root.size[0],root.size[1],root.size[0],0]
    text:'click me'
    on_press:print "I've been pressed"
""")

class TwoColorsButton(ButtonBehavior,Label):
    pass

class TwoColorsApp(App):
    def build(self):
        my_button = TwoColorsButton()
        return my_button

if __name__ == '__main__':
    TwoColorsApp().run()
'''
class Triangle(object):
    
    def __init__(self):
        self.area =  0
        self.circum_radius= ((4*(self.area))/(3*(3**0.5)))**0.5 
    
    #circum_radius= ((4*(area))/(3*(3**0.5)))**0.5 mathematically correct
    #circum_radius is defined in .kv
    def update(self):
        pass
        
