// Part 1

document.body.innerText.split("\n").reduce((s,l)=>(m=l.match(/(\d).*(\d)/))?s+(+(m[1]+m[2])):s+(+l.match(/\d/))*11,0)

// Part 2
d={one:1,two:2,three:3,four:4,five:5,six:6,seven:7,eight:8,nine:9,zero:0}
c=w=>d?.[w]??+w
document.body.innerText.split("\n").reduce((s,l)=>(m=l.match(/(\d|(?:one|two|three|four|five|six|seven|eight|nine|zero)).*(\d|(?:one|two|three|four|five|six|seven|eight|nine|zero))/))?s+(10*c(m[1])+c(m[2])):s+c(l.match(/\d|(?:one|two|three|four|five|six|seven|eight|nine|zero)/))*11,0) 

