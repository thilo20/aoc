package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

// math monkey
type MathMonkey struct {
	op1, op2, operation string
}

// day 23 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	buf, err := os.ReadFile(filePath)
	if err != nil {
		fmt.Errorf("could not read input: %w", err)
	}
	lines := strings.Split(strings.TrimSpace(string(buf)), "\n")

	//keys: row/y, col/x
	//values: true: "#" Elf present, false: "." free space
	board := make(map[int]map[int]bool)

	var boardregexp = regexp.MustCompile(`([\.#])`)
	// init
	for y, line := range lines {
		board[y] = make(map[int]bool)
		m := boardregexp.FindAllString(line, -1)
		for i := 0; i < len(m); i++ {
			switch m[i] {
			case ".":
				board[y][i] = false
			case "#":
				board[y][i] = true
			}
		}
	}
	readFile.Close()

	Print(board)
}

// go math.Abs is for float / requires conversion
func Abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func Print(board map[int]map[int]bool) {
	var b strings.Builder
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			switch board[i][j] {
			case false:
				b.WriteByte('.')
			case true:
				b.WriteByte('#')
			}
		}
		b.WriteByte('\n')
	}
	fmt.Print(b.String())
}
