"""Design artifact authoring only. Does not build or modify the React website."""
from pathlib import Path
from PIL import ImageFont
import html, json

ROOT = Path(__file__).parent
P = {'paper':'#F7F5EF','forest':'#203C32','clay':'#9D442F','sage':'#E3E9DE','muted':'#59655D','border':'#B7C1B4','hover':'#142C23','pressed':'#0C2119','disabled':'#D6DBD2'}
FONTS = {'serif':ROOT/'fonts/Literata.ttf','sans':ROOT/'fonts/GolosText.ttf'}
manifest=[]

def esc(s): return html.escape(str(s),quote=True)
def metric(s,size,kind='sans'):
    return ImageFont.truetype(str(FONTS[kind]),size).getlength(s)
def wrap(s,width,size,kind='sans'):
    lines=[]
    for para in s.split('\n'):
        line=''
        for word in para.split():
            test=(line+' '+word).strip()
            if line and metric(test,size,kind)>width:
                lines.append(line);line=word
            else:line=test
        lines.append(line)
    return lines

class Board:
    def __init__(self,w,h,title,bg='paper'):
        self.w,self.h,self.title=w,h,title
        self.parts=[];self.texts=[]
        self.rect(0,0,w,h,bg)
    def rect(self,x,y,w,h,color,rx=0,stroke=None,sw=1):
        c=P.get(color,color)
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c}"'+(f' stroke="{P.get(stroke,stroke)}" stroke-width="{sw}"' if stroke else '')+'/>')
    def text(self,s,x,y,width,size=20,lh=None,kind='sans',color='forest',weight=400,align='left',lines=None,name=None):
        lh=lh or round(size*1.5)
        lines=lines or wrap(s,width,size,kind)
        anchor={'left':'start','center':'middle','right':'end'}[align]
        px=x+(width/2 if align=='center' else width if align=='right' else 0)
        family='Literata' if kind=='serif' else 'Golos Text'
        spans=''.join(f'<tspan x="{px}" y="{y+size+i*lh}">{esc(t)}</tspan>' for i,t in enumerate(lines))
        self.parts.append(f'<text data-width="{width}" data-x="{x}" data-y="{y}" data-label="{esc(name or s[:50])}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{P.get(color,color)}" text-anchor="{anchor}">{spans}</text>')
        self.texts.append({'copy':s,'x':x,'y':y,'width':width,'height':len(lines)*lh,'size':size,'font':family,'lines':lines})
        return y+len(lines)*lh
    def line(self,x1,y1,x2,y2,color='border',sw=1):
        self.parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{P.get(color,color)}" stroke-width="{sw}"/>')
    def path(self,d,color='clay',sw=2):
        self.parts.append(f'<path d="{d}" fill="none" stroke="{P.get(color,color)}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')
    def node(self,x,y,r=5,color='clay',hollow=False,bg='paper'):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{P[bg] if hollow else P[color]}" stroke="{P[color]}" stroke-width="2"/>')
    def button(self,label,x,y,w=248,h=56,state='default',inverse=False):
        color='paper' if inverse else {'default':'forest','hover':'hover','pressed':'pressed','focus':'forest','disabled':'disabled'}[state]
        if state=='focus':self.rect(x-5,y-5,w+10,h+10,'none',5,'clay',2)
        self.rect(x,y,w,h,color,2)
        self.text(label,x+16,y+(h-24)/2-1,w-32,18,24,color='muted' if state=='disabled' else 'forest' if inverse else 'paper',weight=500,align='center',lines=[label])
    def link(self,label,x,y,w=420,state='default',size=18):
        c='clay' if state in ['default','focus'] else 'forest'
        self.text(label,x,y,w,size,26,color=c,weight=500)
        self.line(x,y+29,x+min(w,metric(label,size)),y+29,c,2 if state=='hover' else 1)
        if state=='focus':self.rect(x-5,y-5,w+10,42,'none',2,'clay',2)
    def photo(self,x,y,w,h):
        self.parts.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="../references/still-life.png" preserveAspectRatio="xMidYMid slice"/>')
    def plus(self,x,y,open=False):
        self.path(f'M{x} {y+10} h20'+('' if open else f' M{x+10} {y} v20'),'forest',2)
    def svg(self):
        style=''.join(f'@font-face{{font-family:"{"Literata" if k=="serif" else "Golos Text"}";src:url(../fonts/{"Literata.ttf" if k=="serif" else "GolosText.ttf"}) format("truetype");font-weight:100 900;font-style:normal;}}' for k in FONTS)
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{esc(self.title)}"><title>{esc(self.title)}</title><defs><style>{style}</style></defs>'+''.join(self.parts)+'</svg>'
    def save(self,name,folder='screens'):
        (ROOT/folder/f'{name}.svg').write_text(self.svg(),encoding='utf-8')
        manifest.append({'name':name,'title':self.title,'path':f'{folder}/{name}.svg','width':self.w,'height':self.h,'textBlocks':self.texts})

def section(name,h,bg='paper'): return Board(1440,h,name,bg)
sections=[]
b=section('01 / Header',96)
b.text('ДРУЖИМ',80,24,300,32,42,'serif')
for label,x,w in [('О нас',722,80),('Кому помогаем',830,170),('Второй сезон',1028,150)]:b.text(label,x,36,w,16,24,weight=500)
b.button('Связаться',1210,20,150)
sections.append(('01-header',b))

b=section('02 / Hero',648)
b.text('У каждого — свой путь.',80,52,1280,88,108,'serif',align='center',lines=['У каждого — свой путь.'])
b.text('Рядом — ДРУЖИМ.',80,160,1280,88,108,'serif','clay',align='center',lines=['Рядом — ДРУЖИМ.'])
b.path('M0 274 C260 280 350 362 720 362 C1050 362 1150 292 1440 274')
b.path('M1240 416 C1040 416 998 362 720 362')
b.node(720,362)
b.text('Помогаем детям, молодежи и семьям развивать навыки, находить поддержку и становиться самостоятельнее.',330,414,780,20,30,align='center')
b.button('Узнать о группах',590,530,260)
sections.append(('02-hero',b))

b=section('03 / Кому мы помогаем',736)
b.text('Кому мы помогаем',80,72,780,56,70,'serif')
b.text('Психологическая и социальная поддержка. Развитие практических и социальных навыков.',928,80,432,18,28)
aud=[('Детям','Помогаем развивать навыки и уверенность.'),('Молодежи','Поддерживаем на пути к самостоятельности.'),('Семьям','Объединяем опыт родителей и специалистов.'),('Людям с особенностями развития','Помогаем включаться в жизнь сообщества.')]
b.path('M104 212 C76 264 130 307 104 358 C78 410 132 454 104 504 C78 554 128 610 104 678','border')
for i,(label,body) in enumerate(aud):
    y=224+i*112
    b.node(104,y+32,6,hollow=True)
    b.text(label,160,y,632,36 if i<3 else 32,44,'serif')
    b.text(body,928,y+8,432,20,30)
    if i<3:b.line(160,y+90,1360,y+90)
sections.append(('03-audience',b))

b=section('04 / Замещающие семьи',840,'sage')
b.text('Замещающие семьи',80,64,1000,18,26,weight=500)
b.text('Семье тоже нужна поддержка',80,106,1280,64,80,'serif',lines=['Семье тоже нужна поддержка'])
b.photo(80,250,704,420)
b.text('Особое внимание — семьям, связанным с опекой, приемным родительством и усыновлением.',848,246,512,24,36)
b.text('Поддержка важна и детям в учреждениях, и выпускникам, которые начинают самостоятельную жизнь.',848,432,512,20,30)
b.link('Обсудить свою ситуацию',848,608,500)
b.text('Визуальный референс. Фотографию центра согласуем.',80,686,704,14,22,color='muted')
b.path('M760 790 C940 722 1170 788 1440 700 M1110 774 C1210 774 1290 814 1440 824')
b.node(1110,774,4)
sections.append(('04-foster-families',b))

b=section('05 / Что происходит в ДРУЖИМ',692)
b.text('Что происходит\nв «ДРУЖИМ»',80,64,1280,64,78,'serif')
items=[('01','Поддержка','Психологическая и социальная помощь.',80,308),('02','Навыки','Практические и социальные навыки для самостоятельной жизни.',528,364),('03','Сообщество','Опыт родителей и знания специалистов — рядом.',976,284)]
b.path('M88 406 C240 390 390 460 536 462 C720 462 778 382 984 382 C1130 382 1250 404 1360 386')
for num,title,copy,x,y in items:
    b.text(num,x,y,300,64,78,'serif','clay');b.node(x+8,y+98,5)
    b.text(title,x,y+120,380,36,46,'serif');b.text(copy,x,y+182,360,20,30)
b.text('Конкретные занятия и состав групп уточняются.',80,638,1280,14,22,color='muted')
sections.append(('05-activities',b))

b=section('06 / Второй сезон',544,'forest')
b.text('Второй сезон.\nНовые встречи.',80,62,760,64,78,'serif','paper')
b.text('Открывается запись в группы второго сезона.',80,256,700,24,36,color='paper')
b.text('Возраст, расписание и условия участия уточняются.',80,380,670,18,28,color='paper')
b.path('M760 0 C820 40 790 310 930 324 M760 544 C830 470 822 340 930 324 M1110 544 C1030 472 1030 360 930 324 M930 324 H1080','paper')
b.node(930,324,5,'paper');b.button('Узнать о группах',1080,296,280,inverse=True)
sections.append(('06-season',b))

b=section('07 / Миссия',676)
b.text('Наша миссия',80,64,1000,18,26,weight=500)
b.text('Больше самостоятельности.\nБольше возможностей\nбыть собой.',80,112,1280,64,80,'serif')
b.text('Создаем безопасное и поддерживающее пространство, где дети, молодежь и семьи могут раскрывать потенциал и уверенно строить будущее без барьеров и стереотипов.',744,430,616,20,30)
b.path('M0 434 C220 430 248 532 588 532 M0 630 C240 630 250 532 588 532')
b.node(588,532,4)
sections.append(('07-mission',b))

b=section('08 / Руководитель',720)
b.rect(80,80,420,524,'sage')
b.text('Портрет руководителя\nпосле согласования',120,298,340,20,30,align='center')
b.text('Руководитель',600,80,760,18,26,weight=500)
b.text('Ирина Анатольевна\nМалышева',600,136,760,56,72,'serif')
b.text('Руководит организацией с 2025 года.',600,340,710,24,36)
b.text('Объединяет опыт родителей и специалистов.',600,438,620,20,30)
b.text('Личную историю публикуем только после согласования.',600,540,620,14,22,color='muted')
b.path('M1170 630 C1290 620 1280 512 1440 492')
sections.append(('08-leader',b))

b=section('09 / Факты',440)
b.line(80,0,1360,0)
b.text('Факты о «ДРУЖИМ»',80,56,1280,56,72,'serif')
b.text('2025',80,178,420,64,80,'serif','clay')
b.text('Ирина Анатольевна приняла руководство организацией.',80,276,420,20,30)
b.text('Второй сезон',648,180,712,56,76,'serif','clay')
b.text('Открывается запись в группы.',648,276,712,20,30)
b.text('Результаты работы добавим после проверки данных.',80,386,1280,14,22,color='muted')
sections.append(('09-facts',b))

faq_questions=['Кому помогает «ДРУЖИМ»?','Как узнать о группах второго сезона?','Каковы возраст, расписание и условия участия?','Как связаться с организацией?']
b=section('10 / FAQ',716)
b.text('Вопросы,\nс которых\nможно начать',80,80,530,56,72,'serif')
b.line(664,84,1360,84,'clay',2)
b.text(faq_questions[0],664,104,646,24,34,weight=500);b.plus(1332,114,True)
b.text('Детям, молодежи, семьям и людям с особенностями развития. Особое внимание — замещающим семьям, детям в учреждениях и выпускникам.',664,160,654,20,30)
for i,q in enumerate(faq_questions[1:]):
    y=326+i*98;b.line(664,y,1360,y);b.text(q,664,y+20,622,22,32,weight=500);b.plus(1332,y+28)
b.line(664,620,1360,620)
b.text('Ответы об участии и контактах требуют согласования.',664,648,696,14,22,color='muted')
sections.append(('10-faq',b))

b=section('11 / Финальный контакт',500,'sage')
b.text('Начнем\nс разговора',80,48,880,72,88,'serif')
b.text('Расскажите, какая поддержка вам нужна.',80,264,750,24,36)
b.button('Связаться с «ДРУЖИМ»',80,344,320)
b.text('TODO: подтвержденный канал связи',80,420,700,14,22,color='clay')
b.path('M1440 0 C1240 200 1220 314 1010 342 M1440 160 C1270 290 1150 338 1010 342 M1440 480 C1260 372 1160 342 1010 342')
b.node(1010,342,6)
sections.append(('11-contact',b))

b=section('12 / Footer',288)
b.text('ДРУЖИМ',80,48,500,40,52,'serif')
b.text('АНО «Центр социализации детей и молодежи „ДРУЖИМ“»',80,122,580,16,24)
for label,x,w in [('О нас',850,80),('Кому помогаем',958,170),('Второй сезон',1170,190)]:b.text(label,x,62,w,16,24,weight=500)
b.line(80,200,1360,200)
b.text('Контакты, реквизиты и правовые документы — после проверки.',80,224,1280,14,22,color='muted')
sections.append(('12-footer',b))

full=Board(1440,sum(s.h for _,s in sections),'ДРУЖИМ — полная главная, desktop 1440')
offset=0
for name,s in sections:
    s.save(name,'sections');full.parts.append(f'<g id="{name}" transform="translate(0 {offset})">'+''.join(s.parts)+'</g>')
    full.texts += [{**t,'y':t['y']+offset} for t in s.texts]
    offset+=s.h
full.save('desktop-1440')

def mobile_header(b,close=False):
    b.text('ДРУЖИМ',24,22,220,26,36,'serif')
    b.rect(274,16,92,48,'none',2,'border');b.text('Закрыть' if close else 'Меню',278,29,84,16,24,weight=500,align='center')

b=Board(390,844,'Mobile / Hero 390')
mobile_header(b)
b.text('У каждого —\nсвой путь.',24,124,342,44,56,'serif')
b.text('Рядом —\nДРУЖИМ.',24,236,342,44,56,'serif','clay')
b.path('M0 396 C130 360 166 434 262 416 C308 406 348 410 390 388');b.node(262,416,4)
b.text('Помогаем детям, молодежи и семьям развивать навыки, находить поддержку и становиться самостоятельнее.',24,462,342,18,28)
b.button('Узнать о группах',24,638,342)
b.text('Кому мы\nпомогаем',24,744,342,34,44,'serif')
b.save('mobile-hero-390')

b=Board(390,1004,'Mobile / Кому помогаем 390')
b.text('Кому мы\nпомогаем',24,48,342,34,44,'serif')
b.text('Психологическая и социальная поддержка. Развитие практических и социальных навыков.',24,172,342,18,28)
b.path('M32 326 V942','border')
for i,(title,copy)in enumerate(aud):
    y=326+i*148;b.node(32,y+24,5,hollow=True)
    end=b.text(title,56,y,310,28,36,'serif')
    b.text(copy,56,end+16,310,18,28)
b.save('mobile-audience-390')

b=Board(390,1084,'Mobile / Замещающие семьи 390','sage')
b.text('Замещающие семьи',24,40,342,16,24,weight=500)
b.text('Семье тоже\nнужна поддержка',24,92,342,34,44,'serif')
b.photo(24,226,342,228)
b.text('Визуальный референс.\nФотографию центра согласуем.',24,470,342,14,22,color='muted')
b.text('Особое внимание — семьям, связанным с опекой, приемным родительством и усыновлением.',24,548,342,20,30)
b.text('Поддержка важна и детям в учреждениях, и выпускникам, которые начинают самостоятельную жизнь.',24,744,342,18,28)
b.link('Обсудить свою ситуацию',24,944,342)
b.path('M0 1040 C138 995 180 1064 390 1022')
b.save('mobile-foster-390')

b=Board(390,676,'Mobile / Второй сезон 390','forest')
b.text('Второй сезон.\nНовые встречи.',24,56,342,40,52,'serif','paper')
b.text('Открывается запись в группы второго сезона.',24,224,342,20,30,color='paper')
b.text('Возраст, расписание и условия участия уточняются.',24,336,342,18,28,color='paper')
b.path('M0 450 C124 450 130 492 195 492 M390 450 C260 450 260 492 195 492 M195 492 V528','paper');b.node(195,492,4,'paper')
b.button('Узнать о группах',24,548,342,inverse=True)
b.save('mobile-season-390')

b=Board(390,924,'Mobile / Контакт и footer 390','sage')
b.text('Начнем\nс разговора',24,48,342,40,52,'serif')
b.text('Расскажите, какая поддержка вам нужна.',24,204,342,20,30)
b.path('M390 296 C274 296 252 328 195 336 M0 296 C112 296 130 334 195 336');b.node(195,336,4)
b.button('Связаться с «ДРУЖИМ»',24,388,342)
b.text('TODO: подтвержденный\nканал связи',24,468,342,14,22,color='clay')
b.rect(0,564,390,360,'paper');b.text('ДРУЖИМ',24,602,342,32,42,'serif')
b.text('АНО «Центр социализации детей и молодежи „ДРУЖИМ“»',24,670,342,16,24)
b.text('О нас',24,772,156,16,24,weight=500);b.text('Второй сезон',204,772,162,16,24,weight=500)
b.text('Контакты и правовые документы — после проверки.',24,836,342,14,22,color='muted')
b.save('mobile-contact-390')

b=Board(390,844,'Mobile / Навигация открыта 390')
mobile_header(b,True)
for i,label in enumerate(['О нас','Кому помогаем','Второй сезон','Контакты']):
    y=144+i*98;b.text(label,24,y,342,30,42,'serif');b.line(24,y+72,366,y+72)
b.button('Узнать о группах',24,580,342)
b.text('Прототип: переход к разделу.\nEsc закрывает меню; фокус возвращается на кнопку «Меню».',24,688,342,14,22,color='muted')
b.save('mobile-menu-open-390')

b=Board(390,1056,'Mobile / FAQ 390')
b.text('Вопросы, с которых\nможно начать',24,48,342,34,44,'serif')
b.line(24,204,366,204,'clay',2)
b.text(faq_questions[0],24,226,296,22,32,weight=500);b.plus(342,238,True)
b.text('Детям, молодежи, семьям и людям с особенностями развития. Особое внимание — замещающим семьям, детям в учреждениях и выпускникам.',24,322,342,18,28)
for i,q in enumerate(faq_questions[1:]):
    y=568+i*130;b.line(24,y,366,y);b.text(q,24,y+24,292,20,30,weight=500);b.plus(342,y+30)
b.text('Ответы об участии и контактах требуют согласования.',24,976,342,14,22,color='muted')
b.save('mobile-faq-390')

b=Board(1440,1860,'Система / типографика, цвета и состояния')
b.text('Живая нить',80,56,1280,80,100,'serif')
b.text('ДРУЖИМ · Предварительная система · Дизайн на рассмотрение',80,182,1280,20,30,color='muted')
for i,(key,name)in enumerate([('paper','Бумага'),('forest','Лесной'),('clay','Терракота'),('sage','Шалфей'),('muted','Вторичный текст')]):
    x=80+i*260;b.rect(x,272,232,100,key,stroke='border' if key=='paper' else None);b.text(name,x,392,232,18,26,weight=500);b.text(P[key],x,432,232,14,22,color='muted')
b.text('Literata / Голос и характер',80,516,1280,56,72,'serif')
b.text('Golos Text / Читаемость и действие',80,610,1280,24,36)
b.text('Desktop: 88/108 · H2 64/80 · H3 36/46 · Body 20/30 · UI 18/24\nMobile: 44/56 · H2 34/44 · Body 18/28 · Caption 14/22',80,674,1280,20,30)
b.text('Состояния управления',80,798,1280,40,54,'serif')
for i,state in enumerate(['default','hover','pressed','focus','disabled']):
    x=80+i*260;b.text(state,x,886,232,14,22,color='muted');b.button('Узнать о группах',x,932,232,state=state)
b.text('Ссылки: подчеркивание сохраняется; hover усиливает линию; focus — контур 2 px с отступом.',80,1050,1280,18,28)
for i,state in enumerate(['default','hover','focus']):b.link('Обсудить свою ситуацию',80+i*436,1118,364,state=state)
b.text('Сетка и интервалы',80,1224,1280,40,54,'serif')
b.text('1440 px: 12 колонок · поля 80 · gutter 24\n1024 px: поля 48 · укрупнение типографики ограничено шириной\n768 px: поля 32 · переход к одной колонке по содержимому\n390 px: 4 колонки · поля 24 · gutter 16',80,1312,700,20,30)
for i,v in enumerate([8,16,24,32,48,64,80,128]):
    x=840+(i%4)*130;y=1312+(i//4)*96;b.rect(x,y,v,16,'clay');b.text(str(v),x,y+30,120,14,22,color='muted')
b.text('Фокус и доступность',80,1496,1280,40,54,'serif')
b.text('Кнопки 56 px, навигация не меньше 48 px. Фокус 2 px + зазор 3 px.\nFAQ: нативный details/summary, Enter/Space, явные открытое и закрытое состояния.\nЛинии декоративны и скрываются от скринридера. Информация доступна без motion.\nКонтактные действия активируются после получения проверенного канала связи.',80,1576,1280,20,32)
b.save('system-states')

b=Board(1440,1320,'Motion / постановка и reduced motion')
b.text('Связь становится видимой',80,56,1280,64,80,'serif')
b.text('Однократная последовательность hero · без циклов и блокировки контента',80,170,1280,20,30,color='muted')
stages=[('0–180 ms','Текст уже доступен','Статика → мягкое проявление',0),('180–900 ms','Появляется путь','stroke-dashoffset → 0',1),('650–1050 ms','Пути встречаются','Узел проявляется без пульса',2),('1050–1200 ms','Композиция спокойна','Никакого дальнейшего движения',3)]
for i,(timing,title,sub,stage)in enumerate(stages):
    x=80+i*328;b.rect(x,282,296,254,'sage');b.text('У каждого —\nсвой путь.',x+20,308,256,28,36,'serif');b.text('Рядом — ДРУЖИМ.',x+20,390,256,24,32,'serif','clay')
    if stage>=1:b.path(f'M{x+20} 464 C{x+120} 446 {x+160} 490 {x+268} 464')
    if stage>=2:b.node(x+156,473,4)
    b.text(timing,x,558,296,16,24,weight=500);b.text(title,x,602,296,22,30);b.text(sub,x,682,296,16,24,color='muted')
b.text('Где движение оправдано',80,798,620,36,48,'serif')
b.text('Hero: одна короткая последовательность.\nАудитории: статическая общая линия.\nЗамещающие семьи: однократное раскрытие фото, 400 ms.\nВторой сезон: схождение путей, 500 ms при входе.\nFAQ и меню: локальная смена состояния, 160–200 ms.',80,870,620,18,30)
b.text('Reduced motion / mobile',784,798,576,36,48,'serif')
b.text('reduce: все пути и узлы сразу в конечном виде;\nнет масок, перемещений и scroll-linked эффектов.\nНа mobile: одна статическая линия, без скраббинга.\nФото без маски, текст сразу виден.\nБез pinning, параллакса и перехвата прокрутки.',784,870,576,18,30)
b.line(80,1100,1360,1100)
b.text('Техническая аннотация для будущей реализации: CSS для hover/focus; GSAP только для координации SVG.\nЕсли JavaScript не загрузился, контент и финальная геометрия остаются видимыми. GSAP-код не создан.',80,1144,1280,18,30,color='muted')
b.save('motion-storyboard')

(ROOT/'manifest.json').write_text(json.dumps({'status':'provisional-design-only','figma':'https://www.figma.com/design/5rxBgN9AgG3vmrmD6eBM9m','figmaSync':'partial: MCP Starter limit blocks full canvas sync','palette':P,'boards':manifest},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'boards':len(manifest),'desktopHeight':full.h,'svgTextBlocks':sum(len(x['textBlocks']) for x in manifest)},ensure_ascii=False))
