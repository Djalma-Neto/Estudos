#include <SoftwareSerial.h>

SoftwareSerial lora(18,19); // TX, RX
const int T = 2000;
int ultimo = 0;

void setup(){
  Serial.begin(9600);
  lora.begin(9600);
}
 
void loop(){
  String menssagem = Serial.readString();
  Enviar(menssagem);
  Receber();
}

void Enviar(String menssagem){
  if(menssagem == NULL)return;
  while (true){
    if (millis() - ultimo > T){
        lora.println(menssagem);
        Serial.println("Você: " + menssagem);
      }
      else{
        return;
      }
      ultimo = millis();
    }
}

void Receber(){
  String menssagem = lora.readString();
  if(menssagem == "")return;
  digitalWrite(led, HIGH);
  digitalWrite(led, LOW);
  digitalWrite(led, HIGH);
  digitalWrite(led, LOW);
  Serial.println("Outro: " + menssagem);
}
