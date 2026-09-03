F = {
'M':["#   #","## ##","# # #","#   #","#   #"],
'A':[" ### ","#   #","#####","#   #","#   #"],
'T':["#####","  #  ","  #  ","  #  ","  #  "],
'H':["#   #","#   #","#####","#   #","#   #"],
'E':["#####","#    ","#### ","#    ","#####"],
'U':["#   #","#   #","#   #","#   #"," ### "],
'S':[" ####","#    "," ### ","    #","#### "],
'D':["#### ","#   #","#   #","#   #","#### "],
'R':["#### ","#   #","#### ","#  # ","#   #"],
'O':[" ### ","#   #","#   #","#   #"," ### "],
}
BG, DIM, LIT, SOFT = "#0c1512", "#1a2a22", "#63b07a", "#509475"
FG, MUTED = "#81B8A8", "#53685B"

CELL, R = 14, 4.6
COLS, ROWS = 72, 22
W, H = COLS*CELL, ROWS*CELL

lit = {}
def place(word, row0, col0, color):
    for i, ch in enumerate(word):
        g = F[ch]
        for r in range(5):
            for c in range(5):
                if g[r][c] == "#":
                    lit[(row0+r, col0+i*6+c)] = color

w1, w2 = "MATHEUS", "MEDRADO"
width_cells = 7*6 - 1
col0 = (COLS - width_cells)//2
place(w1, 3, col0, LIT)
place(w2, 10, col0, LIT)

out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Matheus Medrado, software developer">']
out.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
for r in range(ROWS):
    for c in range(COLS):
        cx, cy = c*CELL + CELL/2, r*CELL + CELL/2
        color = lit.get((r, c), DIM)
        rad = R if (r, c) in lit else R*0.62
        out.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{rad:.1f}" fill="{color}"/>')

ty = 17*CELL + 4
out.append(f'<text x="{W/2:.0f}" y="{ty:.0f}" fill="{FG}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="19" letter-spacing="5.5" text-anchor="middle">software developer</text>')
out.append(f'<text x="{W/2:.0f}" y="{ty+30:.0f}" fill="{MUTED}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="14" letter-spacing="3.5" text-anchor="middle">computer science &#183; ufu &#183; uberl&#226;ndia, brasil</text>')
out.append('</svg>')
open('/tmp/claude-1000/banner/banner.svg','w').write("\n".join(out))
print(W, H, "cells lit:", len(lit))
