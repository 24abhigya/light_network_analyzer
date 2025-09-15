const socket = io();
socket.on('connect', ()=>{document.getElementById('status').innerText='Connected';});
socket.on('packet_prediction',(payload)=>{
  const ul=document.getElementById('packets');
  const li=document.createElement('li');
  const timeStr=new Date(payload.ts*1000).toLocaleTimeString();
  const prob=payload.result.prob!==null?payload.result.prob.toFixed(3):'n/a';
  li.innerText=`[${timeStr}] label=${payload.result.label} prob=${prob} len=${payload.features.pkt_len}`;
  ul.insertBefore(li,ul.firstChild);
  while(ul.childElementCount>50) ul.removeChild(ul.lastChild);
  const stats=document.getElementById('stats');
  const total=(parseInt(stats.dataset.total||'0')+1);
  const malicious=(parseInt(stats.dataset.malicious||'0')+(payload.result.label===1?1:0));
  stats.dataset.total=total; stats.dataset.malicious=malicious; stats.innerText=`Total: ${total}\nMalicious: ${malicious}`;
});
