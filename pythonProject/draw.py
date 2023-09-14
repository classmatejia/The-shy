import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class CarDataPlotter:
    def __init__(self, csv_file):

        self.df = pd.read_csv(csv_file)
        self.data_dict = self._process_data()

    def _process_data(self):
        selected_columns = self.df[["mileage", "price"]]
        data_dict = selected_columns.to_dict(orient='list')
        matched_data_dict = {}
        for column, data in data_dict.items():
            matched_data = []
            for value in data:
                matches = re.findall(r'\d+\.\d+|\d+', value)
                matched_data.extend(matches)
            matched_data_dict[column] = matched_data
        return matched_data_dict

    def plot_price_vs_mileage(self):
        mileage = np.array([float(x) for x in self.data_dict["mileage"]])
        price = np.array([float(x) for x in self.data_dict["price"]])

        sorted_indices = np.argsort(mileage)
        mileage = mileage[sorted_indices]
        price = price[sorted_indices]

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(mileage, price, marker='o', linestyle='-', color='b')

        ax.set_title('Price vs. Mileage')
        ax.set_xlabel('Mileage')
        ax.set_ylabel('Price')

        ax.grid(True)
        plt.show()

    def plot_pie_chart(self):
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用SimHei或其他中文字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负号'-'显示问题

        # 统计每个城市出现的频率
        city_counts = self.df['city'].value_counts()

        # 创建饼图
        plt.figure(figsize=(8, 8))
        plt.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%', startangle=140, pctdistance=0.85)

        # 设置图形标题
        plt.title('二手车城市分布')

        # 调整图形位置以使百分比数字移到饼图的最外围
        plt.gca().set_aspect('equal')
        plt.subplots_adjust(left=0.1, right=0.9)

        # 显示图形
        plt.show()


# 创建CarDataPlotter对象并调用plot_price_vs_mileage方法
csv_file = './data/benchiji.csv'  # 请将'your_file.csv'替换为实际的CSV文件路径
plotter = CarDataPlotter(csv_file)
plotter.plot_price_vs_mileage()

plotter.plot_pie_chart()
