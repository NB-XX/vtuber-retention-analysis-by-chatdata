import numpy as np


def stream_stats(id_list):
    comment_num = len(id_list)
    unique_num = len(np.unique(id_list))
    result = [comment_num, unique_num]
    return result


def retention(id_list_a, id_list_b, isNew):
    try:
        old_num = float(len(np.unique(id_list_a)))
        new_num = float(len(np.unique(id_list_b)))
        set_id = list(set(id_list_a) & set(id_list_b))
        retention_num = float(len(set_id))
        if isNew:
            percentage = "%.2f%%" % (retention_num/old_num * 100)
        else:
            percentage = "%.2f%%" % (retention_num/new_num * 100)
        result = [retention_num, percentage, new_num, old_num]
        return result
    except:
        print('可能传入了没有评论区的数据')
