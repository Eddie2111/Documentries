package main

import (
	"fmt"
	"net/http"
)
func main() {
	m := map[string]int{
		"apple":  1,
		"banana": 2,
		"orange": 3,
	}
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method == http.MethodGet {
			fmt.Fprint(w, m)
		} else if r.Method == http.MethodPost {
			fmt.Fprint(w, m)
		}
	})

	http.ListenAndServe(":3200", nil)
}
