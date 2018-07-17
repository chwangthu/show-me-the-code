# !usr/bin/env python3
# -*- coding:utf-8 -*-

'''
generate 100 coupons
'''
import random
import string
def get_single_coupon(size=6, charset=string.ascii_letters+string.digits):
    return ''.join(random.choice(charset) for _ in range(size))

def get_specify_number_coupons(num=100):
    coupons = []
    tot_coupons = 0
    while True:
        tep = get_single_coupon()
        if tep in coupons:
            continue
        else:
            print(tep)
            coupons.append(tep)
            tot_coupons += 1
        if(tot_coupons == 100):
            break
    return coupons

if __name__ == "__main__":
    result = get_specify_number_coupons()
    f = open("../static/coupons", 'w')

    for item in result:
        f.write(item + '\n')
    # print(result)
    