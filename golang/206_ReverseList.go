/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package main
import (
    "fmt"
)


type ListNode struct {
    Val int
    Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    curr := head

    for curr != nil {
        tmp := curr.Next
        curr.Next = prev
        prev = curr
        curr = tmp
    }
    return prev

}


func main() {
    ll := &ListNode{1, nil}
    ll.Next = &ListNode{2, nil}
    ll.Next = &ListNode{3, nil}
    fmt.Println(reverseList(ll))

}

