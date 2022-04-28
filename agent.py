'''
File: agent.py
Author: Joshua Jacobs-Rebhun
Date: April 21, 2022

agent.py contains the Agent class that is one of the main classes imported
by users for building agent-based models along with the Model class contained
in model.py
'''

class Agent:

    def __init__(self):
        
        # stores the port to connect to in order to do Remote Method Calls
        self.port = None
    
    def setAgentManager(self, agentManager):
        self.agentManager = agentManager

    def step(self):
        pass