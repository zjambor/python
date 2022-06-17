"""
Duónia városában vagy. Úthálózatának alakja szabályos négyszöget alkot,
amelyben N számú út halad a nyugat-keleti irányba és M számú út halad az
észak-déli irányba. El szeretnél jutni A pontból B pontba. Emellett 􀀁gyelembe
kell venned, hogy Duóniában különleges útdíj􀀁zetési rendszer van: először
közlekedési pontokat kell vásárolni.
Tegyük fel, hogy már van X számú közlekedési pontod. Ezt követően
nekivághatsz az útnak. A közlekedés megválasztásakor 􀀁gyelembe kell venned,
hogy egynél többször nem mehetsz végig ugyanazon az – egy egység hosszú –
útszakaszon (útiránytól függetlenül), viszont egy adott kereszteződésen
többször is áthaladhatsz. Az utazás során a közlekedési pontjaid forgalma a
következőképpen alakul:
Ha 1 egységet haladsz északi irányban, az megkétszerezi a közlekedési
pontjaid számát: (X -> X*2).
Ha viszont 1 egységnyit haladsz déli irányban, úgy a közlekedési pontjaid
száma megfeleződik: (X -> X/2).
Ha 1 egységnyit haladsz nyugati irányban, a közlekedési pontjaid száma
kettővel csökken: (X -> X-2).
Ha 1 egységnyit haladsz keleti irányban, a közlekedési pontjaid száma
Ha 1 egységnyit haladsz keleti irányban, a közlekedési pontjaid száma
kettővel növekszik: (X -> X+2).
Példaképpen (lásd az ábrán): ha N=3, M=2, X=2, A=(3,1) és B=(1,2), akkor
négyféle úton keresztül lehetséges A-ból B-be jutni.
Melyik az az útvonal, amelynek a végén a legtöbb közlekedési pontot
lehet szerezni, ha:
N=3; M=3; X=10; A=(2,3); B=(1,1)
Válaszok
NWW
Ha 1 egységnyit haladsz keleti irányban, a közlekedési pontjaid száma
kettővel növekszik: (X -> X+2).
NNE: 10 közlekedési pontod lesz (2 -> 4 -> 8 -> 10)
NEN: 12 közlekedési pontod lesz (2 -> 4 -> 6 -> 12)
ENN: 16 közlekedési pontod lesz (2 -> 4 -> 8 -> 16)
ENWNE: 14 közlekedési pontod lesz (2 -> 4 -> 8 -> 6 -> 12 -> 14)
A helyes válasz:
WWSEENNWW
"""

from itertools import product

d={'N':-10,'E':1,'S':10,'W':-1}
res=0

for i in range(1,13):
    for p in product('ENWS', repeat=i):
        used=set() # edges
        act=10 # points
        pos=23 # A=(2,3)
        ok=True
        for c in p:
            nxt=pos+d[c]
            if (pos,nxt) in used or {nxt//10,nxt%10}&{0,4}:
                ok=False
                break
            elif c=='E':  act+=2
            elif c=='W':  act-=2
            elif c=='S':  act/=2
            elif c=='N':  act*=2
            used.add((pos, nxt))
            used.add((nxt, pos))
            pos=nxt
        if ok and pos==11 and act>res: # B=(1,1)
            print("".join(p),act)
            res=act
