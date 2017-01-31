# Assignment 2 : Stripes
# Luc Doucet
# Feb 29
import random

# A description of your first function
# Gives the picture vertical stripes, importing 1 picture
# Randomizes value of color given or taken per section.
# Gives picture a random color variation each time.
def verticalStripes(picture):
  width=getWidth(picture)#get dimensions of picture
  height=getHeight(picture)
  
  stripe0Tone=(random.uniform(0,1))
  stripe1Tone=(random.uniform(0,1))#randoms your tone for each stripe.
  stripe2Tone=(random.uniform(0,1))
  
  for x in range(0,width):#search the array
    for y in range(0,height):
      pixel=getPixelAt(picture,x,y)#grab pixel within array
      if x<(width/3):
        redish=getRed(pixel)
        setRed(pixel,redish*stripe0Tone) #set color based on what the RNG rolled multiplied by what was there already.
      if x>(width/3) and x<(width*0.66):
        greenish=getGreen(pixel)
        setGreen(pixel,greenish*stripe1Tone)
      else:
        blueish=getBlue(pixel)
        setBlue(pixel,blueish*stripe2Tone)
  explore(picture)

# A description of your second function
# Gives the picture 4 Horizontal stripes, importing 1 picture
# Randomizes value of color given or taken per section. 
# Gives picture a random color variation each time.               
def horizontalStripes(picture):
  width=getWidth(picture)#get dimensions of picture
  height=getHeight(picture)
  stripe0Tone=(random.uniform(0,1))
  stripe1Tone=(random.uniform(0,1))#randoms your tone for each stripe.
  stripe2Tone=(random.uniform(0,1))
  stripe3Tone=(random.uniform(0.5,1))
  for x in range(0,width):#browse through array
    for y in range(0,height):
      pixel=getPixelAt(picture,x,y) #get the pixel in the array
      if y<(width/4):
        redish=getRed(pixel)
        setRed(pixel,redish*stripe0Tone)
      if y>(width/4) and y<(width/2):
        greenish=getGreen(pixel)
        setGreen(pixel,greenish*stripe1Tone)
      if y>(width/2) and y<(width*0.75):
        blueish=getBlue(pixel)
        setBlue(pixel,blueish*stripe2Tone)
      else:
        blueish=getBlue(pixel)
        setBlue(pixel,blueish*stripe3Tone)
  explore(picture)
