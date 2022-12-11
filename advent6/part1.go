package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode/utf8"
)

type Stacks struct {
	Stax []string
}

func (x Stacks) Heads() string {
	h := ""
	for i := 0; i < len(x.Stax); i++ {
		if len(x.Stax[i]) > 0 {
			h += string(x.Stax[i][len(x.Stax[i])-1])
		} else {
			h += " "
		}
	}
	return h
}

func (x Stacks) Move(move, from, to int) string {
	h := x.Stax[from][len(x.Stax[from])-move:]
	x.Stax[from] = x.Stax[from][:len(x.Stax[from])-move]

	h2 := ""
	for i := 0; i < move; i++ {
		h2 += string(h[move-i-1])
	}
	x.Stax[to] += h2

	return h
}

// https://stackoverflow.com/questions/1752414/how-to-reverse-a-string-in-go/34521190#34521190
func Reverse(s string) string {
	size := len(s)
	buf := make([]byte, size)
	for start := 0; start < size; {
		r, n := utf8.DecodeRuneInString(s[start:])
		start += n
		utf8.EncodeRune(buf[size-start:], r)
	}
	return string(buf)
}

// day 4 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	stacks := make([]string, 11)
	// stacks[0] = ""
	// stacks[1] = "ZN"
	// stacks[2] = "MCD"
	// stacks[3] = "P"

	s := Stacks{stacks}
	// s.Move(1, 2, 1)
	fmt.Println(s.Heads())

	re := regexp.MustCompile(`move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)`)

	for scanner.Scan() {
		line := scanner.Text()

		//init: read raster of upper case chars
		if strings.Contains(line, "[") {
			for i := 0; i <= len(line)/4; i++ {
				box := string(line[1+4*i])
				if box != " " {
					stacks[i+1] += box
				}
			}
		}
		if line == "" {
			for i := 0; i < 11; i++ {
				stacks[i] = Reverse(stacks[i])
			}
		}

		//read moves
		m := re.FindStringSubmatch(line)
		if m != nil {
			move, _ := strconv.ParseInt(m[1], 0, 0)
			from, _ := strconv.ParseInt(m[2], 0, 0)
			to, _ := strconv.ParseInt(m[3], 0, 0)
			s.Move(int(move), int(from), int(to))
		}
	}
	readFile.Close()

	fmt.Println(s.Heads())
	fmt.Println(stacks)
}
