window = {}
JSEncrypt = require('jsencrypt')

function encrypt(pwd) {
    var pbk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCN0LdLeyGeIZdUGdxFeHmAjrinbVdXgFmrj+WwxTSrY3gigY1XivP5cBw8UCMzB6/R0UCXKCx3/Wru75AMEr6Bxfk9R15OLmbo0b/W8c0rmVN0cgSsT+JzRmeBzlAPoHJwrdooLqNXx1tuApQSwvxsGJC4zS68PeGSuxKUkJY0iwIDAQAB'
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pbk);
    password = encrypt.encrypt(pwd)
    return password
}
