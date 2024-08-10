const int voltageSensorPin = A3;
float vIn;
float vOut;
float voltageSensorVal;
const float factor = 4.6;
const float vCC = 5.00;

void setup() {
  Serial.begin(9600);
}

void loop() {
  voltageSensorVal = analogRead(voltageSensorPin);
  vOut = (voltageSensorVal / 1024) * vCC;
  vIn =  vOut * factor;

  Serial.println(vIn);

  delay(1000);
}
