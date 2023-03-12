// npm install node-rsa --save
// var NodeRSA = require('node-rsa');
// function rsaEncrypt(text,publicKey) {
//     pubKey = new NodeRSA({b: 1024},publicKey,'pkcs8-public');
//     var encryptedData = pubKey.encrypt(text, 'base64');
//     return encryptedData
// }
//
// var publicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQComqoAyvbCqO1EGsADwfNTWFQIUbm8CLdeb9TgjGLcz95mAo204SqTYdSEUxFsOnPfROOTxhkhfjbRxBV4/xjS06Y+kkUdiMGFtABIxRQHQIh0LrVvEZQs4NrixxcPI+b1bpE0gO/GAFSNWm9ejhZGj7UnqiHphnSJAVQNz2lgowIDAQAB'
// var text = "123456"
// var encrypt = rsaEncrypt(text,publicKey)
// // var decryptedData = rsaDecrypt()
// console.log(encrypt)

window = {}
var JSEncrypt = require('jsencrypt')
var pwd = '123456'
var publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQComqoAyvbCqO1EGsADwfNTWFQIUbm8CLdeb9TgjGLcz95mAo204SqTYdSEUxFsOnPfROOTxhkhfjbRxBV4/xjS06Y+kkUdiMGFtABIxRQHQIh0LrVvEZQs4NrixxcPI+b1bpE0gO/GAFSNWm9ejhZGj7UnqiHphnSJAVQNz2lgowIDAQAB";
var encrypt = new JSEncrypt();
encrypt.setPublicKey(publicKey);
var pwd2 = encrypt.encrypt(pwd);
console.log(pwd2);

