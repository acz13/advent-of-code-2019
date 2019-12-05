const fs = require('fs')
const interpretIntcode = require('./intcode.js')

const intcode = fs.readFileSync('input.txt', 'utf8')

console.log("Part 1")
interpretIntcode(intcode.split(',').map(Number), () => 1, console.log.bind(console))

console.log("Part 2")
interpretIntcode(intcode.split(',').map(Number), () => 5, console.log.bind(console))
