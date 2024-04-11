var CryptoJS = require('crypto-js')

function jh() {
            var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : Date.now()
              , n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "yyyy-MM-dd"
              , r = new Date(t)
              , e = n
              , i = {
                "M+": r.getMonth() + 1,
                "d+": r.getDate(),
                "D+": r.getDate(),
                "h+": r.getHours(),
                "H+": r.getHours(),
                "m+": r.getMinutes(),
                "s+": r.getSeconds(),
                "w+": r.getDay(),
                "q+": Math.floor((r.getMonth() + 3) / 3),
                "S+": r.getMilliseconds()
            };
            return /(y+)/i.test(e) && (e = e.replace(RegExp.$1, "".concat(r.getFullYear()).substr(4 - RegExp.$1.length))),
            Object.keys(i).forEach((function(t) {
                if (new RegExp("(".concat(t, ")")).test(e)) {
                    var n = "S+" === t ? "000" : "00";
                    e = e.replace(RegExp.$1, 1 == RegExp.$1.length ? i[t] : "".concat(n).concat(i[t]).substr("".concat(i[t]).length))
                }
            }
            )),
            e
        };
function WHBeO(t, n) {
    return t(n)
};
function vqQjz(t, n) {
    return t !== n
};
function ORUuH(t, n) {
    return t + n
};
function OTCsl(r, i) {
    function o(t, n, r, i) {
        return e(0, i - 1055, 0, n)
    }
    function u(t, r, e, i) {
        return n(t - 1030, i)
    }
    var c = i.map((function(n) {
        function r(t, n, r, e) {
            return u(r - -1955, 0, 0, e)
        }
        var e = {
            TawGD: function(n, r) {
                return WHBeO(n, r)
            },
            mATtl: "__collect envCollect=",
            cIbmx: "0!@",
            gViuq: "s#l",
            vhdiX: "l1fl",
            Ukhnh: "return",
            SZtXE: "end"
        };
        function i(t, n, r, e) {
            return o(0, e, 0, r - -129)
        }
        if (vqQjz("iPbvw", "QzIXx"))
            return ORUuH(ORUuH(n["key"], ":"), n["value"]);
        for (; ; )
            switch (_0x2650de[i(0, 0, 1536, 1678)] = _0x2be945[i(0, 0, 1425, 1270)]) {
            case 0:
                return _0x502786[r(0, 0, -240, -194)] = 2,
                e.TawGD(_0xf75a79, 1);
            case 2:
                return _0x281154 = _0x5e528f.sent,
                _0x563a8d.fp = this[i(0, 0, 1280, 1305) + "nt"],
                _0x5ca9e8 = _0x2554c3[i(0, 0, 1138, 1277)](_0x38e556, null, 2),
                this[i(0, 0, 1312, 1267)](e[i(0, 0, 1335, 1207)][r(0, 0, -64, -241)](_0xb963e1)),
                _0x3cfcec = _0x194992.AES[r(0, 0, -175, -397)](_0x13aeee, _0x12ff37[i(0, 0, 1432, 1484)][r(0, 0, -488, -611)].parse(["wm", e.cIbmx, "w_", e[r(0, 0, -218, 7)], e[i(0, 0, 1561, 1726)], "o("][i(0, 0, 1242, 1165)]("")), {
                    iv: _0xa038ac[i(0, 0, 1432, 1373)].Utf8[r(0, 0, -268, -331)](["01", "02", "03", "04", "05", "06", "07", "08"][r(0, 0, -423, -647)]("")),
                    mode: _0x5de980[r(0, 0, -67, -245)][i(0, 0, 1392, 1477)],
                    padding: _0x1667f2[r(0, 0, -32, -83)].Pkcs7
                }),
                _0x22f9b5.abrupt(e[r(0, 0, -122, -338)], _0x542eb2[r(0, 0, -91, -192)].toString());
            case 8:
            case e.SZtXE:
                return _0x1bba48.stop()
            }
    }
    )).join("&")
      , a = CryptoJS["HmacSHA256"](c, r)["toString"](CryptoJS.enc["Hex"]);
    return a
}
function test(tk,fp,ts,ai){var rd='LCK1dIW7BU91';var str="".concat(tk).concat(fp).concat(ts).concat(ai).concat(rd);return CryptoJS.SHA256(str,tk);}
function __genSignParams(n, r, i, o) {
    return [""["concat"](i), ""["concat"]("3103138295076170"), ""["concat"]("586ae"), ""["concat"]("tk03wa8391ba318nuZ7Udhn6dnXPm6Acb3CQHa1eKYowom4hVIxSk8ibPKaNgm328jH8lLuCG4fFR2gHiQ4PR79iCIjv"), ""["concat"](n), ""["concat"]("3.1"), ""["concat"](r), "".concat(o)].join(";")
}
function main(body) {
    var c = Date["now"]()
    ,a = jh(c, "yyyyMMddhhmmssSSS")
    ,s = "tk03wa8391ba318nuZ7Udhn6dnXPm6Acb3CQHa1eKYowom4hVIxSk8ibPKaNgm328jH8lLuCG4fFR2gHiQ4PR79iCIjv"
    ,f = ""  // ""
    ,h = "3103138295076170"
    ,l = "586ae"
    ,n = [
        {
            "key": "appid",
            "value": "unionpc"
        },
        {
            "key": "body",
            "value": CryptoJS.SHA256(body).toString()
        },
        {
            "key": "functionId",
            "value": "unionSearch"
        }
    ]
    ,u = test(s, h, a, l).toString()
    ,z = OTCsl(u, n)
    var r = "24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e355076cc27b11bb228be53f32ed20565211b57a03f1e429765aea4b556611ecf015914916af5113e8d4dbc024111755afa3ebcdfa24ae054910f04509e3ae202b3039f3699c21afdaa287dc418104d09f"
    h5st = __genSignParams(z, c, a, r)
    return h5st
}


