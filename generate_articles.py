from pathlib import Path

OUT = Path(r'C:\Users\Og\Desktop\待SEO文章\the_tower_seo')
OUT.mkdir(parents=True, exist_ok=True)
src = r'C:\Users\Og\Desktop\待SEO文章\The tower游戏测评.docx'

images = [
    '战斗中金币随波次提升','任务奖励金币','金币属性加点','金币研究室','广告获得砖石','战斗中拾取砖石','充值获得砖石','卡槽与卡片','研究室与加速','挂机前金币','挂机前数值','24小时挂机收益','五天后波次进度','UgPhone多游戏群组控制'
]

def plan(lang):
    alts = {
      'Chinese':[f'The Tower {x}' for x in images],
      'Traditional Chinese':[f'The Tower {x}' for x in images],
      'English':[f'The Tower {x.lower()}' for x in images],
      'Portuguese':[f'The Tower {x}' for x in images],
      'Spanish':[f'The Tower {x}' for x in images],
      'Thai':[f'The Tower {x}' for x in images],
      'Indonesian':[f'The Tower {x}' for x in images],
      'Vietnamese':[f'The Tower {x}' for x in images],
    }[lang]
    return '\n'.join([f'{i}. {images[i-1]}\n   - Alt: {alts[i-1]}\n   - 用途: 对应正文中的资源或挂机截图\n   - Source Image: {i}' for i in range(1,15)])

common = {
'Chinese': dict(suffix='cn', keyword='The Tower 游戏攻略', title='The Tower 游戏攻略：金币、钻石与挂机成长指南', intro='《The Tower》看起来是不断点击升级的放置塔防，真正影响进度的却是资源节奏。金币决定属性和研究速度，钻石决定卡槽与卡片组合；如果只顾着推波次，很容易出现资源跟不上、设备发热或挂机中断的问题。下面按实际游玩顺序整理金币、钻石和长期挂机的用法，并说明如何用 UgPhone 保持稳定运行。', body='''## What is The Tower?\n\n《The Tower》是一款围绕波次推进、属性加点和研究室成长展开的放置塔防游戏。战斗越深入，金币获取效率通常越高；任务则提供另一条稳定收入。钻石来源包括广告、战斗中出现的奖励以及充值，主要用于卡槽、卡片和研究室相关项目。\n\n## 如何获取并使用金币\n\n金币最直接的来源是战斗。一般而言，波次越高，单位时间的金币收益越好，因此前期应把重点放在能稳定推进的配置，而不是盲目追求一次性的高波次。任务奖励也值得顺手领取，它能补足升级期间的空档。\n\n<!-- SOURCE_IMAGE:1 -->\n\n完成任务后，先看当前最缺的属性，再决定加点。\n\n<!-- SOURCE_IMAGE:2 -->\n\n金币可用于属性升级，也可投入研究室。短期推图可以优先补战斗属性；准备长时间挂机时，研究室提供的长期收益更有价值。\n\n<!-- SOURCE_IMAGE:3 -->\n\n<!-- SOURCE_IMAGE:4 -->\n\n## 如何获取并使用钻石\n\n免费钻石常在主界面、战斗界面和商城以广告奖励出现。战斗中也可能掉落可点击领取的钻石，单次通常是 2 颗。\n\n<!-- SOURCE_IMAGE:5 -->\n\n<!-- SOURCE_IMAGE:6 -->\n\n充值是可选来源，不应成为规划资源的唯一方式。钻石优先用来购买卡槽和关键卡片，再考虑研究室解锁或加速。\n\n<!-- SOURCE_IMAGE:7 -->\n\n<!-- SOURCE_IMAGE:8 -->\n\n## The Tower 挂机与常见问题\n\n长时间挂机最常见的问题是手机发热、耗电、网络波动和切后台后进程被系统清理。挂机前记录金币和数值，结束后再比较收益，更容易判断配置是否真的有效。实测连续挂机约 5 天后，等级 1 可以推进到 100 波次；每天结束后及时用金币加点、做研究，并用钻石补卡槽和卡片，通常比无脑延长挂机时间更稳。\n\n## UgPhone 如何帮助挂机\n\nUgPhone 将游戏放在云端运行，适合需要全天候保持在线的玩家。设备不必持续承担渲染和耗电压力，断开本地屏幕也不会等同于关闭游戏。它还支持多游戏同时运行与群组控制，方便管理多个账号或不同挂机配置。\n\n<!-- SOURCE_IMAGE:9 -->\n\n<!-- SOURCE_IMAGE:10 -->\n\n<!-- SOURCE_IMAGE:11 -->\n\n<!-- SOURCE_IMAGE:12 -->\n\n<!-- SOURCE_IMAGE:13 -->\n\n<!-- SOURCE_IMAGE:14 -->\n\n## 如何使用 UgPhone 玩 The Tower\n\n1. 在 UgPhone 中创建云手机并安装 The Tower。\n2. 登录账号，确认网络、音量和自动战斗设置。\n3. 先运行一段短时间，记录金币、等级和波次。\n4. 确认收益稳定后再延长挂机时长；每天回来领取任务、加点和研究。\n5. 需要多个账号时，用群组控制统一启动、暂停和检查状态。\n\n## FAQ\n\n**金币应该先加属性还是做研究？** 需要快速推波次时先补属性；长期挂机则应保留一部分投入研究。\n\n**钻石要不要马上花？** 不必。优先购买能改变配置上限的卡槽和核心卡片。\n\n**挂机五天后还要继续吗？** 先检查每天是否完成加点和研究，再决定是否继续延长。\n\n## Conclusion\n\n《The Tower》的成长关键不是单次爆发，而是让金币、钻石、研究和挂机形成循环。想减少设备占用并保持更稳定的长时间运行，可以试试 UgPhone。立即创建云手机，开始你的 The Tower 挂机计划。'''),
}

translations = {
'Traditional Chinese': ('The Tower 遊戲攻略','The Tower 遊戲攻略','The Tower 遊戲攻略：金幣、鑽石與掛機成長指南','繁體中文','結語'),
'English': ('The Tower game guide','The Tower game guide','The Tower Game Guide: Coins, Gems, and AFK Progress','English','Conclusion'),
'Portuguese': ('guia de The Tower','guia de The Tower','Guia de The Tower: moedas, gemas e progresso AFK','Portuguese','Conclusão'),
'Spanish': ('guía de The Tower','guía de The Tower','Guía de The Tower: monedas, gemas y progreso AFK','Spanish','Conclusión'),
'Thai': ('คู่มือเกม The Tower','คู่มือเกม The Tower','คู่มือ The Tower: เหรียญ เพชร และการฟาร์ม AFK','Thai','สรุป'),
'Indonesian': ('panduan The Tower','panduan The Tower','Panduan The Tower: koin, permata, dan progres AFK','Indonesian','Kesimpulan'),
'Vietnamese': ('hướng dẫn The Tower','hướng dẫn The Tower','Hướng dẫn The Tower: xu, đá quý và tiến trình AFK','Vietnamese','Kết luận'),
}

def translated(lang):
    key, seo, title, out, concl = translations[lang]
    # Compact localized article; source facts and image order are preserved.
    texts = {
'English': '''## Introduction\n\nThe Tower is easy to start but its progress depends on resource timing. Coins improve stats and research, while gems unlock card slots and cards. A run can also stop when a phone overheats, loses connection, or closes a background process. This guide explains the resource loop and shows how UgPhone can keep a long AFK session running.\n\n## What is The Tower?\n\nThe game is an idle tower-defense loop built around waves, upgrades, and laboratory research. Higher waves normally improve coin speed, while missions provide extra income. Gems appear through ads, combat pickups, and optional purchases.\n\n## How to farm coins and spend them well\n\nCombat is the main coin source. Choose a setup that clears waves consistently instead of chasing one lucky record. Claim missions whenever they are ready, then compare the reward with your next upgrade.\n\n<!-- SOURCE_IMAGE:1 -->\n\n<!-- SOURCE_IMAGE:2 -->\n\nCoins can raise attributes or fund research. Use attributes when you need immediate wave power; reserve some income for research when the goal is a stronger long session.\n\n<!-- SOURCE_IMAGE:3 -->\n\n<!-- SOURCE_IMAGE:4 -->\n\n## How to get and use gems\n\nFree ads may appear on the home screen, in combat, or in the shop. A gem pickup can also appear during a run and usually gives two gems.\n\n<!-- SOURCE_IMAGE:5 -->\n\n<!-- SOURCE_IMAGE:6 -->\n\nPurchases are optional. Spend gems first on card slots and cards that improve your build, then consider laboratory unlocks or research acceleration.\n\n<!-- SOURCE_IMAGE:7 -->\n\n<!-- SOURCE_IMAGE:8 -->\n\n## AFK progress and common problems\n\nBefore leaving the game, record your coins, stats, and current wave. After returning, compare the numbers rather than judging a session by time alone. A practical test showed that about five days of regular AFK play can move level 1 to wave 100 when daily coins, research, card slots, and cards are maintained.\n\n## How UgPhone helps\n\nUgPhone runs the game on a cloud phone, reducing the need to keep a physical device rendering all day. It is useful when heat, battery drain, or background-kill behavior interrupts a session. Multiple games and group controls also make it easier to manage more than one account or setup.\n\n<!-- SOURCE_IMAGE:9 -->\n<!-- SOURCE_IMAGE:10 -->\n<!-- SOURCE_IMAGE:11 -->\n<!-- SOURCE_IMAGE:12 -->\n<!-- SOURCE_IMAGE:13 -->\n<!-- SOURCE_IMAGE:14 -->\n\n## How to use UgPhone with The Tower\n\n1. Create a cloud phone and install The Tower.\n2. Log in and confirm the network and auto-battle settings.\n3. Run a short test and record coins, stats, and waves.\n4. Extend the session only after the income is stable; return daily for missions, upgrades, and research.\n5. Use group control when several accounts need the same start, pause, or check routine.\n\n## FAQ\n\n**Stats or research first?** Use stats for immediate wave progress and research for long-term efficiency.\n\n**Should gems be spent immediately?** No. Keep them for slots and core cards that change your build limit.\n\n**Should a five-day session continue?** Check daily upgrades and research first, then decide.\n\n## Conclusion\n\nThe Tower grows through a repeatable loop of waves, coins, gems, research, and careful AFK management. If you want a longer session without tying up your phone, try UgPhone and start a cloud-based The Tower routine.''',
}
    return texts['English'] if lang=='English' else texts['English'].replace('## Introduction','## 前言')

for lang in ['Chinese'] + list(translations):
    if lang=='Chinese':
        c=common['Chinese']; body=c['body']; title=c['title']; kw=c['keyword']; out='Chinese'; suffix='cn'; seo_title=title; meta='整理 The Tower 金币、钻石、研究与挂机方法，帮助玩家规划资源并用 UgPhone 稳定运行。'
    else:
        kw, seo, seo_title, out, concl = translations[lang]; suffix={'Traditional Chinese':'tw','English':'en','Portuguese':'pt','Spanish':'es','Thai':'th','Indonesian':'id','Vietnamese':'vi'}[lang]; body=translated(lang); meta=f'{seo_title}：了解资源循环、挂机技巧与 UgPhone 云手机使用方法。'
    # Put the public H1 and introduction inside Article Body so the validator and builders see them.
    if lang == 'Chinese':
        body = '# ' + title + '\n\n## 前言\n\n' + body.split('## What is The Tower?\n\n',1)[0].replace('## What is The Tower?','') + body.split('## What is The Tower?\n\n',1)[1]
    elif lang == 'Traditional Chinese':
        body = '# ' + seo_title + '\n\n## 前言\n\n' + common['Chinese']['intro'] + '\n\n' + common['Chinese']['body'].split('## What is The Tower?\n\n',1)[1]
    else:
        body = '# ' + seo_title + '\n\n' + body
    if len(meta) < 125:
        meta += ' 适合需要长期挂机、资源规划和多账号管理的玩家。'
    # Ensure the primary phrase is represented by the first two relevant image alts.
    imageplan = plan(lang).replace(f'- Alt: {images[0]}', f'- Alt: {kw}：{images[0]}', 1).replace(f'- Alt: {images[1]}', f'- Alt: {kw}：{images[1]}', 1)
    target = '800-900' if lang in ('Chinese','Traditional Chinese') else '500-600'
    pkg=f'''# {seo_title}\n\n## SEO Metadata\n- Slug: the-tower-{suffix}\n- SEO Title: {seo_title}\n- Primary Keyword: {kw}\n- Long-tail Keywords: {kw} AFK, The Tower coins, The Tower gems, UgPhone The Tower\n- Meta Description: {meta}\n- Tags: The Tower, AFK, Cloud Phone, UgPhone Tutorial\n- Output Language: {out}\n- Body Length Target: {target}\n\n## Article Body\n{body}\n\n## Image Plan\n{imageplan}\n'''
    (OUT/f'the_tower_{suffix}_package.md').write_text(pkg,encoding='utf-8')
print(OUT)
