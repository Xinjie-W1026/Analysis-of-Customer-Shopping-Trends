from data_loader import load_data
from analysis import ShoppingTrendsAnalyzer
from visualization import DataVisualizer
import os
import sys


def generate_report(results, output_dir):
    """生成分析报告"""
    report_path = os.path.join(output_dir, 'analysis_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=== 顾客购物趋势分析报告 ===\n\n")

        # 问题1结果
        q1 = results['question1']
        f.write("1. 性别和年龄分布:\n")
        f.write(f"   性别分布: {q1['性别分布']}\n")
        f.write(f"   年龄分布: {q1['年龄分布']}\n")
        f.write(f"   不同年龄群体的购买频率: {q1['不同年龄群体的购买频率']}\n\n")

        # 问题2结果
        q2 = results['question2']
        f.write("2. 产品类别与尺寸分析:\n")
        f.write(f"   不同产品类别的平均购买量: {q2['不同产品类别的平均购买量']}\n")
        f.write(f"   尺寸与购买量关联: {q2['尺寸与购买量关联']}\n\n")

        # 问题3结果
        q3 = results['question3']
        f.write("3. 性别购买行为:\n")
        f.write(f"   性别购买次数: {q3['性别购买次数']}\n")
        f.write(f"   性别平均购买金额: {q3['性别平均购买金额']}\n\n")

        # 问题4结果
        q4 = results['question4']
        f.write("4. 类别热门物品与运输偏好:\n")
        f.write(f"   类别热门物品: {q4['类别热门物品']}\n")
        f.write(f"   运输方式偏好: {q4['运输方式偏好']}\n\n")

        # 问题5结果
        q5 = results['question5']
        f.write("5. 季节性消费分析:\n")
        f.write(f"   季节性平均支出: {q5['季节性平均支出']}\n\n")

        # 问题6结果
        q6 = results['question6']
        f.write("6. 评分与购买金额:\n")
        f.write(f"   类别平均评分: {q6['类别平均评分']}\n")
        f.write(f"   评分与购买金额关系: {q6['评分与购买金额关系']}\n\n")

        # 问题7结果
        q7 = results['question7']
        f.write("7. 地理位置购买行为:\n")
        f.write(f"   地点平均购买金额: {q7['地点平均购买金额']}\n\n")

        # 问题8结果
        q8 = results['question8']
        f.write("8. 年龄与产品类别关系:\n")
        f.write(f"   年龄组与产品类别关系: {q8['年龄组与产品类别关系']}\n\n")

    print(f"分析报告已保存至 {report_path}")


def main():
    try:
        # 获取项目根目录
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 创建输出目录
        output_dir = os.path.join(base_dir, 'output')
        figures_dir = os.path.join(output_dir, 'figures')
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(figures_dir, exist_ok=True)

        # 加载数据
        df = load_data()

        # 初始化分析器
        analyzer = ShoppingTrendsAnalyzer(df)

        # 执行所有分析
        results = {
            'question1': analyzer.analyze_question1(),
            'question2': analyzer.analyze_question2(),
            'question3': analyzer.analyze_question3(),
            'question4': analyzer.analyze_question4(),
            'question5': analyzer.analyze_question5(),
            'question6': analyzer.analyze_question6(),
            'question7': analyzer.analyze_question7(),
            'question8': analyzer.analyze_question8()
        }

        # 生成可视化图表
        visualizer = DataVisualizer(df, figures_dir)
        visualizer.create_all_visualizations(results)

        # 生成报告
        generate_report(results, output_dir)

        print("分析完成！")
        print(f"可视化图表保存在: {figures_dir}")
        print(f"分析报告保存在: {output_dir}")

    except Exception as e:
        print(f"发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()