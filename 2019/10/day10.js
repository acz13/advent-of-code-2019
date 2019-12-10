const fs = require('fs')
const inp = fs.readFileSync('input.txt', 'utf8').split('\n').map(s => Array.from(s))

const counts = {}

function isVisible (i, a, b) {
  var [ax, ay] = a
  var [bx, by] = b
  if (ax === bx && ay === by) return false
  var x = bx - ax
  var y = by - ay
  for (var k = 2; k <= Math.max(Math.abs(x), Math.abs(y)) + 1; k++) {
    if (x % k === 0 && y % k === 0) {
      for (var l = 1; l < k; l++) {
        if (i[l * y / k + ay][l * x / k + ax] === '#') {
          return false
        }
      }
    }
  }
  return true
}

function checkAll (i, k) {
  if (inp[k][i] !== '#') return
  const c = [i, k]
  counts[c] = 0
  for (var im = 0; im < inp.length; im++) {
    for (var km = 0; km < inp[0].length; km++) {
      if (inp[km][im] !== '#') continue
      const cm = [im, km]
      if (isVisible(inp, c, cm)) {
        counts[c]++
      }
    }
  }
  return counts[c]
}

function part1 () {
  for (var i = 0; i < inp.length; i++) {
    for (var k = 0; k < inp[0].length; k++) {
      checkAll(i, k)
    }
  }

  const max = Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? a : b);
  console.log(counts[max])

  return max
}

let [x, y] = part1().split(',').map(Number)

const dist = ([x1, y1]) => {
    return Math.sqrt((x1 - x)*(x1 - x) + (y1 - y)*(y1 - y))
}

let queue = Object.keys(counts).map(p => {
    let [x1, y1] = p.split(',').map(Number)
    return [[x1, y1], -Math.atan2(x1 - x, y1 - y), dist([x1, y1])]
})

const annihilate = []

queue.sort((a, b) => a[1] - b[1] || b[2] - a[2])

let c = 0

while (queue.length > 1) {
    const toRemove = []

    for (var i = 0; i < queue.length; i++) {
        if (queue[i][0][0] === x && queue[i][0][1] === y) {
            continue
        }

        if (isVisible(inp, [x, y], queue[i][0])) {
            toRemove.push(i)
            annihilate.push(queue[i])
            inp[queue[i][0][1]][queue[i][0][0]] = false
            c++
        }
    }

    for (var i = toRemove.length - 1; i > 0; i--) {
        queue.pop(toRemove.pop(i))
    }
}

annihilate.push(queue[0])

console.log(annihilate[199][0][0] * 100 + annihilate[199][0][1])