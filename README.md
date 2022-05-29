# vtuber-retention-analysis-by-chatdata
自用小脚本
.
├─ .gitignore
├─ README.md
├─ chat_analyzer.py                                       //分析数据的主入口
├─ chat_dl.py                                             //获取视频链接，下载对应直播的chat获取发言id
├─ chat_num.py                                            //统计单一直播的id数据，不同id列表的相关情况
├─ hololive_data
│    ├─ chloe观众来源数据结果.txt
│    ├─ iroha观众来源数据结果.txt
│    ├─ koyori观众来源数据结果.txt
│    ├─ laplus观众来源数据结果.txt
│    ├─ lui观众来源数据结果.txt
│    ├─ new
│    │    ├─ chloe_0_id_list.txt
│    │    ├─ chloe_1_id_list.txt
│    │    ├─ chloe_2_id_list.txt
│    │    ├─ chloe_3_id_list.txt
│    │    ├─ chloe_4_id_list.txt
│    │    ├─ chloe数据结果.txt
│    │    ├─ iroha_0_id_list.txt
│    │    ├─ iroha_1_id_list.txt
│    │    ├─ iroha_2_id_list.txt
│    │    ├─ iroha_3_id_list.txt
│    │    ├─ iroha_4_id_list.txt
│    │    ├─ iroha数据结果.txt
│    │    ├─ koyori_0_id_list.txt
│    │    ├─ koyori_1_id_list.txt
│    │    ├─ koyori_2_id_list.txt
│    │    ├─ koyori_3_id_list.txt
│    │    ├─ koyori_4_id_list.txt
│    │    ├─ koyori数据结果.txt
│    │    ├─ laplus_0_id_list.txt
│    │    ├─ laplus_1_id_list.txt
│    │    ├─ laplus_2_id_list.txt
│    │    ├─ laplus_3_id_list.txt
│    │    ├─ laplus_4_id_list.txt
│    │    ├─ laplus数据结果.txt
│    │    ├─ lui_0_id_list.txt
│    │    ├─ lui_1_id_list.txt
│    │    ├─ lui_2_id_list.txt
│    │    ├─ lui_3_id_list.txt
│    │    ├─ lui_4_id_list.txt
│    │    └─ lui数据结果.txt
│    └─ old
│           ├─ aqua_id_list_full.txt
│           ├─ aqua数据结果.txt
│           ├─ gura_id_list_full.txt
│           ├─ gura数据结果.txt
│           ├─ miko_id_list_full.txt
│           ├─ miko数据结果.txt
│           ├─ subaru_id_list_full.txt
│           └─ subaru数据结果.txt
├─ niji_holo新人数据统计.xlsx
└─ nijisanji_data
       ├─ Muyu观众来源数据结果.txt
       ├─ Nei观众来源数据结果.txt
       ├─ Salome的第1次直播观众来源数据结果.txt
       ├─ Salome的第2次直播观众来源数据结果.txt
       ├─ Salome的第3次直播观众来源数据结果.txt
       ├─ Salome的第4次直播观众来源数据结果.txt
       ├─ Salome的第5次直播观众来源数据结果.txt
       ├─ Salome观众来源数据结果.txt
       ├─ Yotsuha观众来源数据结果.txt
       ├─ new
       │    ├─ Muyu_0_id_list.txt
       │    ├─ Muyu_1_id_list.txt
       │    ├─ Muyu_2_id_list.txt
       │    ├─ Muyu_3_id_list.txt
       │    ├─ Muyu_4_id_list.txt
       │    ├─ Muyu数据结果.txt
       │    ├─ Nei_0_id_list.txt
       │    ├─ Nei_1_id_list.txt
       │    ├─ Nei_2_id_list.txt
       │    ├─ Nei_3_id_list.txt
       │    ├─ Nei_4_id_list.txt
       │    ├─ Nei数据结果.txt
       │    ├─ Salome_0_id_list.txt
       │    ├─ Salome_1_id_list.txt
       │    ├─ Salome_2_id_list.txt
       │    ├─ Salome_3_id_list.txt
       │    ├─ Salome_4_id_list.txt
       │    ├─ Salome数据结果.txt
       │    ├─ Yotsuha_0_id_list.txt
       │    ├─ Yotsuha_1_id_list.txt
       │    ├─ Yotsuha_2_id_list.txt
       │    ├─ Yotsuha_3_id_list.txt
       │    ├─ Yotsuha_4_id_list.txt
       │    └─ Yotsuha数据结果.txt
       └─ old
              ├─ ange_id_list_full.txt
              ├─ ange数据结果.txt
              ├─ kuzuha_id_list_full.txt
              ├─ kuzuha数据结果.txt
              ├─ mito_id_list_full.txt
              ├─ mito数据结果.txt
              ├─ toya_id_list_full.txt
              └─ toya数据结果.txt
