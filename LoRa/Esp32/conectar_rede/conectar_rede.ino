#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>

#define luz 32

WiFiServer server(80);


const char* ssid = "Fabiano";
const char* password =  "Arduino5432112345";

//------------------------------------------------------------------------------------------------------------------------------------------------
void setup() {
  Serial.begin(115200);
  pinMode(luz,INPUT);
  
  Conectar(ssid, password);
  server.begin();
  Serial.println("Server HTTP inicializado");
}
//------------------------------------------------------------------------------------------------------------------------------------------------ 
void loop() {
  delay(500);
  
  int luminosidade = digitalRead(luz);
  Site(luminosidade);
  
 }
//------------------------------------------------------------------------------------------------------------------------------------------------
void Conectar(const char* ssid, const char* password){
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
}
//------------------------------------------------------------------------------------------------------------------------------------------------
void Site(int luminosidade){
  Serial.println(luminosidade);
  WiFiClient html = server.available();
  html.println("<!DOCTYPE html>");
  html.println("<html lang='pt-br'>");
  html.println("<head>");
  html.println("<title>EVENTOS</title>");
  html.println("<meta charset='UTF-8'/>");
  html.println("<link rel = 'stylesheet' type='text/css' href='C:/Users/Djalma/Documents/ESA/ESP_WiFi/teste.css'/>");
  html.println("</head>");
  
  html.println("<body>");
  
  html.println("<div id='app'>{{luz}}</div>");
  html.println("<script src='https://unpkg.com/vue'></script>");
  html.println("<script> var app = new Vue({el:'#app',data:{luz:"+String(luminosidade)+"}})</script>");
  
  
  html.println("</body>");
  
  html.println("</html>");
}
