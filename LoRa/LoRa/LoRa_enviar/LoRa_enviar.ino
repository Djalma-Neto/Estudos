#include <SoftwareSerial.h>

SoftwareSerial lora(18,19); // TX, RX
const int T = 1000;
int ultimo = 0;

int cont = 0;

#define M0 26
#define M1 27

void setup(){
  pinMode(M0,OUTPUT);
  pinMode(M1,OUTPUT);
  Serial.begin(9600);
  lora.begin(9600);
}
 
void loop(){
  digitalWrite(M0,LOW);
  digitalWrite(M1,LOW);
  String menssagem = (String)"olá"+" "+cont;
  Enviar(menssagem);
}

void Enviar(String menssagem){
  if(menssagem == "")return;
  while (true){
    if (millis() - ultimo > T){
        lora.print(menssagem);
        Serial.println("Enviando: " + menssagem);
        cont++;
      }
      else{
        return;
      }
      ultimo = millis();
    }
}
