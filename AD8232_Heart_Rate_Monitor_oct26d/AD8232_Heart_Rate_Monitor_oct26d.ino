/*AD8232 HEART RATE MONITOR 
 * https://learn.sparkfun.com/tutorials/ad8232-heart-rate-monitor-hookup-guide
 * https://www.dfrobot.com/product-1510.html
 * 
 * 
*/
void setup() {
  // put your setup code here, to run once:
  //initialize the serial communication:
  Serial.begin(9600);
  pinMode(10, INPUT); //Setup for leads off detection L0 +
  pinMode(11, INPUT); //Setup for leads off detection L0 -
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long startTime = micros();
  if((digitalRead(10) == 1) || (digitalRead(11) == 1)){
    Serial.println("!");
  }
  else{
    //send the value of analog input 0:
    Serial.println(analogRead(A0));
  }
  //wait for a bit to keep serial data form saturating
  delay(1);
  unsigned long endTime = micros();
  Serial.println(endTime - startTime);
}
