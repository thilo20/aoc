package main

import (
	"bufio"
	"fmt"
	"os"
)

// day 6 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()

		for n := 4; n < len(line); n++ {
			if HasNUniqueChars(line[n-4:n], 4) {
				fmt.Println(n)
				break
			}
		}

	}
	readFile.Close()
}

func HasNUniqueChars(line string, n int) bool {
	var chars = make(map[byte]int)
	chars[line[0]] = 1
	chars[line[1]] = 1
	chars[line[2]] = 1
	chars[line[3]] = 1

	if len(chars) == n {
		return true
	}
	return false
}
