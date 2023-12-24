#!/usr/bin/env python3
import csv
import sys
import pandas as pd
import os
import os.path
import datetime
import glob

out_dir = "picked/"
os.makedirs(out_dir, exist_ok=True)

import_file = 'C:/Users/0296/TAKAHASHI(Local)/firstChiceDataAnalysis/out/11_20231219.csv'
col_name = range(1,4,1)
df_import = pd.read_csv(import_file, names = col_name, encoding="shift_jis", delimiter=",", dtype="object")
df_import[1] = (pd.to_datetime(df_import[1])).dt.round("min")
df_import[2] = (pd.to_datetime(df_import[2])).dt.round("min")

# import csv files
log6_dir = "//172.25.0.195/fte_data (東日本)/【東京支社】/1.計画物件/3一般企業/ファーストチョイス㈱/ハンバーグフリーザー/HANEW本社監査指摘事項/送受信/Package1/冷凍機_log1"
output_dir = "//172.25.0.195/fte_data (東日本)/【東京支社】/1.計画物件/3一般企業/ファーストチョイス㈱/ハンバーグフリーザー/HANEW本社監査指摘事項/送受信/Package1/冷凍機_log1/"
os.chdir(log6_dir)
log6_list = glob.glob("LOG00006_*.CSV")
col_name = range(1,29,1)
df = pd.read_csv(log6_list[0], names = col_name, encoding="shift_jis", delimiter=",", dtype="object")
print(log6_list[0])
_df = df[13:]


data = {1:[], 11:[], 13:[], 20:[], 24:[], 28:[]}
df_out = pd.DataFrame(data)
df_out[1] = (pd.to_datetime(df_out[1])).dt.round("min")
col_name = range(1,30,1)
n = 0
for log6 in log6_list:
    os.chdir(log6_dir)
    df = pd.read_csv(log6, names = col_name, encoding="shift_jis", delimiter=",", dtype="object")
    _df = df[13:]
    list1 = [2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,21,22,23,25,26,27,29]
    _df = _df.drop(list1, axis=1)
    _df[1] = (pd.to_datetime(_df[1])).dt.round("min")

    for i in range(0,len(df_import)):
        drop_list = []
        for j in range(0,len(_df)):
            if _df.iloc[j,0].date() == df_import.iloc[i,0].date():
                t1 = int((_df.iloc[j,0] - df_import.iloc[i,0]).seconds)
                t2 = int((df_import.iloc[i,1] - _df.iloc[j,0]).seconds)
                t3 = int((df_import.iloc[i,1] - df_import.iloc[i,0]).seconds)
                if t1+t2==t3:
                    print(_df.iloc[j,0])
                else:
                    drop_list.append(j)
            else:
                drop_list.append(j)
        df2 = _df.drop(_df.index[drop_list])
        df_out = pd.concat([df_out,df2], ignore_index=False)
    print('n={0}:{1} END'.format(n,log6))
    n = n + 1
    if n > len(log6_list):
        os.chdir(output_dir)
        df_out = df_out.rename(columns={1:'Time', 11:'MT吐出圧力', 13:'LT吐出圧力', 20:'MT吐出温度',24:'温水取出温度', 28:'温水流量'})
        df_out.to_csv(out_dir+"picked_log06_{0}.csv".format(n/10), encoding="shift_jis", index=False)
        print('picked_log06_{0}.csv SAVED'.format(n/10))
        print('ALL END')
        break
    elif n!=0 and n%10==0:
        os.chdir(output_dir)
        df_out = df_out.rename(columns={1:'Time', 11:'MT吐出圧力', 13:'LT吐出圧力', 20:'MT吐出温度', 24:'温水取出温度', 28:'温水流量'})
        df_out.to_csv(out_dir+"picked_log06_{0}.csv".format(n/10), encoding="shift_jis", index=False)
        df_out = pd.DataFrame(data)
        df_out[1] = (pd.to_datetime(df_out[1])).dt.round("min")
        print('picked_log06_{0}.csv SAVED'.format(n/10))