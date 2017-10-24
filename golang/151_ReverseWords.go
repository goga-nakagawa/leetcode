/*
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
*/

package main
import (
    "fmt"
)
func reverse(s string, start int, end int)(string) {
    r := []rune(s)
    for i, j := start, end; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}

func reverseWords(s string)(string) {
    reversed := reverse(s, 0, len(s) - 1)
    p := 0
    for q, char := range reversed {
        if char == " " {
            reverse(s[p:q], p, q)
            p = q + 1
        }
    }
}
