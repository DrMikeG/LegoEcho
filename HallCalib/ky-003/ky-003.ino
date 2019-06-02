/***************************************************

Hall Effect magnetic switch, a magnet is used to turn on the onboard Led

Hall Effect board is from Keyes. KY-003

Connection:
Pin 1 connect to Arduino Gnd
Pin 2 connect to Arduino 5 volts
Pin 3 marked S connect to Arduino pin D6

Let's understand what we just did here.

The KY-003 has a resistor and an LED and seems to support digital output
This means we can plug it in to pin D6 and use digital read.
"Reads the value from a specified digital pin, either HIGH or LOW."
"Returns HIGH or LOW"

We use pinMode(INPUT)

The board seems to pull the output HIGH
HIGH = 1
LOW = 0.

***************************************************/

# define hallPin 6
# define ledPin 13

void setup() {
  Serial.begin(9600);
  pinMode(hallPin, INPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
}

void loop() {
  
  if ( LOW == digitalRead(hallPin)) {
    Serial.println("Magnetic field detected");
    digitalWrite(ledPin, LOW); // turn on LED
  } else {
    
    digitalWrite(ledPin, HIGH);
  }
}
