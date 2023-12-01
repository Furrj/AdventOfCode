package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	count := 0

	lines, err := readLines("inputs.txt")
	if err != nil {
		fmt.Println("File error")
		os.Exit(-1)
	}

	for _, v := range lines {
		if checkLinePart2(v) {
			count++
		}
	}

	fmt.Printf("Count: %d\n", count)
}

func checkLinePart1(lineToCheck string) bool {
	hasVowels := false
	hasRepeating := false

	// Illicit
	if strings.Contains(lineToCheck, "ab") ||
		strings.Contains(lineToCheck, "cd") ||
		strings.Contains(lineToCheck, "pq") ||
		strings.Contains(lineToCheck, "xy") {
		return false
	}

	// Vowel
	vowelCount := 0
	for _, v := range lineToCheck {

		if string(v) == "a" ||
			string(v) == "e" ||
			string(v) == "i" ||
			string(v) == "o" ||
			string(v) == "u" {
			vowelCount++
		}
	}
	fmt.Println(vowelCount)
	if vowelCount >= 3 {
		hasVowels = true
	}

	// Repeating
	for i := 0; i < len(lineToCheck)-1; i++ {
		currentChar := lineToCheck[i]
		if currentChar == lineToCheck[i+1] {
			hasRepeating = true
			break
		}
	}

	// Flag check
	if hasVowels && hasRepeating {
		return true
	}

	return false
}

func checkLinePart2(lineToCheck string) bool {
	hasRepeat, hasSandwich := false, false

	// Repeat
	for i := 0; i < len(lineToCheck)-1; i++ {
		currentStr := string(lineToCheck[i])
		currentStr += string(lineToCheck[i+1])

		if strings.Count(lineToCheck, currentStr) > 1 {
			hasRepeat = true
		}
	}

	// Sandwhich
	for i := 0; i < len(lineToCheck)-2; i++ {
		currentChar := lineToCheck[i]
		if currentChar == lineToCheck[i+2] {
			hasSandwich = true
			break
		}
	}

	if hasRepeat && hasSandwich {
		return true
	}
	return false
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
