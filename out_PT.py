#!/usr/bin/env python3
import csv
import pandas as pd
import os
import os.path
import datetime
import glob


### Init ###
out_dir = "out/"
os.makedirs(out_dir, exist_ok=True)
import_dir = "//172.25.0.195/fte_data (東日本)/【東京支社】/1.計画物件/3一般企業/ファーストチョイス㈱/ハンバーグフリーザー/HANEW本社監査指摘事項/運転データ/Package1/SOUSA"
output_dir = "C:/Users/0296/Desktop/firstChiceDataAnalysis"
os.chdir(import_dir)
csv_list = glob.glob("AAM00021_*.CSV")

df_s = pd.read_csv(csv_list[0], names = range(1,11,1), encoding="cp932", delimiter=",", dtype="object")
df_s = df_s[15:]
df_s = df_s.drop([1,2,8,9,10], axis=1)
df_s[6] = (pd.to_datetime(df_s[6])).dt.round("min")
d_s = (df_s.iloc[0,3]).date()

df_e = pd.read_csv(csv_list[-1], names = range(1,11,1), encoding="cp932", delimiter=",", dtype="object")
df_e = df_e[15:]
df_e = df_e.drop([1,2,8,9,10], axis=1)
df_e[6] = (pd.to_datetime(df_e[6])).dt.round("min")
d_e = (df_e.iloc[-1,3]).date()

data = {3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
df0 = pd.DataFrame(data)
df0[6] = (pd.to_datetime(df0[6])).dt.round("min")
df0[7] = (pd.to_datetime(df0[7])).dt.round("min")


for csv in csv_list:
    os.chdir(import_dir)
    df = pd.read_csv(csv, names = range(1,11,1), encoding="cp932", delimiter=",", dtype="object")
    record_num = int(df.iloc[3,1])
    df = df[15:]                        # ヘッダー削除
    df = df.drop([1,2,8,9,10], axis=1)  # 不要な列削除
    
    # Filtering1:101(冷却ｾﾚｸﾀｽｲｯﾁ)かつR(動作正常)
    drop_list = []
    for i in range(0,record_num):
        if df.iloc[i,0]=='101' and df.iloc[i,2] == 'R':
            continue
        else:
            drop_list.append(i)
    df = df.drop(df.index[drop_list])
    df[6] = (pd.to_datetime(df[6])).dt.round("min")
    df[7] = (pd.to_datetime(df[7])).dt.round("min")
    df[8] = df[7] - df[6]
    
    ## Filtering2:生産時間=3時間以下及び20時間以上
    drop_list2 = []
    for i in range(0,len(df)):
        if int((df.iloc[i,5]).seconds) >= 3*3600 and int((df.iloc[i,5]).seconds) <= 20*3600:
            continue
        else:
            drop_list2.append(i)            
    df = df.drop(df.index[drop_list2])
    os.chdir(output_dir)
    df0 = pd.concat([df0,df])

### Filtering3:開始時間と終了時間の被り削除
df0 = df0.drop_duplicates(subset=6)
df0 = df0.drop_duplicates(subset=7)

#### Filtering4:開始時間の差=1分以内
drop_list3 = []
for i in range(0,len(df0)):
    for j in range(i+1,len(df0),1):
        dt = df0.iloc[j,3]-df0.iloc[i,3]
        if abs(int(dt.total_seconds())) <= 60:
            drop_list3.append(j)
df0 = df0.drop(df0.index[drop_list3])

df0.to_csv(out_dir+"PT_{0}_{1}.csv".format(d_s,d_e), encoding="shift_jis", header=False, columns=[6,7,8], index=False)
print('"PT_{0}_{1}.csv" SAVED'.format(d_s,d_e))