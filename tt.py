# encoding =utf-8
import inits.mkorders as mkorder
import inits.get_order as getorder
import time
import inits.conf as conf
# 获得所有

mywallet =conf.mywallet
gateway = conf.gateway
secret = conf.secret
# 简单设置参数---------------------
orderlist = []
pricelist = []
allorders = getorder.getaccount_orders(mywallet,gateway,100)

print(allorders)
# mkorder.buyXRP(1.01,2)
# mkorder.sellXRP(1,1)
# 获取订单列表 ：--------------------
for ii in allorders:
    ordertype = allorders[ii][0]
    order = allorders[ii][6]
    price = allorders[ii][8]
    #
    print("%s--%s" % (order, price))
    # if ordertype == 'buy':
    #     pricelist.append(price)
    #     # mkorder.cancelOrder(order, mywallet, secret)
    #     if  price == 1:
    #         mkorder.cancelOrder(order, mywallet, secret)
    #         time.sleep(10)
    # print('当前账户买单价格列表：%s' % pricelist)

    orderlist.append(order)
    # 获得所有订单列表
    pricelist.append(price)
    print("%s	%s	%s	%s	%s"%(allorders[ii][9],allorders[ii][0],allorders[ii][1],order,allorders[ii][8]))
    #
    # 取消价格大于或者小于XXX的订单-------必须设置----------

print('当前账户买单价格列表：%s' % pricelist)



        # if ordertype == 'buy':
    #     pricelist.append(price)
    #     orderlist.append(order)

        # print("订单序号 %s,类型：%s"%(order,ordertype))
# print(pricelist)
# # 批量取消订单---------------------
# #
# for i in orderlist:
#     print(i)
#     mkorder.cancelOrder(i,mywallet,secret)
#     time.sleep(15)


