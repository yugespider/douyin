var _ = ''
var d = 'xyz517cda96abcd'

function o(n) {
    t = _,
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function (n) {
            t += unescape('%u00' + n)
        });
    var t, e = t;
    return String[e](n)
}

function h(n, t) {
    t = t || u();
    for (var e = (n = n['split'](_))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n['join'](_)
}

function v(t) {
    t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function (n, t) {
        return o('0x' + t)
    });

    return btoa(t)

}

function parmA(brand, device) {
    // var a = ['free', 'ipad', 'cn', '36']
    var a = [device, brand, 'cn', '36']
    // var a = ['free', 'iphone', 'us', '36', '2023-01-13', 2, 1, null]  //翻页需要的参数
    var vv = "@#"
    var url = '/rank/index'
    var baseUrl = 'https://api.qimai.cn'
    var r = +new Date - (105333 || 0) - 1661224081041
    a = a['sort']()['join'](_)
    a = v(a)
    a = (a += vv + url['replace'](baseUrl, _)) + (vv + r) + (vv + 3)
    return a
}


function run(brand, device) {
    args = h(parmA(brand, device), d)
    e = v(args)
    return (e)
}