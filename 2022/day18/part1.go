package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// search state
type Coord struct {
	x, y, z int
}

// day 18 part 1
func main2() {

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
	cubes := make([]*Coord, len(lines))
	re := regexp.MustCompile(`\d+`)
	for idx, line := range lines {
		m := re.FindAllString(line, -1)
		x, _ := strconv.Atoi(m[0])
		y, _ := strconv.Atoi(m[1])
		z, _ := strconv.Atoi(m[2])
		cubes[idx] = &Coord{x, y, z}
	}
	readFile.Close()

	fmt.Println("cubes:", len(cubes))

	// triangle algo
	count := 0 // direct neighbors
	for idx1, c1 := range cubes {
		for _, c2 := range cubes[idx1+1:] {
			// is direct neighbor? manhattan distance 3D
			d := Abs(c1.x-c2.x) + Abs(c1.y-c2.y) + Abs(c1.z-c2.z)
			if d == 1 {
				count++
			}
		}
	}

	fmt.Println("cubes:", len(cubes), "neighbors:", count)
	fmt.Println("area:", len(cubes)*6-count*2, "max:", len(cubes)*6)
}

// go math.Abs is for float / requires conversion
func Abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
