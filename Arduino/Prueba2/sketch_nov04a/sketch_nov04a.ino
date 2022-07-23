

void setup() {
  Serial.begin(9600);     // inicializa comunicacion por monitor serie a 9600 bps
  pinMode(8, OUTPUT); //Activar/Desactivar cerradura
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(8, HIGH);
  delay(500);
  digitalWrite(8, LOW);
  delay(500);
}
