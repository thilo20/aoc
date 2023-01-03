package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Mmap map[int]string

func (m Mmap) Get(x, y int) string {
	if y < 0 || y >= len(m) {
		return " "
	}
	if x < 0 || x >= len(m[y]) {
		return " "
	}
	return string(m[y][x])
}

func (m Mmap) GetWrap(x, y, dir int) string {
	switch dir {
	case 0:
		return m.Get(x+1, y)
	case 1:
		return m.Get(x, y+1)
	case 2:
		return m.Get(x-1, y)
	case 3:
		return m.Get(x, y-1)
	}
	return ""
}

// day 22 part 1
func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	mmap := make(Mmap, 0)
	i := 0

	scanner := bufio.NewScanner(readFile)
	// read monkey map
	for scanner.Scan() {
		line := scanner.Text()

		if len(line) < 1 {
			break
		}
		mmap[i] = line
		i++
	}

	// turtle
	x, y, dir := 0, 0, 0
	x = strings.Index(mmap[0], ".")

	// read commands
	if scanner.Scan() {
		line := scanner.Text()

		re := regexp.MustCompile(`([\d]+)|([RL])`)
		m := re.FindAllString(line, -1)
		if m == nil {
			panic("no match")
		}

		for _, cmd := range m {
			switch cmd {
			case "R":
				dir++
				if dir > 3 {
					dir = 0
				}
			case "L":
				dir--
				if dir < 0 {
					dir = 3
				}
			default:
				steps, _ := strconv.ParseInt(cmd, 10, 64)
				x, y = move(x, y, dir, int(steps), mmap)
			}
			fmt.Printf("cmd:%s x=%d y=%d dir=%d\n", cmd, x, y, dir)
		}
	}

	readFile.Close()

	row := y + 1
	column := x + 1
	facing := dir
	// The final password is the sum of 1000 times the row, 4 times the column, and the facing.
	fmt.Println("final password:", 1000*row+4*column+facing)
}

func move(x, y, dir int, steps int, mmap Mmap) (int, int) {
	for i := 0; i < steps; i++ {
		field := mmap.GetWrap(x, y, dir)
		if field == "." { // free
			switch dir {
			case 0:
				x++
			case 2:
				x--
			case 1:
				y++
			case 3:
				y--
			}
		} else if field == "#" { // blocked
			break
		} else if field == " " { // wrap
			switch dir {
			case 0: // check row from left
				for n := 0; n < x; n++ {
					switch mmap.Get(n, y) {
					case "#":
						goto BLOCKED
					case ".":
						x = n
					}
				}
			case 2: // check row from right
				for n := len(mmap[y]) - 1; n > x; n-- {
					switch mmap.Get(n, y) {
					case "#":
						goto BLOCKED
					case ".":
						x = n
					}
				}
			case 1: // check column from top
				for n := 0; n < y; n++ {
					switch mmap.Get(x, n) {
					case "#":
						goto BLOCKED
					case ".":
						y = n
					}
				}
			case 3: // check column from bottom
				for n := len(mmap) - 1; n > y; n-- {
					switch mmap.Get(x, n) {
					case "#":
						goto BLOCKED
					case ".":
						y = n
					}
				}
			}
		BLOCKED:
		}

	}
	return x, y
}
