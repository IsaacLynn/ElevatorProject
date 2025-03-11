!!!!!!!!!!!!!!!!!! Elevator Project README !!!!!!!!!!!!!!!!!!!


#######################
# Running the Project #
#######################

There are 3 ways to run the elevator project, with positional parameters and without (test suite)
1. Run with parameters (ensure python is installed, you may have to add python to PATH)
	a. Open CMD
	b. cd.. to where ElevatorPython.py is located (<folder repo is located in>\ElevatorProject\ElevatorProject)
	c. run 'python ElevatorProject.py x a b c'
		i. Where x is the desired starting floor, a is the first floor you want to travel to, b is the second floor you 
		   want to travel to, etc., you may have as many floors as you like
	d. The program should output the total time traveled the list of floors traveled to in order

2. Run without parameters (ensure python is installed)
	a. Open CMD
	b. cd.. to where ElevatorPython.py is located (<folder repo is located in>\ElevatorProject\ElevatorProject)
	c. run 'python ElevatorProject.py'
	d. The program will then run the test suite and output all expected values, successes, failures, etc.

3. Run via exe
	a. Navigate to where ElevatorPython.exe is located in file explorer 
	   (<folder repo is located in>\ElevatorProject\ElevatorProject\dist)
	b. Double click exe
	c. exe will run the test suite and output all expected values, successes, falures, etc.


###############################################
# ASSUMPTIONS MADE and UNIMPLEMENTED FEATURES #
###############################################

Here are all the assumptions made during the development of this project:

1. No time is spent at any of the floors specified, since no time was specified to be spent
   at the floors in the requirements, I made it so no time stopping at any floors was calculated
    1a. Travel time is the same for all floors, and is per floor i.e. traveling from floor 1 to 10
	yields a travel time of 90, not 10

2. The user will not enter so many floors or floors with such a high number that it would exceed the
   storage capability of the integer type in python when calculating total time

3. The user will not need to enter multiple inputs for the same execution (i.e. you enter one starting floor and
   a list of floors to travel to, you can't enter multiple sets of inputs and get multiple travel times without
   rerunning the progam)

4. No GUI or command line interface, the project can only run preset tests or be run with positional arguments

5. No negative floors - for simplicity sakes no negative floors or floor 0 is allowed, to simulate basement levels
   the bottom basement floor should be considered floor 1

6. No complex elevator features (e.g. no ability to add unexpected emergency stops, no simulation of possible technical
   difficulties, no ability to simulate slowdowns due to exceeding weight limit of elevator)

7. Tests are not unit tests because validateElevatorInputs() is not tested on its own, and dependency functions are not mocked,
   the tests are more just basic functional test and are not expansive