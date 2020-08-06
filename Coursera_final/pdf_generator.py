from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph , Spacer , Image , Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
fruits = {
    "apple" : 1,
    "banana" : 2,
    "orange" : 5,
    "Mango" : 3,
    "kiwi" : 10,
    "pomegranade" : 1,
    "strawberry":3
}
two_d = list()
for k,v in fruits.items():
    two_d.append([k,v])
print(two_d)
styles = getSampleStyleSheet()
report_title = Paragraph("A complete invetory of fruits ",styles["h1"])
report = SimpleDocTemplate("report.pdf")
# report.build([report_title])
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=two_d, style=table_style, hAlign="LEFT")
report_pie = Pie(width = 3*inch , height = 3*inch)

report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruits):
    report_pie.data.append(fruits[fruit_name])
    report_pie.labels.append(fruit_name)
print(report_pie.data)
print(report_pie.labels)
report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title,report_table,report_chart])

