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

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    head := &ListNode{0,nil}
    curr, p, q, carry := head, l1, l2, 0
    for p != nil || q != nil {
        x, y := 0, 0
        if p != nil {
            x = p.Val
            p = p.Next
        }
        if q != nil {
            y = q.Val
            q = q.Next
        }
        digit := x + y + carry
        carry = digit / 10
        curr.Next = &ListNode{digit % 10,nil}
        curr = curr.Next
    }

    if carry > 0 {
        curr.Next = &ListNode{1,nil}
    }
    return head.Next

}


func main() {
    l1 := &ListNode{2,nil}
    l2 := &ListNode{8,nil}
    fmt.Println(addTwoNumbers(l1, l2))

}

