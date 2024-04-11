window = global;
window.WebGLRenderingContext = function (params) {
    console.log("window.WebGLRenderingContext:",params)
}
canvas = {

}
document = {
    createElement:function (params) {
        if (params == "canvas"){
            return {
                getContext:function (params) {
                    if (params == "webgl"){
                        return {
                            canvas:canvas,
                            drawingBufferColorSpace: "srgb",
                            drawingBufferFormat: 32856,
                            drawingBufferHeight: 150,
                            drawingBufferWidth: 300,
                            unpackColorSpace: "srgb"
                        }
                    }
                }
            }
        }
        if (params == "span"){
            return {
                style:{}
            }
        }
        if (params == "div"){
            return {
                baseURI:"https://union.jd.com/proManager/index",
                nodeName:"DIV",
                localName:"div",
                namespaceURI:"http://www.w3.org/1999/xhtml",

            }
        }
    },
    body : {
        appendChild:function (params) {
            return params
        },
        removeChild:function (params) {
            console.log("document.body.removeChild:",params)
        }
    }
}
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    language: "zh-CN",
    languages: ['zh-CN'],
    product: "Gecko",
    productSub: "20030107",
    platform: "Win32",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    vendor: "Google Inc.",
    vendorSub: "",
    "vendorSub":"",
    "productSub":"",
    "vendor":"",
    "maxTouchPoints":"",
    "scheduling":"",
    "userActivation":"",
    "doNotTrack":"",
    "geolocation":"",
    "connection":"",
    "plugins":"",
    "mimeTypes":"",
    "pdfViewerEnabled":"",
    "webkitTemporaryStorage":"",
    "webkitPersistentStorage":"",
    "hardwareConcurrency":"",
    "cookieEnabled":"",
    "appCodeName":"",
    "appName":"",
    "appVersion":"",
    "platform":"",
    "product":"",
    "userAgent":"",
    "language":"",
    "languages":"",
    "onLine":"",
    "webdriver":"",
    "getGamepads":"",
    "javaEnabled":"",
    "sendBeacon":"",
    "vibrate":"",
    "deprecatedRunAdAuctionEnforcesKAnonymity":"",
    "bluetooth":"",
    "storageBuckets":"",
    "clipboard":"",
    "credentials":"",
    "keyboard":"",
    "managed":"",
    "mediaDevices":"",
    "storage":"",
    "serviceWorker":"",
    "virtualKeyboard":"",
    "wakeLock":"",
    "deviceMemory":"",
    "userAgentData":"",
    "login":"",
    "ink":"",
    "mediaCapabilities":"",
    "hid":"",
    "locks":"",
    "gpu":"",
    "mediaSession":"",
    "permissions":"",
    "presentation":"",
    "usb":"",
    "xr":"",
    "serial":"",
    "windowControlsOverlay":"",
    "adAuctionComponents":"",
    "runAdAuction":"",
    "canLoadAdAuctionFencedFrame":"",
    "canShare":"",
    "share":"",
    "clearAppBadge":"",
    "getBattery":"",
    "getUserMedia":"",
    "requestMIDIAccess":"",
    "requestMediaKeySystemAccess":"",
    "setAppBadge":"",
    "webkitGetUserMedia":"",
    "clearOriginJoinedAdInterestGroups":"",
    "createAuctionNonce":"",
    "deprecatedReplaceInURN":"",
    "deprecatedURNToURL":"",
    "getInstalledRelatedApps":"",
    "joinAdInterestGroup":"",
    "leaveAdInterestGroup":"",
    "updateAdInterestGroups":"",
    "registerProtocolHandler":"",
    "unregisterProtocolHandler":"",
    javaEnabled:function () {
        return false
    }
}

var ggg = {
    "pin": "",
    "oid": "",
    "bizId": "unionpc",
    "fc": "IDOVCSYM2M4CBRAATZG7L2UOZPXQ6FI6KRPCNQQTHXTSSHOOSBGTXL2OBJJ4IJJFAMB2DPLYCIKO2MXZQ66HLRTVKM",
    "mode": "strict",
    "p": "s",
    "fp": "f21378699ce23d536684af82263bf7fb",
    "ctype": 1,
    "v": "3.1.1.0",
    "f": "1",
    "o": "union.jd.com/proManager/index",
    "qs": "",
    "jsTk": "jdd03IDOVCSYM2M4CBRAATZG7L2UOZPXQ6FI6KRPCNQQTHXTSSHOOSBGTXL2OBJJ4IJJFAMB2DPLYCIKO2MXZQ66HLRTVKMAAAAMOVXU4H6YAAAAADU3MV3JJJW6FTUX",
    "qi": ""
}
var collectConfig = {
    "fp": {
        "language": "language",
        "userAgent": "userAgent",
        "colorDepth": "colorDepth",
        "screenResolution": "screenResolution",
        "timezoneOffset": "timezoneOffset",
        "sessionStorage": "sessionStorage",
        "localStorage": "localStorage",
        "indexedDb": "indexedDb",
        "addBehavior": "addBehavior",
        "openDatabase": "openDatabase",
        "cpuClass": "cpuClass",
        "platform": "platform",
        "hardwareConcurrency": "hardwareConcurrency",
        "audioKey": "audioKey",
        "doNotTrack": "doNotTrack",
        "plugins": "plugins",
        "canvas": "canvas",
        "webgl": "webgl"
    },
    "env": {
        "color": "color",
        "canvas": "canvas",
        "browserMode": "browserMode",
        "fonts": "fonts",
        "feature": "feature",
        "plugins": "plugins",
        "screen": "screen",
        "position": "position",
        "storeCheck": "storeCheck"
    },
    "store": {
        "giaDKey": "_gia_d",
        "canvasFpKey": "CA1AN5BV0CA8DS2EPC",
        "ldeKey": "GIA_LDE_MAP_KEY",
        "strict": {
            "jsTokenKey": "3AB9D23F7A4B3CSS",
            "fpKey": "PCA9D23F7A4B3CSS",
            "fpTsKey": "PCTSD23F7A4B3CSS",
            "eidKey": "3AB9D23F7A4B3C9B"
        },
        "fast": {
            "jsTokenKey": "3AB9D23F7A4B3CFF",
            "fpKey": "PCA9D23F7A4B3CFF",
            "fpTsKey": "PCTSD23F7A4B3CFF",
            "eidKey": "3AB9D23F7A4B3CFF"
        }
    }
}
var jdtRiskContext = {
    "d": false,
    "canvas_fp_md5": "",
    "isJsTokenFinished": false,
    "version": "3.1.1.0",
    "deviceInfo": {
        "jsToken": "jdd03IDOVCSYM2M4CBRAATZG7L2UOZPXQ6FI6KRPCNQQTHXTSSHOOSBGTXL2OBJJ4IJJFAMB2DPLYCIKO2MXZQ66HLRTVKMAAAAMOVXU4H6YAAAAADU3MV3JJJW6FTUX",
        "eid": "",
        "fp": "f21378699ce23d536684af82263bf7fb"
    }
}
TDEnvCollector = function(l) {
    function m(g) {
        var f = {};
        f.name = g.name;
        f.filename = g.filename.toLowerCase();
        f.description = g.description;
        void 0 !== g.version && (f.version = g.version);
        f.mimeTypes = [];
        for (var d = 0; d < g.length; d++) {
            var a = g[d]
              , b = {};
            b.description = a.description;
            b.suffixes = a.suffixes;
            b.type = a.type;
            f.mimeTypes.push(b)
        }
        return f
    }
    l = l || {};
    var n = function() {
        return {
            execute: function(g) {
                if (this[g]) {
                    var f = (new Date).getTime()
                      , d = this[g]();
                    jdtRiskContext.d && console.log("ENV Collector function : [" + g + "] Cost time :", (new Date).getTime() - f);
                    return d
                }
            },
            getColorRgb: function() {
                var g = {};
                try {
                    var f = document.createElement("div")
                      , d = "ActiveBorder ActiveCaption AppWorkspace Background ButtonFace ButtonHighlight ButtonShadow ButtonText CaptionText GrayText Highlight HighlightText InactiveBorder InactiveCaption InactiveCaptionText InfoBackground InfoText Menu MenuText Scrollbar ThreeDDarkShadow ThreeDFace ThreeDHighlight ThreeDLightShadow ThreeDShadow Window WindowFrame WindowText".split(" ");
                    if (window.getComputedStyle)
                        for (var a = 0; a < d.length; a++)
                            document.body.appendChild(f),
                            f.style.color = d[a],
                            g[d[a]] = window.getComputedStyle(f).getPropertyValue("color"),
                            document.body.removeChild(f)
                } catch (b) {}
                return g
            },
            getCanvasInfo: function() {
                var g = {};
                g.tdHash = jdtRiskContext.canvas_fp_md5 || load(collectConfig.store.canvasFpKey, !1);
                var f = !1;
                if (window.WebGLRenderingContext) {
                    for (var d = ["webgl", "experimental-webgl", "moz-webgl", "webkit-3d"], a = [], b, e = 0; e < d.length; e++)
                        var c = !1;
                        (c = document.createElement("canvas").getContext(d[e], {
                            stencil: !0
                        })) && c && (b = c,
                        a.push(d[e]))
                    a.length && (f = {
                        name: a,
                        gl: b
                    })
                }
                if (f) {
                    d = f.gl;
                    g.contextName = f.name.join();
                    g.webglversion = d.getParameter(d.VERSION);
                    g.shadingLV = d.getParameter(d.SHADING_LANGUAGE_VERSION);
                    g.vendor = d.getParameter(d.VENDOR);
                    g.renderer = d.getParameter(d.RENDERER);
                    f = [];
                    try {
                        f = d.getSupportedExtensions(),
                        g.extensions = f
                    } catch (k) {}
                    try {
                        var h = d.getExtension("WEBGL_debug_renderer_info");
                        h && (g.wuv = d.getParameter(h.UNMASKED_VENDOR_WEBGL),
                        g.wur = d.getParameter(h.UNMASKED_RENDERER_WEBGL))
                    } catch (k) {}
                }
                return g
            },
            getBrowserMode: function() {
                return {
                    documentMode: document.documentMode,
                    compatMode: document.compatMode
                }
            },
            getSupportFonts: function() {
                function g(p) {
                    var q = {};
                    c.style.fontFamily = p;
                    document.body.appendChild(c);
                    q.height = c.offsetHeight;
                    q.width = c.offsetWidth;
                    document.body.removeChild(c);
                    return q
                }
                function f(p) {
                    for (var q = 0; q < e.length; q++) {
                        var t = g(p + "," + b[q])
                          , u = e[q];
                        if (t.height !== u.height || t.width !== u.width)
                            return !0
                    }
                    return !1
                }
                var d = []
                  , a = "Abadi MT Condensed Light;Adobe Fangsong Std;Adobe Hebrew;Adobe Ming Std;Agency FB;Arab;Arabic Typesetting;Arial Black;Batang;Bauhaus 93;Bell MT;Bitstream Vera Serif;Bodoni MT;Bookman Old Style;Braggadocio;Broadway;Calibri;Californian FB;Castellar;Casual;Centaur;Century Gothic;Chalkduster;Colonna MT;Copperplate Gothic Light;DejaVu LGC Sans Mono;Desdemona;DFKai-SB;Dotum;Engravers MT;Eras Bold ITC;Eurostile;FangSong;Forte;Franklin Gothic Heavy;French Script MT;Gabriola;Gigi;Gisha;Goudy Old Style;Gulim;GungSeo;Haettenschweiler;Harrington;Hiragino Sans GB;Impact;Informal Roman;KacstOne;Kino MT;Kozuka Gothic Pr6N;Lohit Gujarati;Loma;Lucida Bright;Lucida Fax;Magneto;Malgun Gothic;Matura MT Script Capitals;Menlo;MingLiU-ExtB;MoolBoran;MS PMincho;MS Reference Sans Serif;News Gothic MT;Niagara Solid;Nyala;Palace Script MT;Papyrus;Perpetua;Playbill;PMingLiU;Rachana;Rockwell;Sawasdee;Script MT Bold;Segoe Print;Showcard Gothic;SimHei;Snap ITC;TlwgMono;Tw Cen MT Condensed Extra Bold;Ubuntu;Umpush;Univers;Utopia;Vladimir Script;Wide Latin".split(";")
                  , b = ["monospace", "sans-serif", "serif"]
                  , e = []
                  , c = document.createElement("span");
                c.style.fontSize = "72px";
                c.style.visibility = "hidden";
                c.innerHTML = "mmmmmmmmmmlli";
                for (var h = 0; h < b.length; h++)
                    e[h] = g(b[h]);
                for (h = 0; h < a.length; h++) {
                    var k = a[h];
                    f(k) && d.push(k)
                }
                return d
            },
            getFeature: function() {
                var g = {}, f = [], d;
                for (d in navigator)
                    "object" != typeof navigator[d] && (g[d] = navigator[d]),
                    f.push(d);
                g.enumerationOrder = f;
                g.javaEnabled = navigator.javaEnabled();
                try {
                    g.taintEnabled = navigator.taintEnabled()
                } catch (a) {}
                return g
            },
            getPlugins: function() {
                var g = [], f = "4game;AdblockPlugin;AdobeExManCCDetect;AdobeExManDetect;Alawar NPAPI utils;Aliedit Plug-In;Alipay Security Control 3;AliSSOLogin plugin;AmazonMP3DownloaderPlugin;AOL Media Playback Plugin;AppUp;ArchiCAD;AVG SiteSafety plugin;Babylon ToolBar;Battlelog Game Launcher;BitCometAgent;Bitdefender QuickScan;BlueStacks Install Detector;CatalinaGroup Update;Citrix ICA Client;Citrix online plug-in;Citrix Receiver Plug-in;Coowon Update;DealPlyLive Update;Default Browser Helper;DivX Browser Plug-In;DivX Plus Web Player;DivX VOD Helper Plug-in;doubleTwist Web Plugin;Downloaders plugin;downloadUpdater;eMusicPlugin DLM6;ESN Launch Mozilla Plugin;ESN Sonar API;Exif Everywhere;Facebook Plugin;File Downloader Plug-in;FileLab plugin;FlyOrDie Games Plugin;Folx 3 Browser Plugin;FUZEShare;GDL Object Web Plug-in 16.00;GFACE Plugin;Ginger;Gnome Shell Integration;Google Earth Plugin;Google Earth Plug-in;Google Gears 0.5.33.0;Google Talk Effects Plugin;Google Update;Harmony Firefox Plugin;Harmony Plug-In;Heroes & Generals live;HPDetect;Html5 location provider;IE Tab plugin;iGetterScriptablePlugin;iMesh plugin;Kaspersky Password Manager;LastPass;LogMeIn Plugin 1.0.0.935;LogMeIn Plugin 1.0.0.961;Ma-Config.com plugin;Microsoft Office 2013;MinibarPlugin;Native Client;Nitro PDF Plug-In;Nokia Suite Enabler Plugin;Norton Identity Safe;npAPI Plugin;NPLastPass;NPPlayerShell;npTongbuAddin;NyxLauncher;Octoshape Streaming Services;Online Storage plug-in;Orbit Downloader;Pando Web Plugin;Parom.TV player plugin;PDF integrado do WebKit;PDF-XChange Viewer;PhotoCenterPlugin1.1.2.2;Picasa;PlayOn Plug-in;QQ2013 Firefox Plugin;QQDownload Plugin;QQMiniDL Plugin;QQMusic;RealDownloader Plugin;Roblox Launcher Plugin;RockMelt Update;Safer Update;SafeSearch;Scripting.Dictionary;SefClient Plugin;Shell.UIHelper;Silverlight Plug-In;Simple Pass;Skype Web Plugin;SumatraPDF Browser Plugin;Symantec PKI Client;Tencent FTN plug-in;Thunder DapCtrl NPAPI Plugin;TorchHelper;Unity Player;Uplay PC;VDownloader;Veetle TV Core;VLC Multimedia Plugin;Web Components;WebKit-integrierte PDF;WEBZEN Browser Extension;Wolfram Mathematica;WordCaptureX;WPI Detector 1.4;Yandex Media Plugin;Yandex PDF Viewer;YouTube Plug-in;zako".split(";"), d = navigator.userAgent.toLowerCase(), a;
                if (a = d.match(/rv:([\d.]+)\) like gecko/))
                    var b = a[1];
                if (a = d.match(/msie ([\d.]+)/))
                    b = a[1];
                if (b)
                    for (d = "AcroPDF.PDF;Adodb.Stream;AgControl.AgControl;DevalVRXCtrl.DevalVRXCtrl.1;MacromediaFlashPaper.MacromediaFlashPaper;Msxml2.DOMDocument;Msxml2.XMLHTTP;PDF.PdfCtrl;QuickTime.QuickTime;QuickTimeCheckObject.QuickTimeCheck.1;RealPlayer;RealPlayer.RealPlayer(tm) ActiveX Control (32-bit);RealVideo.RealVideo(tm) ActiveX Control (32-bit);rmocx.RealPlayer G2 Control;Scripting.Dictionary;Shell.UIHelper;ShockwaveFlash.ShockwaveFlash;SWCtl.SWCtl;TDCCtl.TDCCtl;WMPlayer.OCX".split(";"),
                    b = 0; b < d.length; b++) {
                        var e = d[b];
                        try {
                            var c = new ActiveXObject(e);
                            a = {};
                            a.name = e;
                            try {
                                a.version = c.GetVariable("$version")
                            } catch (h) {}
                            try {
                                a.version = c.GetVersions()
                            } catch (h) {}
                            a.version && 0 < a.version.length || (a.version = "");
                            g.push(a)
                        } catch (h) {}
                    }
                else {
                    d = navigator.plugins;
                    a = {};
                    for (b = 0; b < d.length; b++)
                        e = d[b],
                        a[e.name] = 1,
                        g.push(m(e));
                    for (b = 0; b < f.length; b++)
                        c = f[b],
                        a[c] || (e = d[c],
                        e && g.push(m(e)))
                }
                return g
            },
            getScreenInfo: function() {
                for (var g = {}, f = "availHeight availWidth colorDepth bufferDepth deviceXDPI deviceYDPI height width logicalXDPI logicalYDPI pixelDepth updateInterval".split(" "), d = 0; f.length > d; d++) {
                    var a = f[d];
                    void 0 !== screen[a] && (g[a] = screen[a])
                }
                return g
            },
            getPositionInfo: function() {
                for (var g = {}, f = ["devicePixelRatio", "screenTop", "screenLeft"], d = 0; f.length > d; d++) {
                    var a = f[d];
                    void 0 !== window[a] && (g[a] = window[a])
                }
                return g
            },
            getStoreCheck: function() {
                var g = {};
                try {
                    g.cookie = navigator.cookieEnabled,
                    g.localStorage = !!window.localStorage,
                    g.sessionStorage = !!window.sessionStorage,
                    g.globalStorage = !!window.globalStorage,
                    g.indexedDB = !!window.indexedDB
                } catch (f) {}
                return g
            }
        }
    }();
    return {
        getEncryptedCollectInfo: function() {
            var g = l;
            g = g || {};
            var f = {}
              , d = new Date;
            f.ts = {};
            f.ts.deviceTime = d.getTime();
            g[collectConfig.env.canvas] || (f.ca = n.execute("getCanvasInfo") || {});
            g[collectConfig.env.browserMode] || (f.m = n.execute("getBrowserMode") || {});
            g[collectConfig.env.fonts] || (f.fo = n.execute("getSupportFonts") || []);
            g[collectConfig.env.feature] || (f.n = n.execute("getFeature") || {});
            g[collectConfig.env.plugins] || (f.p = n.execute("getPlugins") || []);
            g[collectConfig.env.position] || (f.w = n.execute("getPositionInfo") || {});
            g[collectConfig.env.screen] || (f.s = n.execute("getScreenInfo") || {});
            g[collectConfig.env.color] || (f.sc = n.execute("getColorRgb") || {});
            g[collectConfig.env.storeCheck] || (f.ss = n.execute("getStoreCheck") || {});
            f.tz = d.getTimezoneOffset();
            f.lil = "";
            f.wil = "";
            f.ts.deviceEndTime = (new Date).getTime();
            jdtRiskContext.d && console.log("collect env data :", f);
            return TDEncrypt(f)
        }
    }
};
var screen = {
    availHeight: 864,
    availLeft: 0,
    availTop: 0,
    availWidth: 1472,
    colorDepth: 24,
    height: 864,
    isExtended: false,
    onchange: null,
    orientation:  {angle: 0, type: 'landscape-primary', onchange: null},
    pixelDepth:24,
    width:1536
}
function load(m, n, g) {
    "undefined" == typeof n && (n = !0);
    g = g || function(d) {
        return !!d
    }
    ;
    var f = null;
    if (n)
        try {
            if (f = jdtRiskCookieManager.getCookie(m),
            g(f))
                return f
        } catch (d) {}
    try {
        if (f = jdtLocalStorageManager.get(m),
        g(f))
            return f
    } catch (d) {}
    try {
        if (window.sessionStorage && (f = window.sessionStorage(m),
        g(f)))
            return f
    } catch (d) {}
    try {
        if (window.globalStorage && (f = window.globalStorage[".localdomain"](m),
        g(f)))
            return f
    } catch (d) {}
    return f
}

function TDEncrypt(m) {
    m = JSON.stringify(m);
    m = encodeURIComponent(m);
    var n = ""
      , g = 0;
    do {
        var f = m.charCodeAt(g++);
        var d = m.charCodeAt(g++);
        var a = m.charCodeAt(g++);
        var b = f >> 2;
        f = (f & 3) << 4 | d >> 4;
        var e = (d & 15) << 2 | a >> 6;
        var c = a & 63;
        isNaN(d) ? e = c = 64 : isNaN(a) && (c = 64);
        n = n + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(b) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(f) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(e) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(c)
    } while (g < m.length);
    return n + "/"
}
function getEnvExcludeOptions(l) {
    if ("strict" == l)
        return {};
    if ("fast" == l)
        return l = {},
        l[this.env.color] = !0,
        l[this.env.fonts] = !0,
        l
}


function main() {
    var a = TDEncrypt(ggg)
    var b = (new TDEnvCollector(getEnvExcludeOptions("strict"))).getEncryptedCollectInfo()
    return [a,b]
}

