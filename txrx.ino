// Programa: Comunicacao Serial Arduino com Raspberry Pi
// Autor: Henrique Almeida

char buf;
 
void setup(){
  Serial.begin(9600);
}
 
void loop(){
  Serial.print("\nSistema ligado\n");
  delay(1000);
  while (Serial.available() > 0){
    buf = Serial.read();
    // Caso seja recebido o caracter significativo
    if (buf!='\n'){
      // Envia a resposta para o Raspberry
      Serial.print("\nRecebido! - Bit: ");
      Serial.println(buf);
    }
  }
}
