import pandas as pd
import datetime

# 获取当前日期
current_date = datetime.datetime.now().strftime('%-m.%d')

# 生成文件名
order_details_file = f'/Users/zyy/Downloads/3.25早订单维度.xlsx'
product_details_file = f'/Users/zyy/Downloads/3.25早商品维度.xlsx'
sheet1_file = '/Users/zyy/Downloads/商品订单.xlsx'
output_file = f'/Users/zyy/Downloads/合并数据_{current_date}.xlsx'

# 读取 Excel 文件
order_details = pd.read_excel(order_details_file, sheet_name='订单明细报表')
product_details = pd.read_excel(product_details_file, sheet_name='订单明细报表')
sheet1 = pd.read_excel(sheet1_file, sheet_name='Sheet1')

# 合并订单明细表和商品明细表，通过订单编号匹配
merged_data = pd.merge(order_details, product_details[['订单编号', '商品名称']], on='订单编号', how='left')

# 合并新的 merged_data 和商品订单表，通过商品名称匹配
merged_data = pd.merge(merged_data, sheet1[['商品名称', '商品直播价']], on='商品名称', how='left')

# 过滤不需要统计的商品名称，订单状态不为“已取消”的数据
filtered_data = merged_data[~merged_data['商品名称'].str.contains('签到|秒杀|visia', case=False, na=False)]
filtered_data = filtered_data[filtered_data['订单状态'] != '已取消']

# 统计每个推广员手机号、订单状态的数量
grouped_data = filtered_data.groupby(['推广员', '推广员手机号', '订单状态']).size().unstack('订单状态', fill_value=0).reset_index()

# 添加“总计”列
grouped_data['总计'] = grouped_data['已完成'] + grouped_data['待发货'] + grouped_data['已发货']

# 只保留“已完成”和“待发货”的数据
grouped_data = grouped_data[(grouped_data['已完成'] > 0) | (grouped_data['待发货'] > 0)]

# 将推广员统计结果追加到新的 Excel 文件中
output_file = f'/Users/zyy/Downloads/合并数据_{current_date}.xlsx'
with pd.ExcelWriter(output_file) as writer:
    filtered_data.to_excel(writer, index=False, sheet_name='订单明细报表')

    # 添加合计行到推广员统计表
    total_row_promoter = grouped_data[['已完成', '待发货', '已发货', '总计']].sum()
    total_row_promoter['推广员'] = '合计'
    total_row_promoter['推广员手机号'] = ''
    grouped_data = pd.concat([grouped_data, pd.DataFrame(total_row_promoter).T], ignore_index=True)

    grouped_data.to_excel(writer, index=False, sheet_name='推广员统计')

    # 统计每个商品名称的订单状态和订单数量，添加“商品直播价”列
    order_summary = filtered_data[['商品名称', '订单状态']].groupby(['商品名称', '订单状态']).size().unstack('订单状态', fill_value=0).reset_index()
    order_summary = pd.merge(order_summary, merged_data[['商品名称', '商品直播价']].drop_duplicates(), on='商品名称', how='left')

    # 添加“已完成金额”列
    order_summary['已完成金额'] = (order_summary['已发货'] + order_summary['已完成']) * order_summary['商品直播价']

    # 添加合计行到订单统计表
    total_row = order_summary[['已完成', '待发货', '已发货', '已完成金额']].sum()
    total_row['商品名称'] = '合计'
    total_row['商品直播价'] = ''
    order_summary = pd.concat([order_summary, pd.DataFrame(total_row).T], ignore_index=True)

    order_summary.to_excel(writer, index=False, sheet_name='订单统计表')

print(f'数据处理完成，结果已保存到文件：{output_file}')