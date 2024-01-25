package main

import (
	"strconv"
    "bufio"
    "fmt"
    "os"
)

//day 1 part 1
func main() {

    scanner := bufio.NewScanner(os.Stdin)

	max:=0
	val:=0

    for scanner.Scan() {

        ucl := scanner.Text()
		x, err:=strconv.Atoi(ucl)
		if err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
			// os.Exit(1)
		}
		if x>0 {
			val+=x
		} else {
			if val>max {
				max = val
			}
			val=0
		}
    }
	fmt.Println(max)

    if err := scanner.Err(); err != nil {
        fmt.Fprintln(os.Stderr, "error:", err)
        os.Exit(1)
    }
}