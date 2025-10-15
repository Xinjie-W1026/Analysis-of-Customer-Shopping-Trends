import pandas as pd
import os


def load_data():
    """
    加载并预处理数据
    """
    # 获取当前脚本所在目录的父目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'shopping_trends.csv')

    # 检查文件是否存在
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"数据文件未找到: {data_path}")

    df = pd.read_csv(data_path)

    # 创建年龄分组
    bins = [0, 20, 30, 40, 50, 60, 100]
    labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

    return df