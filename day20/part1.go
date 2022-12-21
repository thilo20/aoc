package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

// search state
type Coord struct {
	x, y, z int
}

// day 18 part 1
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

	// initial and working number sequence
	start := make([]int, len(lines))
	sequence := make([]int, len(lines))
	// init
	for idx, line := range lines {
		x, _ := strconv.Atoi(line)
		start[idx] = x
		sequence[idx] = x
	}
	readFile.Close()

	fmt.Println("sequence:", len(sequence))

	for idx1, c1 := range start {
		// locate c1 in sequence
		idx := 0
		for idx2, c2 := range sequence {
			if c1 == c2 {
				idx = idx2
				break
			}
		}
		fmt.Printf("%d: found '%d' at idx=%d\n", idx1, c1, idx)
		// shift c1=sequence[idx] to left/right, respect edge cases <0, >len
		idxnew := idx + c1
		for idxnew < 0 {
			idxnew += len(sequence) - 1
		}
		for idxnew >= len(sequence) {
			idxnew -= len(sequence) - 1
		}
		// fmt.Printf("idx=%d c1=%d idx+c1=%d idxnew=%d\n", idx, c1, idx+c1, idxnew)

		seqnew := make([]int, 0)
		switch {
		case idx < idxnew:
			seqnew = append(seqnew, sequence[:idx]...)
			seqnew = append(seqnew, sequence[idx+1:idxnew+1]...)
			seqnew = append(seqnew, sequence[idx])
			seqnew = append(seqnew, sequence[idxnew+1:]...)
			sequence = seqnew
		case idx > idxnew && idxnew == 0: //append at end
			seqnew = append(seqnew, sequence[:idx]...)
			seqnew = append(seqnew, sequence[idx+1:]...)
			seqnew = append(seqnew, sequence[idx])
			sequence = seqnew
		case idx > idxnew:
			seqnew = append(seqnew, sequence[:idxnew]...)
			seqnew = append(seqnew, sequence[idx])
			seqnew = append(seqnew, sequence[idxnew:idx]...)
			seqnew = append(seqnew, sequence[idx+1:]...)
			sequence = seqnew
		}
		// fmt.Println(sequence)
	}

	//count 1000+idx0 % len(start)
	idx := 0
	for idx2, c2 := range sequence {
		if c2 == 0 {
			idx = idx2
			break
		}
	}
	sum := sequence[(idx+1000)%(len(sequence)-1)]
	sum += sequence[(idx+2000)%(len(sequence)-1)]
	sum += sequence[(idx+3000)%(len(sequence)-1)]
	fmt.Println("sum:", sum)
}

// go math.Abs is for float / requires conversion
func Abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
