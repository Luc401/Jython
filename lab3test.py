#decrease red in the picture
def decreaseRed(picture,factor):
  for pixel in getAllPixels(picture):
    value=getRed(pixel)
    setRed(pixel,value*factor)
    
def grayFactor(picture,kickRed,kickGreen,kickBlue):
    for pixel in getAllPixels(picture):
      redValue=getRed(pixel)*kickRed
      blueValue=getBlue(pixel)*kickBlue
      greenValue=getGreen(pixel)*kickGreen
      avg=(redValue+blueValue+greenValue)/3
      setColor(pixel, makeColor( avg, avg, avg))
    
#writePictureTo(pic,"C:\Users\Luc401\Desktop\pic.jpg")