package main

// pather_test.go implements a basic world and tiles that implement Pather for
// the sake of testing.  This functionality forms the back end for
// path_test.go, and serves as an example for how to use A* for a grid.

import (
	"fmt"
	"strings"

	"github.com/beefsack/go-astar"
)

// Kind* constants refer to tile kinds for input and output.
const (
	// KindPlain (.) is a plain tile with a movement cost of 1.
	KindPlain = iota
	// KindRiver (~) is a river tile with a movement cost of 2.
	KindRiver
	// KindMountain (M) is a mountain tile with a movement cost of 3.
	KindMountain
	// KindBlocker (X) is a tile which blocks movement.
	KindBlocker
	// KindFrom (F) is a tile which marks where the path should be calculated
	// from.
	KindFrom
	// KindTo (T) is a tile which marks the goal of the path.
	KindTo
	// KindPath (●) is a tile to represent where the path is in the output.
	KindPath
)

// KindRunes map tile kinds to output runes.
var KindRunes = map[int]rune{
	KindPlain:    '.',
	KindRiver:    '~',
	KindMountain: 'M',
	KindBlocker:  '#', //'X
	KindFrom:     'F',
	KindTo:       'T',
	KindPath:     '●',
}

// RuneKinds map input runes to tile kinds.
var RuneKinds = map[rune]int{
	'.': KindPlain,
	'#': KindBlocker,
	'S': KindFrom,
	'E': KindTo,
}

// KindCosts map tile kinds to movement costs.
var KindCosts = map[int]float64{
	KindPlain: 1.0,
	KindFrom:  1.0,
	KindTo:    1.0,
}

// A Tile is a tile in a grid which implements Pather.
type Tile struct {
	// Kind is the kind of tile, potentially affecting movement.
	Kind int
	// X and Y are the coordinates of the tile.
	X, Y int
	// W is a reference to the World that the tile is a part of.
	W World

	// minute of game
	Minute int
	// true: blocked by <,> blizzard (minute % dimensionX)
	BlockedX map[int]bool
	// true: blocked by ^,v blizzard (minute % dimensionY)
	BlockedY map[int]bool
}

type Blizzard struct {
	X, Y      int
	direction string
}

type Node struct {
	X, Y int
	min  int
	W    World
}

var totalNodesExpanded int

// PathNeighbors returns the neighbors of the tile, excluding blockers and
// tiles off the edge of the board.
func (t *Node) PathNeighbors() []astar.Pather {
	neighbors := []astar.Pather{}
	for _, offset := range [][]int{
		{-1, 0},
		{1, 0},
		{0, -1},
		{0, 1},
		{0, 0}, //wait
	} {
		if n := t.W.Tile(t.X+offset[0], t.Y+offset[1]); n != nil &&
			n.Kind != KindBlocker &&
			!n.IsBlocked(t.min+1) {
			// if n.X > 1 && n.Y == 4 {
			// 	continue
			// }
			newNode := Node{n.X, n.Y, t.min + 1, n.W}
			neighbors = append(neighbors, &newNode)
			// n.Minute++
			// neighbors = append(neighbors, n)
		}
	}
	totalNodesExpanded += len(neighbors)
	if (totalNodesExpanded % 1000) == 0 {
		fmt.Println(totalNodesExpanded)
	}

	return neighbors
}

// PathNeighborCost returns the movement cost of the directly neighboring tile.
func (t *Node) PathNeighborCost(to astar.Pather) float64 {
	// toT := to.(*Tile)
	return 1 //KindCosts[toT.Kind]
}

// PathEstimatedCost uses Manhattan distance to estimate orthogonal distance
// between non-adjacent nodes.
func (t *Node) PathEstimatedCost(to astar.Pather) float64 {
	toT := to.(*Node)
	absX := toT.X - t.X
	if absX < 0 {
		absX = -absX
	}
	absY := toT.Y - t.Y
	if absY < 0 {
		absY = -absY
	}
	return float64(absX + absY)
}

func (t *Tile) BlockX(minute int) {
	if t.BlockedX == nil {
		t.BlockedX = make(map[int]bool, len(t.W))
	}
	t.BlockedX[minute] = true
}

func (t *Tile) BlockY(minute int) {
	if t.BlockedY == nil {
		t.BlockedY = make(map[int]bool, len(t.W[0]))
	}
	t.BlockedY[minute] = true
}

func (t *Tile) IsBlocked(minute int) bool {
	b := false
	if t.BlockedX != nil {
		b = b || t.BlockedX[minute%t.W.DimX()]
	}
	if t.BlockedY != nil {
		b = b || t.BlockedY[minute%t.W.DimY()]
	}
	return b
}

func (t *Tile) ToNode() *Node {
	return &Node{t.X, t.Y, t.Minute, t.W}
}

// World is a two dimensional map of Tiles.
type World map[int]map[int]*Tile
type Blizzards []*Blizzard

func (b Blizzards) String() string {
	st := ""
	for _, v := range b {
		st += fmt.Sprintf("%d/%d/%s ", v.X, v.Y, v.direction)
	}
	return st
}

// Tile gets the tile at the given coordinates in the world.
func (w World) Tile(x, y int) *Tile {
	if w[x] == nil {
		return nil
	}
	return w[x][y]
}

// SetTile sets a tile at the given coordinates in the world.
func (w World) SetTile(t *Tile, x, y int) {
	if w[x] == nil {
		w[x] = map[int]*Tile{}
	}
	w[x][y] = t
	t.X = x
	t.Y = y
	t.W = w
}

// FirstOfKind gets the first tile on the board of a kind, used to get the from
// and to tiles as there should only be one of each.
func (w World) FirstOfKind(kind int) *Tile {
	for _, row := range w {
		for _, t := range row {
			if t.Kind == kind {
				return t
			}
		}
	}
	return nil
}

// From gets the from tile from the world.
func (w World) From() *Tile {
	return w.FirstOfKind(KindFrom)
}

// To gets the to tile from the world.
func (w World) To() *Tile {
	return w.FirstOfKind(KindTo)
}

// RenderPath renders a path on top of a world.
func (w World) RenderPath(path []astar.Pather) string {
	width := len(w)
	if width == 0 {
		return ""
	}
	height := len(w[0])
	pathLocs := map[string]bool{}
	for _, p := range path {
		pT := p.(*Node)
		pathLocs[fmt.Sprintf("%d,%d", pT.X, pT.Y)] = true
	}
	rows := make([]string, height)
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {
			t := w.Tile(x, y)
			r := ' '
			if pathLocs[fmt.Sprintf("%d,%d", x, y)] {
				r = KindRunes[KindPath]
			} else if t != nil {
				r = KindRunes[t.Kind]
			}
			rows[y] += string(r)
		}
	}
	return strings.Join(rows, "\n")
}

// RenderWorld renders the world at the given minute
func (w World) RenderWorld(minute int) string {
	width := len(w)
	if width == 0 {
		return ""
	}
	height := len(w[0])
	rows := make([]string, height)
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {
			t := w.Tile(x, y)
			r := ' '
			if t != nil {
				r = KindRunes[t.Kind]
				blocked := t.IsBlocked(minute)
				if blocked {
					r = 'o'
				}
			}
			rows[y] += string(r)
		}
	}
	return strings.Join(rows, "\n")
}

// ParseWorld parses a textual representation of a world into a world map.
func ParseWorld(input string) (World, Blizzards) {
	w := World{}
	b := Blizzards{}

	for y, row := range strings.Split(strings.TrimSpace(input), "\n") {
		for x, raw := range row {
			kind, ok := RuneKinds[raw]
			if !ok {
				kind = KindPlain //blockers are explicit 'X'
			}
			w.SetTile(&Tile{
				Kind: kind,
			}, x, y)

			switch raw {
			case '>':
				fallthrough
			case '<':
				fallthrough
			case 'v':
				fallthrough
			case '^':
				b = append(b, &Blizzard{x, y, string(raw)})
			}
		}
	}
	return w, b
}

func (w World) ApplyBlizzards(bliz *Blizzards) {
	for _, b := range *bliz {
		w.ApplyBlizzard(b)
	}
}

func (w World) ApplyBlizzard(bliz *Blizzard) {
	switch bliz.direction {
	case ">":
		columns := len(w) - 2
		for i := 0; i < columns; i++ {
			x := bliz.X + i
			if x > columns {
				x -= columns
			}
			w.Tile(x, bliz.Y).BlockX(i)
		}
	case "<":
		columns := len(w) - 2
		for i := 0; i < columns; i++ {
			x := bliz.X - i
			if x < 1 {
				x += columns
			}
			w.Tile(x, bliz.Y).BlockX(i)
		}
	case "v":
		rows := len(w[0]) - 2
		for i := 0; i < rows; i++ {
			y := bliz.Y + i
			if y > rows {
				y -= rows
			}
			w.Tile(bliz.X, y).BlockY(i)
		}
	case "^":
		rows := len(w[0]) - 2
		for i := 0; i < rows; i++ {
			y := bliz.Y - i
			if y < 1 {
				y += rows
			}
			w.Tile(bliz.X, y).BlockY(i)
		}
	}
}

func (w World) DimX() int {
	return len(w) - 2
}

func (w World) DimY() int {
	return len(w[0]) - 2
}
