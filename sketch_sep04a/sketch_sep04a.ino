
void setup() {
  Serial.begin(57600);
  Serial.println("Goodnight moon!");
}

void loop() {
   int pot = analogRead(A1);
   pot = map(pot, 0, 1023, 0, 100);
   Serial.println(pot);
   delay(100);
   
}



