import glob
import os

while True:
    cents = glob.glob("./snapshots/*")

    

    for key in  cents:
        if "./snapshots/resnet50_csv_50.h5" in key:
            cents.remove(key)

    

    for key in  cents:
        os.remove(key)
        print ("removing " + key)
