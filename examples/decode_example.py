import time
import datetime
from dl_segmenter import get_or_create, DLSegmenter
import random
import os
# wget https://raw.githubusercontent.com/yanyiwu/practice/master/nodejs/nodejieba/performance/weicheng.utf8 -O examples/weicheng.utf8
DIR_PATH = os.path.join(os.path.dirname(__file__))

if __name__ == '__main__':
    segmenter = get_or_create(os.path.join(DIR_PATH,"../config/default-config.json"),
                                           src_dict_path=os.path.join(DIR_PATH,"../config/src_dict.json"),
                                           tgt_dict_path=os.path.join(DIR_PATH,"../config/tgt_dict.json"),
                                           weights_path=os.path.join(DIR_PATH,"../models/weights.32--0.18.h5"))

    texts = [
        "昨晚，英国首相特里萨•梅(TheresaMay)试图挽救其退欧协议的努力，在布鲁塞尔遭遇了严重麻烦。"
        "倍感失望的欧盟领导人们指责她没有拿出可行的提案来向充满敌意的英国议会兜售她的退欧计划。"
        ,
        "物理仿真引擎的作用，是让虚拟世界中的物体运动符合真实世界的物理定律，经常用于游戏领域，以便让画面看起来更富有真实感。"
        "PhysX是由英伟达提出的物理仿真引擎，其物理模拟计算由专门加速芯片GPU来进行处理，"
        "在节省CPU负担的同时还能将物理运算效能成倍提升，由此带来更加符合真实世界的物理效果。"
        ,
        "好莱坞女演员奥黛丽·赫本(AudreyHepburn)被称为“坠入人间的天使”，"
        "主演了《蒂凡尼的早餐》《龙凤配》《罗马假日》等经典影片，并以《罗马假日》获封奥斯卡影后。"
        "据外媒报道，奥黛丽·赫本的故事将被拍成一部剧集。"
        ,
        "巴纳德星的名字起源于一百多年前一位名叫爱德华·爱默生·巴纳德的天文学家。"
        "他发现有一颗星在夜空中划过的速度很快，这引起了他极大的注意。"
        ,
        "叶依姆的家位于仓山区池后弄6号，属于烟台山历史风貌区，"
        "一家三代五口人挤在五六十平方米土木结构的公房里，屋顶逢雨必漏，居住环境不好。"
        "2013年11月，烟台山历史风貌区地块房屋征收工作启动，叶依姆的梦想正逐渐变为现实。"
        ,
        "人民网北京1月2日电据中央纪委监察部网站消息，日前，经中共中央批准，"
        "中共中央纪委对湖南省政协原副主席童名谦严重违纪违法问题进行了立案检查。"
    ]
    sent, tag = segmenter.decode_text(texts[0])

    start_time = time.time()
        
    for sent, tag in segmenter.decode_texts(texts):
        print(sent)
        print(tag)

    print("cost {:.2f}ms".format( (time.time() - start_time )* 1000) )

    lines = []
    weicheng = os.path.join(os.path.dirname(__file__),"weicheng.utf8")
    for line in open(weicheng):
        a = line.strip()
        if a:
            lines.append(a)
    result = [""] * 10
    result[random.randint(0, 9)] = '/'.join(str(segmenter.decode_text("南京长江大桥")))
    starttime = datetime.datetime.now()
    segmenter.decode_texts(lines)
    # for i in range(50):
    # for line in lines:
    #     try:
    #         r = '/'.join(str(segmenter.decode_text(line)))
    #     except:
    #         pass
    #     # print(r)
    #     result[random.randint(0, 9)] = r
    #     #result[random.randint(0, 9)] = jieba.cut(line)
    endtime = datetime.datetime.now()
    print (endtime - starttime)