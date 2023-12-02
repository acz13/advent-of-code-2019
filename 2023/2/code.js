n=document.body.innerText.trim().split("\n").map(l=>l.split(": ")[1].split("; ").map(s=>s.split(", ").reduce((o,b)=>(a=b.split(" "),o[a[1].charAt(0)]=+a[0],o),{r:0,b:0,g:0})))
//part1
console.log(n.reduce((s,g,i)=>s+(i+1)*(g.reduce((t,m)=>t&&m.r<=12&&m.g<=13&&m.b<=14,1)),0))
//part2
console.log(n.reduce((s,g)=>s+(l=g.reduce((t,m)=>({r:Math.max(m.r,t.r),b:Math.max(m.b,t.b),g:Math.max(m.g,t.g)})),l.r*l.g*l.b),0))

