# Assignment 4 : Sound Visualization
# Luc Doucet
# April 2016
#
# A description of your program, including both
# The program takes a sound and displays samples of the sound allowing the user to
# Select the starting point and how many samplesperPixel
# The function takes 1 sound, a starting index, and how many samplesPerPixel
def visulize(sound,startSampleIndex,samplePerPixel):
  spot=startSampleIndex#which sound sample to start at
  totalValue=32786 #max sound value 
  canvas=makeEmptyPicture(1000,200,black)#create the canvas
  #Get values and draw them
  for i in range(0,1000):
    #drawing middle line.
    targetPixel=getPixelAt(canvas,i,100)
    setColor(targetPixel,cyan)
    
    value=getSampleValueAt(sound,spot) #Get the hight of the sample at a certain spot.
    percent=int((float(value)/float(totalValue))*100)*-1#calculates amplitude within canvas regions
    targetPixel=getPixelAt(canvas,i,percent+100)#selects where to place the sample on the canvas
    
    #colors
    if 0<abs(percent)<=20: #if the value is smaller than 20 make it yellow
      setColor(targetPixel,yellow)
    elif abs(percent)>85: #if the value is bigger then 85 make it red
      setColor(targetPixel,red)
    else:                 #if the value is anything else make it green.
      setColor(targetPixel,green)
    
    spot=spot+samplePerPixel #increase to where the next sample should be found.
  return canvas


def visualizeRepresentation(sound,startSampleIndex,samplesPerPixel):
  canvas = makeEmptyPicture(1000,200,black)
  totalValue=32768
  location=startSampleIndex
  
  for x in range(0,1000):
    pixel=getPixelAt(canvas,x,100)
    setColor(pixel,cyan)
  for i in range(0,1000):
    value=getSampleValueAt(sound,location)
    multiplier=int((float(value)/float(totalValue))*100)*-1
    targetPixel=getPixelAt(canvas,i,multiplier+100)
  
    if multiplier <= 20:
      setColor(targetPixel,yellow)
    elif multiplier >85:
      setColor(targetPixel,red)
    else:
      setColor(targetPixel,green)
  return canvas
