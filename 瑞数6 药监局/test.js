delete __dirname
delete __filename


content =  "arg1_content"

function get_enviroment(proxy_array) {
    for (var i = 0; i < proxy_array.length; i++) {
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
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

'arg2_function';

require("./生成文件")

function go() {
    return document.cookie
}
console.log(document.cookie)