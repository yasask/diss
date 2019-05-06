import csv
import numpy as np

with open('training.csv', 'r') as bl, open('tracking.csv', 'r') as tk:
    readbl = csv.reader(bl)
    readtk = csv.reader(tk)
    blockList = list(readbl)
    tracking = list(readtk)

blockArray = np.asarray(blockList);
trackingArray = np.asarray(tracking);
trackingArray = trackingArray.flatten();
blockArray = blockArray.flatten();

print(len(blockArray))
print(len(trackingArray))

value = len(blockArray)

print(blockList[1][0])
print(tracking[1][0])

if(blockList[1] == tracking[1]):
    print("false")
else:
    print ("true")

checkArray = []
with open('tmp.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    for i in range(0, len(tracking)):
        flag = False
        for j in range(0, len(blockList)):
            try:
                if blockList[j] != []:
                    if tracking[i][0] == blockList[j][0]:
                #print("i: " + str(i) + " j: " + str(j))
                #print ("blockList: " + blockList[j][0] + " tracking: " + tracking[i][0])
                        flag = True
            except:
                print("ERROR ON: i: " + str(i) + " j: " + str(j))
        print (tracking[i][0] + " is blocked: " + str(flag))
        if not flag:
            writer.writerow([tracking[i][0], "0"])
        else:
            writer.writerow([tracking[i][0], "1"])

writeFile.close()