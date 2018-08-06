
void setup() {
  // put your setup code here, to run once:
  SerialUSB.begin(115200*5);
  Serial1.begin(115200*3);
  //while (!Serial1) {
  //   delay(30);
  //}
  while (!SerialUSB) ;
  pinMode(LED_BUILTIN, OUTPUT);
  delay(2000);
}

int incomingByte = 0;

void loop() {
  //if (Serial1.available() > 0) {
    //digitalWrite(LED_BUILTIN, HIGH);
    //incomingByte = Serial1.read();
    //digitalWrite(LED_BUILTIN, LOW);
    //Serial.print("I received: ");
    //SerialUSB.println(incomingByte, DEC);
    //SerialUSB.write(incomingByte);
    
    //digitalWrite(LED_BUILTIN, LOW);
  //}
    while(Serial1.available()) {
    SerialUSB.write(Serial1.read());
  }

}
