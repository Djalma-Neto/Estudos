#include <WiFi.h>
#include <LiquidCrystal.h>

const char* SSID = "esp";

 
//nome da rede Wifi que o ESP irá buscar

//dB minimo para identificar a rede
#define MINdB -50
const int LED = 12;
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
 Serial.begin(9600);
 pinMode(LED, OUTPUT); // Inicializa o pino como saída.
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void loop() {
  int32_t rssi = getRSSI(SSID); //busca o RSSI da rede desejada 
 
  // For debugging purpose only
  Serial.print("Força do sinal: ");
  Serial.print(rssi);
  Serial.println("dBm");
 
  //se o RSSI for maior que o mínimo desejado e o RSSI é diferente de zero (ou seja, encontramos a rede desejada) 
  if (rssi > (MINdB) && rssi != 0) 
  {
    digitalWrite(LED, HIGH); //liga o LED
    Serial.println("ON");
  }
  else
  {
    digitalWrite(LED, LOW); //desliga o LED
    Serial.println("OFF");
  }

}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//retorna o RSSI da rede buscada (caso não ache, retorna zero)
int32_t getRSSI(const char* target_ssid) {
  byte available_networks = WiFi.scanNetworks(); //escaneia as redes
 
  for (int network = 0; network < available_networks; network++) {
    if (WiFi.SSID(network).compareTo(target_ssid) == 0) { //compara se alguma das redes encontradas é a que desejamos  
      return WiFi.RSSI(network); //retorna o SSID da rede
    }
  }
  return 0;
}
