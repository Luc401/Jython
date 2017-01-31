def simpleMovie(directory, picture):
  canvas = duplicatePicture(picture)
  canvas2 = duplicatePicture(picture)
  width=getWidth(canvas)
  height=getHeight(canvas)
  #Make Blueish
  for frameNumber in range(0,30):
    for x in range(0,width):
      for y in range(0,height):
        pixel=getPixelAt(canvas,x,y)
        redValue=getRed(pixel)
        greenValue=getGreen(pixel)
        blueValue=getBlue(pixel)
        setRed(pixel,redValue-20)
        setGreen(pixel,greenValue+4)
        setBlue(pixel,blueValue+4)        
    writeFrame(frameNumber,directory,canvas)
  #reset canvas 
  canvas = duplicatePicture(picture)
  #Fade to black
  for frameNumber in range(30,60):
    for x in range(0,width):
      for y in range(0,height):
        pixel=getPixelAt(canvas,x,y)
        redValue=getRed(pixel)*0.333
        greenValue=getGreen(pixel)*0.333
        blueValue=getBlue(pixel)*0.333
        luminance=(makeColor(redValue,greenValue,blueValue))
        setColor(pixel,luminance)
    writeFrame(frameNumber,directory,canvas)
  #reset canvas 
  canvas = duplicatePicture(picture)
  #Title Screen
  for frameNumber in range(60,90):
    for x in range(0,width):
      for y in range(0,height):
        pixel=getPixelAt(canvas,x,y)
        str= "Movie by Karl-Eric Demers and AStra Neukom JOyce"
        addText(canvas,20, 20,str,orange)
    writeFrame(frameNumber,directory,canvas)
  movie=makeMovieFromInitialFile(directory+"/frame000.jpg")
  return movie  
    
def writeFrame(frameNumber,directory,picture): #from lab 7.
  numberStr=str(frameNumber)
  if frameNumber<10:
    filename= "/frame00" + numberStr+ ".jpg"
  if (frameNumber>=10) and (frameNumber,100):
    filename= "/frame0" + numberStr+ ".jpg"
  if frameNumber>=100:
    filename= "/frame" + numberStr+ ".jpg"
  writePictureTo(picture,directory+filename)
  
#----------Instructions--------- 
#pic=makePicture(pickAFile())
#direct=pickAFolder()
#mov=simpleMovie(direct,pic)
#playMovie(mov)
  
  