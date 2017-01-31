def matte(picture,border,color):
  width=getWidth(picture)
  height=getHeight(picture)
  canvas = makeEmptyPicture(width+(border*2),height+(border*2),color)
  for x in range(0,width):
    for y in range(0,height):
      sourcePixel= getPixel(picture,x,y)
      color = getColor(sourcePixel)
      targetPixel = getPixel(canvas,x+border,y+border)
      setColor(targetPixel,color)
  return canvas
  
def crop(picture,orgX,orgY,width,height):
  canvas=makeEmptyPicture(width,height)
  for x in range(0,width):
    for y in range(0,height):
      sourcePixel = getPixel(picture,orgX+x,orgY+y)
      color= getColor(sourcePixel)
      
      targetPixel = getPixel(canvas,x,y)
      setColor(targetPixel,color)
  return canvas