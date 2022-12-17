package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

type Valve struct {
	rate    int
	tunnels []Valve
}

// day 16 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	// parsed network of valves and tunnels
	tunnels := map[string]([]string){}
	rates := map[string]int{}

	scanner := bufio.NewScanner(readFile)

	// https://regex101.com/
	// Valve (?P<valve>[A-Z]{2}) has flow rate=(?P<rate>\d+); tunnels lead to valves (?P<conn>[A-Z]{2})
	// (?P<valve>[A-Z]{2})
	re := regexp.MustCompile(`[A-Z]{2}`) //valves
	re2 := regexp.MustCompile(`\d+`)     //flow rate

	for scanner.Scan() {
		line := scanner.Text()
		m := re.FindAllString(line, -1)
		tunnels[m[0]] = m[1:]
		rate := re2.FindString(line)
		val, _ := strconv.Atoi(rate)
		rates[m[0]] = val

	}
	readFile.Close()

	fmt.Println("tunnels:", tunnels)
	fmt.Println("flow rates:", rates)

}
