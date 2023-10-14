package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// lights := [1000000]bool{}
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
		fmt.Println(a)
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
