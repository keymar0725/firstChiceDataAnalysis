# firstChiceDataAnalysis
1. out_ot.py：生産時間自動抽出プログラム
2. pick_parameter：プログラム1で得られたcsvファイルから、生産時間内の必要なパラメータをピックするプログラム


# Requirement

* python3.10.5
* Pandas

# Installation

```bash
pip install pandas
```

# Usage

git clone in any dirctory

```bash
git clone https://github.com/keymar0725/firstChiceDataAnalysis.git
```


make image of graph.

```bash
cd firstChiceDataAnalysis
python3 out_ot.py
python3 pick_parameter.py
```

or

```bash
python3 ./(cloned dir)/firstChiceDataAnalysis/out_ot.py
```

スクリプト実行に必要な引数は以下の二つである。
* argv1: Path to csv file (csvファイルへのパス。相対・絶対問わず)
* argv2: Plot pitch (グラフに記録する点のピッチ、csvファイルのデフォルトは1秒/ピッチである)
    ex)1sec = 1, 1min = 60, 30min = 1800, 1hour = 3600
* argv3,4: minimum temparature / maximum temparature (温度の表示領域)
* argv5,6: minimum vaccum degree / maximum vaccum degree (圧力の表示領域)

# Example

```bash
python out_graph.py ./import/sasami.csv 60 -40 90 50 115
```

or

```bash
python3 ./(cloned dir)/firstChiceDataAnalysis/out_graph.py ./import/sasami.csv 60 -40 90 50 115
```

# Author

* Takahashi KEISUKE
* keisuke.takahashi@foodtechno-eng.co.jp