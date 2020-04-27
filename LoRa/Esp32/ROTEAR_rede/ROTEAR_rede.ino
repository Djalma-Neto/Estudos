#include <WiFi.h>;

const char* ssid = "ESP32_ADS";
const char* password = "19983010";
WiFiServer server(80);
const int leitura = 2;

#define luz 18

void setup()
{
  pinMode(luz,INPUT);
  pinMode(leitura,INPUT);
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);
  server.begin();
}


void loop()
{
  int luminosidade = analogRead(luz);
  int variavel = digitalRead(leitura);
  Serial.println(variavel);
  
  Site(luminosidade);
}


void Site(int luminosidade){
  
  WiFiClient html = server.available();
  html.println("<!DOCTYPE html>");
  
  delay(500);

  html.println("<html lang='pt-br'>");
    
  html.println("<head>");
  html.println("<title>EVENTOS</title>");
  html.println("<meta charset='UTF-8'/>");
  html.println("<link rel = 'stylesheet' type='text/css' href='C:/Users/Djalma/Documents/ESA/ESP_WiFi/sdf.css'/>");
  html.println("</head>");
  
  html.println("<body>");

  html.println("<div id='app'>{{luz}}</div>");
  html.println("<script src='https://unpkg.com/vue'></script>");
  html.println("<script> var app = new Vue({el:'#app',data:{luz:'Olá'}})</script>");
  
  
  html.println("</body>");
  
  html.println("</html>");
}



           


           
