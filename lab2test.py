def rotateColors(picture):
  width=getWidth(picture)
  height=getHeight(picture)
  print (width)
  print (height)
  for x in range(0,width):
   for y in range(0,height):
     pixel = getPixelAt(picture,x,y)
     redvalue=getRed(pixel)
     bluevalue=getBlue(pixel)
     greenvalue=getGreen(pixel)
     setRed=(pixel,2)
     setBlue=(pixel,bluevalue)
     setGreen=(pixel,redvalue)
     
def rotate(picture):
  for pixel in getAllPixels(picture):
    redvalue=getRed(pixel)
    bluevalue=getBlue(pixel)
    greenvalue=getGreen(pixel)
    setRed(pixel,greenvalue)
    setBlue(pixel,redvalue)
    setGreen(pixel,bluevalue)