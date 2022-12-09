package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"

	"k8s.io/apimachinery/pkg/util/sets"
)

// day 3 part 2
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	elves := make([]string, 0)
	lc := 0
	max := 0

	for scanner.Scan() {
		line := scanner.Text()
		lc++

		elves = append(elves, line)

		if lc%3 == 0 {
			a := getDuplicate(elves)
			prio := getPriority(a)
			max += prio
			elves = make([]string, 0)
		}
	}
	readFile.Close()

	fmt.Println(max)
}

func getPriority(a string) int {
	switch {
	case unicode.IsLower(rune(a[0])):
		return int(a[0] - 'a' + 1)
	case unicode.IsUpper(rune(a[0])):
		return int(a[0] - 'A' + 27)
	}
	return 0
}

func getDuplicate(elves []string) string {
	var a sets.String = sets.NewString()
	for _, val := range elves[0] {
		a.Insert(string(val))
	}
	var a2 sets.String = sets.NewString()
	for _, val := range elves[1] {
		a2.Insert(string(val))
	}
	var a3 sets.String = sets.NewString()
	for _, val := range elves[2] {
		a3.Insert(string(val))
	}

	dupl := a.Intersection(a2)
	dupl = dupl.Intersection(a3)
	fmt.Println(dupl.Len(), dupl.List())
	return dupl.List()[0]
}
