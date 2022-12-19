package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

// search state
type State struct {
	minute      int            //search step
	flowrate    int            //aggregated open valves
	valve       string         //where am I?
	valve_prev  string         //where did I come from?
	valves_open map[string]int // valves already opened, value: opened in minute x
	pressure    int            //total pressure released
	action      string         // open or move
}

// parsed network of valves and tunnels
var tunnels = map[string]([]string){}
var rates = map[string]int{}

// day 16 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

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
		if val > 0 { //add only valves where opening will increase flow rate
			rates[m[0]] = val
		}

	}
	readFile.Close()

	fmt.Println("tunnels:", tunnels)
	fmt.Println("flow rates:", rates)

	// mode 1: init breadth first search
	// nodes := []State{{0, 0, "AA", "AA", map[string]int{}, 0, ""}}

	// mode 2: continue previous search (based on console output)
	// Max pressure after 16 minutes: 638 s={17 59 GG FF map[BB:11 CC:13 DD:3 EE:16 JJ:7] 638 move}
	// nodes := []State{{17, 59, "GG", "FF", map[string]int{"BB": 11, "CC": 13, "DD": 3, "EE": 16, "JJ": 7}, 638, "move"}} //with inputs1.txt
	// Max pressure after 16 minutes: 483 s={17 64 MK ZS map[IP:4 OD:11 UF:8 ZJ:14] 483 move}
	nodes := []State{{17, 64, "MK", "ZS", map[string]int{"IP": 4, "OD": 11, "UF": 8, "ZJ": 14}, 483, "move"}} //with inputs2.txt

	next := []State{}
	minutes := 31
	// for minute := 0; minute < minutes; minute++ {
	for minute := 17; minute < minutes; minute++ {
		for _, node := range nodes {
			next = append(next, expand_search(&node)...)
		}
		fmt.Println("minute:", minute, "nodes:", len(nodes), "next:", len(next))
		nodes = next

		calcMaxPressure(nodes, minute)
	}

}

func expand_search(s *State) []State {
	res := []State{}

	opened := s.valves_open
	flowrate := s.flowrate
	if s.action == "open" {
		opened = make(map[string]int)
		for k, v := range s.valves_open {
			opened[k] = v
		}
		opened[s.valve] = s.minute + 1
		flowrate += rates[s.valve]
		// fmt.Println("opened:", opened, "flowrate:", flowrate)
		if len(opened) == len(rates) {
			fmt.Println("all valves opened! min:", s.minute+1, "max flow:", flowrate)
		}
	}

	if opened[s.valve] == 0 && rates[s.valve] > 0 {
		res = append(res, State{s.minute + 1, flowrate, s.valve, s.valve, opened, s.pressure + flowrate, "open"})
	}
	for _, v := range tunnels[s.valve] {
		if v == s.valve_prev {
			continue //prevent cycles
		}
		res = append(res, State{s.minute + 1, flowrate, v, s.valve, opened, s.pressure + flowrate, "move"})
	}
	// fmt.Println("expanded:", len(res))
	return res
}

func calcMaxPressure(nodes []State, minute int) {
	max_pressure := 0
	var s State
	for _, v := range nodes {
		// if v.pressure > 0 {
		// 	fmt.Println("pres:", v.pressure)
		// }
		if v.pressure > max_pressure {
			max_pressure = v.pressure
			s = v
		}
	}
	fmt.Printf("Max pressure after %d minutes: %d s=%v\n", minute, max_pressure, s)
}
