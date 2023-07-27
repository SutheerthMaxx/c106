# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()
    grey=cv2.cvtcolor(frame,cv2.COLOR_BGRTOGREY)
    face=face_cascade.detectMultiScale(grey,1.1,4)

    #draw the reactangle sround each face
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #display resulting face
        cv2.imshow(frame),frame
    vid=cv2.VideoCapture(0)
    face_cascade=c2.CascadeClassifier("harrcascade_frontalface_default.xml")

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()