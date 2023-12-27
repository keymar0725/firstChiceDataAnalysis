#!/usr/bin/env python3
import csv
import sys
import pandas as pd
import os
import os.path
import datetime
import glob

out_dir = "log6/"
os.makedirs(out_dir, exist_ok=True)

# import csv files
import_file = 'C:/Users/0296/Desktop/firstChiceDataAnalysis/out/PT_2023-01-11_2023-12-01.csv'
df_import = pd.read_csv(import_file, names = range(1,4,1), encoding="shift_jis", delimiter=",", dtype="object")
df_import[1] = (pd.to_datetime(df_import[1])).dt.round("min")
df_import[2] = (pd.to_datetime(df_import[2])).dt.round("min")

log6_dir = "//172.25.0.195/fte_data (東日本)/【東京支社】/1.計画物件/3一般企業/ファーストチョイス㈱/ハンバーグフリーザー/HANEW本社監査指摘事項/運転データ/Package1/冷凍機_log1"
output_dir = 'C:/Users/0296/Desktop/firstChiceDataAnalysis/'
os.chdir(log6_dir)
log6_list = glob.glob("LOG00006_*.CSV")

data = {1:[], 11:[], 13:[], 20:[], 24:[], 28:[]}
df_out = pd.DataFrame(data)
df_out[1] = (pd.to_datetime(df_out[1])).dt.round("min")
n = 0

for log6 in log6_list:
    os.chdir(log6_dir)
    df = pd.read_csv(log6, names = range(1,32,1), encoding="shift_jis", delimiter=",", dtype="object")
    _df = df[13:]
    list1 = [2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,21,22,23,25,26,27,29,30,31]
    _df = _df.drop(list1, axis=1)
    _df[1] = (pd.to_datetime(_df[1])).dt.round("min")

    for i in range(0,len(df_import)):
        t_i = df_import.iloc[i,0]
        t_o = df_import.iloc[i,1]
        for j in range(0,len(_df)):
            t = _df.iloc[j,0]
            if t.date() == t_i.date():
                t1 = int((t - t_i).seconds)
                t2 = int((t_o - t).seconds)
                t3 = int((t_o - t_i).seconds)
                if t1+t2==t3:
                    df_out = pd.concat([df_out,_df[j:j+1]], ignore_index=False)
                elif t1==t2+t3:
                    break
            elif (t - t_i).days > 0:
                break
    
    print('n={0}:{1} END'.format(n,log6))
    n = n + 1
    if n > len(log6_list):
        os.chdir(output_dir)
        df_out = df_out.rename(columns={1: 'Time',11: 'MT吐出圧力',13: 'LT吐出圧力',20: 'MT吐出温度',24: '温水取出温度',28:'温水流量'})
        df_out.to_csv(out_dir+"picked_log06_{:02}.csv".format(int(n/10)), encoding="shift_jis", index=False)
        print('picked_log06_{:02}.csv SAVED'.format(int(n/10)))
        print('ALL END')
        break
    elif n!=0 and n%10==0:
        os.chdir(output_dir)
        df_out = df_out.rename(columns={1: 'Time',11: 'MT吐出圧力',13: 'LT吐出圧力',20: 'MT吐出温度',24: '温水取出温度',28:'温水流量'})
        df_out.to_csv(out_dir+"picked_log06_{:02}.csv".format(int(n/10)), encoding="shift_jis", index=False)
        df_out = pd.DataFrame(data)
        df_out[1] = (pd.to_datetime(df_out[1])).dt.round("min")
        print('picked_log06_{:02}.csv SAVED'.format(int(n/10)))