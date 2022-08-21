#define red_led 9
#define green_led 10
#define blue_led 11
#define BLUE_led 13
#define RED_led 12

void setup() {
  pinMode(red_led, 1);
  pinMode(green_led, 1);
  pinMode(blue_led, 1);
  pinMode(BLUE_led, 1);
  pinMode(RED_led, 1);




  Serial.begin(9600);

  Serial.println("Goodnight moon!");
}
void loop() { // run over and over
  if (Serial.available()) {
    char data = Serial.read();
    Serial.println(data);
    if (data == 'R') {
      digitalWrite(red_led, HIGH);
    }
    if (data == 'r') {
      digitalWrite(red_led, LOW);
    }
    if (data == 'G') {
      digitalWrite(green_led, HIGH);
    }
    if (data == 'g') {
      digitalWrite(green_led, LOW);
    }
    if (data == 'B') {
      digitalWrite(blue_led, HIGH);
    }
    if (data == 'b') {
      digitalWrite(blue_led, LOW);
    }
    if (data == '1') {
      digitalWrite(BLUE_led, HIGH);
    }
    if (data == '2') {
      digitalWrite(BLUE_led, LOW);
    }
    if (data == '3') {
      digitalWrite(RED_led, HIGH);
    }

    if (data == '4') {
      digitalWrite(RED_led, LOW);
    }
  }
}
