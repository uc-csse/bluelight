#define LIGHTSENSORPIN A0 //Ambient light sensor reading 
#define SER_SPEED 1000000



byte analogReadFast(byte ADCpin)    // inline library functions must be in header
{ ADC->CTRLA.bit.ENABLE = 0;              // disable ADC
  while( ADC->STATUS.bit.SYNCBUSY == 1 ); // wait for synchronization

  int CTRLBoriginal = ADC->CTRLB.reg;
  int AVGCTRLoriginal = ADC->AVGCTRL.reg;
  int SAMPCTRLoriginal = ADC->SAMPCTRL.reg;
  
  ADC->CTRLB.reg &= 0b1111100011111111;          // mask PRESCALER bits
  ADC->CTRLB.reg |= ADC_CTRLB_PRESCALER_DIV64;   // divide Clock by 64
  ADC->AVGCTRL.reg = ADC_AVGCTRL_SAMPLENUM_1 |   // take 1 sample 
                     ADC_AVGCTRL_ADJRES(0x00ul); // adjusting result by 0
  ADC->SAMPCTRL.reg = 0x00;                      // sampling Time Length = 0

  ADC->CTRLA.bit.ENABLE = 1;                     // enable ADC
  while(ADC->STATUS.bit.SYNCBUSY == 1);          // wait for synchronization

  byte adc = analogRead(ADCpin); 
  
  ADC->CTRLB.reg = CTRLBoriginal;
  ADC->AVGCTRL.reg = AVGCTRLoriginal;
  ADC->SAMPCTRL.reg = SAMPCTRLoriginal;
   
  return adc;
}


void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LIGHTSENSORPIN,  INPUT);
  analogWrite(LED_BUILTIN,0);
  SerialUSB.begin(SER_SPEED); 
  while (!SerialUSB) ;
  delay(1000*5);
}

void loop() {
   byte reading = analogReadFast(LIGHTSENSORPIN); //Read light level
   //byte reading = analogRead(LIGHTSENSORPIN); //Read light level
   //byte reading = 70; //Read light level
  //float square_ratio = reading / 1023.0;      //Get percent of maximum value (1023)
  //square_ratio = pow(square_ratio, 2.0);      //Square to make response more obvious

  //analogWrite(LED_BUILTIN, 255.0 * square_ratio);  //Adjust LED brightness relatively
  SerialUSB.write(reading);                    //Display reading in serial monitor
}
