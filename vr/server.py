import time
import zmq
import pandas as pd
import numpy as np

#ZMQ parameters
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#file parameters
DATA_INPUT = ""

#server loop
while True:
    #socket.recv() fn
    message = socket.recv()
    '''
    #TODO: action here to do work and obtain data
    data = pd.read_csv(DATA_INPUT)

    #using gaze specifics
    eye0 = data[[' gaze_0_x',' gaze_0_y', ' gaze_0_z']]
    eye1 = data[[' gaze_1_x',' gaze_1_y', ' gaze_1_z']]

    #using angle specifics
    angle0 = data[' gaze_angle_x']
    angle1 = data[' gaze_angle_y']
    '''

    #output send here
    #using the socket.send() fn
    #TODO: we format the data and determine the location on the screen we're looking, then send that to UNITY
    #TODO: meaning I think UNITY only ever takes the data and readjusts the scene

    #TODO: additionally, we can make walls that are interacted via facial expression too
    #TODO: this part is done via AU, and we can look at the intensity level as well

    #for now let's just consistently send a random binary value
    RAND = np.around(np.random.random())
    print(message)
    if RAND:
        socket.send_string("true")
    else:
        socket.send_string("false")
    time.sleep(1) #loops every 30 seconds
