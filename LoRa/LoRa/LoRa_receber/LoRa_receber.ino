
#include <SoftwareSerial.h>
#include <LoRa.h>
#define M0 26
#define M1 27

SoftwareSerial lora(18,19); // TX, RX
void setup() {
  
  pinMode(M0,OUTPUT);
  pinMode(M1,OUTPUT);
  Serial.begin(9600);
  lora.begin(9600);
}
 
void loop() {
  digitalWrite(M0,LOW);
  digitalWrite(M1,LOW);
  Receber();
}
void Receber(){
  String menssagem = lora.readString();
  if(menssagem != ""){
    Serial.println("Recebido: " + menssagem);
  }else{
    return;
  }
}
