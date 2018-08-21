
#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
int incoming;
void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(120);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  
  if (Serial.available() >0){
  incoming=Serial.read();
  // step one revolution  in one direction:

  if (incoming == 'O'){
  myStepper.step(2750);//opens door  , 2750 for 11 cm, lead of screw = 8mm , therefore number of steps=(110/8)*200 ,number of revolutions = 13.75
  delay(5000);
  myStepper.step(-2750);// closes door
  
  digitalWrite(8,LOW); // so that current doesn't flow into the driver when it is idle; prevents heating up.
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  
  }
 }
}

