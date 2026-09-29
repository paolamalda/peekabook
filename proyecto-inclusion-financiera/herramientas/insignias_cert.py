# Genera las imágenes de las insignias (PNG 512) y el fondo del certificado (PNG A4 horizontal).
import os, json, subprocess, sys
EN = "--en" in sys.argv
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = "/tmp/assets_tdtf"
F = "/tmp/fnt"
FONTS = "<style>" + "".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(file://{F}/fontsource-{pk}-5.3.0/package/files/{pk}-latin-{w}-normal.woff2)}}" for fam, pk in (("Figtree", "figtree"), ("Bricolage Grotesque", "bricolage-grotesque")) for w in (500, 600, 700, 800)) + "</style>"
B = [("01_M1_mi_dinero_en_orden", "M1", "Mi dinero en orden", "fa-calendar-check-o"),
     ("02_M2_envio_inteligente", "M2", "Envío inteligente", "fa-paper-plane"),
     ("03_M3_credito_con_rumbo", "M3", "Crédito con rumbo", "fa-line-chart"),
     ("04_M4_familia_protegida", "M4", "Familia protegida", "fa-shield"),
     ("05_M5_futuro_en_marcha", "M5", "Futuro en marcha", "fa-leaf"),
     ("06_detective_de_estafas", "ESPECIAL", "Detective de estafas", "fa-search"),
     ("07_comparador_experto", "ESPECIAL", "Comparador experto", "fa-balance-scale"),
     ("08_plan_completo", "CURSO", "Plan completo", "fa-trophy")]
if EN:
    B = [("01_M1_my_money_in_order", "M1", "My money in order", "fa-calendar-check-o"),
         ("02_M2_smart_sending", "M2", "Smart sending", "fa-paper-plane"),
         ("03_M3_credit_on_track", "M3", "Credit on track", "fa-line-chart"),
         ("04_M4_protected_family", "M4", "Protected family", "fa-shield"),
         ("05_M5_future_in_motion", "M5", "Future in motion", "fa-leaf"),
         ("06_scam_detective", "SPECIAL", "Scam detective", "fa-search"),
         ("07_expert_comparer", "SPECIAL", "Expert comparer", "fa-balance-scale"),
         ("08_complete_plan", "COURSE", "Complete plan", "fa-trophy")]
T = dict(top="YOUR MONEY · YOUR FAMILY · YOUR FUTURE", t="Certificate of Completion", otorga="Awarded to", name="Participant name",
         txt="for completing the financial education program <b>Your Money, Your Family, Your Future</b> (California pilot), with its five modules and self-assessments passed.",
         mods=["My money", "Financial system and remittances", "Credit and debt", "Protection", "Future and wealth"],
         date="September 28, 2026", fecha="Date", cod="Verification code",
         nota="An educational recognition from the program. It isn't a professional license or an official accreditation.") if EN else \
    dict(top="TU DINERO · TU FAMILIA · TU FUTURO", t="Constancia de conclusión", otorga="Se otorga a", name="Nombre de la persona",
         txt="por concluir el programa de educación financiera <b>Tu Dinero, Tu Familia, Tu Futuro</b> (piloto California), con sus cinco módulos y autoevaluaciones aprobadas.",
         mods=["Mi dinero", "Sistema financiero y remesas", "Crédito y deudas", "Protección", "Futuro y patrimonio"],
         date="28 de septiembre de 2026", fecha="Fecha", cod="Código de verificación",
         nota="Reconocimiento educativo del programa. No es una licencia profesional ni una acreditación oficial.")
TTMF = "--ttmf" in sys.argv
if TTMF:
    B = [("01_dinero_real", "M1", "Dinero real", "fa-calendar-check-o"),
         ("02_carrera_en_regla", "M2 · M3", "Carrera en regla", "fa-briefcase"),
         ("03_se_elegir", "M4 · M5", "Sé elegir", "fa-balance-scale"),
         ("04_credito_bajo_control", "M6 · M8", "Crédito bajo control", "fa-credit-card"),
         ("05_nadie_me_engana", "M9", "Nadie me engaña", "fa-search"),
         ("06_proteccion_activa", "M10", "Protección activa", "fa-umbrella"),
         ("07_futuro_en_escena", "M11", "Futuro en escena", "fa-star"),
         ("08_plan_completo", "CURSO", "Plan completo", "fa-trophy")]
    T.update(top="TU TALENTO · TU MARCA · TU FUTURO",
             txt="por concluir el programa de educación financiera <b>Tu Talento, Tu Marca, Tu Futuro</b>, con sus once módulos y autoevaluaciones aprobadas.",
             mods=["Tu dinero y tu carrera", "Sistema financiero", "Crédito y deudas", "Protección", "Futuro"])
MODS = "".join(f"<span>{m}</span>" for m in T["mods"])
OUTB, OUTC = [os.path.join(os.path.dirname(BASE), "proyecto-entretenimiento", "moodle", d) for d in ("insignias", "certificado")] if TTMF else [os.path.join(BASE, "moodle/v3/en" if EN else "moodle/v3", d) for d in ("insignias", "certificado")]
def badge(tag, name, icon, gold=False):
    ring = "linear-gradient(135deg,#E4007C,#FF4FA8)" if gold else "linear-gradient(135deg,#0A3161,#061F40)"
    return f'''<!doctype html><html><head><meta charset=utf-8><link rel=stylesheet href="file://{A}/fa.css">{FONTS}
<style>html,body{{margin:0;background:transparent}}.b{{width:512px;height:512px;position:relative}}
.o{{position:absolute;inset:16px;border-radius:50%;background:{ring};box-shadow:0 10px 30px rgba(6,31,64,.35)}}
.i{{position:absolute;inset:44px;border-radius:50%;background:#fff;border:6px solid #E6ECF5}}
.c{{position:absolute;inset:70px;border-radius:50%;background:linear-gradient(160deg,#0A3161,#061F40);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff}}
.c i{{font-size:120px;color:#fff}}.tag{{font:700 26px Figtree;letter-spacing:3px;color:#FF4FA8;margin-top:14px}}
.r{{position:absolute;left:18px;right:18px;bottom:38px;background:#E4007C;color:#fff;border-radius:18px;text-align:center;font:800 34px 'Bricolage Grotesque';padding:12px 6px;box-shadow:0 6px 16px rgba(228,0,124,.35)}}
.brand{{position:absolute;top:84px;width:100%;text-align:center;font:600 17px Figtree;color:#FF4FA8;letter-spacing:2px}}</style></head>
<body><div class=b><div class=o></div><div class=i></div><div class=c><i class="fa {icon}"></i><div class=tag>{tag}</div></div><div class=r>{name}</div></div></body></html>'''
CERT = lambda sample: f'''<!doctype html><html><head><meta charset=utf-8><link rel=stylesheet href="file://{A}/fa.css">{FONTS}
<style>html,body{{margin:0}}.p{{width:2339px;height:1654px;position:relative;background:#fff;font-family:Figtree;overflow:hidden}}
.f{{position:absolute;inset:60px;border:10px solid #0A3161;border-radius:40px}}.f2{{position:absolute;inset:92px;border:3px solid #E4007C;border-radius:28px}}
.band{{position:absolute;left:0;top:0;bottom:0;width:26px;background:#E4007C}}
.circ{{position:absolute;right:-260px;top:-260px;width:760px;height:760px;border-radius:50%;background:#E6ECF5}}
.circ2{{position:absolute;left:-200px;bottom:-260px;width:620px;height:620px;border-radius:50%;background:#F5F7FB}}
.top{{position:absolute;top:190px;width:100%;text-align:center;color:#5A6478;font:600 44px Figtree;letter-spacing:10px}}
.t{{position:absolute;top:270px;width:100%;text-align:center;color:#0A3161;font:800 150px 'Bricolage Grotesque'}}
.otorga{{position:absolute;top:500px;width:100%;text-align:center;color:#5A6478;font:500 46px Figtree}}
.line{{position:absolute;top:760px;left:520px;right:520px;border-top:4px solid #E5E8F0}}
.name{{position:absolute;top:610px;width:100%;text-align:center;color:#0B1220;font:700 110px 'Bricolage Grotesque'}}
.txt{{position:absolute;top:810px;left:330px;right:330px;text-align:center;color:#0B1220;font:500 46px/1.45 Figtree}}
.txt b{{color:#0A3161}}.mods{{position:absolute;top:1010px;width:100%;text-align:center;font:600 32px Figtree;color:#5A6478}}
.mods span{{display:inline-block;margin:0 14px;padding:10px 26px;border-radius:40px;background:#E6ECF5;color:#0A3161}}
.foot{{position:absolute;bottom:170px;left:260px;right:260px;display:flex;justify-content:space-between;align-items:flex-end;color:#5A6478;font:500 34px Figtree}}
.foot .c{{text-align:center;width:560px}}.foot .c div{{border-top:3px solid #0A3161;padding-top:14px;margin-top:70px}}
.seal{{position:absolute;bottom:150px;left:50%;margin-left:-150px;width:300px;height:300px;border-radius:50%;background:linear-gradient(135deg,#E4007C,#FF4FA8);display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(228,0,124,.3)}}
.seal i{{font-size:140px;color:#fff}}.brand{{position:absolute;top:120px;left:150px;font:800 40px 'Bricolage Grotesque';color:#0A3161}}.brand span{{color:#E4007C}}
.nota{{position:absolute;bottom:108px;width:100%;text-align:center;font:500 24px Figtree;color:#5A6478}}.ph{{color:#E4007C}}</style></head><body><div class=p>
<div class=circ></div><div class=circ2></div><div class=band></div><div class=f></div><div class=f2></div>
<div class=brand>Desarrolla <span>Talento</span></div>
<div class=top>{T['top']}</div><div class=t>{T['t']}</div>
<div class=otorga>{T['otorga']}</div>{'<div class=name>'+T['name']+'</div>' if sample else ''}<div class=line></div>
<div class=txt>{T['txt']}</div>
<div class=mods>{MODS}</div>
<div class=seal><i class="fa fa-trophy"></i></div>
<div class=foot><div class=c>{'<span class=ph>'+T['date']+'</span>' if sample else '&nbsp;'}<div>{T['fecha']}</div></div><div class=c>{'<span class=ph>AbC123xYz9</span>' if sample else '&nbsp;'}<div>{T['cod']}</div></div></div>
<div class=nota>{T['nota']}</div>
</div></body></html>'''
jobs = []
os.makedirs(OUTB, exist_ok=True); os.makedirs(OUTC, exist_ok=True)
tmp = "/tmp/badges_html"; os.makedirs(tmp, exist_ok=True)
for fn, tag, name, icon in B:
    p = f"{tmp}/{fn}.html"; open(p, "w").write(badge(tag, name, icon, gold=(tag in ("CURSO", "COURSE"))))
    jobs.append((p, os.path.join(OUTB, fn + ".png"), 512, 512, True))
for s, out in [(False, "certificado_fondo.png"), (True, "certificado_muestra.png")]:
    p = f"{tmp}/{out}.html"; open(p, "w").write(CERT(s))
    jobs.append((p, os.path.join(OUTC, out), 2339, 1654, False))
js = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();for(const [f,o,w,h,t] of %s){const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+f);await p.waitForTimeout(1200);await p.screenshot({path:o,omitBackground:t});await p.close();}await b.close();})();" % json.dumps(jobs)
open(f"{tmp}/r.js", "w").write(js)
subprocess.run(["node", f"{tmp}/r.js"], check=True, env={**os.environ, "NODE_PATH": subprocess.check_output(["npm", "root", "-g"]).decode().strip()})
print("ok")
