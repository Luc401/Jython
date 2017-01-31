def rotate(picture):
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(width,height)
  for x in range(0,width):
    
    for y in range (0,height):
      pixel=getPixelAt(picture,x,y)
      color=getColor(pixel)
      canvasPixel=getPixelAt(canvas,width-x-1,height-y-1)
      setColor(canvasPixel,color)
  return canvas

def sideways(picture):
  width=getWidth(picture)
  height=getHeight(picture)
  canvas=makeEmptyPicture(height,width)
  for x in range(0,height-1):
    for y in range (0,width-1):
      pixel=getPixelAt(picture,y,x)
      color=getColor(pixel)
      canvasPixel=getPixelAt(canvas,x,width-y-1)
      setColor(canvasPixel,color)
  return canvas