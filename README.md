PELMA
===
[PELMA](https://github.com/ashikaro/Elma) is a python event loop manager which can be used by embedded and reactive systems applications in Python.

The source code for this project is available here [github](https://github.com/ashikaro/Elma).

Installation
---

    git clone https://github.com/ashikaro/Elma.git
    cd Elma
    make build
    make run
    make docs


Execution
---
To run the test process in the container, type 

    python -m unittest
    or 
    make test

This runs the unit tests we have written for testing a simple process
and the test robot.


Testing
---
To run tests, do
```bash
    make test
 ```

Architecture
---
   1. This project is designed to work as an ELMA python library which can be published to an artifactory and embedded applications can add this as a dependency to 
      incorporate ELMA into their system.
   1. All the core ELMA classes Manger, Process, Event behave functionally the same way as the C++ ELMA we have built in this class.
   1. As a proof concept to test if ELMA can be used in Embedded apps, we have implemented a simple robot which leverage the ELMA APIs to perform simple operations similar to the assignment 7

Challenges
---

1. Understanding object oriented nuances specific to Python which is a lot different from C++.
2. Steep learning curve considering my inexperience in Python and object oriented languages in general.
3. Implementing virtual methods where we want base class(process) to  have no implementation and expect child classes to implement.
4. Python does not have multi argument constructors.
5. Using python closures with nested function for setting up event handling for all the transitions(StateMachine's init)
6. Writing lambdas in python for event handling.

Results
---
   1. We have written tests for testing Core ELMA APIs and Robot Finite State Machine. 
   Here is the log of the run:
   ```bash
        Running tests for core ELMA APIs Using ELMA Manager to test: 1. Initializing a process 2. Scheduling a process  3. Updating a process 4. Event handler methods watch and emit
        <elma.test.test_process.TestProcess object at 0x7f329ad3efd0>
        watching for hello
        watching for pi
        emitting hello event
        
        emitting event hello
        emitting event hello
        emitting pi event
        
        emitting event pi
        emitting event pi
        
        Running first set of tests for python client Robot Leveraging ELMA APIs.
        Initializing Robot States and making sure states get unique IDs
        Id for state Recharge is 0
        Id for state Wander is 1
        Id for state Find Recharge Station is 2
        Id for state Evade is 3
        Id for state Make Noise is 4
        adding transition for event found recharge station from Find Recharge Station to Recharge
        adding transition for event battery full from Recharge to Wander
        adding transition for event battery low from Wander to Find Recharge Station
        adding transition for event battery low from Evade to Find Recharge Station
        adding transition for event start from Wander to Wander
        adding transition for event reset from Make Noise to Wander
        adding transition for event reset from Evade to Make Noise
        adding transition for event intruder detected from Wander to Make Noise
        adding transition for event proximity warning from Make Noise to Evade
        <elma.api.robot.Robot object at 0x7f329ad3ee48>
        watching for found recharge station
        watching for battery full
        watching for battery low
        watching for battery low
        watching for start
        watching for reset
        watching for reset
        watching for intruder detected
        watching for proximity warning
        <elma.api.robot.Robot object at 0x7f329ad3ee48>
        calling entry method of Wander
        emitting event start
        calling exit method of Wander
        calling entry method of Wander
        Wander
        emitting event intruder detected
        emitting event intruder detected
        calling exit method of Wander
        calling entry method of Make Noise
        Make Noise
        emitting event proximity warning
        calling exit method of Make Noise
        calling entry method of Evade
        Evade
        emitting event battery full
        Evade
        Running First set tests for python client Robot Leveraging ELMA APIs.
        Initializing Robot States and making sure states get unique IDs
        Id for state Recharge is 5
        Id for state Wander is 6
        Id for state Find Recharge Station is 7
        Id for state Evade is 8
        Id for state Make Noise is 9
        adding transition for event found recharge station from Find Recharge Station to Recharge
        adding transition for event battery full from Recharge to Wander
        adding transition for event battery low from Wander to Find Recharge Station
        adding transition for event battery low from Evade to Find Recharge Station
        adding transition for event start from Wander to Wander
        adding transition for event reset from Make Noise to Wander
        adding transition for event reset from Evade to Make Noise
        adding transition for event intruder detected from Wander to Make Noise
        adding transition for event proximity warning from Make Noise to Evade
        <elma.api.robot.Robot object at 0x7f329ad02be0>
        watching for found recharge station
        watching for battery full
        watching for battery low
        watching for battery low
        watching for start
        watching for reset
        watching for reset
        watching for intruder detected
        watching for proximity warning
        <elma.api.robot.Robot object at 0x7f329ad02be0>
        calling entry method of Wander
        Wander
        emitting event battery low
        emitting event battery low
        calling exit method of Wander
        calling entry method of Find Recharge Station
        Find Recharge Station
        emitting event found recharge station
        calling exit method of Find Recharge Station
        calling entry method of Recharge
        Recharge
        emitting event battery full
        calling exit method of Recharge
        calling entry method of Wander
        Wander
        emitting event intruder detected
        calling exit method of Wander
        calling entry method of Make Noise
        Make Noise
        emitting event reset
        calling exit method of Make Noise
        calling entry method of Wander
        Wander
        emitting event intruder detected
        calling exit method of Wander
        calling entry method of Make Noise
        Make Noise
        emitting event proximity warning
        calling exit method of Make Noise
        calling entry method of Evade
        Evade
        emitting event battery low
        calling exit method of Evade
        calling entry method of Find Recharge Station
        Find Recharge Station
        .
        ----------------------------------------------------------------------
        Ran 3 tests in 0.002s
        
        OK

 ```
   
# Milestones
*No changes to the milestones. Going as per the plan.
   1. Requirement Analysis, design, scoping by 12th March 2019
   1. Implement core Elma APIs(Process,Manager) in python by 13th March 2019
   1. Implement API's for FSM.(State,State Machine) in python by 16th March 2019
   1. Implement python client using elma to test a simple robot FSM by 18th March 2019
   1. Documentation using Doxygen generated API descriptions for all classes and methods by 20th March 2019

# Current Accomplishments
   1. Accomplished all the milestones.

# Resources
   * Pluralsight course Python Fundamentals.
   * PyCharm IDE for Python.
   * Will use C++ elma API's used in this course as a reference.
   * Unit Tests for hw_7, for building test robot finite state machine.


Acknowledgements
---


References
---
1. Tests not running -	
 https://stackoverflow.com/questions/43957860/python-unittest-ran-0-tests-in-0-000s
 https://stackoverflow.com/questions/7562775/deriving-a-class-from-testcase-throws-two-errors 
	
2. Docker not able to bring bash shell up. Instead used sh
	https://stackoverflow.com/questions/27959011/why-does-docker-say-it-cant-execute-bash
	
	
3. Docker image for Python reference
	https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
	
4. Python time in milliseconds
    https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3

5. Declaring static variables
	https://www.geeksforgeeks.org/g-fact-34-class-or-static-variables-in-python/
	
6. Inner functions and closures for event handling https://realpython.com/inner-functions-what-are-they-good-for/
