//https://en.wikipedia.org/wiki/Collatz_conjecture
//https://github.com/CihatKsm/library/blob/main/CollatzProblem.js

const logColors = ['\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[33m%s\x1b[0m', '\x1b[34m%s\x1b[0m', '\x1b[35m%s\x1b[0m', '\x1b[36m%s\x1b[0m', '\x1b[33m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[36m%s\x1b[0m', '\x1b[31m%s\x1b[0m']

const log = (text) => console.log(logColors[Math.floor(Math.random() * 10)], text)

function Collatz(number = 1, count = 1, datas = []) {
    if (number % 2 == 0) datas.push(number / 2)
    else datas.push(3 * number + 1)

    let foursCount = datas.filter(data => data == 4)?.length || 0
    let twosCount = datas.filter(data => data == 2)?.length || 0
    let onesCount = datas.filter(data => data == 1)?.length || 0

    if (foursCount + twosCount + onesCount == 3) {
        log(`> Number is ${count}. \n> Datas Length ${datas?.length || "0"} \n> ` +  datas.map(m => String(m)).join(" - ") + " \n")
        datas = []
        return setTimeout(() => Collatz(count + 1, count + 1, datas), 300);
    }

    return setTimeout(() =>  Collatz(datas[(datas.length || 1) - 1], count, datas), 100);
}

Collatz()