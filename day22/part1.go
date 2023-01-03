package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
)

// day 22 part 1
func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	mmap := make(map[int]string, 0)
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
	// read commands
	if scanner.Scan() {
		line := scanner.Text()

		re := regexp.MustCompile(`([\d]+)|([RL])`)
		m := re.FindAllString(line, -1)
		if m == nil {
			panic("no match")
		}

		// turtle
		x, y, dir := 0, 0, 0

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
				switch dir {
				case 0:
					x += int(steps)
				case 2:
					x -= int(steps)
				case 1:
					y += int(steps)
				case 3:
					y -= int(steps)
				}
			}
			fmt.Printf("cmd:%s x=%d y=%d dir=%d\n", cmd, x, y, dir)
		}
	}

	readFile.Close()

}

// decode snafu to decimal value
func Decode(snafu string) int {
	val := 0
	for i := 0; i < len(snafu); i++ {
		mult := int(math.Pow(5, float64(i)))
		char := snafu[len(snafu)-1-i]
		switch char {
		case '2':
			val += 2 * mult
		case '1':
			val += 1 * mult
		case '0':
			val += 0 * mult
		case '-':
			val -= 1 * mult
		case '=':
			val -= 2 * mult
		}
	}
	return val
}

// decode snafu to decimal value
func Encode(decimal int) string {
	res := ""
	//base5
	for decimal > 0 {
		rem := decimal % 5
		decimal /= 5
		if rem < 3 {
			res += fmt.Sprint(rem)
		} else {
			switch rem {
			case 4:
				res += "-"
			case 3:
				res += "="
			}
			decimal++
		}
	}
	return Reverse(res)
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
