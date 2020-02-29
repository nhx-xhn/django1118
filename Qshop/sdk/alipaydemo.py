##支付宝demo
alipay_public_key_string="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg0OUOwIfwo4do42TkDsXt4zs2GfIuJfcW3fuoMRdcTehK//Xl/B1qBus963/ZrdTJj0N4rYgTscMLqdm0MbC7R3xuFhBr+WdNxAKTkFvCl9HGSfct1PsRpna/tF6ubRgOdeHt9CdDdpqHOcEvsT/3E2bqXpL+AiUNfmDkY+MJeAQu9Ta7MsSstjJFs4QCf6c6B702cOD1+dazI6SM7+0j8dYZyGKyuYkB8BY8lBrow82UIxyL7ftiO1YgwyqyPrXB1mpJdStlRcuLOR50SBY8/gknSc+LrrBdddcFOvoJ/gt3uUj6js+sERe49q/4BEqkYRbBEskUByN0lDoAax3HwIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAg0OUOwIfwo4do42TkDsXt4zs2GfIuJfcW3fuoMRdcTehK//Xl/B1qBus963/ZrdTJj0N4rYgTscMLqdm0MbC7R3xuFhBr+WdNxAKTkFvCl9HGSfct1PsRpna/tF6ubRgOdeHt9CdDdpqHOcEvsT/3E2bqXpL+AiUNfmDkY+MJeAQu9Ta7MsSstjJFs4QCf6c6B702cOD1+dazI6SM7+0j8dYZyGKyuYkB8BY8lBrow82UIxyL7ftiO1YgwyqyPrXB1mpJdStlRcuLOR50SBY8/gknSc+LrrBdddcFOvoJ/gt3uUj6js+sERe49q/4BEqkYRbBEskUByN0lDoAax3HwIDAQABAoIBAHfQO4ERE0RWzB75n3PLPH7CF34AXWqA0xZ6hkogctpg2LB8uqFpTzu+50a8f5+WPkNs/zus2hiN/0SmcGaoxkwBRR3rESopADO+ZGnBuEVTamY/yGteIxDeZtKpCshvKFYjsTHLLU/zyV/QTriCwLip7ifoBWfFDOOneLxotpfqeC7O8Aa5rVPvsrtkdGEt29n8/BG8otXOCIlZ2gUhUGpf3hkFUhDRdxmi8WaeHqnSI3XGMTMTXMjlazQva3hLmkwfvbmJtifZWC7ctP95Beiw99U89+wrhu8tmAmlUp3UFVm3iwzdQGK3iINx7LSeDjY66hL5uZJkE8EjCrQ5I8ECgYEA0a5We7eG32fWz1gGNhq9eBZnJyJfikJsD5Vu2wvtDRbU1teSEDIhJEBuMPJV7sUUZviv2muLqeHVWbas4LXJ+gFrA2AOWybAPS5XhFoJlYbbJgfn6mLIvF+Q9OCqg74NNTFwjnCdCNie4MSEMKNc3/SQ6eXsN5jT/pxKMReQiRcCgYEAoEKu30uL+drqHmYYfsqPm8GA7nf3GhShbDi0pRm0DsOQQ4VyOmUgYB9myZ8gczZ5+WcOMCmhBuH0A0bBvXoxqCWTIG9QYVEn0LnaKWaG8vBCXGFb9ffJeJrecuHCBBPAVXvX82H+bOThCE2u7A6pfrgYZfvcmlOQXD7Y34WGNzkCgYEAoUH03RzeKz6O49OMo1uZT5vbJSu4UnqW5L1GDkxzuNdQRRJxEOecuWab2CTnlcQX1sF3bQG83aADFwX4mrD0bsNca7IaGFwLCIJ1aCJesJKQRAVchNQIEWdl8g4+1Sb6vWgSalmNS9pdBfvcthNNQCe0s03Sh0eP8oZ8QJkg3W0CgYEAoBx/IdAUdPfl16Eg7+voNjDJY3avhXr/G2Q79ocLgYSY6Ry11umZwu8cfmtgvDq8+hOf9TZiDsJIS82xWmBupBOGPm133QJ7yOklsR8hzC2F303V1pRM0RXJEPXEJNam3cDxK9PHoXu559XU4Tp01ImQtrM+32CFZePUQNziDuECgYABOWTVq/pjCDi5/Qy1/Mq6Dv9LnkuVukJIi9VaqrvtcH1UrILqOpGBTLy+4BX4mKSFrudsXuddPdZvR3n+tec5JZTx71V1m98HgBwb4mdyYMSC38qXMJDePPSLG5weg8pnFOYufVKFKPg/J2f/K2xnzaunuvpVRSsv8Ky3ZuWOBA==
-----END RSA PRIVATE KEY-----"""


##导包
from alipay import AliPay

##2实例化对象
alipay =AliPay(
    appid='2016101800717559',
    app_notify_url=None,
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type='RSA2',
    debug=False
)

##3  实例化订单
order_string=alipay.api_alipay_trade_page_pay(
    subject='军火交易',##主题
    out_trade_no='23136546851654',##订单号
    total_amount='100000.00',##交易金额  字符串
    return_url=None, ##回调地址
    notify_url=None  ##通知
)



##4 返回支付宝支付的url

result='https://openapi.alipaydev.com/gateway.do?' + order_string
print(result)




