package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

// day 4 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	max := 0
	for scanner.Scan() {
		line := scanner.Text()

		re := regexp.MustCompile(`\d+`)
		m := re.FindAllString(line, -1)
		if m == nil {
			panic("mo match")
		}

		lo1, _ := strconv.ParseInt(m[0], 10, 64)
		hi1, _ := strconv.ParseInt(m[1], 10, 64)
		lo2, _ := strconv.ParseInt(m[2], 10, 64)
		hi2, _ := strconv.ParseInt(m[3], 10, 64)

		d1 := hi1 - lo1
		d2 := hi2 - lo2
		ma := Max(d1, d2)

		x1 := hi2 - lo1
		x2 := hi1 - lo2

		if x1 <= ma && x2 <= ma {
			max += 1
		}

	}
	readFile.Close()

	fmt.Println(max)
}

func Min(x, y int64) int64 {
	if x < y {
		return x
	}
	return y
}

func Max(x, y int64) int64 {
	if x > y {
		return x
	}
	return y
}
