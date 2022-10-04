const asciiCode = (letter) => {
    if (!letter.slice(0)) return undefined;
    if (letter.slice(1)) return `This is not a latter, it is a word or words`;
    return String(letter.codePointAt(0))
}

function asciiToBinary(letter, toBase = 2, output = "") {
    if (toBase <= 1) return "Error: An integer less than two cannot be used in this conversion."

    const division = (code) => {
        if (code < toBase) return `${code}${output}`;
        output = `${Math.floor(code % toBase)}${output}`
        return division(Math.floor(code / toBase))
    }

    const putZero = (number, zeros = []) => {
        for (let index = 0; index < number; index++) zeros.push("0")
        return `${zeros.map(m => m).join("")}`
    }

    const binaryCode = (code) => {
        if (code.split("").length < 8) return `${putZero(8 - code.split("").length)}${code}`
        return code
    }

    return { letter, asciiCode: asciiCode(letter), binaryCode: binaryCode(division(asciiCode(letter))) }
}

console.log(asciiToBinary("0"))

//Online Test: https://runkit.com/cihatksm/ascii-binary
