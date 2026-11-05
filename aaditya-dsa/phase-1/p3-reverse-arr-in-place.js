'use strict'

const reverseInPlace = (values) => {
    let left = 0, right = values.length - 1

    while(left < right) {
        [values[left], values[right]] = [values[right], values[left]]

        left++
        right--
    }

    return values
}

console.log(reverseInPlace([2, 5, 9, 1])) // [1, 9, 5, 2]
console.log(reverseInPlace([4, 8, 15])) // [15, 8, 4]
console.log(reverseInPlace([7])) // [7]
console.log(reverseInPlace([])) // []