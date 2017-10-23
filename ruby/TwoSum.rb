# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash = {}
    nums.each_with_index do |num, i|
        if hash.has_key?(target - num)
            return [hash[target - num], i]
        else
            hash[num] = i
        end

    end
    false
end



p two_sum([2,7,11,15], 9)
