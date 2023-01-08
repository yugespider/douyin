var Cry = require('crypto-js')
// const t = (new Date).getTime();
var t= 1672748046145
function p(e) {
    return Cry.MD5(e).toString()
}

function b(e, t) {
    var r= 'fanyideskweb'
    var i = 'webfanyi'
    return p(`client=${r}&mysticTime=${e}&product=${i}&key=${t}`)
}


function sign(){
    var e = 'fsdsogkndfokasodnaso'
    return b(t, e)
}
function run(){
    return [sign(),t]
}




