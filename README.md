# PELMA
    PELMA - Python Event Loop Manager

# Project Goals
   * In this project, i will implement a fully functioning Event Loop Manager(ELMA)      Library in python. 
   * Python applications can leverage ELMA interface to develop embedded applications    and specifically for running event loops.
   * We will use events for Interprocess communication.

   I will consider this project to be successful if:
   * A Python client can use this library to define processes.
   * A Python client can use this library to schedule processes to run at a certain      frequency.
   * A Python client use this library communicate between processes via events.
   * A Python client can build a Finite State Machine using PELMA library.

   We will build a simple test robot finite state machine using the PELMA library.

# Resources
   * Pluralsight course Python Fundamentals
   * Will use C++ elma API's used in this course as a reference
   * Unit Test for hw_7, for building test robot finite state machine.


# Milestones
*No changes to the milestones. Going as per the plan.
   1. Requirement Analysis, design, scoping by 12th March 2019
   1. Implement core Elma APIs(Process,Manager) in python by 13th March 2019
   1. Implement API's for FSM.(State,State Machine) in python by 16th March 2019
   1. Implement python client using elma to test a simple robot FSM by 18th March 2019
   1. Documentation using Doxygen generated API descriptions for all classes and methods by 20th March 2019

# Current Accomplishments
   1. Completed requirement analysis, design in python and scoping 
   1. Dockerized the python Elma App
   1. Implemented some of the the core Elma APIs - Manager, Process and Event classes in Python
   1. Added a test for some of the core APIs in Process and Manager
      
# Code implemented so far
   1. Created a new package elma.api to hold all the ELMA classes.
   1. We have implemented Manger, Process, Event classes in event.py, manager.py and process.py
   1. Test has been added under the package elma.test

Installation
---

    git clone https://github.com/ashikaro/Elma.git
    cd Elma
    make build
    make run
    
Execution
---
To run the test process once in the container, type 

    python -m unittest
   

Testing
---
To run tests, do
```bash
python -m unittest
```

Architecture
---
Describe how your project was designed, what choices you made, how things are organized, etc.

Results
---
Describe the results of testing and running your code. Include visuals when possible.

Acknowledgements
---
Mention anyone who helped you and how.

References
---
List all libraries, articles, stack overflow answers, etc. that you used to get your code working.
    
Tests not running
	
	https://stackoverflow.com/questions/43957860/python-unittest-ran-0-tests-in-0-000s
	https://stackoverflow.com/questions/7562775/deriving-a-class-from-testcase-throws-two-errors 
	
Docker not able to bring bash shell up. Instead used sh
	https://stackoverflow.com/questions/27959011/why-does-docker-say-it-cant-execute-bash
	
	
Docker image for Python reference
	https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
	
Python time in milliseconds
    https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
