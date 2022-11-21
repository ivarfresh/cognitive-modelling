### 
### This code is developed by Christian P. Janssen of Utrecht University
### It is intended for students from the Master's course Cognitive Modeling
### Large parts are based on the following research papers:
### Janssen, C. P., & Brumby, D. P. (2010). Strategic adaptation to performance objectives in a dual‐task setting. Cognitive science, 34(8), 1548-1560. https://onlinelibrary.wiley.com/doi/full/10.1111/j.1551-6709.2010.01124.x
### Janssen, C. P., Brumby, D. P., & Garnett, R. (2012). Natural break points: The influence of priorities and cognitive and motor cues on dual-task interleaving. Journal of Cognitive Engineering and Decision Making, 6(1), 5-29. https://journals.sagepub.com/doi/abs/10.1177/1555343411432339
###
### If you want to use this code for anything outside of its intended purposes (training of AI students at Utrecht University), please contact the author:
### c.p.janssen@uu.nl



### 
### import packages
###

import numpy
from numpy.random import normal 


###
###
### Global parameters. These can be called within functions to change (Python: make sure to call GLOBAL)
###
###


###
### Car / driving related parameters
###
steeringUpdateTime = 250    #in ms ## How long does one steering update take? (250 ms consistent with Salvucci 2005 Cognitive Science)
timeStepPerDriftUpdate = 50 ### msec: what is the time interval between two updates of lateral position?
startingPositionInLane = 0.27 			#assume that car starts already slightly away from lane centre (in meters) (cf. Janssen & Brumby, 2010)


#parameters for deviations in car drift due the simulator environment: See Janssen & Brumby (2010) page 1555
gaussDeviateMean = 0
gaussDeviateSD = 0.13 ##in meter/sec


#When the car is actively controlled, calculate a value using equation (1) in Janssen & Brumby (2010). However, some noise is added on top of this equation to account for variation in human behavior. See Janssen & Brumby (2010) page 1555. Also see function "updateSteering" on how this function is used
gaussDriveNoiseMean = 0
gaussDriveNoiseSD = 0.1	#in meter/sec


### The car is controlled using a steering wheel that has a maximum angle. Therefore, there is also a maximum to the lateral velocity coming from a steering update
maxLateralVelocity = 1.7	# in m/s: maximum lateral velocity: what is the maximum that you can steer?
minLateralVelocity = -1* maxLateralVelocity

startvelocity = 0 	#a global parameter used to store the lateral velocity of the car


###
### Switch related parameters
###
retrievalTimeWord = 200   #ms. ## How long does it take to think of the next word when interleaving after a word (time not spent driving, but drifting)
retrievalTimeSentence = 300 #ms. ## how long does it take to retrieve a sentence from memory (time not spent driving, but drifting)



###
### parameters for typing task
###
timePerWord = 0  ### ms ## How much time does one word take
wordsPerMinuteMean = 39.33   # parameters that control typing speed: when typing two fingers, on average you type this many words per minute. From Jiang et al. (2020; CHI)
wordsPerMinuteSD = 10.3 ## this si standard deviation (Jiang et al, 2020)


## Function to reset all parameters. Call this function at the start of each simulated trial. Make sure to reset GLOBAL parameters.
def resetParameters():
    global timePerWord
    global retrievalTimeWord
    global retrievalTimeSentence 
    global steeringUpdateTime 
    global startingPositionInLane 
    global gaussDeviateMean
    global gaussDeviateSD 
    global gaussDriveNoiseMean 
    global gaussDriveNoiseSD 
    global timeStepPerDriftUpdate 
    global maxLateralVelocity 
    global minLateralVelocity 
    global startvelocity
    global wordsPerMinuteMean
    global wordsPerMinuteSD
    
    timePerWord = 0  ### ms

    retrievalTimeWord = 200   #ms
    retrievalTimeSentence = 300 #ms
	
    steeringUpdateTime = 250    #in ms
    startingPositionInLane = 0.27 			#assume that car starts already away from lane centre (in meters)
	

    gaussDeviateMean = 0
    gaussDeviateSD = 0.13 ##in meter/sec
    gaussDriveNoiseMean = 0
    gaussDriveNoiseSD = 0.1	#in meter/sec
    timeStepPerDriftUpdate = 50 ### msec: what is the time interval between two updates of lateral position?
    maxLateralVelocity = 1.7	# in m/s: maximum lateral velocity: what is the maximum that you can steer?
    minLateralVelocity = -1* maxLateralVelocity
    startvelocity = 0 	#a global parameter used to store the lateral velocity of the car
    wordsPerMinuteMean = 39.33
    wordsPerMinuteSD = 10.3

	



##calculates if the car is not accelerating more than it should (maxLateralVelocity) or less than it should (minLateralVelocity)  (done for a vector of numbers)
def velocityCheckForVectors(velocityVectors):
    global maxLateralVelocity
    global minLateralVelocity

    velocityVectorsLoc = velocityVectors

    if (type(velocityVectorsLoc) is list):
            ### this can be done faster with for example numpy functions
        velocityVectorsLoc = velocityVectors
        for i in range(len(velocityVectorsLoc)):
            if(velocityVectorsLoc[i]>1.7):
                velocityVectorsLoc[i] = 1.7
            elif (velocityVectorsLoc[i] < -1.7):
                velocityVectorsLoc[i] = -1.7
    else:
        if(velocityVectorsLoc > 1.7):
            velocityVectorsLoc = 1.7
        elif (velocityVectorsLoc < -1.7):
            velocityVectorsLoc = -1.7

    return velocityVectorsLoc
	




## Function to determine lateral velocity (controlled with steering wheel) based on where car is currently positioned. See Janssen & Brumby (2010) for more detailed explanation. Lateral velocity update depends on current position in lane. Intuition behind function: the further away you are, the stronger the correction will be that a human makes
def vehicleUpdateActiveSteering(LD):

    latVel = 0.2617 * LD*LD + 0.0233 * abs(LD) - 0.022
    
    if LD > 0:
        returnValue = -abs(velocityCheckForVectors(latVel))
    else:
        returnValue = abs(velocityCheckForVectors(latVel))
	
    return returnValue
	


### function to update steering angle in cases where the driver is NOT steering actively (when they are distracted by typing for example)
def vehicleUpdateNotSteering():
    
    global gaussDeviateMean
    global gaussDeviateSD 

    

    vals = numpy.random.normal(loc=gaussDeviateMean, scale=gaussDeviateSD,size=1)[0]
    returnValue = velocityCheckForVectors(vals)
    return returnValue





### Function to run a trial. Needs to be defined by students (section 2 and 3 of assignment)

def runTrial(nrWordsPerSentence =5,nrSentences=3,nrSteeringMovementsWhenSteering=2, interleaving="word"): 
    resetParameters()
    
    locDrifts = [] # this will hold the vaLues of the lane drift OVER TIME
    trialTime = 0
    
    if interleaving == "word": # check if strategy is word
        trialTime = 0
        locDrifts.append(startingPositionInLane)
        
        # sample typing speed from normal distribution (loc and scal given above)
        WordsPerMinute = normal(loc = wordsPerMinuteMean, scale = wordsPerMinuteSD)
        timePerWord = 60000 / WordsPerMinute # time per word in MILISECONDS
        
        seconds_per_drift_update = timeStepPerDriftUpdate / 1000 #converting ms to s
        
        print(f"Words per minute: {WordsPerMinute}, ms per word: {timePerWord}")
        
        # Loop through sentences
        
        for sentence in range(nrSentences):
            firstWord = True # ms
            for word in range(nrWordsPerSentence):
                timeDelta = firstWord * retrievalTimeSentence + retrievalTimeWord + timePerWord
                trialTime += timeDelta #update 
                print(f"Time elapsed typing sentence {sentence}, word {word}: {timeDelta} ms")
                firstWord = False # other words in sentence are NOT the first word
                
                                

                
                
                # CALCULATE CAR'S DRIFT DURING THIS WORD
                nr_vehicle_updates = int(timeDelta / timeStepPerDriftUpdate)
                
                print(f"This means location updated {nr_vehicle_updates} times while typing")
                
                for i in range(nr_vehicle_updates):
                    LatVel = vehicleUpdateNotSteering() #random velocity
                    locDrifts.append(locDrifts[-1] + LatVel * seconds_per_drift_update)
                    
                print(f"Location updated while typing from {locDrifts[-nr_vehicle_updates-1]} to {locDrifts[-1]}")
                
                if sentence < nrSentences-1 or word < nrWordsPerSentence-1: # if NOT last word of sentence
                
                    
                    
                    nr_steering_steps = int((steeringUpdateTime * nrSteeringMovementsWhenSteering) / timeStepPerDriftUpdate)
                    
                    print(f"The dirver steers between words: {nr_steering_steps} steering steps")
                    
                    for step in range(nr_steering_steps):
                        LD = locDrifts[-1] #current drift location
                        LatVel = vehicleUpdateActiveSteering(LD) # lat vel based on drift location
                        
                        # new drift location
                        locDrifts.append(locDrifts[-1] + seconds_per_drift_update * LatVel)
                        
                    print(f"Location updated while steering from {locDrifts[-nr_steering_steps-1]} to {locDrifts[-1]}")
                    
                    steeringTimeDelta = steeringUpdateTime * nrSteeringMovementsWhenSteering
                    trialTime += steeringTimeDelta
                    print(f"{steeringTimeDelta} ms elapsed while steering.")
                    
                    
                    
                print("")
                    #Steering update
                    
                

        
        
        
    else:
        pass
    
runTrial()
	
	




### function to run multiple simulations. Needs to be defined by students (section 3 of assignment)
def runSimulations(nrSims = 100):
    print("hello world")



	




