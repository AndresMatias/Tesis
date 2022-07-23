void setup() 
{ 
  Serial.begin(9600);
  // Configurar Serial3 para el bus RS-485
  //Serial3.begin(9600);
} 
 
void loop() 
{ 
  //Serial.print('\n'); //envio caracter a cada 100 ms
  Serial.print('a');
  delay(1000);                           
} 
