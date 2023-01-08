const crypto = require('crypto')
function m(e) {
    return crypto.createHash("md5").update(e).digest()
}
function decode(t, o, n) {
    if (!t)
        return null;
    const a = Buffer.alloc(16, m(o))
        , r = Buffer.alloc(16, m(n))
        , i = crypto.createDecipheriv("aes-128-cbc", a, r);
    let s = i.update(t, "base64", "utf-8");
    return s += i.final("utf-8"),
        s
}
// var n ='Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ysrEuPNKkODn7po6VcuUUdOhXRO9VoaHHPXgSaHRFizTz-JCINt-6OGxXUMnvnl4Icel-PKx-6P06bZ0ChlyfLqtVuMv4wvTpMBUWwO4fxJUft4eBxScgAPfditcov7L8guD-TYAoCRbGQYql2LuN7jTV2kAejWgqN1n7QXmS_slkFPMZX8PnvM9qsXmVeI-7fXTgvl3fKFfhfldrucbOcLsFkhLX3Yn68ChD7L1nIlVZolN1uA73aYQz3VuKV627YtjkjGx1sNQjsS2sfWsM9m7O7FKvuJyuo-yOhXfo4jD4rljZsHbyAf70JFwjyLiR3GtB88vf1v3_OlGjaHvD3FaZ9DYuMYKo3ApEdUdmMBsbA7CV_ZMn8dlMyIhJuKRhkveP5u7b4JWtS0gR7nwrnRFrHc2sgAsm3RbbvH4ORv-kfrK0V0SaHYMo0MFSl8ToI9wmt24souV9uzzZ--128dZ7yXJjgT8018p60FY_dLdERkau2aRGLIAON3y0CR-PHQY_xfxMkdGKzZdWqEIVyUPIbfyOxYSBDZ1sxPHYIqlolv9QPqlTssvoOiXKtxfR6ZzMk1ukVZzpCIEt-q-bv-nloqObpLcSUgfY4twKPwmGTrePN90xYElQav96MH9FCrWmlgnLaB_AuavW3DQyqxV3NPKR9yHwVl-Hn1PbT1mYjAy045CG3sEZkzh_XdsK1SzJ6eSw0vYjDCaJWT2C3Ly3D1IWXOGJF0tyCtAQv2nxzhEkNnpGAo0i4VOcnttFwJdl4XEov0_7rLCaBHel_j3gKXwiHAe-N5JPd3teU5sxb-UI8E9vcUYf3Ew_axMhSlSjCNWa96HLkK75K9_zlGFnwoOTmCeFmLFiPp0SyMXjrTf3H6sBu6Rx0YextKtSIbhthkiIoq191uwWXZ-SV94xam_tW7fS8HaS_DjrVGdeF_BpqgOL4P-YxojsH_cl_Aza9XMBQTcIZytv7FG6eR12HenJF6dNU759hDHN6cIXjtvQjmlGb59vNMtfZIOJm_Pw7WVwPfomK0uBsYcobyVV3ZcSOCFeQBvsSx6B1n6beMhx3vgA2bKpPNwOMJiDXwxP4kFfcaGrFPOrQjL9P-XRHqiR9qzzH5NxDJpP-1MrjGbVYQW9idWDKdaB5_Xl0O7RvidkoJFRPjvB9fnZ0lit8gPqmXFYXjSUgFWiN8LNZ4F5IsJtdQM0at2t53SwQyChFr71eFWJ-2H133v8rXgduCkr3NOo8LF7FWl4vvGPlCalaRCvEFbwBsskInrzcSBzZOE483Pxj-1t8k2VchSWo5mRVtvEZY_PPIOnRw0R0KMgxjLeOHwapFKB70sr4GxbieGngOOIZUTkeznIXeqce-4rXGjKqZgIYVq-MOuqxhsM0VCrwEvhFrpxg5xb2obJ_Uj7qbqP4BqgH10dqhjS1c8IkD0ZMHpYTNkNn5qhGOYow7BXXsbBFPB3qzawdNRNfz-Hu0iQ539n1sqynh6O2dyXpvXMXU2mCU-ewke80yJIsvqKr4u1nxv1md_n3Vp9zKLHpfuRGFaJfnhM5RVUe__Va6i5xkWIvTGmxJvB60yQjH9wCmRdHFwtzCcf9taBkpRAI-Axkgp4dDuCn80MuSb3Y207yA6XvAVZ9W52lagudRDR5UKIVGgukcfaI='
var k = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
var iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'


function run(encode_data){
    return (decode(encode_data, k, iv))
}