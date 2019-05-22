package main

import (
	"context"
	"google.golang.org/grpc"
	"log"

	"github.com/evgeniy-scherbina/hard_and_soft/robot"
)

func main() {
	// Set up a connection to the server.
	conn, err := grpc.Dial("localhost:8080", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := robot.NewRobotServiceClient(conn)

	{
		resp, err := c.PutEnvironmentInfo(context.Background(), &DefaultEnvInfo)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("resp: %v", resp)
	}

	{
		resp, err := c.PutHumanHeartInfo(context.Background(), &DefaultHumanHeartInfo)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("resp: %v", resp)
	}

	{
		resp, err := c.PutHumanCommonInfo(context.Background(), &DefaultHcInfo)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("resp: %v", resp)
	}

	{
		resp, err := c.PutFlowerpotInfo(context.Background(), &DefaultFlowerpotInfo)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("resp: %v", resp)
	}
}

var (
	DefaultEnvInfo = robot.EnvironmentInfo{
		EnvironmentTemp:    1,
		AtmospherePressure: 2,
		Altitude:           3,
		Humidity:           4,
		RobotBatteryLvl:    5,
		Brightness:         6,
	}

	DefaultHumanHeartInfo = robot.HumanHeartInfo{
		HeartRate:        1,
		HeartRhythm:      2,
		DeviceBatteryLvl: 3,
	}

	DefaultHcInfo = robot.HumanCommonInfo{
		Humidity: 1,
		Temp:     2,
	}

	DefaultFlowerpotInfo = robot.FlowerpotInfo{
		PouredOn: false,
		Humidity: 1,
	}
)