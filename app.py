from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang=\"id\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>Untuk Shefira</title>

<style>
:root{
  --pink:#ff6f91;
  --rose:#ffd6e8;
  --dark:#0b0b14;
  --blue:#1b1b2f;
}
*{box-sizing:border-box}
body{
  margin:0;height:100vh;overflow:hidden;
  background:radial-gradient(circle at top,var(--blue),var(--dark));
  font-family:'Segoe UI',sans-serif;color:white;
}
.scene{
  position:absolute;inset:0;
  display:flex;align-items:center;justify-content:center;
  opacity:0;transform:scale(0.95);
  transition:all .9s ease;
  pointer-events:none;
}
.scene.active{opacity:1;transform:scale(1);pointer-events:auto}
.card{
  width:90%;max-width:820px;
  padding:55px 50px;
  border-radius:30px;
  background:rgba(255,255,255,0.08);
  backdrop-filter:blur(14px);
  box-shadow:0 30px 80px rgba(0,0,0,0.55);
  text-align:center;
}
h1{font-size:2.6rem;margin-bottom:8px}
h2{font-weight:400;opacity:.85;margin-bottom:24px}
.text{font-size:1.35rem;line-height:1.85}
.highlight{color:var(--rose);font-weight:700}
.btns{display:flex;gap:18px;justify-content:center;flex-wrap:wrap;margin-top:34px}
.btn{
  padding:13px 30px;border:none;border-radius:40px;
  background:linear-gradient(135deg,var(--pink),var(--rose));
  color:#3b0a1a;font-size:1.02rem;font-weight:600;
  cursor:pointer;box-shadow:0 15px 35px rgba(0,0,0,.35);
  transition:all .25s ease
}
.btn:hover{transform:scale(1.08)}
.emoji{display:inline-block;animation:bounce 1.6s infinite}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.star{position:absolute;width:3px;height:3px;background:white;border-radius:50%;opacity:.7;animation:float 6s linear infinite}
@keyframes float{from{transform:translateY(100vh)}to{transform:translateY(-10vh)}}
.final{font-size:1.6rem;line-height:2}
.final span{color:var(--pink);font-weight:700}
@keyframes pop{0%{transform:scale(1)}50%{transform:scale(1.08)}100%{transform:scale(1)}}
.sparkle{position:absolute;font-size:1.4rem;animation:fly 1.2s ease forwards}
@keyframes fly{from{opacity:1;transform:translateY(0)}to{opacity:0;transform:translateY(-60px)}}
#gift{font-size:6rem;cursor:pointer;animation:wiggle 1.8s infinite;user-select:none}
@keyframes wiggle{0%,100%{transform:rotate(0)}25%{transform:rotate(5deg)}75%{transform:rotate(-5deg)}}
.popEmoji{position:absolute;font-size:2rem;animation:popUp 1.2s ease forwards}
@keyframes popUp{from{opacity:1;transform:translateY(0) scale(1)}to{opacity:0;transform:translateY(-80px) scale(1.4)}}
</style>
</head>
<body>

<div class=\"scene active\" id=\"s1\">
  <div class=\"card\">
    <h1>Buat Shefira <span class=\"emoji\">✨</span></h1>
    <h2>Ini hadiah kecilnyaa dari aku, Tori</h2>
    <div class=\"text\">
      Jujurr aku bikinnya sambil senyum sendirii <span class=\"emoji\">😆</span><br>
      Semoga kamu suka ya sama hadiah kecil inii<br>
      <span class=\"highlight\">Aku buat ini ada alesannya kok</span>
    </div>
    <div class=\"btns\">
      <button class=\"btn\" onclick=\"next(1)\">Apa alesannya?</button>
    </div>
  </div>
</div>

<div class=\"scene\" id=\"s2\">
  <div class=\"card\">
    <h1>Congratsss yaa!! <span class=\"emoji\">🥳</span></h1>
    <div class=\"text\">
      Selamat!, aku denger-denger nilai UAS
      <span class=\"highlight\">Fisika</span> kamu tertinggi<br>
      di kelas yaa <span class=\"emoji\">🏆</span><br><br>
      Aku tau kamu pasti seneng bangett<br>
      Aku juga jadi ikutan senenggg <span class=\"emoji\">🥰</span>
    </div>
    <div class=\"btns\">
      <button class=\"btn\" onclick=\"prev(2)\">⬅ Balik</button>
      <button class=\"btn\" onclick=\"next(2)\">CONGRATS YA SHEF ➡</button>
    </div>
  </div>
</div>

<div class=\"scene\" id=\"s3\">
  <div class=\"card\">
    <h1>Sekali lagii congratss yaa SHEF :) <span class=\"emoji\">🌷</span></h1>
    <div class=\"text\">
      Aku buat ini sebenernya iseng doang tauu wkwkwkwk<br>
      tapi semoga bisa jadi kenang-kenangan kecil yaa <span class=\"emoji\">💌</span><br><br>
      Mungkin ini sedikit doa dari aku buat kamu<br>
      Semoga kamu bisa terus berprestasi yaa<br>
      dan juga bisa ngeraihh hal-hal hebat lainnya :) <span class=\"emoji\">✨</span>
    </div>
    <div class=\"btns\">
      <button class=\"btn\" onclick=\"prev(3)\">⬅ Balik</button>
      <button class=\"btn\" onclick=\"next(3)\">AAMMIINN</button>
    </div>
  </div>
</div>

<div class=\"scene\" id=\"s4\">
  <div class=\"card\">
    <div id=\"gift\" onclick=\"openGift()\">🎁</div>
    <p id=\"hint\" style=\"opacity:.7;margin-top:18px;font-size:1.1rem\"> Klik ya kadonya :)</p>
    <div class=\"btns\">
      <button class=\"btn\" onclick=\"prev()\">⬅ Balik</button>
    </div>
  </div>
</div>

<script>
let current=1;
function show(n){
  document.querySelectorAll('.scene').forEach(s=>s.classList.remove('active'));
  document.getElementById('s'+n).classList.add('active');
  current=n;
}
function next(){if(current<4)show(current+1)}
function prev(){if(current>1)show(current-1)}

for(let i=0;i<90;i++){
  const s=document.createElement('div');
  s.className='star';
  s.style.left=Math.random()*100+'vw';
  s.style.animationDuration=(4+Math.random()*6)+'s';
  s.style.animationDelay=Math.random()*5+'s';
  document.body.appendChild(s);
}
function sparkle(){
  const emojis=['🌷','🌸','🌹','💐','🌺'];
  for(let i=0;i<8;i++){
    const e=document.createElement('div');
    e.className='sparkle';
    e.innerText=emojis[Math.floor(Math.random()*emojis.length)];
    e.style.left=(50+Math.random()*120-60)+'px';
    e.style.bottom='120px';
    document.body.appendChild(e);
    setTimeout(()=>e.remove(),1200);
  }
  const f=document.getElementById('finalText');
  f.style.animation='pop .4s';
  setTimeout(()=>f.style.animation='',400);
}
let opened=false;
function openGift(){
  if(opened) return;
  opened=true;
  document.getElementById('gift').innerText='🌷';
  document.getElementById('hint').innerText='Hadiah dari Tori 😊';
  const emojis=['💖','🌷','✨','🥰','💫','🫶'];
  for(let i=0;i<10;i++){
    const e=document.createElement('div');
    e.className='popEmoji';
    e.innerText=emojis[Math.floor(Math.random()*emojis.length)];
    e.style.left=(window.innerWidth/2+Math.random()*120-60)+'px';
    e.style.top=(window.innerHeight/2)+'px';
    document.body.appendChild(e);
    setTimeout(()=>e.remove(),1200);
  }
}
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
