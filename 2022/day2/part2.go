package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
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

// day 2 part 2
func main() {

	scanner := bufio.NewScanner(os.Stdin)

	elves := make([]Round, 0)
	max := 0
	fmt.Println(Rock)
	for scanner.Scan() {
		line := scanner.Text()
		elves = append(elves, roundFromLine(line))
	}
	//sort.Ints(elves)
	fmt.Println(elves)

	//	best := elves[len(elves)-3:]
	for _, value := range elves {
		// use '_' as blank identifier, see https://www.geeksforgeeks.org/what-is-blank-identifierunderscore-in-golang/
		// fmt.Printf("%d = %d\n", key, value)
		max += value.points
	}

	fmt.Println(max)
}
