package main

import "fmt"

func main() {
	fmt.Println("hello, world!")
	var a int = 1
	fmt.Println(a)
	b := 5
	c := a + b
	fmt.Printf("%d\n", c)
	e1, e2 := GetData()
	// e1, e2 = e2, e1
	fmt.Println(e1, e2)
}

func GetData() (int, int) {
	return 10, 20
}

