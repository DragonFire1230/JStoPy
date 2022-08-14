import requests
import webbrowser
import time
import os

# Console from JS to Python
# Made by DragonFire
class console():
    def log(output):
        print(output)
        return "undefined"
    
    def error(output):
        print(output)
        return "undefined"
    
    def warn(output):
        print(output)
        return "undefined"
    
    def info(output):
        print(output)
        return "undefined"

    def debug(output):
        print(output)
        return "undefined"
    
    def trace(output):
        print(output)
        return "undefined"
    
    def clear():
        print("\n" * 100)
        return "undefined"






# Console from JS to Python
# Made by DragonFire
class XMLHttpRequest():
    def __init__(self):
        self.responseText = ""
        self.status = 0
        self.readyState = 0
        self.onreadystatechange = None
        self.onload = None
        self.onerror = None
        self.ontimeout = None
        self.timeout = 0
        self.responseType = ""
        self.responseURL = ""
        self.responseXML = ""
        self.response = ""
        self.responseText = ""
        self.responseJSON = ""
        self.responseArrayBuffer = ""
        self.responseBlob = ""
        self.responseStream = ""
        self.responseBodyUsed = False
        #self.upload = XMLHttpRequestUpload()
        self.upload = "TODO"
        self.withCredentials = False
        self.onprogress = None
        self.onabort = None
        self.onerror = None
        self.ontimeout = None
        self.onload = None
        self.onloadstart = None
        self.onloadend = None
        self.onprogress = None
        self.onreadystatechange = None
        self.onunload = None
    
    def open(self, method, url, isasync=True, user=None, password=None):
        self.method = method
        self.url = url
        self.isasync = isasync
        self.user = user
        self.password = password
        self.readyState = 1
        self.onreadystatechange()

        return "undefined"
    
    def setRequestHeader(self, header, value):
        self.headers[header] = value
        return "undefined"
    
    def send(self, data=None):
        if self.method == "GET":
            r = requests.get(self.url)
        elif self.method == "POST":
            r = requests.post(self.url, data=data)
        elif self.method == "PUT":
            r = requests.put(self.url, data=data)
        elif self.method == "DELETE":
            r = requests.delete(self.url, data=data)
        elif self.method == "HEAD":
            r = requests.head(self.url)
        elif self.method == "OPTIONS":
            r = requests.options(self.url)
        elif self.method == "PATCH":
            r = requests.patch(self.url, data=data)
        elif self.method == "TRACE":
            r = requests.trace(self.url)
        else:
            r = requests.get(self.url)
        
        self.status = r.status_code
        self.responseText = r.text
        self.responseXML = r.text
        self.responseJSON = r.json()
        self.responseArrayBuffer = r.content
        self.responseBlob = r.content
        self.responseStream = r.content
        self.responseBodyUsed = False
        self.readyState = 4
        self.onreadystatechange()
        self.onload()
        return "undefined"
    
    def abort(self):
        self.readyState = 0
        self.onreadystatechange()
        self.onerror()
        return "undefined"









# window from JS to Python
# Made by DragonFire
class window():
    def __init__(self):
        self.location = location()
        self.history = history()
        self.screen = screen()
        self.navigator = navigator()
        self.document = document()
        self.localStorage = localStorage()
        self.sessionStorage = sessionStorage()
        self.console = console()
        self.XMLHttpRequest = XMLHttpRequest()
        self.alert = alert
        self.confirm = confirm
        self.prompt = prompt
        self.open = open
        self.setTimeout = setTimeout
        self.clearTimeout = clearTimeout
        self.setInterval = setInterval
        self.clearInterval = clearInterval
        self.setImmediate = setImmediate
        self.clearImmediate = clearImmediate
        self.requestAnimationFrame = requestAnimationFrame
        self.cancelAnimationFrame = cancelAnimationFrame
        self.requestIdleCallback = requestIdleCallback
        self.cancelIdleCallback = cancelIdleCallback
        self.cancelAnimationFrame = cancelAnimationFrame
        self.cancelIdleCallback = cancelIdleCallback
        self.performance = performance()
        self.crypto = crypto()
        self.atob = atob
        self.btoa = btoa
        self.escape = escape
        self.unescape = unescape
        self.decodeURI = decodeURI
        self.decodeURIComponent = decodeURIComponent
        self.encodeURI = encodeURI
        self.encodeURIComponent = encodeURIComponent
        self.escape = escape
        self.unescape = unescape
        self.eval = eval
        self.isFinite = isFinite
        self.isNaN = isNaN
        self.parseFloat = parseFloat
        self.parseInt = parseInt
        self.Number = Number
        self.Math = Math
        self.Object = Object
        self.Function = Function
        self.Array = Array
        self.String = String
        self.Boolean = Boolean
        self.Date = Date
        self.RegExp = RegExp
        self.Error = Error
        self.EvalError = EvalError
        self.RangeError = RangeError
        self.ReferenceError = ReferenceError
        self.SyntaxError = SyntaxError
        self.TypeError = TypeError
        self.URIError = URIError
        self.JSON = JSON
        self.ArrayBuffer = ArrayBuffer
        self.DataView = DataView
        self.Int8Array = Int8Array
        self.Uint8Array = Uint8Array
        self.Uint8ClampedArray = Uint8ClampedArray
        self.Int16Array = Int16Array
        self.Uint16Array = Uint16Array
        self.Int32Array = Int32Array
        self.Uint32Array = Uint32Array
        self.Float32Array = Float32Array
        self.Float64Array = Float64Array
        self.console = console()
        self.atob = atob
        self.btoa = btoa
        self.escape = escape
        self.unescape = unescape
    
    def alert(self, msg):
        print(msg)
        return "undefined"
    
    def prompt(msg):
        return input(msg)

    def open(url):
        return webbrowser.open(url)
    
    def setTimeout(func, delay):
        time.sleep(delay)
        func()
    
    def clearTimeout(id):
        pass

    def setInterval(func, delay):
        while True:
            time.sleep(delay)
            func()

    def clearInterval(id):
        pass

class fs():
    def __init__(self):
        self.readFile = readFile
        self.writeFile = writeFile
        self.appendFile = appendFile
        self.readdir = readdir
        self.readdirSync = readdirSync
        self.readdirAsync = readdirAsync
        self.readFile = readFile
        self.readFileSync = readFileSync
        self.readFileAsync = readFileAsync
        self.writeFile = writeFile
        self.writeFileSync = writeFileSync
        self.writeFileAsync = writeFileAsync
        self.appendFile = appendFile
        self.appendFileSync = appendFileSync
        self.appendFileAsync = appendFileAsync
        self.unlink = unlink
        self.unlinkSync = unlinkSync
        self.unlinkAsync = unlinkAsync
        self.rmdir = rmdir
        self.rmdirSync = rmdirSync
        self.rmdirAsync = rmdirAsync
        self.mkdir = mkdir
        self.mkdirSync = mkdirSync
        self.mkdirAsync = mkdirAsync
        self.stat = stat
        self.statSync = statSync
        self.statAsync = statAsync
        self.lstat = lstat
        self.lstatSync = lstatSync
        self.lstatAsync = lstatAsync
        self.fstat = fstat
        self.fstatSync = fstatSync
        self.fstatAsync = fstatAsync
        self.rename = rename
        self.renameSync = renameSync
        self.renameAsync = renameAsync
        self.link = link
        self.linkSync = linkSync
        self.linkAsync = linkAsync
        self.symlink = symlink
        self.symlinkSync = symlinkSync
        self.symlinkAsync = symlinkAsync
        self.chmod = chmod
        self.chmodSync = chmodSync
        self.chmodAsync = chmodAsync
        self.chown = chown
        self.chownSync = chownSync
        self.chownAsync = chownAsync
        self.utimes = utimes
        self.utimesSync = utimesSync
        self.utimesAsync = utimesAsync
        self.truncate = truncate
        self.truncateSync = truncateSync
        self.truncateAsync = truncateAsync
        self.ftruncate = ftruncate
        self.ftruncateSync = ftruncateSync
        self.ftruncateAsync = ftruncateAsync
        self.copyFile = copyFile
        self.copyFileSync = copyFileSync
        self.copyFileAsync = copyFileAsync
        self.realpath = realpath
        self.realpathSync = realpathSync
        self.realpathAsync = realpathAsync
        self.stat = stat
    
    def readFile(self, path, encoding):
        with open(path, "r") as f:
            return f.read()
    
    def writeFile(self, path, data, encoding):
        with open(path, "w") as f:
            f.write(data)
    
    def appendFile(self, path, data, encoding):
        with open(path, "a") as f:
            f.write(data)

    def readdir(self, path):
        return os.listdir(path)
    
    def readdirSync(self, path):
        return os.listdir(path)

    def readdirAsync(self, path, callback):
        callback(os.listdir(path))

    def readFile(self, path, encoding):
        with open(path, "r") as f:
            return f.read()
    
    def readFileSync(self, path, encoding):
        with open(path, "r") as f:
            return f.read()
    
    def readFileAsync(self, path, encoding, callback):
        with open(path, "r") as f:
            callback(f.read())

    def writeFile(self, path, data, encoding):
        with open(path, "w") as f:
            f.write(data)

    def writeFileSync(self, path, data, encoding):
        with open(path, "w") as f:
            f.write(data)

    def writeFileAsync(self, path, data, encoding, callback):
        with open(path, "w") as f:
            f.write(data)

    def appendFile(self, path, data, encoding):
        with open(path, "a") as f:
            f.write(data)

    def appendFileSync(self, path, data, encoding):
        with open(path, "a") as f:
            f.write(data)

    def appendFileAsync(self, path, data, encoding, callback):
        with open(path, "a") as f:
            f.write(data)

    def unlink(self, path):
        os.remove(path)

    def unlinkSync(self, path):
        os.remove(path)
    
    def unlinkAsync(self, path, callback):
        os.remove(path)
        callback()

    def rmdir(self, path):
        os.rmdir(path)

    def rmdirSync(self, path):
        os.rmdir(path)

    def rmdirAsync(self, path, callback):
        os.rmdir(path)
        callback()

    def mkdir(self, path):
        os.mkdir(path)
    
    def mkdirSync(self, path):
        os.mkdir(path)

    def mkdirAsync(self, path, callback):
        os.mkdir(path)
        callback()

    def stat(self, path):
        return os.stat(path)

    def statSync(self, path):
        return os.stat(path)

    def statAsync(self, path, callback):
        callback(os.stat(path))

    def lstat(self, path):
        return os.lstat(path)

    def lstatSync(self, path):
        return os.lstat(path)

# require
def require(module):
    if module == "fs":
        return fs()
    else:
        raise Exception("Module not found")