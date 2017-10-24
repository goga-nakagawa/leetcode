package main
import (
    "fmt"
    "regexp"
    "strings"
)

func isPalindrome(s string) bool {

    re := regexp.MustCompile("^[a-zA-Z0-9]*$")
    p, q := 0, len(s) - 1

    for p < q {
        for !re.MatchString(string(s[p])) && p < q {
            p++
        }
        for !re.MatchString(string(s[q])) && p < q {
            q--
        }
        if strings.ToLower(string(s[p])) != strings.ToLower(string(s[q])) {
            return false
        } else {
            p++
            q--
        }
    }

    return true
}



func main() {
    fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
    fmt.Println(isPalindrome("race a car"))

}
