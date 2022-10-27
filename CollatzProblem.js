//https://en.wikipedia.org/wiki/Collatz_conjecture
//https://github.com/CihatKsm/library/blob/main/CollatzProblem.js

function Collatz(number = 1, count = 1, arr = []) {
    number % 2 == 0 ? arr.push(number / 2) : arr.push(3 * number + 1)
    let count = (number) => arr.filter(x => x == number)?.length || 0

    if (count(4) + count(2) + count(1) == 3) {
        console.log(`> Number is ${count}. \n` + `> Array Length ${arr?.length || "0"} \n` + `> ${arr.map(m => String(m)).join(" - ")} \n`)
        return setTimeout(() => Collatz(count + 1, count + 1, []), 300);
    }

    Collatz(arr[(arr?.length || 1) - 1], count, arr)
}

Collatz()