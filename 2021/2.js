h = d = 0; document.body.textContent.trim().split("\n").forEach(s => {let [k, i] = s.split(" "); i = +i; switch (k) {case 'forward': {h += i; break} case 'down': {d += i; break}; case 'up': {d -= i; break}}; console.log(s, h, d)})

h = d = a = 0; document.body.textContent.trim().split("\n").forEach(s => {let [k, i] = s.split(" "); i = +i; switch (k) {case 'forward': {h += i; d += a*i; break} case 'down': {a += i; break}; case 'up': {a -= i; break}}; console.log(s, h, d)})
