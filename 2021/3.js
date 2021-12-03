a = document.body.textContent.trim().split("\n").map(s => parseInt(s, 2)); gamma = 0; for (let i = 1; i < (1 << 12); i <<= 1) { gamma += i * +(a.reduce((c, n) => c + (n & i), 0) > (a.length / 2)*i) }
console.log(`Part 1: ${((1 << 12) - gamma - 1) * gamma}`)

a = document.body.textContent.trim().split("\n").map(s => parseInt(s, 2)); b = [...a]; for (let s = 11; s >= 0; s--) { i = 1 << s; d = i * +(a.reduce((c, n) => c + (n & i), 0) >= (a.length / 2)*i); a = a.filter(n => !((n & i) ^ d)); e = i * +(b.reduce((c, n) => c + (n & i), 0) < (b.length / 2)*i); b = b.filter(n => !((n & i) ^ e)); console.log(a, b) }
// Just look at console.log I'm too lazy to extract the numbers automatically.
