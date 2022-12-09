package main

import (
	"strconv"
    "bufio"
    "fmt"
    "os"
	"sort"
)

//day 1 part 2
func main() {

    scanner := bufio.NewScanner(os.Stdin)

	elves :=make([]int, 1, 1)
	n:=0
	max:=0
	val:=0

    for scanner.Scan() {

        ucl := scanner.Text()
		x, err:=strconv.Atoi(ucl)
		if err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
		}
		if x>0 {
			val+=x
		} else {
			elves =append(elves, val)
			val=0
			n++
		}
    }
	sort.Ints(elves)
	fmt.Println(elves[len(elves)-3:])
	
	best := elves[len(elves)-3:]
	for _, value := range best {
		//use '_' as blank identifier, see https://www.geeksforgeeks.org/what-is-blank-identifierunderscore-in-golang/
        //fmt.Printf("%d = %d\n", key, value)  
		max+=value 
	}

	fmt.Println(max)
}