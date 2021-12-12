k = document.body.textContent

graph = {
  start: [],
  end: []
}

function small(cave) {
  return cave.toLowerCase() == cave
}

for (const line of k.trim().split("\n")) {
  const [a, b] = line.trim().split("-")
  if (!(a in graph)) {
    graph[a] = []
  }
  if (!(b in graph)) {
    graph[b] = []
  }
  graph[a].push(b)
  graph[b].push(a)
}

completed = []
frontier = [{ path: ["start"], smalls: new Set(["start"]) }]
while (frontier.length > 0) {
  let { path, smalls } = frontier.pop()
  let c = path[path.length-1]

  if (c == "end") {
    completed.push(path)
    continue
  }
  
  for (const n of graph[c])  {
    let _smalls = smalls
    if (small(n)) {
      if (smalls.has(n)) {
        continue
      }
      _smalls = new Set([...smalls, n])
    }
		_path = [...path, n]
		frontier.push({ path: _path, smalls: _smalls })
  }
}


console.log(completed.length)

completed = []
frontier = [{ path: ["start"], smalls: new Set([]), double: false }]
while (frontier.length > 0) {
  let { path, smalls, double } = frontier.pop()
  let c = path[path.length-1]

  if (c == "end") {
    completed.push(path)
    continue
  }
  
  for (const n of graph[c])  {
    if (n === "start") {
      continue
    }
    let _smalls = smalls
    let _double = double
    if (small(n)) {
      if (smalls.has(n)) {
        if (double) {
        	continue
        }
        _double = true;
      }
      _smalls = new Set([...smalls, n])
    }

		_path = [...path, n]
		frontier.push({ path: _path, smalls: _smalls, double: _double })
  }
}


console.log(completed.length)
