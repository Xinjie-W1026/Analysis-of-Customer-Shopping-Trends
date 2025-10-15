import pandas as pd


class ShoppingTrendsAnalyzer:
    def __init__(self, df):
        self.df = df

    def analyze_question1(self):
        """问题1: 性别年龄分布与购买频率"""
        # 性别分布
        gender_dist = self.df['Gender'].value_counts(normalize=True)

        # 年龄分布
        age_dist = self.df['Age Group'].value_counts(normalize=True).sort_index()

        # 不同年龄群体的购买频率
        age_freq = self.df.groupby('Age Group')['Frequency of Purchases'].value_counts(normalize=True)

        return {
            "性别分布": gender_dist.to_dict(),
            "年龄分布": age_dist.to_dict(),
            "不同年龄群体的购买频率": age_freq.unstack().to_dict()
        }

    def analyze_question2(self):
        """问题2: 产品类别与尺寸分析"""
        # 不同产品类别的平均购买量
        category_avg = self.df.groupby('Category')['Purchase Amount (USD)'].mean()

        # 尺寸与购买量关联分析
        size_corr = self.df.groupby('Size')['Purchase Amount (USD)'].mean()

        return {
            "不同产品类别的平均购买量": category_avg.to_dict(),
            "尺寸与购买量关联": size_corr.to_dict()
        }

    def analyze_question3(self):
        """问题3: 性别购买行为"""
        # 性别购买次数
        gender_count = self.df['Gender'].value_counts()

        # 性别平均购买金额
        gender_avg = self.df.groupby('Gender')['Purchase Amount (USD)'].mean()

        return {
            "性别购买次数": gender_count.to_dict(),
            "性别平均购买金额": gender_avg.to_dict()
        }

    def analyze_question4(self):
        """问题4: 类别热门物品与运输偏好"""
        # 每个类别最常购买的物品
        popular_items = self.df.groupby('Category')['Item Purchased'].agg(lambda x: x.mode()[0])

        # 每个类别最受欢迎的运输方式
        shipping_pref = self.df.groupby('Category')['Shipping Type'].agg(lambda x: x.mode()[0])

        return {
            "类别热门物品": popular_items.to_dict(),
            "运输方式偏好": shipping_pref.to_dict()
        }

    def analyze_question5(self):
        """问题5: 季节性消费分析"""
        # 季节性平均支出
        seasonal_avg = self.df.groupby('Season')['Purchase Amount (USD)'].mean()

        return {
            "季节性平均支出": seasonal_avg.to_dict()
        }

    def analyze_question6(self):
        """问题6: 评分与购买金额"""
        # 类别平均评分
        category_rating = self.df.groupby('Category')['Review Rating'].mean()

        # 评分与购买金额关系
        rating_spending = self.df.groupby('Review Rating')['Purchase Amount (USD)'].mean()

        return {
            "类别平均评分": category_rating.to_dict(),
            "评分与购买金额关系": rating_spending.to_dict()
        }

    def analyze_question7(self):
        """问题7: 地理位置购买行为"""
        # 地点平均购买金额
        location_avg = self.df.groupby('Location')['Purchase Amount (USD)'].mean().nlargest(10)

        return {
            "地点平均购买金额": location_avg.to_dict()
        }

    def analyze_question8(self):
        """问题8: 年龄与产品类别关系"""
        # 年龄组与产品类别关系
        age_category = pd.crosstab(self.df['Age Group'], self.df['Category'], normalize='index')

        return {
            "年龄组与产品类别关系": age_category.to_dict()
        }