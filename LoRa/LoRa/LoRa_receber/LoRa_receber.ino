#include <SoftwareSerial.h>

SoftwareSerial lora(18,19); // TX, RX
const int led = 13;
const int T = 2000;
int ultimo = 0;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  lora.begin(9600);
}
 
void loop(){
  Receber();
}

void Receber(){
  String menssagem = lora.readString();
  if(menssagem == "") return;
  Serial.println("RECEBIDO: " + menssagem);
}
