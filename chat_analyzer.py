import chat_dl
import chat_num
import json
# 六期频道
holox_channel = {'chloe': 'https://www.youtube.com/channel/UCIBY1ollUsauvVi4hW4cumw',
                 'laplus': 'https://www.youtube.com/channel/UCENwRMx5Yh42zWpzURebzTw',
                 'koyori': 'https://www.youtube.com/channel/UC6eWCld0KwmyHFbAqK3V-Rw',
                 'iroha': 'https://www.youtube.com/channel/UC_vMYWcDjmfdpH6r4TTn1MQ',
                 'lui': 'https://www.youtube.com/channel/UCs9_O1tRPMQTHQ-N_L6FU2g'}

# NIJI头部频道（随便来几个头部）
niji_channel = {'kuzuha': 'https://www.youtube.com/channel/UCSFCh5NL4qXrAy9u-u2lX3g',
                'mito': 'https://www.youtube.com/channel/UCD-miitqNY3nyukJ4Fnf4_A',
                'toya': 'https://www.youtube.com/channel/UCv1fFr156jc65EMiLbaLImw',
                'ange': 'https://www.youtube.com/channel/UCHVXbQzkl3rDfsXWo8xi2qw'}

# HOLO头部频道（随便来几个头部）
holo_channel = {'gura': 'https://www.youtube.com/channel/UCoSrY_IQQVpmIRZ9Xf-y93g',
                'Pekora': 'https://www.youtube.com/channel/UC1DCedRgGHBdm81E1llLhOQ',
                'miko': 'https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA',
                'aqua': 'https://www.youtube.com/channel/UC1opHUrw8rvnsadT-iGp7Cg'
                }
# NIJISANJI新人
niji_new_channel = {'Nei': 'https://www.youtube.com/channel/UCe22Bcwd_GCpTjLxn83zl7A',
                    'Yotsuha': 'https://www.youtube.com/channel/UCtHY-tP0dyykhTRMmnfPs_g',
                    'Muyu': 'UCAQDFeCTVdx90GtwohwjHzQ'}


# 头部算总计用的
def channel_id_data_get(name, channel_link, sort):
    video_list = chat_dl.get_video_urls(channel_link, sort)
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
        id_list_full = json.loads(f.read())
    return id_list_full


# 新人算留存用的
def channel_retention(name, channel_link, sort):
    id_lis_dic = {}
    video_list = chat_dl.get_video_urls(channel_link, sort)
    for url in video_list:
        for i in range(len(video_list)):
            id_list = chat_dl.get_chat_id(url)
            id_lis_dic[i] = id_list
            with open(f'{name}_{i}_id_list.txt', 'w', encoding='utf-8') as f:
                f.write(json.dumps(id_list))
    # 首播比
    for k in id_lis_dic:
        if k == 4:
            break
        else:
            result = chat_num.retention(id_lis_dic[0], id_lis_dic[k+1])
        with open(f'{name}数据结果.txt', 'a') as f:
            f.write(
                f'{name}的第{k+1}场直播与首播相同的人数有：{result[0]}个，首播留存率为：{result[1]}\n')
    # 环比
        if k == 4:
            break
        else:
            result = chat_num.retention(id_lis_dic[k], id_lis_dic[k+1])
        with open(f'{name}数据结果.txt', 'a') as f:
            f.write(
                f'{name}的第{k+2}场直播与第{k+1}相同的人数有：{result[0]}个，环比留存率为：{result[1]}\n')


def analyzer_group_data(group_dic, isNew):
    for k, v in group_dic.items():
        if isNew:
            channel_retention(k, v, "new")
            print(f"{k}的数据都计算好了！")
        else:
            channel_id_data_get(k, v, "old")
            print(f"{k}的数据都计算好了！")


analyzer_group_data(holox_channel, True)
analyzer_group_data(niji_new_channel, True)
analyzer_group_data(holo_channel, False)
analyzer_group_data(niji_channel, False)
