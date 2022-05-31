import chat_dl
import chat_num
import json
# 六期频道
holox_channel = {
    'chloe': 'https://www.youtube.com/channel/UCIBY1ollUsauvVi4hW4cumw',
    'laplus': 'https://www.youtube.com/channel/UCENwRMx5Yh42zWpzURebzTw',
    'koyori': 'https://www.youtube.com/channel/UC6eWCld0KwmyHFbAqK3V-Rw',
    'iroha': 'https://www.youtube.com/channel/UC_vMYWcDjmfdpH6r4TTn1MQ',
    'lui': 'https://www.youtube.com/channel/UCs9_O1tRPMQTHQ-N_L6FU2g'
}

# NIJI头部频道（随便来几个头部）
niji_channel = {
    'kuzuha': 'https://www.youtube.com/channel/UCSFCh5NL4qXrAy9u-u2lX3g',
    'mito': 'https://www.youtube.com/channel/UCD-miitqNY3nyukJ4Fnf4_A',
    'toya': 'https://www.youtube.com/channel/UCv1fFr156jc65EMiLbaLImw',
    'ange': 'https://www.youtube.com/channel/UCHVXbQzkl3rDfsXWo8xi2qw'
}

# HOLO头部频道（随便来几个头部）
holo_channel = {
    'gura': 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g',
    'subaru': 'https://www.youtube.com/channel/UCvzGlP9oQwU--Y0r9id_jnA',
    'miko': 'https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA',
    'aqua': 'https://www.youtube.com/channel/UC1opHUrw8rvnsadT-iGp7Cg'
}
# NIJISANJI新人
niji_new_channel = {
    'Nei': 'https://www.youtube.com/channel/UCe22Bcwd_GCpTjLxn83zl7A',
    'Yotsuha': 'https://www.youtube.com/channel/UCtHY-tP0dyykhTRMmnfPs_g',
    'Muyu': 'https://www.youtube.com/channel/UCAQDFeCTVdx90GtwohwjHzQ',
    'Salome': 'https://www.youtube.com/channel/UCgIfLpQvelloDi8I0Ycbwpg'
}


# 头部算总计用的
def channel_id_data_get_full(name, channel_link, sort):
    video_list = chat_dl.get_video_urls(channel_link, sort)
    print(video_list)
    id_list_full = []
    for url in video_list:
        id_list_full.extend(chat_dl.get_chat_id(url))
    # 将获取的所有直播观众id写入文件 之所以这样是因为获取id实在是太慢了 存起来以防程序崩掉数据全没了
    with open(f'{name}_id_list_full.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(id_list_full))
    print(f'{name}_id_list_full.txt 写入成功')
    result = chat_num.stream_stats(id_list_full)
    with open(f'{name}数据结果.txt', 'a') as f:
        f.write(f'{name}的5场直播抽样数据：评论{result[0]}个，评论人数{result[1]}人\n')
    print(f'{name}的报告生成完毕')


# 读取本地存档用的
def id_list_file_open(path):
    with open(path, 'r', encoding='utf-8') as f:
        id_list = json.loads(f.read())
    return id_list


# 新人算留存用的
def channel_id_data_get_full_single(name, channel_link, sort):
    id_lis_dic = {}
    video_list = chat_dl.get_video_urls(channel_link, sort)
    i = 0
    for url in video_list:
        id_list = chat_dl.get_chat_id(url)
        id_lis_dic[i] = id_list
        # 将获取的所有直播观众id写入文件 之所以这样是因为获取id实在是太慢了 存起来以防程序崩掉数据全没了
        with open(f'{name}_{i}_id_list.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(id_list))
        i = i+1
    analyzer_start(id_lis_dic, name)


def analyzer_start(id_lis_dic, name):
    # 首播比
    for k in id_lis_dic:
        if k == 5:
            break
        else:
            result = chat_num.retention(id_lis_dic[0], id_lis_dic[k], True)
        with open(f'{name}数据结果.txt', 'a') as f:
            f.write(
                f'{name}的第{k+1}场直播有{result[2]}个人。与首播相同的人数有：{result[0]}个，首播留存率为：{result[1]}\n')
    # 环比
        if k == 4:
            break
        else:
            result = chat_num.retention(id_lis_dic[k], id_lis_dic[k+1], True)
        with open(f'{name}数据结果.txt', 'a') as f:
            f.write(
                f'{name}的第{k+2}场直播{result[2]}个人。与第{k+1}相同的人数有：{result[0]}个，环比留存率为：{result[1]}\n')


def analyzer_group_data(group_dic, isNew):
    for k, v in group_dic.items():
        if isNew:
            channel_id_data_get_full_single(k, v, "new")
            print(f"{k}的数据都计算好了！")
        else:
            channel_id_data_get_full(k, v, "old")
            print(f"{k}的数据都计算好了！")


def read_all_id_data(name, group):
    id_lis_dic = {}
    for i in range(8):
        id_lis_dic[i] = id_list_file_open(
            f'./{group}_data/new/{name}_{i}_id_list.txt')
        print(f"第{i+1}条已写入成功")
    return id_lis_dic


# 计算新人与两箱老人重合度 先把两大箱子的观众池读出来
def niji_holo_old():
    old_niji_id_list_full = []
    for k in niji_channel:
        old_niji_id_list_full.extend(id_list_file_open(
            f'./nijisanji_data/old/{k}_id_list_full.txt'))
    old_holo_id_list_full = []
    for k in holo_channel:
        old_holo_id_list_full.extend(id_list_file_open(
            f'./hololive_data/old/{k}_id_list_full.txt'))
    result = [old_holo_id_list_full, old_niji_id_list_full]
    return result


def niji_holo_contact(new_channel, group):
    result = niji_holo_old()
    for k in new_channel:
        new_id_list_first = id_list_file_open(
            f'./{group}_data/new/{k}_0_id_list.txt')
        result_retention = chat_num.retention(
            result[1], new_id_list_first, False)
        with open(f'{k}观众来源数据结果.txt', 'a') as f:
            f.write(
                f'共统计nijisanji的观众池{result_retention[3]}人，{k}首播{result_retention[2]}人，重合了{result_retention[0]}人，重合度{result_retention[1]}\n')
        result_retention = chat_num.retention(
            result[0], new_id_list_first, False)
        with open(f'{k}观众来源数据结果.txt', 'a') as f:
            f.write(
                f'共统计hololive的观众池{result_retention[3]}人，{k}首播{result_retention[2]}人，重合了{result_retention[0]}人，重合度{result_retention[1]}\n')


# 单独计算新人V的留存率
# for k in holox_channel:
#     id_lis_dic = read_all_id_data(k, 'hololive')
#     analyzer_start(id_lis_dic, k)


# niji_holo_contact(niji_new_channel, 'nijisanji')
# niji_holo_contact(holox_channel, 'hololive')

# 单独下载没下载成功的chat
# name = 'salome'
# url = 'https://www.youtube.com/watch?v=gIdJ0Gn9O24'
# i = 7
# id_list = chat_dl.get_chat_id(url)
# with open(f'{name}_{i}_id_list.txt', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(id_list))

# 单独计算salome所有直播的观众来源
result = niji_holo_old()
id_lis_dic = read_all_id_data('Salome', 'nijisanji')
for k in id_lis_dic:
    id_lis_dic[k]
    result_retention = chat_num.retention(
        result[1], id_lis_dic[k], False)
    with open(f'Salome的第{k+1}次直播观众来源数据结果.txt', 'a') as f:
        f.write(
            f'共统计nijisanji的观众池{result_retention[3]}人，首播{result_retention[2]}人，重合了{result_retention[0]}人，重合度{result_retention[1]}\n')
    result_retention = chat_num.retention(
        result[0], id_lis_dic[k], False)
    with open(f'Salome的第{k+1}次直播观众来源数据结果.txt', 'a') as f:
        f.write(
            f'共统计hololive的观众池{result_retention[3]}人，首播{result_retention[2]}人，重合了{result_retention[0]}人，重合度{result_retention[1]}\n')


# 计算下虹杏一家亲程度
# result = niji_holo_old()
# result_retention = chat_num.retention(result[0], result[1], False)
# print(result_retention)

# analyzer_group_data(holox_channel, True)
# analyzer_group_data(niji_new_channel, True)
# analyzer_group_data(holo_channel, False)
# analyzer_group_data(niji_channel, False)
