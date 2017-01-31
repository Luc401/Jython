     
def chroma(image):
  height=getHeight(source)
  width=getWidth(source)
  canvas=makeEmptyPicture(width,height)  
  for x in range(0,width):
    for y in range(0,height):
      location=getPixelAt(source,x,y)
      canvasLocation=getPixelAt(canvas,x,y)
      if (getRed(location)+getBlue(location)>getGreen(location)):
        setColor(canvasLocation,getColor(location))
  return canvas
