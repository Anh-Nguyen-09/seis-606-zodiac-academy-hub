import asyncio, json
from playwright.async_api import async_playwright
U='file://' + __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'index.html'))
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); ctx = await b.new_context(viewport={'width':1000,'height':900}); pg = await ctx.new_page()
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
        R={}
        await pg.goto(U); await pg.wait_for_timeout(600)
        R['empty_state'] = await pg.evaluate("()=>({cont: getComputedStyle(document.getElementById('contBtn')).display, contDisabled: document.getElementById('contBtn').disabled, saveCard: document.getElementById('saveCard').innerText.slice(0,80)})")
        # start new game, play a bit, then save exists
        await pg.click('#newBtn'); await pg.wait_for_timeout(100); await pg.click('.card >> nth=4'); await pg.click('#startBtn'); await pg.wait_for_timeout(800)
        # rapid input spam
        for k in ['l','j','k','q','u',' ','e','h']*25:
            await pg.keyboard.press(k)
        await pg.wait_for_timeout(500)
        R['spam'] = await pg.evaluate("()=>({mode: window.__dungeon.mode, hp: window.__dungeon.G.player.hp, el: window.__dungeon.G.el})")
        R['save_after_start'] = await pg.evaluate("()=>localStorage.getItem('astraeum-tower-save')")
        # refresh mid floor
        await pg.evaluate("()=>{ window.__dungeon.G.gold = 77; }")
        await pg.reload(); await pg.wait_for_timeout(700)
        R['after_reload'] = await pg.evaluate("()=>({mode: window.__dungeon.mode, cont: getComputedStyle(document.getElementById('contBtn')).display, card: document.getElementById('saveCard').innerText.slice(0,120)})")
        await pg.click('#contBtn'); await pg.wait_for_timeout(1500)
        R['continue'] = await pg.evaluate("()=>({mode: window.__dungeon.mode, floor: window.__dungeon.G.floorIdx+1, gold: window.__dungeon.G.gold})")
        # security: edit save
        await pg.evaluate("()=>{ const s=JSON.parse(localStorage.getItem('astraeum-tower-save')); s.gold=99999; s.floor=14; localStorage.setItem('astraeum-tower-save', JSON.stringify(s)); }")
        await pg.reload(); await pg.wait_for_timeout(700); await pg.click('#contBtn'); await pg.wait_for_timeout(1500)
        R['edited_save'] = await pg.evaluate("()=>({floor: window.__dungeon.G.floorIdx+1, gold: window.__dungeon.G.gold, boss: !!window.__dungeon.G.F.boss})")
        # corrupt save
        await pg.evaluate("()=>{ localStorage.setItem('astraeum-tower-save', '{not json'); localStorage.setItem('astraeum-tower-records','<script>alert(1)</script>'); }")
        await pg.reload(); await pg.wait_for_timeout(700)
        R['corrupt'] = await pg.evaluate("()=>({mode: window.__dungeon.mode, cont: getComputedStyle(document.getElementById('contBtn')).display})")
        # weird values in save (strings, negative, html)
        await pg.evaluate("""()=>{ localStorage.setItem('astraeum-tower-save', JSON.stringify({floor:'<img src=x onerror=alert(1)>', gold:-50, char:'<b>x</b>', hp:'abc', inv:{herb:'lots'}})); }""")
        await pg.reload(); await pg.wait_for_timeout(700)
        R['weird_card'] = await pg.evaluate("()=>document.getElementById('saveCard').innerHTML.slice(0,300)")
        try:
            await pg.click('#contBtn', timeout=2000); await pg.wait_for_timeout(1200)
            R['weird_continue'] = await pg.evaluate("()=>({mode: window.__dungeon.mode, floor: window.__dungeon.G && window.__dungeon.G.floorIdx})")
        except Exception as e: R['weird_continue']='click failed '+str(e)[:80]
        # dev tools god mode
        await pg.evaluate("()=>localStorage.clear()"); await pg.reload(); await pg.wait_for_timeout(600)
        await pg.click('#newBtn'); await pg.wait_for_timeout(100); await pg.click('.card >> nth=4'); await pg.click('#startBtn'); await pg.wait_for_timeout(800)
        R['devtools'] = await pg.evaluate("()=>{ const D=window.__dungeon; D.G.player.hp=1e9; D.G.player.maxHp=1e9; D.startFloor(14,null); return {floor:D.G.floorIdx+1, hp:D.G.player.hp}; }")
        # blur pause
        await pg.evaluate("()=>window.dispatchEvent(new Event('blur'))"); await pg.wait_for_timeout(200)
        R['blur'] = await pg.evaluate("()=>window.__dungeon.mode")
        # resize small
        await pg.set_viewport_size({'width':420,'height':800}); await pg.wait_for_timeout(300)
        R['mobile_canvas'] = await pg.evaluate("()=>{const c=document.querySelector('canvas').getBoundingClientRect(); return [Math.round(c.width),Math.round(c.height), document.documentElement.scrollWidth]}")
        R['errors']=errs
        print(json.dumps(R, indent=1))
        await b.close()
asyncio.run(main())
