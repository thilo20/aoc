package main

import (
	"bufio"
	"fmt"
	"os"
)

// day 6 part 2
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

		for n := 14; n < len(line); n++ {
			if HasNUniqueChars(line[n-14:n], 14) {
				fmt.Println(n)
				break
			}
		}

	}
	readFile.Close()
}

func HasNUniqueChars(line string, n int) bool {
	var chars = make(map[byte]int)
	for i := 0; i < 14; i++ {
		chars[line[i]] = 1
	}

	if len(chars) == n {
		return true
	}
	return false
}
