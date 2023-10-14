package main

import (
	"crypto/md5"
	"fmt"
)

func main() {
	key := "bgvyzdsv"
	var count uint64 = 0
	solved := false

	for !solved {
		data := []byte(fmt.Sprintf("%s%d", key, count))
		h := md5.Sum(data)

		if h[0] == 0 && h[1] == 0 && h[2] == 0 {
			solved = true
		} else {
			count++
		}

	}

	fmt.Printf("%s%d\n", key, count)
}
