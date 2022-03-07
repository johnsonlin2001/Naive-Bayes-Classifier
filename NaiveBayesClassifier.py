from cmath import exp
from email.errors import MalformedHeaderDefect
from os import stat
import sys
from traceback import print_tb
import statistics 
import numpy as np
from math import sqrt
import math
import time

trainingname = sys.argv[1]
testname = sys.argv[2]


totalcount = 0
correctcount = 0
total2 = 0
highp = 0 #high performers
lowp = 0
under35 = 0
between35and49 =0
greater49 = 0
highorlow = ""
under35h = 0  #high performance and age
between35and49h =0 
greater49h = 0
under35l = 0  #low performance and age
between35and49l =0
greater49l = 0
gender = ""
male = 0
female = 0
maleh = 0 #male high performance
malel = 0 #male low performances
femaleh = 0
femalel = 0
maxh = 0
minh = 200
heighth =[]
heightl =[]
weighth = []
weightl = []
bfph = [] #body fat percentage of high performers
bfpl = []
diastolich=[]
diastolicl=[]
systolich = []
systolicl = []
griph = []
gripl = []
sabfh = [] #sit and bend forward of high performers
sabfl = []
situph = []
situpl = []
broadh = []  #broad jump of high performers
broadl = []
ageh = [] #age of high performers
agel = []
start1 = time.time()
file = open(trainingname,'r')
with open(trainingname) as file:
    for line in file:
        attributes = line.split(",")
        highorlow=line[-2]
        currentage = float(attributes[0])
        gender = attributes[1]
        height = float(attributes[2])
        weight = float(attributes[3])
        bfp = float(attributes[4])
        diastolic = float(attributes[5])
        systolic = float(attributes[6])
        grip = float(attributes[7])
        sabf = float(attributes[8])
        situp = float(attributes[9])
        broad = float(attributes[10])
        if(highorlow=="1"):  #loading data of high and low performers into corresponding array
            highp +=1
            heighth.append(height)
            weighth.append(weight)
            bfph.append(bfp)
            diastolich.append(diastolic)
            systolich.append(systolic)
            griph.append(grip)
            sabfh.append(sabf)
            situph.append(situp)
            broadh.append(broad)
            ageh.append(currentage)
        elif(highorlow=="0"):
            lowp +=1
            heightl.append(height)
            weightl.append(weight)
            bfpl.append(bfp)
            diastolicl.append(diastolic)
            systolicl.append(systolic)
            gripl.append(grip)
            sabfl.append(sabf)
            situpl.append(situp)
            broadl.append(broad)
            agel.append(currentage)
        if(height>maxh):
            maxh=height
        if(height<minh):
            minh = height
        if(currentage<35):
            under35+=1
            if(highorlow=="1"):
                under35h+=1
            else:
                under35l+=1
        elif(currentage<49):
            between35and49+=1
            if(highorlow=="1"):
                between35and49h+=1
            else:
                between35and49l+=1
        elif(currentage>49):
            greater49+=1
            if(highorlow=="1"):
                greater49h+=1
            else:
                greater49l+=1

        if(gender=="M"):
            male+=1
            if(highorlow=="1"):
                maleh+=1
            else:
                malel+=1
        elif(gender=="F"):
            female+=1
            if(highorlow=="1"):
                femaleh+=1
            else:
                femalel+=1
        totalcount+=1
pmaleh = maleh/male #probability that a male is a high performer
pfemaleh = femaleh/female

pmalel = malel/male #probability that a male is a low performer
pfemalel = femalel/female




    #age stats
agehmean = statistics.mean(ageh)
agelmean = statistics.mean(agel)
agehstdev = statistics.mean(ageh)
agelstdev = statistics.mean(agel)

    #height stats
heighthmean = statistics.mean(heighth)
heightlmean = statistics.mean(heightl)
heightlstdev = statistics.stdev(heightl)
heighthstdev = statistics.stdev(heighth)
    #weight stats
weighthmean = statistics.mean(weighth)
weightlmean = statistics.mean(weightl)
weighthstdev = statistics.stdev(weighth)
weightlstdev = statistics.stdev(weightl)
    #body fat percentage stats
bfphmean = statistics.mean(bfph)
bfplmean = statistics.mean(bfpl)
bfphstdev = statistics.stdev(bfph)
bfplstdev = statistics.stdev(bfpl)
    #Diastolic stats
diastolichmean = statistics.mean(diastolich)
diastoliclmean = statistics.mean(diastolicl)
diastolichstdev = statistics.stdev(diastolich)
diastoliclstdev = statistics.stdev(diastolicl)
    #systolic stats
systolichmean = statistics.mean(systolich)
systoliclmean = statistics.mean(systolicl)
systolichstdev = statistics.stdev(systolich)
systoliclstdev = statistics.stdev(systolicl)
    #grip strength stats
griphmean = statistics.mean(griph)
griplmean = statistics.mean(gripl)
griphstdev = statistics.stdev(griph)
griplstdev = statistics.stdev(gripl)
    #sit and bend forward stats
sabfhmean = statistics.mean(sabfh)
sabflmean = statistics.mean(sabfl)
sabfhstdev = statistics.stdev(sabfh)
sabflstdev = statistics.stdev(sabfl)
    #sit up count stats
situphmean = statistics.mean(situph)
situplmean = statistics.mean(situpl)
situphstdev = statistics.stdev(situph)
situplstdev = statistics.stdev(situpl)
    #broad jump stats
broadhmean = statistics.mean(broadh)
broadlmean = statistics.mean(broadl)
broadhstdev = statistics.stdev(broadh)
broadlstdev = statistics.stdev(broadl)

end1 = time.time()

def pdf1(x , mean , sd):
    return (1/(sd*(2*np.pi)**0.5))*exp(-0.5*((x-mean)/sd)**2)

def pdf(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * np.pi) * stdev)) * exponent

probh = 0.5 #probability of being a high performer
probl = 0.5
start2 = time.time()
file = open(testname,'r')
with open(testname) as file:
    for line in file:
        currentathlete = line.split(",")
        if(currentathlete[1]=="M"):
            pgenderh = maleh/highp
            pgenderl = malel/lowp
            probh = pmaleh
            probl = pmalel
        elif(currentathlete[1]=="F"):
            pgenderh = femaleh/highp
            pgenderl = femalel/lowp
            probh = pfemaleh
            probl = pfemalel
            
        

        pageh = pdf(float(currentathlete[0]),agehmean,agehstdev) #probability of age given that they are a high performer
        pagel = pdf(float(currentathlete[0]),agelmean,agelstdev)

        pheighth = pdf(float(currentathlete[2]),heighthmean,heighthstdev) #probability of the current height given that they are a high performer
        pheightl = pdf(float(currentathlete[2]),heightlmean,heightlstdev) #probability of the current height given that they are a low performer

        pweighth = pdf(float(currentathlete[3]),weighthmean,weighthstdev)
        pweightl = pdf(float(currentathlete[3]),weightlmean,weightlstdev)

        pbfph = pdf(float(currentathlete[4]),bfphmean,bfphstdev)
        pbfpl = pdf(float(currentathlete[4]),bfplmean,bfplstdev)

        pdiastolich = pdf(float(currentathlete[5]),diastolichmean,diastolichstdev)
        pdiastolicl = pdf(float(currentathlete[5]),diastoliclmean,diastoliclstdev)
        
        psystolich = pdf(float(currentathlete[6]),systolichmean,systolichstdev)
        psystolicl = pdf(float(currentathlete[6]),systoliclmean,systoliclstdev)

        pgriph = pdf(float(currentathlete[7]),griphmean,griphstdev)
        pgripl = pdf(float(currentathlete[7]),griplmean,griplstdev)

        psabfh = pdf(float(currentathlete[8]),sabfhmean,sabfhstdev)
        psabfl = pdf(float(currentathlete[8]),sabflmean,sabflstdev)

        psituph = pdf(float(currentathlete[9]),situphmean,situphstdev)
        psitupl = pdf(float(currentathlete[9]),situplmean,situplstdev)

        pbroadh = pdf(float(currentathlete[10]),broadhmean,broadhstdev)
        pbroadl = pdf(float(currentathlete[10]),broadlmean,broadlstdev)

        if(currentathlete[1]=="M"):
            pheighth=pheighth
        elif(currentathlete[1]=="F"): #smoothing to mitigate female athletes from being unfairly penalized
            pheighth+=0.005
            pweighth+=0.015
            pgriph+=0.0025
            psituph+=0.0005

        probhigh = math.log2((pgenderh*pageh*pheighth*pweighth*pbfph*pdiastolich*psystolich*pgriph*psabfh*psituph*pbroadh*probh).real)
        problow = math.log2((pgenderl*pagel*pheightl*pweightl*pbfpl*pdiastolicl*psystolicl*pgripl*psabfl*psitupl*pbroadl*probl).real)

        if(probhigh.real>problow.real):
            print(1)
            prediction = 1
        elif(probhigh.real<problow.real):
            print(0)
            prediction = 0

        if(prediction == int(line[-2])):
            correctcount+=1
        end2 = time.time()
        total2+=1
        
#print(correctcount)    #this code is used for finding and printing the accuracy of the classifier
#print(total2) 
#print(correctcount/total2)
#print("training time is")      #code to print out training and testing time
#print(end1-start1)
#print("testing time is")
#print(end2-start2)