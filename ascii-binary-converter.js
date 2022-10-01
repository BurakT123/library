function asciiAndBinary(letter, toBase = 2, output = "") {
    const asciiCode = letter.slice(0) && !letter.slice(1) ? letter.codePointAt(0) : null
    if (toBase <= 1) return "Error: An integer less than two cannot be used in this conversion."

    const division = (code) => {
        if (code < toBase) return `${code}${output}`;
        output = `${Math.floor(code % toBase)}${output}`
        return division(Math.floor(code / toBase))
    }

    const binaryCode = (code) => {
        if (code.split("").length == 7) return `0${code}`
        return code
    }

    return { letter, asciiCode, binaryCode: binaryCode(division(asciiCode)) }
}

console.log(asciiAndBinary("a"))

//Online Test: https://runkit.com/cihatksm/ascii-binary
