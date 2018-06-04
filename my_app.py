import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line
import serial,time
global ser
ser=serial.Serial('COM7',9600)

ser.write('L')
#arduino code:
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

class Circly(Widget):
      
    def on_touch_down(self, touch):   #self refers to the widget, touch to the the tough motion event#on_touch_down is the function called by kivy when you touch. It's name is standard(not variable)
            
            print(touch)
            print self.center_x,'cwnt x'
            print App.get_running_app().SIZ,'siz'
            
            xc=touch.x
            yc=touch.y
            xc1=(float(xc)-self.center_x)**2
            yc1=(float(yc)-self.center_y)**2

            print "xc,yc,xcl,ycl"
           # print xc,yc,xcl,ycl
            if xc1 +yc1 <= (App.get_running_app().SIZ/2)**2:      #make sure the size here is same as that in kv file
                print True
                ser.write('H')
                
                ser.write('L')
            else:
                print False
                
            
class MyCrowApp(App):
    SIZ=400
    def build(self):
        return Circly()
 

if __name__ == '__main__':
    MyCrowApp().run()
