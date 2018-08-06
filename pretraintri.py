import kivy,datetime
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line,Fbo,Rectangle
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
import serial,time
#global ser
#ser=serial.Serial('COM7',9600)

#ser.write('L')

'''
#Physical pixel
const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}

'''




class Triangle(Widget):
    area =  40000
    circum_radius= NumericProperty(((4*(area))/(3*(3**0.5)))**0.5)
    def __init__(self, **kwargs):
        super(Triangle,self).__init__(**kwargs)
        self.nextt='o'

    
    
    #circum_radius,R= ((4*(area))/(3*(3**0.5)))**0.5 mathematically correct
    #circum_radius is defined in .kv
    # then the co-ordinates of the triangle are:(0,R),(-root(3)R/2,-R/2),(root(3)R/2,-R/2)
    def on_touch_down(self, touch):   #self refers to the widget, touch to the the tough motion event#on_touch_down is the function called by kivy when you touch. It's name is standard(not variable)
          if  self.nextt =='o': 
                print(touch)
                                        
                x=touch.x
                y=touch.y

                x1,y1,x2,y2,x3,y3 = self.center_x,self.center_y + self.circum_radius , self.center_x - 0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius  , self.center_x +0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius
                print x1,y1,x2,y2,x3,y3
                print 'x1,y1,x2,y2,x3,y3'
                a=(x-x1)-((y-y1)*((x2-x1)/(y2-y1)))
                a1=(x3-x1)-((y3-y1)*((x2-x1)/(y2-y1)))
                b=(x-x1)-((y-y1)*((x3-x1)/(y3-y1)))
                b1=(x2-x1)-((y2-y1)*((x3-x1)/(y3-y1)))
                c=y-y3   #(y3=y2, the third lines equation is y=y3)
                c1=y1-y3
                if a*a1>=0 and b*b1>=0 and c*c1>=0:
                    print 'inside_triangle'
                    current1=datetime.datetime.now()
                    self.nextt=current1+datetime.timedelta(0,3,0,0)
                                            #datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]]

                    with self.canvas.after:     #to add a screen to the  canvas, canvas.after appears above canvas
                            Color(1, 1, 1)
                            Rectangle(pos=self.pos, size=self.size)
                else:
                    print 'nope'
                    
    def update(self,dt):        #just check why is it necesaary to add dt, it is not working without dt
        if self.nextt!='o':
            if datetime.datetime.now().time() > self.nextt.time():
                self.canvas.after.clear()
                self.nextt='o'
        
        
from kivy.lang import Builder
kv_string= '''
#:kivy 1.10.0
<Triangle>:
	canvas.before:
        Color:
            rgba: 1, 1, 1 , 1
        Rectangle:
            pos: self.pos
            size: self.size
	canvas:
		Color:
			rgb:1,0,0
		Triangle:
			points: self.center_x, self.center_y + self.circum_radius , self.center_x - 0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius  , self.center_x +0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius
'''
#points: self.center_x, self.center_y + self.circum_radius , self.center_x - 0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius  , self.center_x +0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius

Builder.load_string(kv_string)
    
class PreTrainApp(App):
    def build(self):
        tri=Triangle()
        Clock.schedule_interval(tri.update, 1.0 / 60.0)
        return tri
    
if __name__ == '__main__':
    PreTrainApp().run()
