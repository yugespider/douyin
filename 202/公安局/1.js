Crypto = require('crypto-js')
hash = {
    'sha256': function (a) {
        return Crypto.SHA256(a).toString()
    },
    'md5': function (a) {
        return Crypto.MD5(a).toString()
    },
    'sha1': function (a) {
        return Crypto.SHA1(a).toString()
    }
}
var _0x3cee67 = new Date();

function _0x3512b1(_0x52ce10, _0x1b93e1) {
    var _0x25a8a2 = _0x3c68ae['chars']['length'];
    for (var _0x114199 = 0; _0x114199 < _0x25a8a2; _0x114199++) {
        for (var _0x10f394 = 0; _0x10f394 < _0x25a8a2; _0x10f394++) {
            var _0x4ddac8 = ((_0x1b93e1[0] + _0x3c68ae['chars']['substr'](_0x114199, 1)) + _0x3c68ae['chars']['substr'](_0x10f394, 1)) + _0x1b93e1[1];
            if (hash[_0x3c68ae['ha']](_0x4ddac8) == _0x52ce10) {
                return [_0x4ddac8, (new Date() - _0x3cee67)];
            }
        }
    }
}

function run(a) {
    _0x3c68ae = JSON.parse(a)
    cookie = _0x3512b1(_0x3c68ae['ct'], _0x3c68ae['bts'])[0]
    return cookie
}

