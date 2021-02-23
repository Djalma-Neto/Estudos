#include <SoftwareSerial.h>

SoftwareSerial lora(18,19); // TX, RX
const int led = 13;
const int T = 2000;
int ultimo = 0;
int cont = 0;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  lora.begin(9600);
}
 
void loop(){
  cont++;
  String menssagem = ("MENSSAGEM - " + String(cont));
  Enviar(menssagem);
}

void Enviar(String menssagem){
  if(menssagem == NULL)return;
  while (true){
    if (millis() - ultimo > T){
        lora.println(menssagem);
        Serial.println("ENVIADO: " + menssagem);
      }
      else{
        return;
      }
      ultimo = millis();
    }
}
