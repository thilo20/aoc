package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/beefsack/go-astar"
)

// day 12 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)

	if err != nil {
		fmt.Println(err)
	}
	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	world := ParseWorld(".F........T.")
	// world := ParseWorld(".F.....X...T.") //blocked route

	// t1 and t2 are *Tile objects from inside the world.
	path, distance, found := astar.Path(world.From(), world.To())
	if !found {
		fmt.Println("Could not find path")
	} else {
		for i := 0; i < len(path); i++ {
			t, ok := (path[i].(*Tile)) //type assertion
			if ok {
				fmt.Printf("%d-%d ", t.X, t.Y)
			}
		}
		fmt.Println("dist:", distance)
	}

	for scanner.Scan() {
		line := scanner.Text()

		fmt.Println(line)

	}
	readFile.Close()
}
