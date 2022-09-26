import re

def df_revision(
    file_path,
    multi_params_name,
    single_params,
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
        Dict[str, list]: 整理されたデータが辞書で返ってきます。

    English

    A fusion of single and multi-parameter,
    CSV-like and non-CSV files into a clean CSV file.
    Function to turn a CSV file into a CSV file

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
        Dict[str, list]: A dictionary with revised data is returned.

    """

    with open(file_path, 'r', encoding=encoding) as f:
        file_lines = f.read().splitlines()

        if has_header:
            file_lines.pop(0)

        file_lines = [
            line.split(',') for line in file_lines
        ]

    shaped_values = {
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
                    file_lines[y].remove(value)
                    break

    # 残ったデータを最後を整形データに追加
    shaped_values[multi_params_name] = file_lines

    return shaped_values
