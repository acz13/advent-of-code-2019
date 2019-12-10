const inp = document.body.innerText.split('\n').map(s => Array.from(s))

const visible = {}
const counts = {}

function isVisible (i, a, b) {
  if (b in visible[a]) return visible[a][b]
  if (a in visible[b]) return visible[b][a]
  var [ax, ay] = a
  var [bx, by] = b
  if (ax === bx && ay === by) return false
  var x = bx - ax
  var y = by - ay
  for (var k = 2; k <= Math.max(Math.abs(x), Math.abs(y)) + 1; k++) {
    if (x % k === 0 && y % k === 0) {
      for (var l = 1; l < k; l++) {
        if (i[l * y / k + ay][l * x / k + ax] === '#') {
          visible[a][b] = false
          visible[b][a] = false
          return false
        }
      }
    }
  }
  visible[a][b] = true
  visible[b][a] = true
  return true
}

function checkAll (i, k) {
  if (inp[k][i] !== '#') return
  const c = [i, k]
  if (!(c in visible)) {
    visible[c] = {}
  };
  counts[c] = 0
  for (var im = 0; im < inp.length; im++) {
    for (var km = 0; km < inp[0].length; km++) {
      if (inp[km][im] !== '#') continue
      const cm = [im, km]
      if (!(cm in visible)) {
        visible[cm] = {}
      };
      if (isVisible(inp, c, cm)) {
        counts[c]++
      }
    }
  }
  return counts[c]
}

function run () {
  for (var i = 0; i < inp.length; i++) {
    for (var k = 0; k < inp[0].length; k++) {
      checkAll(i, k)
    }
  }

  console.log(counts, Math.max(...Object.values(counts)))
}

run()
