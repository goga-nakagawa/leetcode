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
    Val  int
    Next *ListNode
}




func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{0,nil}
    dummy.Next = head
    length := 0
    first := head
    for first != nil {
        length += 1
        first = first.Next
    }
    length -= n
    first = dummy
    for length > 0 {
        length--
        first = first.Next
    }
    first.Next = first.Next.Next
    return dummy.Next
}

func main() {
    ll := &ListNode{1, nil}
    ll.Next = &ListNode{2, nil}
    ll.Next = &ListNode{3, nil}
    ll.Next = &ListNode{4, nil}
    ll.Next = &ListNode{5, nil}

    ll = removeNthFromEnd(ll,2)
}
