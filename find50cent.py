import glob
import os
import time

while True:
    cents = glob.glob("./snapshots/*")

    

    for key in  cents:
        if "./snapshots/resnet50_csv_50.h5" in key:
            cents.remove(key)

    

    for key in  cents:
        time.sleep(1)
        os.remove(key)
        print ("removing " + key)
