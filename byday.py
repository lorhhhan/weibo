import pandas as pd
#导入配置模块
from pyecharts import options as opts
from pyecharts.charts import  *
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.faker import Faker
# # 导入Excel 文件
path="H:/byday.xlsx"
# data = xlrd.open_workbook(path)

data = pd.read_excel(path)
# print(data)
data.loc[:,'发布日期']=data.loc[:,'发布日期'].astype('str')
# print(data.loc[:,'截止日期'])
x_data=data.loc[:,'发布日期'][::-1].values.tolist()
# print(x_data)
ldbl_num=data.loc[:,'热度趋势'][::-1].values.tolist()

lxzf_num=data.loc[:,'点赞量'][::-1].values.tolist()
zbzz_num=data.loc[:,'转发量'][::-1].values.tolist()
cqbl_num=data.loc[:,'评论量'][::-1].values.tolist()

bar=Bar()
#增加横轴数据
bar.add_xaxis(xaxis_data=x_data)
#增加纵轴数据
bar.add_yaxis(
    series_name='点赞量',
    y_axis=lxzf_num ,
    yaxis_index=0,
).add_yaxis(
    series_name='转发量',
    y_axis=zbzz_num,
    yaxis_index=2, #使用的y轴的index，在单个图表实例中存在多个y轴的时候有用
    stack="stack1",#柱状堆叠
).add_yaxis(
    series_name='评论量',
    y_axis=cqbl_num,
    yaxis_index=2, #使用的y轴的index，在单个图表实例中存在多个y轴的时候有用
    stack="stack1",
)

# c.添加 额外的坐标轴
bar.extend_axis(
    # 对y轴配置
    yaxis=opts.AxisOpts(
        type_='value',#value 代表数据轴 ，category 代表类目轴，time代表时间轴
         name='转发量/评论量', #轴的名称
         is_show=True,#展示该轴
        min_=0, #轴刻度的最小值
        max_=60000,#轴刻度的最大值
        position='right',
        # 轴线配置
        axisline_opts=opts.AxisLineOpts(
            is_show=True,#显示轴线
            # 轴线风格
            linestyle_opts=opts.LineStyleOpts(
                color='#708090',
            )
        ),
    #     轴线对应的标签
        axislabel_opts=opts.LabelOpts(
                formatter='{value}', #轴线对应的标签 ----{value}---数据
        )
    )
)

bar.extend_axis(
    # 对y轴配置
    yaxis=opts.AxisOpts(
        type_='value',#value 代表数据轴 ，category 代表类目轴，time代表时间轴
         name='存货周转天数(天)', #轴的名称
         is_show=False,#展示该轴
        min_=0, #轴刻度的最小值
        max_=60000,#轴刻度的最大值
        position='right',
        offset=-10,  #轴线偏移
        # 轴线配置
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示轴线
            # 轴线风格
            linestyle_opts=opts.LineStyleOpts(
                color='#708090',
            )
        ),
        #     轴线对应的标签
        axislabel_opts=opts.LabelOpts(
            formatter='{value}',  # 轴线对应的标签 ----{value}---数据
        )
    )
)
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title='微博关于”ChatGPT“话题热度数据图(按日)',#标题
        subtitle='话题评论量、转发量、点赞量与总体热度趋势',#子标题
        # 设置标题样式
        subtitle_textstyle_opts=opts.TextStyleOpts(
            font_size=12,
            width=1.5,
            color='#000000',
 ),
    pos_left='3%',#title位置
    pos_top='1%'
),
# 图例设置
legend_opts=opts.LegendOpts(
    pos_top='7%', #图例位置
    pos_left='25%',),
# 提示款
tooltip_opts=opts.TooltipOpts(
    trigger='axis',  # 'axis': 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
    axis_pointer_type='cross',  # 'cross'：十字准星指示器。其实是种简写，表示启用两个正交的轴的 axisPointer。
),
# 对纵轴的全局配置
yaxis_opts=opts.AxisOpts(
    type_='value',
    name='热度趋势/点赞量',
    position='left',
    min_=0,
    max_=180000,
    offset=0,
    # 轴线配置
    axisline_opts=opts.AxisLineOpts(
        is_show=True,  # 显示轴线
        # 轴线风格
        linestyle_opts=opts.LineStyleOpts(
            color='#000000',
        )
    ),
    #     轴线对应的标签
    axislabel_opts=opts.LabelOpts(
        formatter='{value}',  # 轴线对应的标签 ----{value}---数据
    )
),
)
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),#显示标签

)
bar.datazoom_opts = [opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]#横轴缩放
#绘制
line_ensur=Line()
#添加横轴
line_ensur.add_xaxis(x_data)

#添加纵轴
line_ensur.add_yaxis(series_name='热度趋势',
                     y_axis=ldbl_num,
                     color='#4b0101',
                     # yaxis_index=2,
                     label_opts=opts.LabelOpts(
                         is_show=False,),
                     # 线配置
                     linestyle_opts=opts.LineStyleOpts(
                         width=1.2,
                         color='#FFA500',
                     )
                     )
line_suspect=Line()
#a.添加横轴
line_suspect.add_xaxis(x_data)

#b.添加纵轴
# line_suspect.add_yaxis(series_name='速动比率',
#                        y_axis=sdbl_num,
#                        color='#FFA500',
#                        yaxis_index=0,
#                        # 标签配置
#                        label_opts=opts.LabelOpts(
#                            is_show=False),
#                        # 线配置
#                        linestyle_opts=opts.LineStyleOpts(
#                                        width=1.2,
#                            color='#00BFFF'
#                        )
#                        )
all=bar.overlap(line_ensur).overlap(line_suspect)
aa=Grid(
    #画布配置
    init_opts=opts.InitOpts(
        width="2500px",  #图的大小
        height='450px',

))
aa.add(all,
       #网格配置
       grid_opts=opts.GridOpts(
           pos_top="20%",
           pos_left="5%",
           pos_right="40%",
       ),
       # 索引
       is_control_axis_index=True #控制索引
       )
aa.render('H:\weibobar1.html')
# aa.show()