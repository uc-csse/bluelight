void setup() {
  // put your setup code here, to run once:
  SerialUSB.begin(115200*5);
  Serial1.begin(115200*3);
  pinMode(LED_BUILTIN, OUTPUT);
  while (!SerialUSB) ;
  delay(2000);

}

int incomingByte = 0;

void loop() {
  // put your main code here, to run repeatedly:
  //if (SerialUSB.available() > 0) {
    //digitalWrite(LED_BUILTIN, HIGH);
    // read the incoming byte:
    //incomingByte = SerialUSB.read();
    //SerialUSB.println(incomingByte, DEC);
    //Serial1.write(incomingByte);
  //}

  while(SerialUSB.available()) {
    Serial1.write(SerialUSB.read());
  }
}

