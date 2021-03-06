# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import robot_pb2 as robot__pb2


class RobotServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PutEnvironmentInfo = channel.unary_unary(
        '/robot.RobotService/PutEnvironmentInfo',
        request_serializer=robot__pb2.EnvironmentInfo.SerializeToString,
        response_deserializer=robot__pb2.Empty.FromString,
        )
    self.PutHumanHeartInfo = channel.unary_unary(
        '/robot.RobotService/PutHumanHeartInfo',
        request_serializer=robot__pb2.HumanHeartInfo.SerializeToString,
        response_deserializer=robot__pb2.Empty.FromString,
        )
    self.PutHumanCommonInfo = channel.unary_unary(
        '/robot.RobotService/PutHumanCommonInfo',
        request_serializer=robot__pb2.HumanCommonInfo.SerializeToString,
        response_deserializer=robot__pb2.Empty.FromString,
        )
    self.PutFlowerpotInfo = channel.unary_unary(
        '/robot.RobotService/PutFlowerpotInfo',
        request_serializer=robot__pb2.FlowerpotInfo.SerializeToString,
        response_deserializer=robot__pb2.Empty.FromString,
        )


class RobotServiceServicer(object):

  def PutEnvironmentInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutHumanHeartInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutHumanCommonInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutFlowerpotInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RobotServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PutEnvironmentInfo': grpc.unary_unary_rpc_method_handler(
          servicer.PutEnvironmentInfo,
          request_deserializer=robot__pb2.EnvironmentInfo.FromString,
          response_serializer=robot__pb2.Empty.SerializeToString,
      ),
      'PutHumanHeartInfo': grpc.unary_unary_rpc_method_handler(
          servicer.PutHumanHeartInfo,
          request_deserializer=robot__pb2.HumanHeartInfo.FromString,
          response_serializer=robot__pb2.Empty.SerializeToString,
      ),
      'PutHumanCommonInfo': grpc.unary_unary_rpc_method_handler(
          servicer.PutHumanCommonInfo,
          request_deserializer=robot__pb2.HumanCommonInfo.FromString,
          response_serializer=robot__pb2.Empty.SerializeToString,
      ),
      'PutFlowerpotInfo': grpc.unary_unary_rpc_method_handler(
          servicer.PutFlowerpotInfo,
          request_deserializer=robot__pb2.FlowerpotInfo.FromString,
          response_serializer=robot__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'robot.RobotService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
