var CryptoJS = require('crypto-js')

const lF = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
function dne(e, t) {
    switch (arguments.length) {
    case 1:
        return parseInt(Math.random() * e + 1, 10);
    case 2:
        return parseInt(Math.random() * (t - e + 1) + e, 10);
    default:
        return 0
    }
}
function hne(e) {
    return [...Array(e)].map(()=>lF[dne(0, 61)]).join("")
}

const a = Date.now()
  , l = hne(16)
  , c = "k8tUyS$m"
  , d = {
    "X-Dgi-Req-App": "ggzy-portal",
    "X-Dgi-Req-Nonce": l,
    "X-Dgi-Req-Timestamp": a
};

function strrr(data) {
    var queryString = Object.entries(data)
    .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
    .join('&');
    return queryString
}


function t1(e={}) {
    const {p: t, t: n, n: u, k: o} = e
      , r = pne(t);
    return CryptoJS.SHA256(u + o + decodeURIComponent(r) + n)
}
function pne(e) {
    let t = "";
    return typeof e == "object" ? t = Object.keys(e).map(n=>`${n}=${e[n]}`).sort().join("&") : typeof e == "string" && (t = e.split("&").sort().join("&")),
    t
}

function main(data) {
    const p = t1({
        p: strrr(data),
        t: a,
        n: l,
        k: c
    });
    return [p.toString(),a,l]
}

console.log(main({
    "type": "trading-type",
    "openConvert": 'false',
    "keyword": "",
    "siteCode": "44",
    "secondType": "A",
    "tradingProcess": "",
    "thirdType": "[]",
    "projectType": "",
    "publishStartTime": "",
    "publishEndTime": "",
    "pageNo": 1,
    "pageSize": 10
}));