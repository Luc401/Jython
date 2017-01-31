# COMP 1631 December 8, 2015
# Jansen Porter

# This program watches a game of Pong
# Each time the program is loaded, and the frames are deleted - the ball will start in a different, and random spot 
# around the middle of the screen
# The ball will bounce off each paddle until one of the paddles misses, or the max number of frames is reached
# When 1 point is scored, the screen is filled entirely in black

def pong():

  folder = pickAFolder()
  numFrames = 336    # 21 seconds long at 16 frames/sec
  canvasWidth = 832
  canvasHeight = 520
  diameter = 50     # diameter of ball
  # ball starts in the middle
  #x = 416    # current ball x location
  import random 
  x = (random.randint(200, 600)) # chooses a random starting x location of the ball
  y = (random.randint(25,495)) # chooses a random starting y location of the ball
  # speed of ball
  xChange = 8  
  yChange = 8  
  # left paddle location
  leftX = 0
  leftY = 260
  # right paddle location
  rightX = 792
  rightY = 260
  # both paddles width and height
  widthRect = 40
  heightRect = 120
  # up and down speed of left and right paddles
  leftYChange = 24
  rightYChange = 28
  
  
  for currFrame in range(0, numFrames):
    # make new frame, ball, and paddles
    canvas = makeEmptyPicture(canvasWidth, canvasHeight, lightGray)
    ball = addOvalFilled(canvas, x, y, diameter, diameter, white)
    r1 = addRectFilled(canvas, leftX, leftY, widthRect, heightRect, cyan)
    r2 = addRectFilled(canvas, rightX, rightY, widthRect, heightRect, cyan)
# ------------------------------------------------------------------------------------
# ball and paddle movement

    # distance formula for paddles and ball
    distLeft = sqrt( ((x+20)-(leftX+40))**2 + ( (y+25) - (leftY+70) )**2 )
    distRight = sqrt( ((x+20)-rightX)**2 + ( (y+25) - (rightY+70) )**2)
    
    # change to black screen if ball goes out either side 
    if x + diameter < 0 or x + diameter > 832:
      r1 = addRectFilled(canvas, leftX, leftY, widthRect, heightRect, black)
      r2 = addRectFilled(canvas, rightX, rightY, widthRect, heightRect, black)
      canvas = makeEmptyPicture(canvasWidth, canvasHeight, black)
    
    # detect if ball hits top wall
    if y <= 0 and yChange < 0:
      yChange = -yChange 
      
    # detect if ball hits bottom wall
    if y + diameter >= canvasHeight: #diameter
      yChange = -yChange
     
    # detect if left paddle hits top wall
    if leftY <= 0 and leftYChange < 0:
      leftYChange = -leftYChange
      
    # detect if left paddle hits bottom wall
    if leftY + heightRect >= canvasHeight:
      leftYChange = -leftYChange
      
    # detect if right paddle hits top wall
    if rightY <= 0 and rightYChange < 0:
      rightYChange = -rightYChange
      
    # detect if right paddle hits bottom wall
    if rightY + heightRect >= canvasHeight:
      rightYChange = -rightYChange
      
    # detect if ball hits left paddle
    if distLeft <= 60 and xChange < 0:
      xChange = -xChange
      
    # detect if ball hits right paddle
    if distRight <= 60 and xChange > 0:
      xChange = -xChange
      
    # update values for next frame
    x = x + xChange
    y = y + yChange
    leftY = leftY + leftYChange
    rightY = rightY + rightYChange
    
    # taken from lab7.py:  
    if currFrame < 10:
      fileName = "frame00" + str(currFrame) + ".jpg"
    elif 10 <= currFrame < 100:
      fileName = "frame0" + str(currFrame) + ".jpg"
    else:
      fileName = "frame" + str(currFrame) + ".jpg"
    writePictureTo(canvas, folder + fileName)
            
  mov = makeMovieFromInitialFile(folder + "frame000.jpg")
  return mov
  
# ----------------------------------------------------------------------------------------
# to run program:
# >>> m = pong()
# >>> playMovie(m)                                                    