// include library
#include<FastLED.h>

//define number of LED and pin
#define NUM_LEDS 212
#define DATA_PIN 7

//timer
unsigned long startMillis;
unsigned long currentMillis;
const unsigned long period = 60000;

// create the ld object array
CRGB leds[NUM_LEDS];

// define 3 byte for the random color
byte  r, g, b;

void setup() {
  // init the LED object
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  // set random seed
  randomSeed(analogRead(0));

  //Set up serial connection
  Serial.begin(115200);
  Serial.setTimeout(1);

  FastLED.clear(true);
  FastLED.show();

  startMillis = millis();
}

void loop() {

  currentMillis = millis();
  if(currentMillis - startMillis >= period){
    FastLED.clear(true);
    FastLED.show();
    startMillis = millis();
  }
  
  if(Serial.available()>0){
    String data = Serial.readStringUntil('>');
    int comma_index = data.indexOf(',');
    int first = data.substring(1,comma_index).toInt();
    int last = data.substring(comma_index+1,data.length()).toInt();
    light(first, last);
    startMillis = millis();

  }

}

// Method used to light a specific range of lights on the LED Strip (INCLUSIVE)
// first = start index
// last = end index
void light(int first, int last){

  FastLED.clear(true);

  for (int cur = 0; cur < NUM_LEDS; cur++) {
    if(cur < first || cur > last){
      continue;
    }

  r = random(0, 255);
  g = random(0, 255);
  b = random(0, 255);

  //set the value to the led
  leds[cur] = CRGB (r, g, b);

  // set the colors set into the physical LED
  FastLED.show();
  
  }
}

void serialFlush(){
  while(Serial.available()>0){
    char t = Serial.read();
  }
}
  
