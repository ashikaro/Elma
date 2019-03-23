from elma.api.state_machine import StateMachine
from elma.api.state import State

class RobotState(State):

    def __init__(self, name):
        if name:
            super().__init__(name)

    #! A method that derived instances should define. It is called when the state is
    #! entered by the state machine either when the machine starts or when a transition
    #! to the state is fired.
    #! \param e The event that led to the transition into the state
    def entry(self, event):
        print("calling entry method of {}".format(self.name()))

    #! A method that derived instances should define. It is called repeatedly by the
    #! update() method of the containing StateMachine when the state is active.
    def during(self):
        print("calling during method of {}".format(self.name()))

    #! A method that derived instances should define. It is called just before the state is
    #! exited by the state machine when a transition
    #! from the state is fired.
    #! \param e The event that led to the transition out of the state
    def exit(self, event):
        print("calling exit method of {}".format(self.name()))


class Robot(StateMachine):

    def __init__(self, name=""):
        super().__init__(name)

        print("Initializing Robot States and making sure states get unique IDs")

        self.recharge = RobotState("Recharge")
        self.wander = RobotState("Wander")
        self.find_recharge_station = RobotState("Find Recharge Station")
        self.evade = RobotState("Evade")
        self.make_noise = RobotState("Make Noise")

        self.set_initial(self.wander)
        self.set_propagate(True)
        self.add_transition("found recharge station", self.find_recharge_station,self.recharge)
        self.add_transition("battery full", self.recharge,self.wander)
        self.add_transition("battery low", self.wander,self.find_recharge_station)
        self.add_transition("battery low", self.evade,self.find_recharge_station)
        self.add_transition("start",self.wander,self.wander)
        self.add_transition("reset",self.make_noise,self.wander)
        self.add_transition("reset",self.evade,self.make_noise)
        self.add_transition("intruder detected",self.wander,self.make_noise)
        self.add_transition("proximity warning", self.make_noise,self.evade)







