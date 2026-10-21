import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':900,'height':900})
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'index.html'))); await pg.wait_for_timeout(700)
        for i in range(12):
            await pg.click('#newBtn') if i==0 else None
            r = await pg.evaluate("""async (i)=>{ const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n));
              document.querySelectorAll('.card')[i].click(); document.getElementById('startBtn').click(); await wait(500);
              const G=D.G, P=G.player; P.hp=9999; G.L.enemies.length=0;
              const es=[0,1,2].map(k=>D.makeEnemy('brute', P.x+40+k*30, P.y)); es.forEach(e=>{e.hp=e.maxHp=999; G.L.enemies.push(e)});
              P.face='e'; D.weaponAttack(); await wait(600);
              const out=[D.pick.id, D.WEAPONS[D.pick.id].name, es.map(e=>999-e.hp)];
              D.goLobby && D.setMode('menu'); return out; }""", i)
            print(r)
            await pg.goto('file://' + __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'index.html'))); await pg.wait_for_timeout(500); await pg.click('#newBtn')
        print(errs)
        await b.close()
asyncio.run(main())
