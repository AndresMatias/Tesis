from pyecharts import Gauge
gauge=Gauge('Probabilidad de trabajar horas extras hoy')
gauge.add('', "Posibilidad", 99.99, angle_range=[225, -45],
scale_range=[0, 100], is_legend_show=False)
gauge.render()
gauge