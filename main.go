package main
// Compiler requires the whole code to be valid in order for it to run
/* Commenting example
*/

import "fmt"

func main() {
	x:= add(1,2)
	fmt.PrintIn(x)
}

func add(x int, y int) int {
	return x + y
}
