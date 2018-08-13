import kivy,datetime
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line,Fbo,Rectangle
from kivy.clock import Clock
from kivy.properties import NumericProperty
import serial,time
import math
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




class Elly(Widget):
    area =  40000
    a_int=150 #width/2 (because int and numericproperty can't be multiplied)
    a=NumericProperty(a_int)      #width/2
    b= NumericProperty((area/(a_int*math.pi)))    #height/2    
    #(size reference: a=100, b=127.32, area = pi.a.b = 40000)
    def __init__(self, **kwargs):
        super(Elly,self).__init__(**kwargs)
        self.nextt='o'
        
    
    
    
    def on_touch_down(self, touch):   #self refers to the widget, touch to the the tough motion event#on_touch_down is the function called by kivy when you touch. It's name is standard(not variable)
          if  self.nextt =='o': 
                print(touch)
                                       
                xc=touch.x
                yc=touch.y
                xc1=((float(xc)-self.center_x)**2)/(self.a**2)
                yc1=(float(yc)-self.center_y)**2/(self.b**2)

                print "xc,yc,xcl,ycl"
                # print xc,yc,xcl,ycl
                if xc1 +yc1 <= 1:  
                    print 'inside_circle'
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
<Elly>:
    canvas.before:
        Color:
            rgba: 1, 1, 1 , 1
        Rectangle:
            pos: self.pos
            size: self.size
    canvas:
        Color:
            rgb:1,0,0
        Ellipse:
            pos:self.center_x - self.a,self.center_y - self.b
            size:2*self.a,2*self.b
'''
#points: self.center_x, self.center_y + self.circum_radius , self.center_x - 0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius  , self.center_x +0.866025*self.circum_radius , self.center_y -0.5*self.circum_radius

Builder.load_string(kv_string)
    
class PreTrainApp(App):
    def build(self):
        el=Elly()
        Clock.schedule_interval(el.update, 1.0 / 60.0)
        return el
    
if __name__ == '__main__':
    PreTrainApp().run()
