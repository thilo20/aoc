package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"

	"k8s.io/apimachinery/pkg/util/sets"
)

type Shape int64

const (
	// since iota starts with 0, the first value
	// defined here will be the default
	Undefined Shape = iota
	Rock
	Paper
	Scissors
)

func (s Shape) String() string {
	switch s {
	case Rock:
		return "rock"
	case Paper:
		return "paper"
	case Scissors:
		return "scissors"
	}
	return "unknown"
}

func (s Shape) IntVal() int {
	switch s {
	case Rock:
		return 1
	case Paper:
		return 2
	case Scissors:
		return 3
	}
	return 0
}

type Round struct {
	opponent, you Shape
	win           string
	points        int
}

func (s Round) String() string {
	return fmt.Sprintf("%s %s %s %d", s.opponent, s.you, s.win, s.points)
}

func CalcShape(opp Shape, win string) Shape {
	switch {
	case opp == Rock && win == "no":
		return Scissors
	case opp == Rock && win == "yes":
		return Paper
	case opp == Paper && win == "no":
		return Rock
	case opp == Paper && win == "yes":
		return Scissors
	case opp == Scissors && win == "no":
		return Paper
	case opp == Scissors && win == "yes":
		return Rock
	}
	return opp
}

func CalcPoints(s Round) int {
	points := 0
	points += s.you.IntVal()
	switch {
	case s.win == "draw":
		points += 3
	case s.win == "yes":
		points += 6
	}
	return points
}

func roundFromLine(line string) Round {
	var r Round
	switch {
	case strings.HasPrefix(line, "A"):
		r.opponent = Rock
	case strings.HasPrefix(line, "B"):
		r.opponent = Paper
	case strings.HasPrefix(line, "C"):
		r.opponent = Scissors
	}
	switch {
	case strings.HasSuffix(line, "X"):
		r.win = "no"
	case strings.HasSuffix(line, "Y"):
		r.win = "draw"
	case strings.HasSuffix(line, "Z"):
		r.win = "yes"
	}

	r.you = CalcShape(r.opponent, r.win)
	r.points = CalcPoints(r)
	return r
}

// day 3 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	max := 0
	fmt.Println(Rock)
	for scanner.Scan() {
		line := scanner.Text()

		left := line[:len(line)/2]
		right := line[len(line)/2:]
		fmt.Println(left, right)

		a3 := getDuplicate(left, right)

		prio := getPriority(a3)
		max += prio
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

func getDuplicate(left string, right string) string {
	var a sets.String = sets.NewString()
	for _, val := range left {
		a.Insert(string(val))
	}
	var a2 sets.String = sets.NewString()
	for _, val := range right {
		a2.Insert(string(val))
	}
	a3 := a.Intersection(a2)
	fmt.Println(a3.Len(), a3.List())
	return a3.List()[0]
}
