
void setup() {
  Serial.begin(115200);  
}

void loop() { 
   //guarda o valor lido do sensor hall
   int measurement = 0; 
   //faz a leitura do sensor hall
   measurement = hallRead();
   Serial.print("Imprime a medida: ");
   Serial.println(measurement);
  
   delay(100);
}
