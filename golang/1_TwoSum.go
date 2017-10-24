package main

import (
    "fmt"
)

func twoSum(nums []int, target int) []int {

    m := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        for _, v := range m {
            if idx, ok := m[target - nums[i]]; ok {
                if idx == v {
                    return []int{idx, i}
                }
            }
        }
        m[nums[i]] = i
    }
    return []int{}
}

func main() {
    fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
    fmt.Println(twoSum([]int{3,2,4}, 6))

}
