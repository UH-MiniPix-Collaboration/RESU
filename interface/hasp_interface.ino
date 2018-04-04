//https://forum.arduino.cc/index.php?topic=100028.0

#include <SoftwareSerial.h>

const byte rxPin = 2;
const byte txPin = 3;

// set up a new serial object
//SoftwareSerial mySerial(rxPin, txPin);

void setup() {
  Serial1.begin(4800);
  Serial.begin(4800);
}

void loop() {
  // HASP_SOH              0x01                                                                    
  // HASP_STX              0x02                                                                    
  // HASP_CMD_BYTE1        0x10                                                                    
  // HASP_CMD_BYTE2        0x20                                                                    
  // HASP_ETX              0x03                                                                    
  // HASP_CR               0x0D                                                                    
  // HASP_LF               0x0A                                                                    
  // HASP_CMD_COMPLETE     0x30
  
  byte CMD[8] = {0x01, 0x02, 0x10, 0x20, 0x03, 0x0D, 0x0A, 0x30};
  while(Serial.available() >= 2) {
    Serial1.flush();
    byte arg1 = Serial.read();
    byte arg2 = Serial.read();
    CMD[2] = arg1;
    CMD[3] = arg2;
    for (int c = 0; c < sizeof(CMD); c++) {
      Serial1.write(CMD[c]);
      Serial.print(CMD[c], HEX);
      Serial.println();
    }
    while (Serial1.available() > 0) { 
     Serial.println(Serial1.read());
    }
  }
  delay(10);
  
}