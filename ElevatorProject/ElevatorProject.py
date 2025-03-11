import sys

# Runs as simple elevator simulation that takes a starting floor and number of floors and returns
# the total time (10 per floor) and all the floors that were traveled to
#   :param _startingFloor: the starting floor number
#   :param _listOfFloors: the number of all the floors to be traveled to, pass in as an array
#   :returns: Total travel time (int) and list of floors traveled to (integer array)
def runElevator(_startingFloor, _listOfFloors):

    totalTravelTime = 0
    # Set our current floor to the starting floor so we can keep track
    currFloor = _startingFloor
    listOfFloorsTraveledTo = [currFloor]

    for floor in _listOfFloors:
        # Since the travel time is 10 per floor, we will take the absolute
        # difference between the current floor and the floor we want to
        # go to and add it to the total travel time
        totalTravelTime += abs(currFloor - floor) * 10
        currFloor = floor
        listOfFloorsTraveledTo.append(currFloor)
        
    return totalTravelTime, listOfFloorsTraveledTo



############### Utility Functions ###############3

# Validation function that validates system input to later be passed into runElevatorMethod
#   :param _startingFloor: Raw starting floor input that should be an int greater than 0
#   :param _listOfFloors: Raw list of floors that should be a list of integers greater than 0
#   :returns: error message string (empty if no error)
def validateElevatorInputs(_startingFloor, _listOfFloors):
    # Validates starting floor input to make sure it is a non-negative, non-zero integer
    try:
        intStartingFloor = int(_startingFloor)
        if intStartingFloor < 1:
            return "Starting floor is zero or negative, please choose a positive, non-negative starting floor."
    except ValueError:
        return "Starting floor is not an integer."

    # Validates that list of floors are non-negative, non-zero integers
    try:
        for supposedFloorNum in _listOfFloors:
            integerFloor = int(supposedFloorNum)
            if integerFloor < 1:
                return "Floor " + supposedFloorNum + " is zero or negative, please choose a positive, non-negative floor."      
    except ValueError:
        return "Not all floors in list of floors are integers"
        
    # Returns empty string if validation successful
    return ''


# Utility function that processes system argument input
#   :param _sysArguments: all arguments passed in through the command line
#   :returns: starting floor int, integer array of floors to travel to, error message string (empty if no error)
def processInput(_sysArguments):
    # Store raw input for validation and further processing
    rawStringArrayOfFloors = _sysArguments[2:]
    # we take the second arugment (position 1) because the first is the file name which we don't use
    rawFloorInput = _sysArguments[1]
    
    # Validate inputs
    errorMsg = validateElevatorInputs(rawFloorInput, rawStringArrayOfFloors)
    if len(errorMsg) != 0:
        return '', [], errorMsg

    # Turn initial floor and list of floors into integers
    startingFloorInput = int(rawFloorInput)
    integerArrayOfFloors = []

    # Go through the array and turn them into integers
    for arg in rawStringArrayOfFloors:
        num = int(arg)
        integerArrayOfFloors.append(num)

    return startingFloorInput, integerArrayOfFloors, ''


# Main function that runs runElevator() with parameters if parameters are passed in, if no params are passed
# then it runs the test suite
def main():

    try:
        if len(sys.argv) > 2:
            startingFloorInt, arrayOfFloorsIntArray, errorMsg = processInput(sys.argv)   
            totalTravelTimeint, listOfFloorsIntArray = runElevator(startingFloorInt, arrayOfFloorsIntArray)
            
            if len(errorMsg) != 0:
                print(errorMsg)
                return

            print("Total travel time: " + str(totalTravelTimeint))
            print("List of floors traveled to: " + str(listOfFloorsIntArray))
              
        else:
            runTestSuite()
                
    except Exception as e:
        print(e)
        
    input("Press RETURN to close")
    


################# Testing Functions ##############3

# Runs all tests and prints successes and failures
def runTestSuite():
    totalSuccesses = 0
    totalExpectedSuccesses = 0
    
    successes, expectedSuccesses = runElevatorShouldReturnCorrectValues()
    totalSuccesses = totalSuccesses + successes
    totalExpectedSuccesses = totalExpectedSuccesses + successes
    
    successes, expectedSuccesses = processInputShouldProcessInputsCorrectly()
    totalSuccesses = totalSuccesses + successes
    totalExpectedSuccesses = totalExpectedSuccesses + successes
    
    print("Total successes: " + str(totalSuccesses) + " out of " + str(totalExpectedSuccesses) + " expected successes.")
    print(str(totalExpectedSuccesses - totalSuccesses) + " failures.")


# Tests runElevator() method with various inputs and makes sure the outputs are correct (not-expansive)
#   :returns: successes (int) and expected successes (int)    
def runElevatorShouldReturnCorrectValues():
    
    print("Running test: runElevatorShouldReturnCorrectValues\n")
    successes = 0
    expectedSuccesses = 4
    #Data format = [starting floor, floor1, floor2, etc.]
    testInputData = [[10, 11, 12, 13, 14],
                     [1, 10, 100, 200],
                     [5, 100, 10, 1],
                     [1000, 1, 1000, 1]]
    
    #Data format = [Total time, starting floor, floor1, floor2, etc.]
    testOutputData = [[40, 10, 11, 12, 13, 14],
                      [1990, 1, 10, 100, 200],
                      [1940, 5, 100, 10, 1],
                      [29970, 1000, 1, 1000, 1]]
     
    testNum = 0
    # Iterate through both arrays at once
    for inputData, outputData in zip(testInputData, testOutputData):
        sampleOutputTime, sampleOutputFloors = runElevator(inputData[0], inputData[1:])
        testNum = testNum + 1
        
        # Print what we expected and what we got
        print("Input: Start Floor = " + str(inputData[1]) + ". Floors to travel to = " + str(inputData[2:]) + ".")
        print("Expected total time: " +str(outputData[0]) + ". Expected floors: " + str(outputData[1:]) + ".")
        print("Actual total time: " + str(sampleOutputTime) + ". Actual floors: " + str(sampleOutputFloors) + ".")
        
        # Tally success
        if sampleOutputTime == outputData[0] and sampleOutputFloors == outputData[1:]:
            print("Test case " + str(testNum) + " ran successfully.\n")
            successes = successes + 1
        else:
            print("Test case " + str(testNum) + " failed.\n")

    return successes, expectedSuccesses


# Test various valid and invalid arguements to make sure processInput() is returning correctly formated inputs
#   :returns: successes (int) and expected successes (int)
def processInputShouldProcessInputsCorrectly():
    
    print("Running test: processInputShouldErrorWhenPassedInvalidInputs\n")
    successes = 0
    expectedSuccesses = 4
    #Data format = [empty string represents file name not used by process input, starting floor, floor1, floor2, etc.]
    testInputData = [
                     # Valid inputs
                     ['', "10", "11", "12", "13", "14"],
                     ['', "1", "10", "100", "200"],
                     ['', "5", "100", "10", "1"],
                     ['', "1000", "1", "1000", "1"],
                     # Invalid inputs
                     ['', "10", "11", "12", "13", "frog"],
                     ['', "elbow", "10", "100", "200"],
                     ['', "-1", "100", "10", "1"],
                     ['', "0", "100", "10", "1"],
                     ['', "1", "100", "-10", "1"],
                     ['', "1000", "orange", '', "pickle"],
                     ['', '', '']]
    
    #Data format = [first floor, array of floors, error message]
    testOutputData = [
                      # Successful outputs
                      [10, [11, 12, 13, 14], ''],
                      [1, [10, 100, 200], ''],
                      [5, [100, 10, 1], ''],
                      [1000, [1, 1000, 1], ''],
                      # Errors
                      ['', [], "Not all floors in list of floors are integers"],
                      ['', [], "Starting floor is not an integer."],
                      ['', [], "Starting floor is zero or negative, please choose a positive, non-negative starting floor."],
                      ['', [], "Starting floor is zero or negative, please choose a positive, non-negative starting floor."],
                      ['', [], "Floor -10 is zero or negative, please choose a positive, non-negative floor."],
                      ['', [], "Not all floors in list of floors are integers"],
                      ['', [], "Starting floor is not an integer."]]
    
    testNum = 0
    # Iterate through both arrays at once
    for inputData, outputData in zip(testInputData, testOutputData):
        sampleOutputFirstFloor, sampleOutputFloorList, errorMsg = processInput(inputData)
        testNum = testNum + 1
        
        # Print what we expected and what we got
        print("Input: " + str(inputData) + ".")
        
        print("Expected starting floor: " + str(outputData[0]) + ".")
        print("Expected list of floors: " + str(outputData[1]) + ".")
        print("Expected error message: " + str(outputData[2]) + ".")
        
        print("Actual starting floor: " + str(sampleOutputFirstFloor) + ".")
        print("Actual list of floors: " + str(sampleOutputFloorList) + ".")
        print("Actual error message: " + str(errorMsg) + ".")
        
        # Tally successes
        if outputData[0] == sampleOutputFirstFloor and outputData[1] == sampleOutputFloorList and outputData[2] == errorMsg:
            print("Test case " + str(testNum) + " ran successfully.\n")
            successes = successes + 1
        else:
            print("Test case " + str(testNum) + " failed.\n")

    return successes, expectedSuccesses


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
