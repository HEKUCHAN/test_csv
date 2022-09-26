from itertools import chain
from sample import df_revision

def test_normal_data():
    test_data_path = './test_data/normal_data.csv'

    correct_data = {
        '年齢': ['22', '33', '54', '42'],
        '行ってみたい都市': [
            ['ローマ', 'フィレンツェ', 'パリ'],
            ['ロンドン'],
            ['ワシントン', 'ロンドン', 'アテネ'],
            ['プラハ']
        ],
        '顧客ID': [
            'Customer000001',
            'Customer000002',
            'Customer000003',
            'Customer000004'
        ]
    }

    testing_data = df_revision(
        file_path=test_data_path,
        multi_params_name='行ってみたい都市',
        single_params={
            '顧客ID': 'Customer[0-9]{1,}',
            '年齢': '[0-9]{,3}'
        }
    )

    assert testing_data == correct_data

def test_random_order_data():
    test_data_path = './test_data/random_order_data.csv'

    correct_data = {
        '年齢': ['22', '33', '54', '42'],
        '行ってみたい都市': [
            ['ローマ', 'フィレンツェ', 'パリ'],
            ['ロンドン'],
            ['ワシントン', 'ロンドン', 'アテネ'],
            ['プラハ']
        ],
        '顧客ID': [
            'Customer000001',
            'Customer000002',
            'Customer000003',
            'Customer000004'
        ]
    }

    testing_data = df_revision(
        file_path=test_data_path,
        multi_params_name='行ってみたい都市',
        single_params={
            '顧客ID': 'Customer[0-9]{1,}',
            '年齢': '[0-9]{,3}'
        }
    )

    assert testing_data == correct_data

def test_a_lot_of_data():
    test_data_path = './test_data/a_lot_of_data.csv'

    num = 50000

    correct_data = {
        '年齢': list(chain.from_iterable(
            [['22', '33', '54', '42'] for _ in range(num)])),
        '行ってみたい都市': list(chain.from_iterable([[
            ['ローマ', 'フィレンツェ', 'パリ'],
            ['ロンドン'],
            ['ワシントン', 'ロンドン', 'アテネ'],
            ['プラハ']
        ] for _ in range(num)])),
        '顧客ID': list(chain.from_iterable([[
            'Customer000001',
            'Customer000002',
            'Customer000003',
            'Customer000004'
        ] for _ in range(num)]))
    }

    testing_data = df_revision(
        file_path=test_data_path,
        multi_params_name='行ってみたい都市',
        single_params={
            '顧客ID': 'Customer[0-9]{1,}',
            '年齢': '[0-9]{,3}'
        }
    )

    assert testing_data == correct_data