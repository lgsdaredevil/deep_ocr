# -*- coding: utf-8 -*-

from deep_ocr.langs.digits import data as digit_data
from deep_ocr.langs.chi_sim import data as sim_data


class CharSet(object):
    def __init__(self):
        self.data = {}
        self.data["name"] = set(sim_data) - set(digit_data)
        self.data["sex"] = set(u"男女")
        self.data["minzu"] = set(
            u"汉蒙古回藏维吾尔苗彝壮布依朝鲜满侗瑶白土家哈尼哈萨克"\
            u"傣黎傈僳佤畲拉祜水东乡纳西景颇柯尔克孜"\
            u"土达斡尔仫佬羌布朗撒拉毛南仡佬锡伯阿昌"\
            u"普米塔吉克怒俄罗斯鄂温克德昂保安裕固京"\
            u"塔塔尔独龙鄂伦春赫哲乌孜别克门巴珞巴"\
            u"基诺高山穿青人")
        self.data["year"] = set("0123456789")
        self.data["month"] = set("0123456789")
        self.data["day"] = set("0123456789")
        self.data["address"] = set(sim_data)
        self.data["id"] = set(u"0123456789X")

    def get(self):
        return self.data