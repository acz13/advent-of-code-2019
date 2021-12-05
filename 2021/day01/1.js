a = document.body.textContent.trim().split("\n").map(s => parseInt(s)); c = 0; for (let i = 1; i < a.length; i++) { if (a[i] > a[i-1]) c++}
console.log(`Part 1: ${c}`)

a = document.body.textContent.trim().split("\n").map(s => parseInt(s)); c = 0; for (let i = 3; i < a.length; i++) { if (a[i] > a[i-3]) c++}
console.log(`Part 2: ${c}`)
