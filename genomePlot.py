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

def graph(x, y, plt):
    plt.plot(x, y)

def totalGenomes(filename):
    startTime=0
    plt.title("Unique Genomes vs Time")
    plt.ylabel("Number of Genomes")
    plt.xlabel("Time (min)")
    #print("running")
    f = os.path.join("formattedResults", filename)
    #print(f)
    myFile=open(f, "r")
    x=[]
    y=[]
    timeStampList=[]
    genomeList=[]
    firstLine=True
    dict={}
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
        if runTime not in dict.keys():
            dict[runTime]=[genome]
        exists = False
        #for v in dict.get(runTime):
        if genome in dict.get(runTime):
            exists = True
        if not exists:
            dict[runTime].append(genome)
        #timeStampList.append(runTime)
        #genomeList.append(genome)
        #if runTime not in x:
        #    x.append(runTime)
    #for runTime in runTimeList:
    #print(x, y)
    for key in dict:
        y.append(len(dict[key]))
        x.append(key)

    graph(x, y, plt)
    plt.savefig("unique_vs_time_" + filename + ".png")
def main():
    totalGenomes("fooresults_1")


main()
