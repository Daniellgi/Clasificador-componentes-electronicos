#define DEBUG_ARRAY(a) {for (int index = 0; index < sizeof(a) / sizeof(a[0]); index++)    {Serial.print(a[index]); Serial.print('\t');} Serial.println();};

//____esto es del motor paso a paso
//Motor 1
#define dir1Pin 12
#define step1Pin 11
// Motor 2
#define dir2Pin 4
#define step2Pin 5


#define bandapin 6
#define vibradorpin 3
#define tolvapin 10

#define tolvaUp 7
#define tolvaDown 8 

unsigned long tiempo1 = 0;
unsigned long tiempo2 = 0;
unsigned long tiempoSegundos = 0;

//___________________________________________


//_______________________________________________________________________________
// Esto es con el uso de la funcion milis()

bool state_1 = LOW; //Estado tolvaUp
bool state_2 = HIGH; //Esatdo tolvaDown
bool Bandera = 0;
unsigned long previousMillis = 0; //Variables auxiliares para intervalos de tiempo
unsigned long previousMillis_2 = 0;
//_______________________________________________________________________________


int pwm;
String str = "";
const char separator = ',';
const int dataLength = 6;
int data[dataLength];

int retardo;

 
void setup()
{
   Serial.begin(9600);
   // Motor 1
  pinMode(step1Pin, OUTPUT);
  pinMode(dir1Pin, OUTPUT);
  // Motor 2
  pinMode(step2Pin, OUTPUT);
  pinMode(dir2Pin, OUTPUT);
  pinMode(vibradorpin,OUTPUT);
  pinMode(bandapin,OUTPUT);
  pinMode(tolvaUp,OUTPUT);
  pinMode(tolvaDown,OUTPUT);
  
  
}
//____________________________________________________________________________________
//Esto es para los motores paso a paso
int anterior1=1;
int anterior2=1;
int clase1=0;
int clase2=0;
String inByte;
int lado=3;
int pos;
int bandera=0;
int BanderaM10=0;
int BanderaM11=0;
int BanderaM20=0;
int BanderaM21=0;
int i=0;
int j=0;

//____________________________________________________________________________________

boolean bandera_tiempoTolva=false; //Esta bandera la utilizaba para lo de la funcion millis()

int velbanda; // velocidadd de la banda
int velvibrador; // velocidad del vibrador

int ActBanda;
int ActRanV;
int ActSistema;

//lado=0 izquierdo y lado=1 derecho del motor paso a paso
int stepsPerRevolution1=0; // Inicializo los pasos por revolucion
int stepsPerRevolution2=0;


void loop()
{
   if (Serial.available())
   {
      str = Serial.readStringUntil('\n');
      for (int i = 0; i < dataLength ; i++)
      {
         bandera_tiempoTolva=true;
         int index = str.indexOf(separator);
    
         data[i] = str.substring(0, index).toInt();
         str = str.substring(index + 1);
      }
      //DEBUG_ARRAY(data);
     

   }
   pos=data[0]; //el dato lo recibimos en la posicion 0 del mensaje
   ActBanda=data[1];
   velbanda=data[2]; //velocidad de la banda
   ActRanV=data[3];
   velvibrador=ActRanV*80;//Fijo un valor de pwm del vibrador que estaria en la posicion 2 (empezando desde 0 del mensaje)
   retardo=data[4]; // Este retardo lo recibo del mensaje en la posicion 4 (empezando desde 0)
   ActSistema=data[5];
   //Serial.println(data[5]);
   
   if(ActSistema==1){
    //Serial.println("encendido");
    if(ActBanda==1){
      analogWrite(bandapin,velbanda*2.55);
      //delay(1000);
      }
    if(ActBanda==0){
      analogWrite(bandapin,0);
      //delay(1000);
      }
    if(ActRanV==1){
      analogWrite(vibradorpin,velvibrador);
      //Serial.println(ActRanV);
      //Serial.println(velvibrador);
      
      //delay(1000);
      tiempo2 = millis();  
      if(tiempo2 > (tiempo1+retardo*1000)){  //Si ha pasado 1 segundo ejecuta el IF
          switch(Bandera){
            case 1:
              Serial.println("Abrir");
              digitalWrite(tolvaUp,HIGH);
              digitalWrite(tolvaDown,LOW);
              delay(100);
              digitalWrite(tolvaUp,LOW);
              digitalWrite(tolvaDown,LOW);
              tiempo1 = millis(); //Actualiza el tiempo actual
              Bandera=0;
              
              break;
             case 0:
              Serial.println("Cerrar");
              digitalWrite(tolvaUp,LOW);
              digitalWrite(tolvaDown,HIGH);
              delay(100);
              digitalWrite(tolvaUp,LOW);
              digitalWrite(tolvaDown,LOW);
              tiempo1 = millis(); //Actualiza el tiempo actual
              Bandera=1;
              break;
            }
          
      }
      
    }
    if(ActRanV==0){
        analogWrite(vibradorpin,0);
        digitalWrite(tolvaUp,LOW);
        digitalWrite(tolvaDown,LOW); 
        }
    //_____________________________________________________MOTORES PASO A PASO________________________________________________  
    switch(pos){
      //lado izquierdo
      case 11:
        lado=0;
        clase1=1; 
        break;
      case 12:
        lado=0;
        clase1=2;
        break;
      case 13:
        lado=0;
        clase1=3;
        break;
      case 14:
        lado=0;
        clase1=4;
        break;
      case 15:
        lado=0;
        clase1=5; 
        break;
      case 16:
        lado=0;
        clase1=6;
        break;
      case 17:
        lado=0;
        clase1=7;
        break;
      case 18:
        lado=0;
        clase1=8;
        break;
      case 19:
        lado=0;
        clase1=9; 
        break;
      case 110:
        lado=0;
        clase1=10;
        break;
      case 111:
        lado=0;
        clase1=11; 
        break;
      case 112:
        lado=0;
        clase1=12;
        break; 
      //lado derecho
      case 21:
        lado=1;
        clase2=1; 
        break;
      case 22:
        lado=1;
        clase2=2; 
        break;
      case 23:
        lado=1;
        clase2=3; 
        break;
      case 24:
        lado=1;
        clase2=4; 
        break;
      case 25:
        lado=1;
        clase2=5;  
        break;
      case 26:
        lado=1;
        clase2=6; 
        break;
      case 27:
        lado=1;
        clase2=7;  
        break;
      case 28:
        lado=1;
        clase2=8; 
        break;
      case 29:
        lado=1;
        clase2=9;  
        break;
      case 210:
        lado=1;
        clase2=10; 
        break;
      case 211:
        lado=1;
        clase2=11;  
        break;
      case 212:
        lado=1;
        clase2=12; 
        break;
      }
    if(lado==0){
      //Serial.println(anterior1);
      //Serial.println(clase1);
      if(anterior1>clase1){
          //Serial.println("Lado0");
          digitalWrite(dir1Pin, LOW);
          stepsPerRevolution1=(anterior1-clase1)*16.7;
          BanderaM10=1;
          }
      if(BanderaM10==1){
        if(i < stepsPerRevolution1){
          // These four lines result in 1 step:
          digitalWrite(step1Pin, HIGH);
          delayMicroseconds(1000);
          digitalWrite(step1Pin, LOW);
          delayMicroseconds(1000);
          i=i+1;
          }
        if(i == stepsPerRevolution1){
          anterior1=clase1;
          i=0;
          BanderaM10=0;
          }
        }
      if(anterior1<clase1){
        digitalWrite(dir1Pin,HIGH);
        stepsPerRevolution1=(clase1-anterior1)*16.7;
        BanderaM11=1;
        }
      if(BanderaM11==1){
        if(i < stepsPerRevolution1){
          // These four lines result in 1 step:
          digitalWrite(step1Pin, HIGH);
          delayMicroseconds(1000);
          digitalWrite(step1Pin, LOW);
          delayMicroseconds(1000);
          i=i+1;
          }
        if(i == stepsPerRevolution1){
          anterior1=clase1;
          i=0;
          BanderaM11=0;
          }
        } 
    }
    if(lado==1){
        if(anterior2>clase2){
          //Serial.println("Lado1");
           digitalWrite(dir2Pin, LOW);
           stepsPerRevolution2=(anterior2-clase2)*16.7;
           BanderaM20=1;
           }
        if(BanderaM20==1){
          if(j < stepsPerRevolution2){
            // These four lines result in 1 step:
            digitalWrite(step2Pin, HIGH);
            delayMicroseconds(1000);
            digitalWrite(step2Pin, LOW);
            delayMicroseconds(1000);
            j=j+1;
            }
          if(j == stepsPerRevolution2){
            anterior2=clase2;
            j=0;
            BanderaM20=0;
            }
          }
        if(anterior2<clase2){
          digitalWrite(dir2Pin,HIGH);
          stepsPerRevolution2=(clase2-anterior2)*16.7;
          BanderaM21=1;
          }
        if(BanderaM21==1){
          if(j < stepsPerRevolution2){
            // These four lines result in 1 step:
            digitalWrite(step2Pin, HIGH);
            delayMicroseconds(1000);
            digitalWrite(step2Pin, LOW);
            delayMicroseconds(1000);
            j=j+1;
            }
          if(j == stepsPerRevolution2){
            anterior2=clase2;
            j=0;
            BanderaM21=0;
            }
          }
                 
        }
    }
    if(ActSistema==0){
      analogWrite(vibradorpin,0);
      digitalWrite(tolvaUp,LOW);
      digitalWrite(tolvaDown,LOW);
       
      digitalWrite(step1Pin, LOW);
      digitalWrite(step2Pin, LOW);
      analogWrite(bandapin,0);
      }
    }
 
