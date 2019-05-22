import robot_pb2
import robot_pb2_grpc

import grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channel = grpc.insecure_channel('localhost:8080')
    stub = robot_pb2_grpc.RobotServiceStub(channel)
    response = stub.PutEnvironmentInfo(robot_pb2.EnvironmentInfo(
        EnvironmentTemp=1,
        AtmospherePressure=2,
        Altitude=3,
        Humidity=4,
        RobotBatteryLvl=5,
        Brightness=6
    ))
    # print("Robot client received: " + response)

run()
