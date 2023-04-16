# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    print(bodies)
    for (x,y,w,h) in bodies:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
       cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()