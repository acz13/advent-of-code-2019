l = document.body.textContent
k =  l.trim().split("\n\n")

function inc(obj, key, amount) {
  obj[key] = (obj[key] ?? 0) + (amount ?? 0)
}

function pairs(s) {
  const o = {}
  for (let i = 0; i < s.length-1; i++) {
    inc(o, s.substr(i, 2), 1)
  }
  return o
}

function unpair(s, b, e) {
  const o = {}
  for (const pair in s) {
    inc(o, pair[0], s[pair])
    inc(o, pair[1], s[pair])
  }
  inc(o, b, 1)
  inc(o, e, 1)
  return o
}

str = pairs(k[0])
rules = Object.fromEntries(k[1].trim().split("\n").map(o => o.split(" -> ")))

function iterate(s) {
  const a = {}
  for (const rule in rules) {
    inc(a, rule[0] + rules[rule], s[rule])
    inc(a, rules[rule] + rule[1], s[rule])
  }
  return a
}

function _d(s) {
  u = unpair(s, k[0][0], k[0][k[0].length-1])
  c = Object.values(u)
  return (Math.max(...c) - Math.min(...c)) / 2
}

i = 0
for (; i < 10; i++) {
  str = iterate(str)
}
console.log("Part 1", _d(str))
for (; i < 40; i++) {
  str = iterate(str)
}
console.log("Part 2", _d(str))
