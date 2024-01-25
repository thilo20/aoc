package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// math monkey
type MathMonkey struct {
	op1, op2, operation string
}

// day 21 part 2
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
	numbermonkeys := make(map[string]int, len(lines))
	mathmonkeys := make(map[string]MathMonkey, len(lines))

	var numberregexp = regexp.MustCompile(`(\w+): (\d+)`)
	var mathregexp = regexp.MustCompile(`(\w+): (\w+) ([+\-*/]) (\w+)`)

	// init
	for _, line := range lines {
		m := mathregexp.FindStringSubmatch(line)
		if len(m) > 0 {
			mathmonkeys[m[1]] = MathMonkey{m[2], m[4], m[3]}
			continue
		}
		m2 := numberregexp.FindStringSubmatch(line)
		if len(m2) > 0 {
			i, _ := strconv.Atoi(m2[2])
			numbermonkeys[m2[1]] = i
		}
	}
	readFile.Close()

	// part 2 modifications:
	// humn: 909 // replace me!
	numbermonkeys["humn"] = 3456431714010
	// root: wvvv + whqc // interpret as "wvvv = whqc"
	// mathmonkeys["root"].op1 = "=" // see https://pkg.go.dev/golang.org/x/tools/internal/typesinternal#UnaddressableFieldAssign
	// replace entire entry
	mathmonkeys["root"] = MathMonkey{mathmonkeys["root"].op1, mathmonkeys["root"].op2, "="}

	fmt.Println("numbers:", len(numbermonkeys), "math:", len(mathmonkeys))

	for len(mathmonkeys) > 0 {
		for k, v := range mathmonkeys {
			if numbermonkeys[v.op1] != 0 && numbermonkeys[v.op2] != 0 {
				number := 0
				switch v.operation {
				case "+":
					number = numbermonkeys[v.op1] + numbermonkeys[v.op2]
				case "-":
					number = numbermonkeys[v.op1] - numbermonkeys[v.op2]
				case "*":
					number = numbermonkeys[v.op1] * numbermonkeys[v.op2]
				case "/":
					number = numbermonkeys[v.op1] / numbermonkeys[v.op2]
				case "=":
					number = numbermonkeys[v.op1] - numbermonkeys[v.op2] //delta
					fmt.Printf("root yells: no! op1=%d op2=%d delta=%d humn=%d\n", numbermonkeys[v.op1], numbermonkeys[v.op2], number, numbermonkeys["humn"])
					if numbermonkeys[v.op1] == numbermonkeys[v.op2] {
						fmt.Println("root yells: OK!")
					}
				default:
					panic("invalid operation!")
				}
				numbermonkeys[k] = number
				delete(mathmonkeys, k)

				if k == "root" {
					fmt.Println("root yells: ", number)
					goto END
				}
			}
		}
	}
END:
}

// go math.Abs is for float / requires conversion
func Abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
