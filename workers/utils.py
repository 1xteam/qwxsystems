import re

PLATE_RX = re.compile(r'[A-Z]\d{3}[A-Z]{2}\d{2,3}')
RU2LAT = {'А':'A','В':'B','Е':'E','К':'K','М':'M','Н':'H','О':'O','Р':'P','С':'C','Т':'T','У':'Y','Х':'X','Ы':'Y'}
FIXES  = {'U':'0','O':'0','€':'E','₽':'P','"':'','/':'',',':'','<':'','|':'','I':'1','Z':'2','.':'',':':'','—':''}

def normalize_plate(text: str) -> str:
    cleaned = ''.join(c for c in text if c.isalnum() or c in FIXES)
    out = []
    for i, c in enumerate(cleaned):
        u = c.upper()
        if i == 1 and u in ('U','O'):
            out.append('0')
        elif u in FIXES:
            out.append(FIXES[u] if FIXES[u] else '')
        else:
            out.append(RU2LAT.get(u, u))
    return ''.join(out)

def extract_plate(s: str):
    m = PLATE_RX.search(s)
    return m.group() if m else None
