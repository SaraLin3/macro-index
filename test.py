# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:43:57 2023

@author: china
"""

# interactive_chart.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import dcc
from dash import html
# 创建示例数据（替换成你的实际数据）
data = pd.read_excel(r"D:\LJX\工作\4-东方固收\20223-10-10 GCI\副本各相关性指标和流动性.xlsx",index_col=0)
data.replace(0, np.nan, inplace=True)
data.ffill(inplace=True)



# 创建 Streamlit 应用
st.title('资产相关性-流动性框架')

# 多选框，用于选择显示哪些指标
selected_indicators = st.multiselect('选择指标', data.columns)
st.write(f"你选择了：{', '.join(selected_indicators)}")


# 如果有选择的指标，创建图表
if selected_indicators:
    # 创建图表
    fig = go.Figure()

    # 添加主坐标轴数据

    for indicator in data.columns[3:]:
        if indicator in selected_indicators:
            fig.add_trace(go.Scatter(x=data.index, y=data[indicator], mode='lines', name=indicator,yaxis='y1'))


    # 添加次坐标轴并关联数据
    if '全球主要市场股指' in selected_indicators:
        fig.add_trace(
            go.Scatter(x=data.index, y=data['全球主要市场股指'], mode='lines', name='全球主要市场股指', yaxis='y2')
        )
    if '大类资产' in selected_indicators:
        fig.add_trace(
            go.Scatter(x=data.index, y=data['大类资产'], mode='lines', name='大类资产', yaxis='y2')
        )
    if '短债' in selected_indicators:
        fig.add_trace(
            go.Scatter(x=data.index, y=data['短债'], mode='lines', name='短债', yaxis='y2')
        )
    if '长债' in selected_indicators:
        fig.add_trace(
            go.Scatter(x=data.index, y=data['长债'], mode='lines', name='长债', yaxis='y2')
        )
    # 更新次坐标轴
    fig.update_layout(
        yaxis2=dict(
            title='次坐标轴',
            overlaying='y',
            side='right',
            showgrid=False,  # 隐藏次坐标轴的网格线，可根据需要调整
        )
    )

    # fig.update_layout(
    #     xaxis=dict(
    #         rangeselector=dict(
    #             buttons=list([
    #                 dict(count=1, label='1d', step='day', stepmode='backward'),

    #             ])
    #         ),
    #         rangeslider=dict(
    #             visible=True
    #         ),
    #         type='date'
    #     )
    # )
            
    # selected_range = st.slider(
    #     "选择时间范围",
    #     min_value=0,
    #     max_value=len(data) - 1,
    #     value=[0, len(data) - 1],
    #     format="MMM YY",  # 指定时间标签的显示格式
    #  )
    
    # # 在滑动条下方显示当前时间范围
    # start_date = data.index[selected_range[0]].strftime('%Y-%m-%d')
    # end_date = data.index[selected_range[1]].strftime('%Y-%m-%d')
    # st.write(f"当前时间范围：{start_date} 到 {end_date}")
    
    # # 更新图表显示选定的时间范围
    # selected_data = data.loc[selected_range[0]:selected_range[1]]
    # fig.update_xaxes(rangebreaks=[dict(values=data.index[1:-1])])  # 避免 x 轴标签重叠
    # fig.update_xaxes(range=[selected_data.index.min(), selected_data.index.max()])

    # 显示图表
    st.plotly_chart(fig)
    
else:
    st.write('请选择至少一个指标。')
    

