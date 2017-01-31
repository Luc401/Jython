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
    location=location+samplesPerPixel
  return canvas
