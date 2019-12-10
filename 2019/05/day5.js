const fs = require('fs')
const interpretIntcode = require('./intcode.js')

const intcode = fs.readFileSync('input.txt', 'utf8')

const readline = require('readline')

const rli = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function input() {
    return new Promise((resolve, reject) => {
        rli.question('Input: ', input => {
            const num = +input
            if (isNaN(num)) {
                reject('Must enter int')
            } else {
                resolve(num)
            }
        })
    })
}

interpretIntcode(intcode.split(',').map(Number), input, console.log.bind(console))
    .then(() => rli.close())