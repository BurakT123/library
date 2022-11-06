const asciiCode = (letter) => !letter.slice(0) || letter.slice(1) ? `This 'latter' value must be one charecter long!` : String(letter.codePointAt(0));
const asciiToLetter = (ascii) => String.fromCharCode(ascii)

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

    const binaryCode = (code) => code.split("").length < 8 ? `${putZero(8 - code.split("").length)}${code}` : code;

    return { letter, asciiCode: asciiCode(letter), binaryCode: binaryCode(division(asciiCode(letter))) }
}

console.log(asciiToBinary("A"))

//Online Test: https://runkit.com/cihatksm/ascii-binary


for (let number = 0; asciiToLetter(number); number++) console.log(asciiToBinary(asciiToLetter(number)))