import matplotlib.pyplot as plt
import seaborn as sns
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


class DataVisualizer:
    def __init__(self, df, output_dir):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def visualize_question1(self, results):
        """问题1可视化：性别年龄分布与购买频率"""
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        # 性别分布饼图
        gender_data = results['性别分布']
        axes[0].pie(gender_data.values(), labels=gender_data.keys(), autopct='%1.1f%%')
        axes[0].set_title('性别分布')

        # 年龄分布柱状图
        age_data = results['年龄分布']
        axes[1].bar(age_data.keys(), age_data.values(), color='skyblue')
        axes[1].set_title('年龄分布')
        axes[1].set_xlabel('年龄组')
        axes[1].set_ylabel('比例')

        # 年龄与购买频率热力图
        age_freq_data = results['不同年龄群体的购买频率']
        if age_freq_data:
            # 转换为DataFrame以便绘制热力图
            import pandas as pd
            heatmap_data = pd.DataFrame(age_freq_data).T.fillna(0)
            sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='Blues', ax=axes[2])
            axes[2].set_title('年龄组与购买频率关系')
            axes[2].set_xlabel('购买频率')
            axes[2].set_ylabel('年龄组')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question1_visualization.png'))
        plt.close()

    def visualize_question2(self, results):
        """问题2可视化：产品类别与尺寸分析"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # 不同产品类别的平均购买量
        category_data = results['不同产品类别的平均购买量']
        axes[0].bar(category_data.keys(), category_data.values(), color='lightcoral')
        axes[0].set_title('不同产品类别的平均购买金额')
        axes[0].set_xlabel('产品类别')
        axes[0].set_ylabel('平均购买金额 (USD)')
        axes[0].tick_params(axis='x', rotation=45)

        # 尺寸与购买量关联
        size_data = results['尺寸与购买量关联']
        axes[1].bar(size_data.keys(), size_data.values(), color='lightgreen')
        axes[1].set_title('不同尺寸的平均购买金额')
        axes[1].set_xlabel('尺寸')
        axes[1].set_ylabel('平均购买金额 (USD)')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question2_visualization.png'))
        plt.close()

    def visualize_question3(self, results):
        """问题3可视化：性别购买行为"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # 性别购买次数
        gender_count_data = results['性别购买次数']
        axes[0].bar(gender_count_data.keys(), gender_count_data.values(),
                    color=['skyblue', 'pink'])
        axes[0].set_title('各性别购买次数')
        axes[0].set_xlabel('性别')
        axes[0].set_ylabel('购买次数')

        # 性别平均购买金额
        gender_avg_data = results['性别平均购买金额']
        axes[1].bar(gender_avg_data.keys(), gender_avg_data.values(),
                    color=['skyblue', 'pink'])
        axes[1].set_title('各性别平均购买金额')
        axes[1].set_xlabel('性别')
        axes[1].set_ylabel('平均购买金额 (USD)')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question3_visualization.png'))
        plt.close()

    def visualize_question4(self, results):
        """问题4可视化：类别热门物品与运输偏好"""
        fig, axes = plt.subplots(2, 1, figsize=(12, 10))

        # 类别热门物品
        popular_items_data = results['类别热门物品']
        categories = list(popular_items_data.keys())
        items = list(popular_items_data.values())

        y_pos = range(len(categories))
        colors = ['gold', 'lightblue', 'lightgreen', 'orange']
        axes[0].bar(y_pos, [1] * len(categories), color=colors[:len(categories)])
        axes[0].set_xticks(y_pos)
        axes[0].set_xticklabels(categories)
        axes[0].set_title('每个类别中最常购买的物品')
        axes[0].set_ylabel('类别')

        # 在条形图上标注物品名称
        for i, item in enumerate(items):
            axes[0].text(i, 0.5, item, ha='center', va='center', fontsize=10, rotation=45)

        # 运输方式偏好
        shipping_data = results['运输方式偏好']
        shipping_types = list(shipping_data.values())
        y_pos2 = range(len(categories))
        colors2 = ['purple', 'brown', 'red', 'cyan']
        axes[1].bar(y_pos2, [1] * len(categories), color=colors2[:len(categories)])
        axes[1].set_xticks(y_pos2)
        axes[1].set_xticklabels(categories)
        axes[1].set_title('每个类别最受欢迎的运输方式')
        axes[1].set_ylabel('类别')

        # 在条形图上标注运输方式
        for i, shipping in enumerate(shipping_types):
            axes[1].text(i, 0.5, shipping, ha='center', va='center', fontsize=10, rotation=45)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question4_visualization.png'))
        plt.close()

    def visualize_question5(self, results):
        """问题5可视化：季节性消费分析"""
        seasonal_data = results['季节性平均支出']

        plt.figure(figsize=(10, 6))
        plt.bar(seasonal_data.keys(), seasonal_data.values(), color='lightcoral')
        plt.title('不同季节的平均支出')
        plt.xlabel('季节')
        plt.ylabel('平均支出 (USD)')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question5_visualization.png'))
        plt.close()

    def visualize_question6(self, results):
        """问题6可视化：评分与购买金额"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # 类别平均评分
        category_rating_data = results['类别平均评分']
        axes[0].bar(category_rating_data.keys(), category_rating_data.values(), color='gold')
        axes[0].set_title('每个产品类别的平均评分')
        axes[0].set_xlabel('产品类别')
        axes[0].set_ylabel('平均评分')
        axes[0].tick_params(axis='x', rotation=45)

        # 评分与购买金额关系
        rating_spending_data = results['评分与购买金额关系']
        axes[1].plot(list(rating_spending_data.keys()), list(rating_spending_data.values()),
                     marker='o', color='purple')
        axes[1].set_title('评论评级与平均购买金额的关系')
        axes[1].set_xlabel('评论评级')
        axes[1].set_ylabel('平均购买金额 (USD)')

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question6_visualization.png'))
        plt.close()

    def visualize_question7(self, results):
        """问题7可视化：地理位置购买行为"""
        location_data = results['地点平均购买金额']

        plt.figure(figsize=(12, 6))
        plt.bar(location_data.keys(), location_data.values(), color='lightblue')
        plt.title('平均购买金额最高的前10个地点')
        plt.xlabel('地点')
        plt.ylabel('平均购买金额 (USD)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question7_visualization.png'))
        plt.close()

    def visualize_question8(self, results):
        """问题8可视化：年龄与产品类别关系"""
        import pandas as pd
        age_category_data = pd.DataFrame(results['年龄组与产品类别关系']).T

        plt.figure(figsize=(12, 8))
        sns.heatmap(age_category_data, annot=True, fmt='.2f', cmap='Blues')
        plt.title('年龄组与产品类别关系热力图')
        plt.xlabel('产品类别')
        plt.ylabel('年龄组')
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'question8_visualization.png'))
        plt.close()

    def create_all_visualizations(self, results):
        """为所有问题创建可视化图表"""
        self.visualize_question1(results['question1'])
        self.visualize_question2(results['question2'])
        self.visualize_question3(results['question3'])
        self.visualize_question4(results['question4'])
        self.visualize_question5(results['question5'])
        self.visualize_question6(results['question6'])
        self.visualize_question7(results['question7'])
        self.visualize_question8(results['question8'])
        print("所有可视化图表已生成并保存到 output/figures/ 目录")