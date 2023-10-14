package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	lights := [1000][1000]light{}
	actions := []Action{}

	// Read input
	strings, err := readLines("inputs.txt")
	if err != nil {
		fmt.Println("Error")
		os.Exit(-1)
	}

	for _, s := range strings {
		actions = append(actions, ParseAction(s))
	}

	for _, a := range actions {
		if a.Action == 1 {
			for i := a.Start.X; i <= a.End.X; i++ {
				for j := a.Start.Y; j <= a.End.Y; j++ {
					lights[i][j].Value += 1
				}
			}
		} else if a.Action == 2 {
			for i := a.Start.X; i <= a.End.X; i++ {
				for j := a.Start.Y; j <= a.End.Y; j++ {
					lights[i][j].decrease()
				}
			}
		} else {
			for i := a.Start.X; i <= a.End.X; i++ {
				for j := a.Start.Y; j <= a.End.Y; j++ {
					lights[i][j].Value += 2
				}
			}
		}
	}

	count := 0
	for _, i := range lights {
		for _, j := range i {
			count += j.Value
		}
	}

	fmt.Printf("Answer: %d\n", count)
}

type light struct {
	Value int
}

func (l *light) decrease() {
	if l.Value > 0 {
		l.Value--
	}
}

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}
