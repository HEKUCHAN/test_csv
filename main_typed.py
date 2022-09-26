import re
import pandas as pd
from typing import Any, Dict, List

def df_revision(
    file_path: str,
    multi_params_name: str,
    single_params: Dict[str, str],
    encoding='utf-8',
    has_header=True
):
    """Data Frame Revision Function
    Japanese

    シングルパラメーターとマルチパラメーターが融合した、CSVのようでCSVじゃないファイルを綺麗な
    CSVファイルにする関数

    Args:
        file_path(str): 読み込むCSVファイルのパス
        multi_params_name(str): マルチパラメーターの名前
        single_params(Dict[str]): シングルパラメーターの名前をキー、条件式となる正規表現を
            値となった辞書

            Example:
            {
                '顧客ID': 'Customer[0-9]{1,}',
                '年齢': '[0-9]{,3}'
            }
        encoding(str, optional): ファイルのエンコードタイプ。デフォルトは`utf-8`.
        has_header(bool, optional): CSVファイルのヘッダの有無。デフォルトは`True`

    Returns:
        DataFrame: 整理されたデータがpandas DataFrameで返ってきます。

    English

    Args:
        file_path(str): Add the file path you want to modify
        multi_params_name(str): Add multi-parameter names
        single_params(str): Add a dictionary with the name of the single value as the key and
            the regular expression that is the conditional expression of the single value as the value

            Example:
            {
                'CustomerID': 'Customer[0-9]{1,}',
                'age': '[0-9]{,3}'
            }
        encoding(str, optional): Add the character encoding type. Default is `utf-8`.
        has_header(bool, optional): Presence of headers in CSV file. default is `True`

    Returns:
        DataFrame: A DataFrame of pandas with revised data is returned.

    """

    with open(file_path, 'r', encoding=encoding) as f:
        file_lines: List[str] = f.read().splitlines()

        if has_header:
            file_lines.pop(0)

        file_lines: List[List[str]] = [
            line.split(',') for line in file_lines
        ]

    shaped_values: Dict[str, List[Any]] = {
        param: [] for param in single_params
    }
    shaped_values[multi_params_name] = []

    # マルチパラメーター以外を取得し、該当したら削除
    for param in single_params:
        for y, line in enumerate(file_lines):
            for x, value in enumerate(line):
                if re.fullmatch(
                    single_params[param], value
                ):
                    shaped_values[param].append(value)
                    file_lines[y].pop(x)
                    break

    # 残ったデータを最後を整形データに追加
    shaped_values[multi_params_name] = file_lines

    return pd.DataFrame(shaped_values)
