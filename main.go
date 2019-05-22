package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"log"
	"net"

	"github.com/evgeniy-scherbina/hard_and_soft/robot"
)

type rpcServer struct {}

func (s *rpcServer) PutEnvironmentInfo(ctx context.Context, req *robot.EnvironmentInfo) (*robot.Empty, error) {
	log.Println("PutEnvironmentInfo")
	fmt.Println(req)

	return &robot.Empty{}, nil
}

func (s *rpcServer) PutHumanHeartInfo(ctx context.Context, req *robot.HumanHeartInfo) (*robot.Empty, error) {
	log.Println("PutHumanHeartInfo")
	fmt.Println(req)

	return &robot.Empty{}, nil
}

func (s *rpcServer) PutHumanCommonInfo(ctx context.Context, req *robot.HumanCommonInfo) (*robot.Empty, error) {
	log.Println("PutHumanCommonInfo")
	fmt.Println(req)

	return &robot.Empty{}, nil
}

func (s *rpcServer) PutFlowerpotInfo(ctx context.Context, req *robot.FlowerpotInfo) (*robot.Empty, error) {
	log.Println("PutFlowerpotInfo")
	fmt.Println(req)

	return &robot.Empty{}, nil
}

func main() {
	fmt.Println("Hello world")

	lis, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	robot.RegisterRobotServiceServer(s, &rpcServer{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}