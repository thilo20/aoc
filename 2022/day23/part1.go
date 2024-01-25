package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

type Elf struct {
	x, y   int
	action string
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
	elves := make([]Elf, 0)

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
				elves = append(elves, Elf{i, y, ""})
			}
		}
	}
	readFile.Close()

	Print(board)
	tests := []string{"NSWE", "SWEN", "WENS", "ENSW"}

	for round := 0; round < 10; round++ {
		fmt.Printf("round: %d tests: %s\n", round, tests[round%4])

		// propose moves, find duplicates
		moves := make(map[int]map[int]int)
		anyone_moves := false // if true: process ends

		for i, elf := range elves {
			// true: another elf present, false: area free
			north := board[elf.y-1][elf.x-1] || board[elf.y-1][elf.x] || board[elf.y-1][elf.x+1]
			south := board[elf.y+1][elf.x-1] || board[elf.y+1][elf.x] || board[elf.y+1][elf.x+1]
			west := board[elf.y-1][elf.x-1] || board[elf.y][elf.x-1] || board[elf.y+1][elf.x-1]
			east := board[elf.y-1][elf.x+1] || board[elf.y][elf.x+1] || board[elf.y+1][elf.x+1]

			// false: no elf around, stay here
			move := north || south || west || east
			if move {
				x := elf.x
				y := elf.y
				action := ""
				for _, dir := range tests[round%4] {
					switch byte(dir) {
					case 'N':
						if !north {
							y--
							action = "N"
							goto MOVE
						}
					case 'S':
						if !south {
							y++
							action = "S"
							goto MOVE
						}
					case 'W':
						if !west {
							x--
							action = "W"
							goto MOVE
						}
					case 'E':
						if !east {
							x++
							action = "E"
							goto MOVE
						}
					}
				}
			MOVE:
				// propose move
				if moves[y] == nil {
					moves[y] = make(map[int]int)
				}
				moves[y][x]++
				elf.action = action
				anyone_moves = true
			} else {
				elf.action = "stay"
			}
			//store changes
			elves[i] = elf
		}

		//apply moves
		for i, elf := range elves {
			switch elf.action {
			case "N":
				if moves[elf.y-1][elf.x] < 2 {
					board[elf.y][elf.x] = false
					elf.y--
					if board[elf.y] == nil {
						board[elf.y] = make(map[int]bool)
					}
					board[elf.y][elf.x] = true
				} else {
					elf.action = "denied"
				}
			case "S":
				if moves[elf.y+1][elf.x] < 2 {
					board[elf.y][elf.x] = false
					elf.y++
					if board[elf.y] == nil {
						board[elf.y] = make(map[int]bool)
					}
					board[elf.y][elf.x] = true
				} else {
					elf.action = "denied"
				}
			case "W":
				if moves[elf.y][elf.x-1] < 2 {
					board[elf.y][elf.x] = false
					elf.x--
					board[elf.y][elf.x] = true
				} else {
					elf.action = "denied"
				}
			case "E":
				if moves[elf.y][elf.x+1] < 2 {
					board[elf.y][elf.x] = false
					elf.x++
					board[elf.y][elf.x] = true
				} else {
					elf.action = "denied"
				}
			}
			//store changes
			elves[i] = elf
		}
		Print(board)
		if !anyone_moves {
			break
		}
	}

	//determine bbox
	xmin := 10
	xmax := 0
	ymin := 10
	ymax := 0
	for _, elf := range elves {
		if elf.x < xmin {
			xmin = elf.x
		}
		if elf.x > xmax {
			xmax = elf.x
		}
		if elf.y < ymin {
			ymin = elf.y
		}
		if elf.y > ymax {
			ymax = elf.y
		}
	}
	ground := 0
	for x := xmin; x <= xmax; x++ {
		for y := ymin; y <= ymax; y++ {
			if !board[y][x] {
				ground++
			}
		}
	}
	fmt.Println("empty ground tiles:", ground)

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
