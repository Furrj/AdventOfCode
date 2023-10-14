package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Coord struct {
	X int
	Y int
}

type Action struct {
	Action string
	Start  Coord
	End    Coord
}

func ParseAction(line string) Action {
	action := Action{}

	if strings.Contains(line, "turn on") {
		action.Action = "on"

		trimmedString := line[8:]
		start := ""

		for _, c := range trimmedString {
			if string(c) == " " {
				break
			}
			start += string(c)
		}

		startSplit := strings.Split(start, ",")
		x, err := strconv.Atoi(startSplit[0])
		if err != nil {
			fmt.Printf("Error with startsplit: %+v\n", err)
			os.Exit(1)
		}
		action.Start.X = x
		y, err := strconv.Atoi(startSplit[1])
		if err != nil {
			fmt.Printf("Error with startsplit: %+v\n", err)
			os.Exit(1)
		}
		action.Start.Y = y

		index := strings.Index(trimmedString, "through")
		trimmedString = trimmedString[index+8:]
		endSplit := strings.Split(trimmedString, ",")
		x, err = strconv.Atoi(endSplit[0])
		if err != nil {
			fmt.Printf("Error with startSplit: %+v\n", err)
			os.Exit(1)
		}
		action.End.X = x
		y, err = strconv.Atoi(endSplit[1])
		if err != nil {
			fmt.Printf("Error with endSplit: %+v\n", err)
			os.Exit(1)
		}
		action.End.Y = y
	} else if strings.Contains(line, "turn off") {
		action.Action = "off"

		trimmedString := line[9:]
		start := ""

		for _, c := range trimmedString {
			if string(c) == " " {
				break
			}
			start += string(c)
		}

		startSplit := strings.Split(start, ",")
		x, err := strconv.Atoi(startSplit[0])
		if err != nil {
			fmt.Printf("Error with startsplit: %+v\n", err)
			os.Exit(1)
		}
		action.Start.X = x
		y, err := strconv.Atoi(startSplit[1])
		if err != nil {
			fmt.Printf("Error with startsplit: %+v\n", err)
			os.Exit(1)
		}
		action.Start.Y = y

		index := strings.Index(trimmedString, "through")
		trimmedString = trimmedString[index+8:]
		endSplit := strings.Split(trimmedString, ",")
		x, err = strconv.Atoi(endSplit[0])
		if err != nil {
			fmt.Printf("Error with startSplit: %+v\n", err)
			os.Exit(1)
		}
		action.End.X = x
		y, err = strconv.Atoi(endSplit[1])
		if err != nil {
			fmt.Printf("Error with endSplit: %+v\n", err)
			os.Exit(1)
		}
		action.End.Y = y
	} else {
		action.Action = "toggle"

		trimmedString := line[7:]
		start := ""

		for _, c := range trimmedString {
			if string(c) == " " {
				break
			}
			start += string(c)
		}

		startSplit := strings.Split(start, ",")
		x, err := strconv.Atoi(startSplit[0])
		if err != nil {
			fmt.Printf("Error with startsplit: %+v\n", err)
			os.Exit(1)
		}
		action.Start.X = x
		y, err := strconv.Atoi(startSplit[1])
		if err != nil {
			fmt.Printf("Error with startsplit: %+v\n", err)
			os.Exit(1)
		}
		action.Start.Y = y

		index := strings.Index(trimmedString, "through")
		trimmedString = trimmedString[index+8:]
		endSplit := strings.Split(trimmedString, ",")
		x, err = strconv.Atoi(endSplit[0])
		if err != nil {
			fmt.Printf("Error with startSplit: %+v\n", err)
			os.Exit(1)
		}
		action.End.X = x
		y, err = strconv.Atoi(endSplit[1])
		if err != nil {
			fmt.Printf("Error with endSplit: %+v\n", err)
			os.Exit(1)
		}
		action.End.Y = y
	}

	return action
}
