package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

// day 25 part 1
func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	sum := 0

	scanner := bufio.NewScanner(readFile)
	for scanner.Scan() {
		line := scanner.Text()

		decimal := Decode(line)
		snafu := Encode(decimal)
		fmt.Printf("%10s\t%10d\t%10s\n", line, decimal, snafu)
		sum += decimal
	}
	readFile.Close()

	snafusum := Encode(sum)
	fmt.Println("sum:", sum, "snafu:", snafusum)
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
