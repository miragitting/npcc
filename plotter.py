import matplotlib.pyplot as plt
import os
import numpy as np

def convertTime(origString):
    splitTime=origString.split(":")
    hours=splitTime[0]
    mins=splitTime[1]
    minsFromHours=int(hours)*60
    totTime=minsFromHours+int(mins)
    return totTime

def graph(x, y, plt, title):
    plt.plot(x, y, label = title)

def totalGenomes():
    startTime=0
    plt.title("Total Genome Count vs Time")
    plt.ylabel("Genome Count")
    plt.xlabel("Time (min)")
    leg = plt.legend(loc = 'upper left')
    #print("running")
    for filename in  os.listdir('formattedResults'):
        f = os.path.join("formattedResults", filename)
        #print(f)
        myFile=open(f, "r")
        x=[]
        y=[]
        timeStampList=[]
        firstLine=True
        for line in myFile:
            splitLine=line.split("/")
            secondSplitLine=splitLine[1].split("_")
            timeStamp=secondSplitLine[0]
            thirdSplit=secondSplitLine[1].split(":")
            splitGenome= thirdSplit[1].split("\n")
            genome=splitGenome[0]
            #print(genome, timeStamp)
            #print(timeStamp)
            formattedTime=convertTime(timeStamp)
            if firstLine:
                startTime=formattedTime
                firstLine=False
            runTime=int(formattedTime)-int(startTime)
            timeStampList.append(runTime)
            if runTime not in x:
                x.append(runTime)
        for runTime in x:
            y.append(timeStampList.count(runTime))
        #print(x, y)
        graph(x, y, plt, splitLine[0])
    plt.savefig("countVsRuntime.png")
def main():
    totalGenomes()


main()
