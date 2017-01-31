# Assignment 3 : Chromakey
# Luc Doucet
# March 20th 2016
# This program takes 3 pictures, a portrait, a background source, and a new shirt color.
# It will take color values from all locations of the picture and see if they are the
# "Correct" color for the if statements.
# Blue will turn into space. Green will turn into a green landscape.   
def chroma(human,background,shirt,landScapeStart,spaceStart): #Get the human image, the landscape for the second image, and the space picture for the third image.
                                                              # Max value of "starts" is 555
  height=getHeight(human) #Take human picture Width & Height
  width=getWidth(human)
  canvas=makeEmptyPicture(width,height)  
  for x in range(0,width): 
    for y in range(0,height):
      canvasPixel=getPixelAt(canvas,x,y)
      humanPixel=getPixelAt(human,x,y)
      if (getRed(humanPixel)+getBlue(humanPixel)<getGreen(humanPixel)): #If green is dominant color in Human Picture
        backgroundPixel=getPixelAt(background,x+landScapeStart,y+landScapeStart) #Retrieve pixel on background picture.
        pixelColor=getColor(backgroundPixel) #Get color from (X,Y) background picture
        setColor(canvasPixel,pixelColor) # Set that color on the canvas (X,Y).
      elif(getBlue(humanPixel)+10>getRed(humanPixel)+getGreen(humanPixel)): #If Blue+10 is dominant color in (X,Y)
        shirtPixel=getPixelAt(shirt,x+spaceStart,y+spaceStart)
        pixelColor=getColor(shirtPixel)
        setColor(canvasPixel,pixelColor)
      else:                               #Else, copy the rest of the human picture to the canvas.
        pixelColor=getColor(humanPixel)
        setColor(canvasPixel,pixelColor)        
  return canvas
