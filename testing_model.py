import time
import numpy as np
import cv2
from grab_screen import grab_screen
from direct_key import UP,Down,no_key
def testing_model(model):
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    while(True):
        screen =  np.array(grab_screen(region=(0,40,800,640)))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        cv2.imshow('',screen)
        screen = cv2.resize(screen, (80,60))
        prediction = model.predict([screen.reshape(1,80,60,1)])[0]
        print(prediction)
        up_thresh=.55
        do_thresh=.55
        n_thresh=.55
        if prediction[0] >up_thresh:
            UP()
            print("up action took")
        elif prediction[2] > do_thresh:
            Down()
            print("down action took")
        elif prediction[1] > n_thresh:
            no_key()
            print("no action took")
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break        