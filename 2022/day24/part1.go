package main

import (
	"bufio"
	"fmt"
	"os"

	"github.com/beefsack/go-astar"
)

// day 24 part 1
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

	world, blizzards := ParseWorld(worldmap)
	// world := ParseWorld(".F.....X...T.") //blocked route
	fmt.Println("Parsed map:")
	fmt.Println(world.RenderPath([]astar.Pather{}))
	fmt.Println("outer dimensions:", len(world), len(world[0]))
	fmt.Println("inner dimensions:", world.DimX(), world.DimY())
	fmt.Println("Parsed blizzards:", blizzards)

	world.ApplyBlizzards(&blizzards)
	lastMinute := 1000
	search := InitSearch(world, lastMinute)

	// minutes := []int{0, world.DimX() * world.DimY(),world.DimX(), world.DimY()}
	minutes := []int{world.DimX() * world.DimY()}
	// for i := 0; i < 10; i++ {
	for _, i := range minutes {
		fmt.Printf("\nWorld at minute %d:\n%s\n", i, world.RenderWorld(i))
	}

	// t1 and t2 are *Tile objects from inside the world.
	// dest := world.Tile(len(world)-2, len(world[0])-1)
	// path, distance, found := astar.Path(world.Tile(1, 0), dest)
	// dest := world.Tile(len(world)-2, len(world[0])-1).ToNode()
	// dest := search.Node(1, 1, 1)
	// dest := search.Node(2, 0, 1) //must fail, tile is blocked #
	// dest := search.Node(1, 2, 5) //must fail, tile is blocked >
	// dest := search.Node(5, 1, 6)
	// dest := search.Node(len(world)-2, len(world[0])-1, 18) //success for inputs2.txt
	// dest := search.Node(len(world)-2, len(world[0])-1, lastMinute) //success for inputs3? with 2000 minutes :)
	// dest := search.Node(len(world)-2, len(world[0])-1, lastMinute) //success for inputs3? with 274 minutes :)
	start := search.Node(1, 0, 0)
	dest := search.Node(len(world)-2, len(world[0])-1, 274)
	path, distance, found := astar.Path(start, dest)
	if !found {
		fmt.Println("Could not find path")
	} else {
		fmt.Println("Path found:")
		fmt.Println(world.RenderPath(path))

		// PrintPath(path)
		fmt.Println("dist:", distance, "minutes")
	}

	fmt.Println("search nodes expanded:", totalNodesExpanded)
}

func PrintPath(path []astar.Pather) {
	for i := 0; i < len(path); i++ {
		x := len(path) - i - 1
		t, ok := (path[x].(*Node)) //convert with type assertion
		if ok {
			fmt.Printf("%d: %d/%d\n", i, t.X, t.Y)
		}
	}
}
