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
	// scanner.Split(bufio.ScanLines)
	worldmap := ""
	for scanner.Scan() {
		line := scanner.Text()
		worldmap += line + "\n"
	}
	readFile.Close()

	world := ParseWorld(worldmap)
	// world := ParseWorld(".F.....X...T.") //blocked route
	fmt.Println("Parsed map:")
	fmt.Println(world.RenderPath([]astar.Pather{}))

	// t1 and t2 are *Tile objects from inside the world.
	path, distance, found := astar.Path(world.From(), world.To())
	if !found {
		fmt.Println("Could not find path")
	} else {
		fmt.Println("Path found:")
		fmt.Println(world.RenderPath(path))

		PrintPath(path)
		fmt.Println("dist:", distance)
	}

}

func PrintPath(path []astar.Pather) {
	for i := 0; i < len(path); i++ {
		x := len(path) - i - 1
		t, ok := (path[x].(*Tile)) //convert with type assertion
		if ok {
			fmt.Printf("%d: %s %d/%d\n", i, string(t.Elevation), t.X, t.Y)
		}
	}
}
