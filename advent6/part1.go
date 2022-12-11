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
			var employee = make(map[byte]int)
			employee[line[n-3]] = 1
			employee[line[n-2]] = 1
			employee[line[n-1]] = 1
			employee[line[n-0]] = 1

			if len(employee) == 4 {
				fmt.Println(n + 1)
				break
			}
		}

	}
	readFile.Close()
}
