#include <WiFi.h>
const char* ssid = "Fabiano";
const char* password =  "Arduino5432112345";
const int iluminacao = 27;
int last = 1000;
boolean val = false;
String ligar;
WiFiServer server(8082);

//------------------------------------------------------------------------------------------------------------------------------------------------
void setup() {
  pinMode(iluminacao, INPUT);
  Serial.begin(115200);
  Serial.print("Conectando-se a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi conectada.");
  Serial.println("Endereço de IP: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  int ilum = analogRead(iluminacao);
  if((millis()-last) > 1000){
    Serial.println(ilum);
    last = millis();
  }
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client.");
    String currentLine = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();
            client.print("<a href='/ON'>LIGAR</a>");
            client.print("<a href='/OFF'>DESLIGAR</a><br>");
            client.print("<div>LUMINOSIDADE: "+String(ilum)+"</div><br>");
            client.print("<a href='/'>update</a><br>");
            client.print("<div>"+ligar+"</div>");
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
        if (currentLine.endsWith("GET /ON")) {
          ligar = "ON";
        }
        if (currentLine.endsWith("GET /OFF")) {
          ligar = "OFF";
        }
      }
    }
    client.stop();
    Serial.println("Client Disconnected.");
  }
}
