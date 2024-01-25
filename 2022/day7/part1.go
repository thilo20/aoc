package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Directory struct {
	name    string
	parent  *Directory
	subdirs map[string]*Directory
	files   []File
}

type File struct {
	size int
	name string
}

// day 7 part 1
func main() {

	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}

	// f1 := File{123, "hello"}
	// f2 := File{400, "world.txt"}
	// home := Directory{"/", nil, map[string]*Directory{}, []File{f1, f2}}
	home := Directory{"/", nil, map[string]*Directory{}, []File{}}
	fmt.Println(home)

	cwd := &home

	scanner := bufio.NewScanner(readFile)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()

		switch {
		case line == "$ cd /":
			fmt.Println("dir home")
			cwd = &home
		case line == "$ cd ..":
			fmt.Println("dir up")
			cwd = cwd.parent
		case line == "$ ls":
			fmt.Println("list content")
		case strings.HasPrefix(line, "$ cd"):
			fmt.Println("change dir")
			fields := strings.Fields(line)
			dirname := fields[2]
			if cwd.subdirs[dirname] != nil {
				cwd = cwd.subdirs[dirname]
			}
		default:
			fmt.Println("add content")
			fields := strings.Fields(line)
			if fields[0] == "dir" {
				dirname := fields[1]
				newdir := Directory{dirname, cwd, map[string]*Directory{}, []File{}}
				cwd.subdirs[dirname] = &newdir
			} else {
				filesize, _ := strconv.Atoi(fields[0])
				filename := fields[1]
				cwd.files = append(cwd.files, File{filesize, filename})
			}
		}
	}
	readFile.Close()

	fmt.Println("home:", home)
	fmt.Println("cwd:", *cwd)

	total := 0
	fmt.Println("total size:", home.Size(100000, &total), "limited:", total)
}

func (d *Directory) Size(limit int, total *int) int {
	size := 0
	for _, v := range d.files {
		size += v.size
	}
	for _, v := range d.subdirs {
		size += v.Size(limit, total)
	}
	fmt.Println("dir:", d.name, "size:", size)
	if size < limit {
		*total += size
	}
	return size
}
