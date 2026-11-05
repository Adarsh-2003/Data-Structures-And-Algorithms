'use strict'

const secondLargest = (values) => {

    const uniqueVals = new Set(values)
    if(uniqueVals.size <= 1) return null

    let max = -Infinity, secondLargest = -Infinity

    for(const num of values) {
        if(num > max) {
            secondLargest = max
            max = num
        } else if(num > secondLargest && num !== max) {
            secondLargest = num
        }
    }

    return secondLargest
}

console.log(secondLargest([4, 11, 7, 11])) // 7
console.log(secondLargest([11, 11, 8])) // 8
console.log(secondLargest([-8, -2, -5])) // -5
console.log(secondLargest([-2, -1])) // -2
console.log(secondLargest([3, 3])) // null
console.log(secondLargest([3])) // null
console.log(secondLargest([])) // null