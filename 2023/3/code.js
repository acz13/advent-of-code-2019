lastnum={};lastsym={};sum=0;gear=0
for (const line of (document.body.innerText+"\n").split("\n")) {
  sym={};num={}
  for (const {2:s,1:m,index:i} of line.matchAll(/(\d+)|([^0-9\.])/g)) {
    if (s) {
      sym[i]=o={s,g:[]}
      for (j=i-1;j<=i+1;j++) {
        if (k=lastnum[j]){sum+=k.n;k.n=0;if(k!=o.g[0]&&k!=o.g[1])o.g.push(k)}
        if (k=num[j]){sum+=k.n;k.n=0;if(k!=o.g[0]&&k!=o.g[1])o.g.push(k)}
      }
    } else {
      k={n:+m};k.g=k.n
      for (j=i-1;j<=i+m.length;j++) {
        if (o=lastsym[j]){sum+=k.n;k.n=0;o.g.push(k)}
        if (o=sym[j]){sum+=k.n;k.n=0;o.g.push(k)}
        if (j>=i&&j<i+m.length)num[j]=k
      }
    }
  }
  for({s,g}of Object.values(lastsym)){if(s=="*"&&g.length==2)gear+=g[0].g*g[1].g}
  lastsym=sym;lastnum=num
}
console.log(sum)
console.log(gear)
