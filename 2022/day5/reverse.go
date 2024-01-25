package main

import (
	"fmt"
	"testing"
	"unicode/utf8"
)

func reverse_yazu(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func reverse_russ(s string) string {
	rune, n := make([]rune, len(s)), 0
	for _, r := range s {
		rune[n] = r
		n++
	}
	rune = rune[0:n]
	for i := 0; i < n/2; i++ {
		rune[i], rune[n-1-i] = rune[n-1-i], rune[i]
	}
	return string(rune)
}

func reverse_yuku(s string) string {
	// slight modification, his answer did not work
	o := make([]rune, utf8.RuneCountInString(s))
	i := len(o)
	for _, c := range s {
		i--
		o[i] = c
	}
	return string(o)
}

func reverse_simon(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func reverse_peterSO(s string) string {
	n := len(s)
	runes := make([]rune, n)
	for _, rune := range s {
		n--
		runes[n] = rune
	}
	return string(runes[n:])
}

func reverse_ivan(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func reverse_rmuller(s string) string {
	size := len(s)
	buf := make([]byte, size)
	for start := 0; start < size; {
		r, n := utf8.DecodeRuneInString(s[start:])
		start += n
		utf8.EncodeRune(buf[size-start:], r)
	}
	return string(buf)
}

func generateBiggerString(s string, n int) string {
	res := ""
	for i := 0; i < n; i++ {
		res += s
	}
	return res
}

func Benchmark_rmuller(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_rmuller(s)
	}
}

func Benchmark_peterSO(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_peterSO(s)
	}
}

func Benchmark_russ(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_russ(s)
	}
}

func Benchmark_ivan(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_ivan(s)
	}
}

func Benchmark_yazu(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_yazu(s)
	}
}

func Benchmark_yuku(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_yuku(s)
	}
}

func Benchmark_simon(b *testing.B) {
	s := generateBiggerString("abcdef", 100) + generateBiggerString("是以九家之說", 100)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		reverse_simon(s)
	}
}

func main2() {
	fmt.Println(reverse_rmuller("hello world"))
}
