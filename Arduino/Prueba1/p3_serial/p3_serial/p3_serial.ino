void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); //Configuro Salida
  digitalWrite(LED_BUILTIN, LOW);    // Apagado
}

void loop() {
  delay(30);
  if (Serial.available()) {
    char angulo = Serial.read(); //Leemos el dato recibido
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  }
}
