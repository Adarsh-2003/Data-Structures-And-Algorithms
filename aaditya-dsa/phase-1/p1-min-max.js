'use strict'

const findMinMax = (values) => {

    if(!values.length) return null
    // return {min: Math.min(...values), max: Math.max(...values)}

    let min = values[0], max = values[0]

    for (const num of values) {
        if(num > max) {
            max = num
        }

        if(num < min) {
            min = num
        }
    }

    return {min, max}
}

console.log(findMinMax([9, 2, 15, 4])) // { min: 2, max: 15 }
console.log(findMinMax([-12, -3, -20])) // { min: -20, max: -3 }
console.log(findMinMax([7])) // { min: 7, max: 7 }
console.log(findMinMax([5, 5, 5])) // { min: 5, max: 5 }
console.log(findMinMax([])) // null
