// include library
#include<FastLED.h>

//define number of LED and pin
#define NUM_LEDS 60
#define DATA_PIN 7

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
  Serial.begin(9600);
  Serial.setTimeout(1);

  FastLED.clear(true);
}


void loop() {

  while(!Serial.available());

  int x = Serial.readString().toInt();
  delay(1000);
  int y = Serial.readString().toInt();
  FastLED.clear(true);
  delay(1000);
  
  // loop over the NUM_LEDS
  for (int cur = 0; cur < NUM_LEDS; cur++) {
    if(cur < x || cur > y){
//      leds[cur] = CRGB(0, 0, 0);
      continue;
    }

    
    // chose random value for the r/g/b
    r = random(0, 255);
    g = random(0, 255);
    b = random(0, 255);

    //set the value to the led
    leds[cur] = CRGB (r, g, b);

    // set the colors set into the physical LED
    FastLED.show();

    // delay 50 millis
    //FastLED.delay(200);
    
  }

}
