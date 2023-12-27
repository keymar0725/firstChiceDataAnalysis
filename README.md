# firstChiceDataAnalysis
1. out_PT.py：生産時間自動抽出プログラム
2. pick_log*.py：プログラム1で得られたcsvファイルから、生産時間内の必要なパラメータをピックするプログラム

以下の制約を満たしているものとする。
* LOGファイルのファイル名は時系列順に降順している。

# Requirement

* python3
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
python3 out_PT.py
python3 pick_log1.py
python3 pick_log6.py
```

or

```bash
python3 ./(cloned dir)/firstChiceDataAnalysis/out_PT.py
python3 ./(cloned dir)/firstChiceDataAnalysis/pick_log1.py
python3 ./(cloned dir)/firstChiceDataAnalysis/pick_log6.py
```


# Example

```bash
python3 out_PT.py
python3 pick_log1.py
python3 pick_log6.py
```

or

```bash
python3 ./(cloned dir)/firstChiceDataAnalysis/out_PT.py
python3 ./(cloned dir)/firstChiceDataAnalysis/pick_log1.py
python3 ./(cloned dir)/firstChiceDataAnalysis/pick_log6.py
```

# Author

* Takahashi KEISUKE
* keisuke.takahashi@foodtechno-eng.co.jp