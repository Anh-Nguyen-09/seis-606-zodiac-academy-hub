import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':900,'height':900})
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: m.type=='error' and errs.append(m.text))
        await pg.goto('file://' + __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'index.html'))); await pg.wait_for_timeout(700)
        await pg.screenshot(path='T_lobby_empty.png')
        # 1. map generator: 300 maps, all floors 3..14
        gen = await pg.evaluate("""()=>{ const D=window.__dungeon; let bad=0, sizes=[], counts={};
          for(let n=3;n<=14;n++){ if(n===5||n===10) continue; for(let k=0;k<25;k++){ const m=D.genMap(n); const g=m.map(r=>r.split(''));
            let sx,sy,tx,ty; g.forEach((r,y)=>r.forEach((c,x)=>{ if(c==='P'){sx=x;sy=y;} if(c==='>'){tx=x;ty=y;} counts[c]=(counts[c]||0)+1; }));
            const reach=D.bfsTiles(g,sx,sy,ch=>'BXoLRCS'.includes(ch));
            if(!reach.has(ty*g[0].length+tx)) bad++;
            // moi chest/quai phai toi duoc (o ke ben)
            g.forEach((r,y)=>r.forEach((c,x)=>{ if('spbgC'.includes(c)){ const ok=[[0,0],[1,0],[-1,0],[0,1],[0,-1]].some(([dx,dy])=>reach.has((y+dy)*g[0].length+x+dx)); if(!ok) bad++; } }));
            if(n===4||n===9||n===14){ if(!m.join('').includes('S')) bad++; }
            sizes.push(g[0].length+'x'+g.length);
          } }
          return {bad, counts, sizes:[...new Set(sizes)]}; }""")
        print('GEN', gen)
        # 2. new game via UI
        await pg.click('#newBtn'); await pg.wait_for_timeout(100); await pg.click('#startBtn'); await pg.wait_for_timeout(1500)
        await pg.screenshot(path='T_f1.png')
        st = await pg.evaluate("()=>{const D=window.__dungeon; return [D.mode, D.G.floorIdx, D.G.gold, document.getElementById('pauseBtn').classList.contains('show')]}")
        print('start', st)
        # pause button
        await pg.click('#pauseBtn'); await pg.wait_for_timeout(200); await pg.screenshot(path='T_pause.png')
        print('paused', await pg.evaluate("()=>window.__dungeon.mode"))
        await pg.click('[data-act=resume]'); await pg.wait_for_timeout(100)
        # 3. walk all 15 floors: kill everything on each, check difficulty, bosses
        res = await pg.evaluate("""async ()=>{
          const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n)), out=[];
          for(let i=0;i<15;i++){
            D.startFloor(i, null); await wait(60);
            const G=D.G, L=G.L, P=G.player;
            const info={f:i+1, name:G.F.name, enemies:L.enemies.length, types:[...new Set(L.enemies.map(e=>e.spr))].join(','), shop:!!L.shop, boss:L.boss?L.boss.name:null,
              hp0: L.enemies[0] ? L.enemies.find(e=>!e.isBoss)?.maxHp : null, size:L.w+'x'+L.h};
            if(L.boss){
              const B=L.boss; P.x=B.x; P.y=B.y+150; await wait(1500);
              info.bossAtk = B.atk; info.awake=G.bossAwake;
              P.shield = 99999;
              await wait(5000);  // xem boss tan cong
              info.bullets = L.bullets.length; info.minions = L.enemies.length;
              D.damageEnemy(B, B.maxHp*0.6, null, 0, 0); await wait(2500); info.phase=B.phase;
              D.damageEnemy(B, B.maxHp, null, 0, 0); await wait(1800);
              info.portals = [!!G.L.lobby, !!G.L.stairs]; info.mode=D.mode;
              P.shield = 0;
            }
            out.push(info);
          }
          return out; }""")
        for r in res: print(r)
        print('mode after f15', await pg.evaluate("()=>window.__dungeon.mode"))
        await pg.screenshot(path='T_win.png')
        print('errors', errs)
        await b.close()
asyncio.run(main())
