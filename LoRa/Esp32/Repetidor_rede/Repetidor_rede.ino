#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <HTTPClient.h>
#include "index.h"

WebServer server(80);
 
const char* ssid = "Fabiano";
const char* password = "Arduino5432112345";
 
void View() {
  FILE *HTML;
  HTML = fopen("index.html", "r");
  String pag = MAIN_page;
  server.send(200, "text/html", pag);
}

void View2() {
  String pag = teste;
  server.send(200, "text/html", pag);
}

void setup(void){
  
  Serial.begin(115200);
    
  WiFi.mode(WIFI_STA); //Conectar no wifi
  WiFi.begin(ssid, password);
 
  Serial.println("Conectando a: ");
  Serial.print(ssid);
 
  while(WiFi.waitForConnectResult() != WL_CONNECTED){      
      Serial.print(".");
      delay(1000);
    }
  Serial.print("Conectado em: ");
  Serial.println(ssid);
  Serial.print("IP LOCAL: ");
  Serial.println(WiFi.localIP());
 
  server.on("/", View);
  server.on("/teste", View2);
 
  server.begin();
  Serial.println("Server HTTP inicializado");
}

void loop(void){
  
  server.handleClient();
  delay(1000);
}
