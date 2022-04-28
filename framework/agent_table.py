'''
Author: Joshua Jacobs-Rebhun
Date: April 23, 2022

Contains the class implementing the DistributedAgentTable data type for
keeping track of agents in the system.
'''

import threading
import socket

class AgentTable:

    # nodes must be a dictionary mapping node numbers to IP endpoints
    # i.e. (IP address, port), and agentAssignmentFunc is a function
    # mapping agent numbers to node numbers. NodeNumber is the number
    # of the node that contains the DAT
    def __init__(self, numAgents, nodeNumber, nodes, port, agentAssignmentFunc=None):

        self.numAgents = numAgents
        self.numOwnAgents = 0
        self.nodeNumber = nodeNumber

        # dictionary containing the agents contained in this node
        self.ownAgents = {}

        # self.port stores the port number that the RPC server binds to
        self.port = port

        self.nodes = nodes
        self.numNodes = len(nodes)

        if agentAssignmentFunc is None:
            def assignmentFunc(self, agentNumber):
                self.agentToNode[agent] = hash(agentNumber) % self.numNodes
            
            self.agentAssignmentFunc = assignmentFunc
        
        else:
            self.agentAssignmentFunc = agentAssignmentFunc
        
        
    def handleRequest(self, socket, address):
        pass


    def runRPCServer(self):

        # create socket and bind it to a specific address
        rpcSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rpcSocket.bind((socket.gethostbyname(socket.gethostname()), self.port))
        rpcSocket.listen()

        while True:
            clientSocket, address = rpcSocket.accept()
            threading.Thread(self.handleRPCServer, args=(clientSocket, address)).start()
            
    
    def startServer(self):
        serverThread = threading.Thread(target=self.runRPCServer)
        serverThread.start()
    

    def getAgent(self, agentNumber):
        node = self.agentAssignmentFunc(agentNumber)

        if node == self.nodeNumber:
            return self.ownAgents[agentNumber]
        
        else:
            agent = list(ownAgents.values())[0]
            stub = agent.__class__.__new__(agent.__class__)
            stub.__init__()
            stub.port = self.port
            return stub


    def addAgent(self, agent):
        node = self.agentAssignmentFunc(agent.id)
        
        if node == self.nodeNumber:
            self.ownAgents[agent.id] = agent
            self.ownAgents[agent.id].port = self.port


    def isOwn(self, agentNumber):
        return self.agentAssignmentFunc(agent.id) == self.nodeNumber


    def removeAgent(self, agent):
        node = self.agentAssignmentFunc(agent.id)

        if node = self.nodeNumber:
            del(self.ownAgents[agent.id])