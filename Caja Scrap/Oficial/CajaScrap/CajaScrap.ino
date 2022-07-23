#include <SPI.h>      // incluye libreria bus SPI
#include <MFRC522.h>      // incluye libreria especifica para MFRC522

//----Para Arduino Uno----
#define RST_PIN  9      // constante para referenciar pin de reset
#define SS_PIN  10      // constante para referenciar pin de slave select

//----Estados-----
#define Estado1 1 //Tapa Exterior Abierta
#define Estado2 2 //Cerrando Tapa Exterior
#define Estado3 3 //Tapa Exterior Cerrada
#define Estado4 4 //Fallo en algun sensor y/o no es la pieza correcta
#define Estado5 5 //Todo Correcto en los sensores de pieza y se compuerta interna
#define Estado6 6 //Retardo del golpeteo de la puerta interna
#define Estado7 7 //Termino de cerrar la compuerta interna y empeiza a abrir la compuerta externa

//----Variables----
int Estados=Estado1; // Estado actual

MFRC522 mfrc522(SS_PIN, RST_PIN); // crea objeto mfrc522 enviando pines de slave select y reset

void setup() {
  Serial.begin(9600);     // inicializa comunicacion por monitor serie a 9600 bps
  SPI.begin();        // inicializa bus SPI
  mfrc522.PCD_Init();     // inicializa modulo lector
  
  //----Pines de Sensores maquina de estado----
  pinMode(2, INPUT);  //pulsador
  pinMode(3, INPUT);  //sensor magnetico externo
  pinMode(4, INPUT);  //sensor magnetico interno
  //-------------------------------------
  //pinMode(5, INPUT);  //barrera laser
  pinMode(5, OUTPUT);  //barrera laser
  //-------------------------------------
  pinMode(6, INPUT);  //sensor posicion
  
  //----Pines de puerta externa para retirar piezas----
  pinMode(19, INPUT);  //Sensor Puerta Caja de Scrap
  pinMode(14, OUTPUT); //Activar/Desactivar cerradura

  
  
  //----Pines para controlar y resetear contador----
  pinMode(7, OUTPUT);  //clk contador
  pinMode(8, OUTPUT);  //reset contador

  //----Configuraciones Iniciales-----
  digitalWrite(7, LOW); //Inicializo a cero
  
  //Reseto Contador
  digitalWrite(8, HIGH); //Inicializo a cero
  delay(10);
  digitalWrite(8, LOW); //Inicializo a cero
  
  //Cerradura Activa
  digitalWrite(14, LOW); //Inicializo a Cero
}

void loop() {
  // put your main code here, to run repeatedly:
  static int x; // el static evita el reinicio de la variable cada vez que entra al loop guardando su valor
  static bool banderaPuerta=false; // Bandera para manejar la habilitacion de la puerta para retirar piezas
  static bool banderaEstado=false; // Bandera para que la maquina de estado no pueda salir del estado 1 en caso de que este abierta la tapa magnetica
  //llaveMagnetica();
  maquinaEstado();
  //digitalWrite(7, HIGH);
  //delay(10);
  //digitalWrite(7, LOW);
  //delay(1000);
}

void llaveMagnetica(){
  /*Metodo para leer la llave magnetica y determinar si es la correcta*/
  //Los espacios estan incluidos por el programa de prueba
  String tar=""; //Donde se almacena codigo de lectura del sensor de tarjeta/llavero
  String llavero=" 249 212 142 193"; //Codigo de identificacion del llavero: F9 D4 8E C1 y en decimal 249 212 142 193
  String tarjeta=" 182 255 207 43"; //Codigo de identificacion de la tarjeta: B6 FF CF 2B y en decimal 182 255 207 43
  bool bandera=false;
  
  bool banderaPuerta; //Estado de la puerta
  //banderaPuerta=estadoPuerta(); //determino el estado de la puerta
  
  if (Estados!=Estado1){ //Inabilita la la apertura de la puerta para retirar piezas si la maquina no esta en el estado 1
    return;
  }
  if ( ! mfrc522.PICC_IsNewCardPresent()) // si no hay una tarjeta presente
    return;         // retorna al loop esperando por una tarjeta
  
  if ( ! mfrc522.PICC_ReadCardSerial())   // si no puede obtener datos de la tarjeta
    return;         // retorna al loop esperando por otra tarjeta
    
  for (byte i = 0; i < mfrc522.uid.size; i++) { // bucle recorre de a un byte por vez el UID
    if (mfrc522.uid.uidByte[i] < 0x10){   // si el byte leido es menor a 0x10
      //Serial.print(" 0");     // imprime espacio en blanco y numero cero
      }
      else{         // sino
      tar=tar+" ";
      }
    tar=tar+mfrc522.uid.uidByte[i];  // imprime el byte del UID leido en hexadecimal  
  }
  if (tar==llavero or tar==tarjeta){ //Se verifica que sea el llavero y/o tarjeta correcta
    //Serial.println("Correcto");
    //Serial.print("A");     // imprime espacio en blanco y numero cero
    //----------------------Manejo de seguro mas tiempo de espera----------------------------
    digitalWrite(5, HIGH); //Saco Seguro
    delay(5000);
    digitalWrite(5, LOW); //Pongo Seguro
    
    //---------------------------------------------------------------------------------------
    //bandera=estadoPuerta(); //Determino si la puerta esta abierta o cerrada
    //if (bandera==true){ //Puerta Cerrada
       //No reseto contador
    //}
    //else{ //Puerta Abierta
      //Reseteo contador
    //}
  }
  tar=""; //Limpio variable
  mfrc522.PICC_HaltA();                   // detiene comunicacion con tarjeta
}

bool maquinaEstado(){
  /*Metodo para que implementa la logica de la maquina de estado*/
  //----Leo sensores de entrada y almaceno en variables----
  bool p=digitalRead(2); //pulsador
  bool sl1=digitalRead(3);; //sensor magnetico externo
  bool sl2=digitalRead(4);; //sensor magnetico interno
  //bool bl=digitalRead(5);; //barrera laser
  bool sp=digitalRead(6);; //sensor posicion
  //bool r=digitalRead(7);; //retardo de la tapa interna
  //bool banderaPuerta; //Estado de la puerta
  //bool banderaEstado=estadoPuerta(); //determino el estado de la puerta (1=true creo)
  //bool banderaEstado=0;
  
  /*Nota: esta maquina difiere un poco de la original por la llave magnetica*/
  //----Transicion de Estados----
  //if(p==1 and bl==1 and banderaEstado==0 and Estados==Estado1){//Transicion del estado 1 al 2
  //if(p==1 and banderaEstado==0 and Estados==Estado1){//Transicion del estado 1 al 2 //AGREGAR el IF de ARRIVA CUANDO CORRIJA BORNERA
  if(p==1 and Estados==Estado1){//Transicion del estado 1 al 2 //AGREGAR el IF de ARRIVA CUANDO CORRIJA BORNERA
    /*Acciones de transicion: Activar motor para cerrar tapa externa*/
    Estados=Estado2;
    //Serial.println("Estado 1 al 2");  
  }
  else if(sl1==1 and Estados==Estado2){//Transicion del estado 2 al 3
    /*Acciones de transicion: Desactivar motor para cerrar tapa externa*/
    Estados=Estado3;
    //Serial.println("Estado 2 al 3"); 
  }
  //else if((sp==0 or bl==0 or sl1==0) and Estados==Estado3){//Transicion del estado 3 al 7
  else if((sp==1 or sl1==0) and Estados==Estado3){//Transicion del estado 3 al 7
    /*Acciones de transicion: Nada*/
    Estados=Estado7;
    //Serial.println("Estado 3 al 7"); 
  }
  //else if(sp==1 and bl==1 and sl1==1 and Estados==Estado3){//Transicion del estado 3 al 4
  else if(sp==0 and sl1==1 and Estados==Estado3){//Transicion del estado 3 al 4
    /*Acciones de transicion: Nada*/
    Estados=Estado4;
    //Serial.println("Estado 3 al 4"); 
  }
  else if(sl2==1 and Estados==Estado4){//Transicion del estado 4 al 5
    /*Acciones de transicion: Desactivar traba de tapa interna*/
    Estados=Estado5;
    //Serial.println("Estado 4 al 5"); 
  }
  //else if(r==1 and Estados==Estado5){//Transicion del estado 5 al 6
  else if(Estados==Estado5){//Transicion del estado 5 al 6
    /*Acciones de transicion: Retardo de golpeteo en caso de no ser por hardware*/
    
    digitalWrite(5, HIGH); //Saco Seguro
    delay(2000); //Retardo para la tapa de golpeteo
    digitalWrite(5, LOW); //Pongo Seguro
    
    //----Incremento Contador de piezas----
    digitalWrite(7, HIGH);
    delay(10);
    digitalWrite(7, LOW);
    
    //----Envio caracter por puerto serial a Rpi----
    //Serial.print('a');
     
    Estados=Estado6;
    //Serial.println("Estado 5 al 6"); 
  }
  else if(sl2==1 and Estados==Estado6){//Transicion del estado 6 al 7
    /*Acciones de transicion: Activar traba tapa interna*/
    Estados=Estado7;
    //Serial.println("Estado 6 al 7"); 
  }
  else if(sl1==1 and Estados==Estado7){//Transicion del estado 7 al 1
    /*Acciones de transicion: Nada*/
    Estados=Estado1;
    //Serial.println("Estado 7 al 1");
    return(true); // Se habilita a la puerta magnetica en caso de querer abrirla
  }
  return(false); // Se inabilita la puerta para retirar piezas 
}

bool estadoPuerta(){
  /*Metodo que devuelve el estado de la puerta*/
  //---------------------------------------------------------------------------------
  //Nota: podria agregar una variable para determinar si la tarjeta concedio acceso de esa manera si no lo concedio y la peurta esta abierta significa q la puerta fue forzada CAMBIAR PIN
  //---------------------------------------------------------------------------------
  bool puerta=digitalRead(6); //Se determina si la puerta esta abierta o cerrada (VER LOGICA NEGADA IMPORTANTE)
  return puerta;
}
