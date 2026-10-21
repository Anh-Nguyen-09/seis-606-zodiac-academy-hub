import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':900,'height':900})
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'index.html'))); await pg.wait_for_timeout(700)
        await pg.click('#newBtn'); await pg.wait_for_timeout(100)
        await pg.click('.card >> nth=4'); await pg.click('#startBtn'); await pg.wait_for_timeout(800)
        # floor 4 shop
        r = await pg.evaluate("""async ()=>{ const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n));
          D.startFloor(3, 60); await wait(1600); const G=D.G; G.gold=300; G.inv.amethyst=3; G.inv.sapphire=2;
          G.player.x=G.L.shop.x; G.player.y=G.L.shop.y+30; G.L.enemies.length=0; await wait(100);
          D.interact(); await wait(100); return [D.mode, G.gold]; }""")
        print('shop open', r)
        await pg.screenshot(path='T_shop.png')
        await pg.click('#shopList .srow:nth-child(4) .btn')   # whetstone
        await pg.click('#shopList .srow:nth-child(3) .btn')   # vitality
        await pg.click('#sellBtn')
        r = await pg.evaluate("()=>{const G=window.__dungeon.G; return [G.gold, G.up, G.player.maxHp, G.player.hp, G.inv.amethyst]}")
        print('after buy', r)
        await pg.keyboard.press('Escape'); await pg.wait_for_timeout(100)
        print('mode', await pg.evaluate("()=>window.__dungeon.mode"))
        # next floor -> 5 (boss) -> kill -> lobby portal
        r = await pg.evaluate("""async ()=>{ const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n)), G=D.G;
          G.player.x=G.L.stairs.x; G.player.y=G.L.stairs.y+8; D.interact(); await wait(200);
          const f=G.floorIdx; const B=G.L.boss; D.damageEnemy(B, 9999, null,0,0); await wait(2200);
          G.player.x=G.L.lobby.x; G.player.y=G.L.lobby.y+8; await wait(50); D.interact(); await wait(200);
          return [f, D.mode, JSON.parse(localStorage.getItem('astraeum-tower-save')).floor, Object.keys(D.RECORDS.floors)]; }""")
        print('boss->lobby', r)
        await pg.screenshot(path='T_lobby_saved.png')
        await pg.click('#contBtn'); await pg.wait_for_timeout(1700)
        r = await pg.evaluate("()=>{const G=window.__dungeon.G; return [window.__dungeon.mode, G.floorIdx+1, G.gold, G.up.wpn, G.player.maxHp, G.char]}")
        print('continue', r)
        # bat lord fight observation
        r = await pg.evaluate("""async ()=>{ const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n));
          D.startFloor(9, null); await wait(300); const G=D.G, B=G.L.boss; G.player.x=B.x; G.player.y=B.y+170; G.player.hp=9999; G.player.maxHp=9999;
          const seen=new Set(); let maxB=0, hits=0; const hp0=G.player.hp;
          for(let i=0;i<120;i++){ await wait(100); seen.add(B.atk); maxB=Math.max(maxB,G.L.bullets.length); if(i===60) D.damageEnemy(B, B.maxHp*0.55, null,0,0); }
          return [[...seen], maxB, hp0-G.player.hp, B.phase, G.L.enemies.length]; }""")
        print('batlord', r)
        await pg.evaluate("""async ()=>{ const D=window.__dungeon, G=D.G, B=G.L.boss; B.atk='swoop'; B.atkT=40; B.jx=G.player.x; B.jy=G.player.y; }""")
        await pg.wait_for_timeout(250); await pg.screenshot(path='T_batlord.png')
        # emperor + win
        r = await pg.evaluate("""async ()=>{ const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n));
          D.startFloor(14, null); await wait(300); const G=D.G, B=G.L.boss; G.player.x=B.x; G.player.y=B.y+170; G.player.shield=1e9; await wait(4000);
          return G.L.bullets.length; }""")
        await pg.screenshot(path='T_emperor.png')
        r2 = await pg.evaluate("""async ()=>{ const D=window.__dungeon, wait=n=>new Promise(r=>setTimeout(r,n)), G=D.G; D.damageEnemy(G.L.boss, 99999,null,0,0); await wait(3500);
          return [D.mode, localStorage.getItem('astraeum-tower-save'), D.RECORDS.clears, D.RECORDS.best]; }""")
        print('emperor bullets', r, 'win', r2)
        await pg.screenshot(path='T_win.png')
        await pg.click('#winScreen [data-act=lobby]'); await pg.wait_for_timeout(300)
        await pg.screenshot(path='T_lobby_after.png')
        # death -> lobby
        await pg.click('#newBtn'); await pg.click('#startBtn'); await pg.wait_for_timeout(1500)
        await pg.evaluate("()=>{const D=window.__dungeon; D.G.player.hp=1; D.hurtPlayer(50, D.G.player.x+10, D.G.player.y);}")
        await pg.wait_for_timeout(900)
        print('dead mode', await pg.evaluate("()=>window.__dungeon.mode"))
        await pg.screenshot(path='T_dead.png')
        print('errors', errs)
        await b.close()
asyncio.run(main())
