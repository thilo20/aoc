# Advent of Code 2022
https://adventofcode.com/2022

Ich versuche es mal mit IDE vscode und Programmiersprache go!

# How to run..

## go-Modul initialisieren
thilo@Thilos-MBP advent % go mod init advent/part1 
go: creating new go.mod: module advent/part1

## inputs piped via stdin
run via terminal:
thilo@Thilos-MBP advent1 % cat inputs2.txt|go run part1.go

Nachteil: debuggen mit vscode unklar, da stdin eingelesen werden muss!
vgl. launch.json mit
            "console": "integratedTerminal",
einzelne Eingaben via debug console moeglich, aber unklar wie die ganze Datei abgearbeitet werden kann.

## inputs via file
run via terminal:
thilo@Thilos-MBP advent3 % go run part1.go inputs1.txt

So kann man auch richtig debuggen :)

# References

1. https://adventofcode.com/
2. https://go.dev/tour
3. https://code.visualstudio.com/
4. https://github.com/golang/tools/blob/master/gopls/doc/workspace.md
5. https://www.sohamkamani.com/golang/enums/
6. https://www.golangprograms.com/go-language/struct.html
7. https://pkg.go.dev/k8s.io/apimachinery/pkg/util/sets#String.List
8. https://pkg.go.dev/unicode#IsLower
