CryptoJS = require('crypto-js')

// var aa =['http:', '', 'ggzy.zwfwb.tj.gov.cn:80', 'jyxxcggg', '1006631.jhtml']
// var ccc = '1006631'

function encrypt(ccc,aa){
    var aaa = aa.length;
    var bbb = aa[aaa - 1].split('.');
    var s = 'qnbyzzwmdgghmcnm'
    var srcs = CryptoJS.enc.Utf8.parse(ccc);
    var k = CryptoJS.enc.Utf8.parse(s);
    var en = CryptoJS.AES.encrypt(srcs, k, {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
    });
    var ddd = en.toString();
    ddd = ddd.replace(/\//g, "^");
    ddd = ddd.substring(0, ddd.length - 2);
    var bbbb = ddd + '.' + bbb[1];
    aa[aaa - 1] = bbbb;
    var uuu = '';
    for (i = 0; i < aaa; i++) {
    uuu += aa[i] + '/'
    }
    uuu = uuu.substring(0, uuu.length - 1)
    return uuu
}

// console.log(encrypt(ccc, aa));