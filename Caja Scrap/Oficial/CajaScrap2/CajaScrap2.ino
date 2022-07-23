#include <SPI.h>      // incluye libreria bus SPI
#include <MFRC522.h>      // incluye libreria especifica para MFRC522

/*NOTAS:
   Cuando cargo el programa los imanes de los sensores no tienen q estar cerca de los mismos pq sino generar error(ni idea de pq es asi)
*/

//----Para Arduino Uno----
#define RST_PIN  9      // constante para referenciar pin de reset
#define SS_PIN  10      // constante para referenciar pin de slave select

//----Pines de Sensores y Control----
#define cerraduraPuertaTrasera 18 //Pin para controlar cerradura de puerta trasera
#define cerraduraPuertaInterna 19 //Pin para controlar cerradura de puerta trasera
#define pulsador 17  //Pulsador para iniciar maquina de estado
#define senMagExterno 16 //Sensor magnetico externo
#define senMagInterno 15 //Sensor magnetico interno
#define senPosicion 14 //Sensor Posicion de la pieza
#define senPuertaTrasera 0//Sensor puerta trasera
#define clkCont 7 //Clock Contador
#define resetCont 8 // Reset del contador de los 7 segmentos

//----Estados-----
#define Estado0 0
#define Estado1 1
#define Estado2 2
#define Estado3 3
#define Estado4A 4
#define Estado4B 5
#define Estado5 6

//----Constantes----
#define topePiezas 2//Nro de piezas maximo que admite la caja

//--Variables Globales--
byte estadoActual = Estado0;

MFRC522 mfrc522(SS_PIN, RST_PIN); // crea objeto mfrc522 enviando pines de slave select y reset

void setup() {
  Serial.begin(9600);     // inicializa comunicacion por monitor serie a 9600 bps
  SPI.begin();        // inicializa bus SPI
  mfrc522.PCD_Init();     // inicializa modulo lector  
  
  //**********************************************
  //******Defino Pines de Entradas y Salidas******
  //**********************************************

  //----Puerta Externa Delantera-----
  pinMode(senMagExterno, INPUT);  //sensor magnetico externo

  //----Puerta Interna-----
  pinMode(senMagInterno, INPUT);  //sensor magnetico interno
  pinMode(cerraduraPuertaInterna, OUTPUT);  //Cerradura Puerta Interna

  //----Puerta Externa Trasera----
  pinMode(senPuertaTrasera, INPUT); //Sensor Puerta Caja de Scrap
  pinMode(cerraduraPuertaTrasera, OUTPUT); //Activar/Desactivar cerradura

  //----Contador----
  pinMode(clkCont, OUTPUT);  //clk contador
  pinMode(resetCont, OUTPUT);  //reset contador

  //----Pulsador de Inicio----
  pinMode(pulsador, INPUT);  //pulsador

  //----Sensor Posicion----
  pinMode(senPosicion, INPUT);  //sensor posicion


  //***************************************************
  //*************Configuraciones Iniciales*************
  //***************************************************
  //Nota: Inicializar todas las salidas que tengan rele o bobina antes de un delay para el contador de lo contrario el programa no reconoce la tarjeta magnetica
  //----Cerraduras Activa----
  digitalWrite(cerraduraPuertaTrasera, HIGH); //Inicializo a Cero
  digitalWrite(cerraduraPuertaInterna, HIGH); //Inicializo a Cero
  
  //----Inicializo Clock del Contador a Cero----
  digitalWrite(clkCont, LOW); //Inicializo a cero el clk del contador a cero

  //----Reseto Contador----
  digitalWrite(resetCont, HIGH); //Inicializo a cero
  delay(10);
  digitalWrite(resetCont, LOW); //Inicializo a cero
  
}

void loop() {
  // put your main code here, to run repeatedly:
  //static int estados=Estado0; // el static evita el reinicio de la variable cada vez que entra al loop guardando su valor
  transicionEstado();
  maquinaEstado();
}

bool llaveMagnetica() {
  /*Metodo para leer la llave magnetica y determinar si es la correcta*/
  //Los espacios estan incluidos por el programa de prueba
  String tar = ""; //Donde se almacena codigo de lectura del sensor de tarjeta/llavero
  String llavero = " 249 212 142 193"; //Codigo de identificacion del llavero: F9 D4 8E C1 y en decimal 249 212 142 193
  String tarjeta = " 182 255 207 43"; //Codigo de identificacion de la tarjeta: B6 FF CF 2B y en decimal 182 255 207 43
  bool bandera = false;
  if ( ! mfrc522.PICC_IsNewCardPresent()) // si no hay una tarjeta presente
    return false;         // retorna al loop esperando por una tarjeta

  if ( ! mfrc522.PICC_ReadCardSerial())   // si no puede obtener datos de la tarjeta
    return false;         // retorna al loop esperando por otra tarjeta

  for (byte i = 0; i < mfrc522.uid.size; i++) { // bucle recorre de a un byte por vez el UID
    if (mfrc522.uid.uidByte[i] < 0x10) {  // si el byte leido es menor a 0x10
    }
    else {        // sino
      tar = tar + " ";
    }
    tar = tar + mfrc522.uid.uidByte[i]; // imprime el byte del UID leido en hexadecimal
  }
  if (tar == llavero or tar == tarjeta) { //Se verifica que sea el llavero y/o tarjeta correcta
    bandera = true; //Si la tarjeta es correcta
  }
  else {
    bandera = false; //Si no es la tarjeta correcta o no hay
  }
  tar = ""; //Limpio variable
  mfrc522.PICC_HaltA();                   // detiene comunicacion con tarjeta
  return (bandera);
}

void transicionEstado() {
  /*Metodo para que implementa la logica de las transiciones entre estados y define el estado que se va a ejecutar*/
  //----Variables----
  bool p = digitalRead(pulsador); //pulsador
  bool sl1 = digitalRead(senMagExterno); //sensor magnetico externo delantero
  bool sl2 = digitalRead(senMagInterno); //sensor magnetico interno
  bool sp = digitalRead(senPosicion); //sensor posicion
  bool spt = digitalRead(senPuertaTrasera); //sensor magnetico puerta trasera
  //----Transicion de Estados----
  if (p == 0 and spt == 1 and estadoActual == Estado0) { //Transicion del estado 0 al 1
    estadoActual = Estado1;  
  } else if (p == 1 and spt == 0 and estadoActual == Estado0) { //Transicion del estado 0 al 2
    estadoActual = Estado0;
  } else if (p == 1 and spt == 1 and estadoActual == Estado0) { //Me mantengo en el estado 0
    estadoActual = Estado2;
  } else if (p == 0 and spt == 0 and estadoActual == Estado1) { //Transicion del estado 1 al 0
    estadoActual = Estado0;
  } else if (p == 1 and spt == 1 and estadoActual == Estado1) { //Transicion del estado 1 al 2
    estadoActual = Estado2;
  } else if (sp == 0 and sl1 == 1 and sl2 == 1 and estadoActual == Estado2) { //Transicion del estado 2 al 3
    estadoActual = Estado3;
  } else if ((sp == 1 or sl1 == 0) and estadoActual == Estado2) { //Transicion del estado 2 al estado 0
    estadoActual = Estado0;
  } else if (sp == 1 and sl1 == 1 and estadoActual == Estado3) { //Transicion del estado 3 al 4A
    //and sl2==1: lo inclui al transicionar al estado 5 para eliminar el retardo de golpeteo dado la forma fisica de la traba
    estadoActual = Estado4A;
  } else if (sp == 1 and (sl1 == 0 or sl2 == 0) and estadoActual == Estado3) { //Transicion del estado 3 al 4B
    estadoActual = Estado4B;
  } else if (estadoActual == Estado4B and sp == 1 and sl1 == 1 and sl2 == 1) { //Transicion del estado 4B al estado 0
    //Elimine esto del if ya que esto es un else if y solo es para dar aviso
    estadoActual = Estado0;
    Serial.print('e');  //Envio caracter para informar que se dejo de violar la seguridad de la caja, este print va en realidad en el estado 0 o estado 1 pero para que no mande continuamente este serial print lo pongo aca
  } else if (sl2 == 1 and estadoActual == Estado4A) { //Transicion del estado 4A al 5
    estadoActual = Estado5;
  } else if (estadoActual == Estado5) { //Transicion del estado 5 al 6
    /*Acciones de transicion: Son las de transcion del 4A al 5 solo que como el if contempla la condicion mas el estado directamente ejecuto en la transicion*/
    estadoActual = Estado0;
  }
}

void maquinaEstado() {
  /*Ejecuta las acciones del estado correspondiente*/
  //--Variables--
  static int piezas = 0;
  switch (estadoActual) {
    case Estado0:
      estado_0();
      break;
    case Estado1:
      piezas = estado_1(piezas);
      break;
    case Estado2:
      estado_2();
      break;
    case Estado3:
      estado_3();
      break;
    case Estado4A:
      estado_4A();
      break;
    case Estado4B:
      estado_4B();
      break;
    case Estado5:
      piezas = estado_5(piezas);
      break;
    default:
      //Caso desconocido
      break;
  }
}

void estado_0() {
  /*Este metodo ejecuta las acciones del estado 1
    Acciones:No Hace Nada
  */
  digitalWrite(cerraduraPuertaTrasera, HIGH);
}

int estado_1(int piezas) {
  /*Este metodo ejecuta las acciones del estado 1
      -Acciones: *Leer Tarjeta Magnetica
                 Retirar piezas si se abre la puerta trasera
                 Resetear contador segun sea el caso
  */
  
  bool banderaAux1 = false; //Bandera para saber si esta abierta o no la caja
  bool spt = digitalRead(senPuertaTrasera); //sensor magnetico puerta trasera
  banderaAux1 = llaveMagnetica();
  if (banderaAux1 == true) { //Si se la tarjeta magnetica es la correcta
    digitalWrite(cerraduraPuertaTrasera, LOW);
    Serial.print('b');  //Envio caracter para informar que se retiraron las piezas por puerto serial a Rpi
    delay(3000);  //Retardo para poder abrir la puerta
    spt = digitalRead(senPuertaTrasera); //sensor magnetico puerta trasera
    while (spt == 0) {
      spt = digitalRead(senPuertaTrasera); //sensor magnetico puerta trasera
      delay(5); //Delay de 5 ms para NO poner el bucle while a todo lo que da
    }
    delay(750);  //Retardo para poder cerrar la puerta
    digitalWrite(cerraduraPuertaTrasera, HIGH);
    Serial.print('c');  //Envio caracter para informar que se retiraron las piezas por puerto serial a Rpi
    digitalWrite(resetCont, HIGH);
    delay(10);
    digitalWrite(resetCont, LOW);
    piezas = 0;
  } else {
    digitalWrite(cerraduraPuertaTrasera, HIGH);
  }
  return (piezas);
}

void estado_2() {
  /*Este metodo ejecuta las acciones del estado 2
      -Acciones: Cerrar Puerta Trasera
  */
  digitalWrite(cerraduraPuertaTrasera, HIGH);
}

void estado_3() {
  /*Este metodo ejecuta las acciones del estado 3
      -Acciones: *Desactivar traba interna y retardo
  */
  bool sl1;
  bool sl2;
  bool sp;
  /*Podria Quitar este estado y no pasa nada*/
  digitalWrite(cerraduraPuertaInterna, LOW);  //Desactivo traba interna
  delay(3000);  //Retardo para que baje la tapa, TENGO QUE VER SI INCLUYO EL GOLPETEO
}

void estado_4A() {
  /*Este metodo ejecuta las acciones del estado 4A
      -Acciones: Activar traba interna
  */
  digitalWrite(cerraduraPuertaInterna, HIGH); //Activo traba interna
}

void estado_4B() {
  /*Este metodo ejecuta las acciones del estado 4B
      -Acciones: Enviar mensaje de violacion de la caja
  */
  Serial.print('f');
  digitalWrite(cerraduraPuertaInterna, HIGH); //Activo traba interna
}

int estado_5(int piezas) {
  /*Este metodo ejecuta las acciones del estado 5
      -Acciones de transicion: *Enviar caracter de pieza depositada
                                Actualizar contador de piezas
                                Envio aviso de caja llena si se llena el contador
  */
  //Serial.println("Incremento contador");
  //----Incrementar Contador----
  digitalWrite(clkCont, HIGH);
  delay(10);
  digitalWrite(clkCont, LOW);
  piezas = piezas + 1;
  //----Envio caracter por puerto serial a Rpi----
  Serial.print('a'); //Ingreso una pieza
  if (piezas >= topePiezas) {
    delay(10); //Espero un poco para que haya tiempo de escribir en la tabla sql
    Serial.print('d'); //Limite piezas dentro de la caja superados
  }
  return (piezas);
}
