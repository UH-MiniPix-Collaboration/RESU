//https://forum.arduino.cc/index.php?topic=100028.0

#include <SoftwareSerial.h>

const byte rxPin = 2;
const byte txPin = 3;

// set up a new serial object
SoftwareSerial mySerial(rxPin, txPin);

void setup() {
  mySerial.begin(4800);
}

void loop() {
  //if (Serial.available() > 0){ //take action when a byte is received 
  //  int incomingByte = Serial.read(); // read the byte
  //  Serial.print("Incoming Byte: " + incomingByte);
  //}

  //HASP_SOH              0x01                                                                    
  //HASP_STX              0x02                                                                    
  //HASP_CMD_BYTE1        0x10                                                                    
  //HASP_CMD_BYTE2        0x20                                                                    
  //HASP_ETX              0x03                                                                    
  //HASP_CR               0x0D                                                                    
  //HASP_LF               0x0A                                                                    
  //HASP_CMD_COMPLETE     0x30
  
  byte CMD[8] = {0x01, 0x02, 0x10, 0x20, 0x03, 0x0D, 0x0A, 0x30};
  for (int c = 0; c < sizeof(CMD); c++)
  {
    mySerial.write(CMD[c]);
    delay(500);
    mySerial.flush();
  }
}
