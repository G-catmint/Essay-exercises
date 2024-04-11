content = "CdpgHDkhyEkLDUo1vYOB_PpaoGqWHcgRFAkPxPh8rWdSIiW7BQB1lPgmlkYyjuxT"

function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof  7666target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        console.log("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
            + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}
proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'aaa', 'target']


window = global
window.top = window
window.addEventListener = function () {}
window.name = ''
window.self = window

div = {
    getElementsByTagName: function () {
        return {length: 0}
    }
}
script = {
    0: {
        type:"text/javascript"
    },
    1: {
        type:"text/javascript",
        charset:"utf-8"
    }
}
meta = {
    0: {
        content: "text/html; charset=utf-8",
        http_Equiv: "Content-Type",
        getAttribute: function (arg) {
            if (arg === 'r') {
                return 'm'
            }
        },
        parentNode: {
            removeChild: function () {}
        }
    },
    1: {
        content: content,
        getAttribute: function (arg) {
            if (arg === 'r') {
                return 'm'
            }
        },
        parentNode: {
            removeChild: function () {}
        },
        parentElement: {
            removeChild: function () {}
        }
    },
    length: 2
}
form={}
base = {length: 0}

document = {
    createElement: function (arg) {
        console.log('document的createElement:', arg)
        if (arg === 'div') {
            return div
        }
        if (arg === 'a') {
            return {length:0}
        }
        if(arg==='form'){
            return form
        }


    },
    getElementsByTagName: function (arg) {
        console.log('document的getelementsbytagname:', arg)
        if (arg === 'script') {
            return script
        }
        if (arg === 'meta') {
            return meta
        }
        if (arg === 'base') {
            return base
        }

    },
    getElementById: function (arg) {
        console.log(arg)
        if (arg === 'root-hammerhead-shadow-ui') {
            return null
        }
    },
    documentElement: {
        addEventListener: function () {}
    },
    visibilityState:'visible'
}
document.appendChild = function () {
}
document.removeChild = function () {
}
document.addEventListener = function (arg) {
}


navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    webkitPersistentStorage: {},
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    language: "zh-CN",
    webdriver: false,
    languages: ['zh-CN'],
    platform:'Win32',
    productSub:"20030107",
    product:"Gecko",
    vendor:"Google Inc.",
    connection:{
        downlink:5.2,
        effectiveType:"4g",
        onchange:null,
        rtt:100,
        saveData:false
    }
}


location = {
    "ancestorOrigins": {},
    "href": "https://www.nmpa.gov.cn/",
    "origin": "https://www.nmpa.gov.cn",
    "protocol": "https:",
    "host": "www.nmpa.gov.cn",
    "hostname": "www.nmpa.gov.cn",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}


window.document = document
window.navigator = navigator
window.location = location

window.clientInformation=navigator

setTimeout = function () {}
setInterval = function () {}

get_enviroment(proxy_array)

$_ts=window['$_ts'];if(!$_ts)$_ts={};$_ts.nsd=51613;$_ts.cd="qWRqrpAltaEqDGWFqr93qGqFrfLoDpGcqq9qcqEqDGAFrp93DGqRHaVcJfLDcs3YtGaErcWcqrLkDO3RDqEqDG3FrS93qGqFrpL0DpGcqrLqDGlRDrLDkq9llfLmxGVFqr9drAEqDG3FrnZ3qGqFrpLcDpGcqrLqDGlBDq3mkqLlxGEqDGEFqS93JqqxJG7cqrLqDGlRDqEqDOlFrr93qGqFqG9Cm1LWcaA.qGqFrSLlDpGFqS9drqEqhqlFrf93DGVRHaEFiaa9vqlCWAEmWOKQEeSa7ntVbEkBun6Egc5SDEnLmLyD182sp6nn.z8bugw0qqAuraArv1aEcm2ZxODLw9YbKuYKA5Nzpb22MbYbykwLY9W2H2.nwbSNhb2SMIqBMvrXFnfB_Ke7tKSnFDCaMUYNM2LLE_ToJlSBYTwXNKpyRCYPFDPzwu2PWb3biZwzwK2XtCN0ZDZ7F6w.Fc6nwbSNhb2SMIqBMvrXFT9zBOr.s9rSVsOxhUwwQm3SiHYA1lA_QVWON2fXQDy.tDdNMCaNMoxLMMrzwK2XtCN0ZDZ7F6w.FmnaEsYqiOp2WezTMDpaYTRsNDy.3lr5UVc5iYz.wCzLhIxCMD9XFUmzZceXQDy.tDdNMCaNMoxLMQlBEOJpQ2ri.OmBJYflsYhzwleG3Tx0QJ7fi2y7Qbfz7DTTFKg.FvsaMnS.wCzLhIxCMD9XFUmzZmg7xuYWwokLY6mQJYx5wwfh39L4QVz2e0EPHT2NQK6ahCyaMb7LM52BMc27Qbfz7DTTFKg.FvsaMT0NEkeK8HfK1kr.MuxtSlpKIDRzMV.KK0QvimSjwHrBhDz6FCGzZvR7F1yNQK6ahCyaMb7LM52BMmGXxsTPaTJVRTRHp6hn8sY0ibf7Q5NL3bAGHYeB_Ke7tKSnFDCaMUYNMPzjwHrBhDz6FCGzZvR7FYZ.x9hFMV2bRTTxpe2E8spOAkrg0sNVsUW2H2.nwbSNhb2SMIqBMvrXFnfB_Ke7tKSnFDCaMUYNM2LLEeevAsps1Dxkn0Ra3VZNUUIiR6fSYK3biZwzwK2XtCN0ZDZ7F6w.Fc6nwbSNhb2SMIqBMvrXFT9zB9rjAvVTwVuxJVVuJTTwR5RoK2R1tVVON2fXQDy.tDdNMCaNMoxLMMrzwK2XtCN0ZDZ7F6w.FmnaEVGZ3mmopHwnJml_1V2JZVN.AuWaVKc5iYz.wCzLhIxCMD9XFUmzZceXQDy.tDdNMCaNMoxLMQlBE9TfwbSx_vrKYKSiwDk0RDzDibyEiH0fi2y7Qbfz7DTTFKg.FvsaMnS.wCzLhIxCMD9XFUmzZmg7x07dJbdtpC2KRkxZFzwRYTx4FnNk.vEPHT2NQK6ahCyaMb7LM52BMc27Qbfz7DTTFKg.FvsaMT0NElyn1BzcWm0nYCrDeo9gsbebRTb7YblvimSjwHrBhDz6FCGzZvR7F1yNQK6ahCyaMb7LM52BMmGXxYp.TbECA2JKQoIeJ2NLYKxZWIx.MDAGHYeB_Ke7tKSnFDCaMUYNMPzjwHrBhDz6FCGzZvR7FYZ.x2ksRoJtMuwth53_1vewQ2Rc72a0JUW2H2.nwbSNhb2SMIqBMvrXFnfB_Ke7tKSnFDCaMUYNM2LLEZyTA9RtHupz.kznMDJiVl6eR2rqF93biZwzwK2XtCN0ZDZ7F6w.Fc6nwbSNhb2SMIqBMvrXFT9zB2rssuzVRVBChsfCi0e21jVasuJoJlVON2fXQDy.tDdNMCaNMoxLMMrzwK2XtCN0ZDZ7F6w.FmnaEYJ.sKT2RzpJVUYuWYxld9paIkx9Mbc5iYz.wCzLhIxCMD9XFUmzZceXQDy.tDdNMCaNMoxLMQlBE2mFFTW6SvzfMbaNF6O0JkmxUVxEKI0fi2y7Qbfz7DTTFKg.FvsaMnS.wCzLhIxCMD9XFUmzZmg7xCrcVK45FvYOwUlCFZ2T32pHVKwSnvEPHT2NQK6ahCyaMb7LM52BMc27Qbfz7DTTFKg.FvsaMT0NEDE01XS2iD7_RDzCjbr3pkJ9p6vdsVlvimSjwHrBhDz6FCGzZvR7F1yNQK6ahCyaMb7LM52BMmGXxKmUCKf6WVTHU9kdpTevs2wiptSGW9AGHYeB_Ke7tKSnFDCaMUYNMPzjwHrBhDz6FCGzZvR7FYZ.xbIX1YmiwOpe18pM1oA7Q0zg7OxVVVV2H2.nwbSNhb2SMIqBMvrXFnfB_Ke7tKSnFDCaMUYNM2LLEdz4ssTpWTyBCmS.MUm6wcd.10TsJlqbiZwzwK2XtCN0ZDZ7F6w.Fc6nwbSNhb2SMIqBMvrXFT9zBbNcpOASR0uJ19N6MOqZM_yBsUZupbVON2fXQDy.tDdNMCaNMoxLMMrzwK2XtCN0ZDZ7F6w.FmnaEK2Iiupt8FeJWPzWMvxja0YXs9eqMUc5iYz.wCzLhIxCMD9XFUmzZceXQDy.tDdNMCaNMoxLMQlBEbZ_ICm0Z6R2AOW0WmInYDzDK2rAhe0fi2yRUc3X_CRPtbJ6wc4eQC9jw6pfQeebMvmvw1zzeKr2F6mPYUHIMDpGhKJf3Xy_Qom1RvRGZUqPtURTQKsrhT7vhUrf34JPQoVzRvpL76Ru3orl3KdLRvEjMbyvRHxaR1N23vrJeKr2F6mP1DOBwnENwvYSRWm8hDz6FCGzZvR7F1yNQK6ahCyaMb7LM52BMmGXxKeLe0Y9wVmPVCuFYVyNsCaaQtpYRUAGHYeB_Ke7tKSnFDCaMUYNMPzjwHrBhDz6FCGzZvR7FYZ.xb6k8Vz9WbSvQzYh89SqJ9SanOJoQvW2H2.nwbSNhb2SMIqBMvrXFnfB_Ke7tKSnFDCaMUYNM2LLEdJnFYwUUvx25TxWwvwX3KuWAVYDFb3biZwzwK2XtCN0ZDZ7F6w.Fc6nwbSNhb2SMIqBMvrXFT9zBvpY3lSrRbXnRKmzJTRe1IY0sOSxpKVON2fXQDy.tDdNMCaNMoxLMMrzwK2XtCN0ZDZ7F6w.FmnaEUNQiuxMMXTDFOp9H0zT0CmDtTmeR9c5iYz.wCzLhIxCMD9XFUmzZceXQDy.tDdNMCaNMoxLMQm5hDz6FCfQ2GEiRby9JvhYFK35JYRD1QpE3YZy39fASorkIkVZ1OvTpCSa1D9d85YYQsJ9JDV_0bYcp2mXFvtXso2niKm0QWTSR0ET1uxSZufOsvYupTUF80pxYYWdRHTE1bwiAOTO4KSbtuq5WDhdiuW.FoAdWt21QKmFH2QCZ9wmtuq5WDhdiuW.FoAdYBZuYVxlVDS.ylpHtuq5WDhdiuW.FoAds7SHJTRiRKWS.YNgtCf0H6vYJVNEWDRfQzwAwsgSR92guDmnRCY.QTPvWDNORve1pzzYKlJzHDW6ely_wvNBMmhF31g6iuJv3jAahbeSHmTl_0SAMbzXWuMgKng6iuJv3jAahbeSHcLuNswOROL0tbBBqaqmquQlqt0klCTCQ6pnNO7SWOV5Ws1BJuLSJOAlr_g_JDRfHaAcjOA0rAGCJkbBJkqCWkgnqRG6Wka0rSA1q5.3UWlWeysU0y5sMFGgq3uOy.zWpWoUFatQrGEcrGF3qnqvmiTQcUMcct6qxpiHN4gMqM8JcN6u.kNUqH9lAvcwGAVEJkQn.k7nWsWdWADwWGqHWuq0W_g_WklTWqAj6sroQ6N.tb.xFTrGsl2xJzzPKvSTWOpH4ULaslm33KMIJkrApKx7MFYQRaVcraVTvqEarAWarOD.81S93CAL3HmShDpnMcfG4Cg7RopXtDHeFcSv36WL3dYzhDwBwnfOyOl7RPy9RKia3DeLhbp0QMrGQ63XRow67DwfQ1yOFDCaRCebhbJ.3XABRDNCtCr75ne2FDg.3K4LhCYeRnzPMI0BRb2ftCxz_PebFba.3b4nwnSOMUWLRBffhDxjFcfbeKV73vG.MD67hCfTQPz7wIZBFKRztCTB5PeNFC7.MKdBhC2T3nzzQBWBFbpatCyG_bE7M6xP3n6CQCQNFoALF5e7MP2XMb3zZDSvtKZuR16S3vqNMCyGhImjM12BMoEzZKS9tKeLQP6SQuWNM6QahImu312BwCmb7Dya3PyjwoDaMvJ7hbfbF4r7360XFDJb7DS7RnyLFD1aMopOhbfn3hru3U3XwCwG4cea3KA.wDMSh6r731z0MIVBQD2.woqz4DTvtUx6F167Q6WNQvwah8Suwo0Xw6w27oJytUx5Rn6zFb3NQ6JZh8TGM6Eat6RG7omfFcyTRUiaQKYPhvYfQ.rSM12aFvxO7om03nyTQDu7h6JvMPz6R5ABQCLXwoxb7or6Rcy0QC8aQo2ChvJ2Q4r63UZXQCJ47owN3nyuMKI_h6pjQoYfM5GBwom9t6ry_ceCwb3.QvhBh6RCw1zn8IGBwCp0t6J9dvW7QbebtoMSw1SnMKmPh8z7RbWat6JS4ne63Drjtov5MPSeMvAL8Ira8c2_FbGzyoJztUN0Fc6981SdhvTzQRakqqmwEClyvqwIEKRlrqUkxC90qGJMxINKqqQSJGAkjuEqrkWorsq";if($_ts.lcd)$_ts.lcd();

require("./生成文件")

console.log(document.cookie)
console.log(document.cookie.split(";")[0].split("=")[1].length)


