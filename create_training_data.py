import time
from grab_screen import grab_screen
import cv2
from key_check import key_check,keys_to_output
def training_model(file_name,training_data):
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    while True:
        img=grab_screen()
        screen = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('',screen)
        screen = cv2.resize(screen, (80,60))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen,output])
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        if len(training_data) % 100 == 0:
            print("length is ",len(training_data))
            np.save(file_name,training_data)
