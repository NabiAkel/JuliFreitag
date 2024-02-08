from PyQt6.QtCharts import QChart, QChartView, QValueAxis, QSplineSeries, QDateTimeAxis, QLineSeries
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor

#pyqt6-charts installieren
class ChartView(QChartView):

    def __init__(self, parent):
        super().__init__(parent)

        # Achsen erstellen + Format für Datum setzen + beschriften (Datum)
        self.date_axis = QDateTimeAxis()
        self.date_axis.setFormat("dd.MMMM.yyyy")
        self.date_axis.setTitleText("Jahr")
        self.date_axis.setGridLineColor(QColor("blue"))

        # Achse mit QDateTime festlegen
        start_date_time = QDateTime().currentDateTime()
        end_date_time = QDateTime().currentDateTime().addYears(10)
        self.date_axis.setRange(start_date_time, end_date_time)

        # Achse mit speziellem DatumsBereich festlegen
        #start_date_time1 = QDateTime(2020, 11, 11, 0, 0)
        #end_date_time1 = QDateTime(2033, 11, 11, 0, 0)
        #self.date_axis.setRange(start_date_time1, end_date_time1)

        # Achse erstellen + Reichweite + beschriften + Gitter färben + Beschriftung(Reichweite) färben (Zahlen)
        self.value_axis = QValueAxis()
        self.value_axis.setRange(2, 10)
        self.value_axis.setTitleText("Preis in €")
        self.value_axis.setGridLineColor(QColor("blue"))
        self.value_axis.setLabelsColor(QColor("blue"))

        # chart erstellen und Achsen setzen
        self.chart = QChart()
        self.chart.addAxis(self.date_axis, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.value_axis, Qt.AlignmentFlag.AlignLeft)
        # Hintergrundfarbe setzen
        self.chart.setBackgroundBrush(QColor("white"))

        self.setChart(self.chart)

        # SplineSeries erstellen und Farbe setzen
        self.series = QSplineSeries()
        self.series.setColor(QColor("red"))

        self.series1 = QSplineSeries()
        self.series1.setColor(QColor("blue"))
        #SplineSeries/Lineseries erstellen um zweiten Graphen zu erstelle

        # series mit festgelegtem Datum hinzufügen (Jahr, Monat, Tag, Stunde, Minute)
        #für zweite series kopieren und anpassen
        self.series.append(QDateTime(2024, 2, 10, 0, 0).toMSecsSinceEpoch(), 3.5)
        self.series.append(QDateTime(2026, 2, 10, 0, 0).toMSecsSinceEpoch(), 6.5)
        self.series.append(QDateTime(2028, 2, 10, 0, 0).toMSecsSinceEpoch(), 8.5)
        self.series.append(QDateTime(2030, 2, 10, 0, 0).toMSecsSinceEpoch(), 3.5)
        self.series.append(QDateTime(2032, 2, 10, 0, 0).toMSecsSinceEpoch(), 7.5)

        self.series1.append(QDateTime(2024, 3, 10, 0, 0).toMSecsSinceEpoch(), 3.5)
        self.series1.append(QDateTime(2026, 3, 10, 0, 0).toMSecsSinceEpoch(), 6.5)
        self.series1.append(QDateTime(2028, 3, 10, 0, 0).toMSecsSinceEpoch(), 8.5)
        self.series1.append(QDateTime(2030, 3, 10, 0, 0).toMSecsSinceEpoch(), 3.5)
        self.series1.append(QDateTime(2032, 3, 10, 0, 0).toMSecsSinceEpoch(), 7.5)
        # dem chart hinzufügen + Series den Axen zufügen + Name setzen
        #dem chart auch die zweite Series hinzufügen, falls benötigt
        self.chart.addSeries(self.series)
        self.series.attachAxis(self.date_axis)
        self.series.attachAxis(self.value_axis)
        self.series.setName("Preisverlauf Döner")

        self.chart.addSeries(self.series1)
        self.series1.attachAxis(self.date_axis)
        self.series1.attachAxis(self.value_axis)
        self.series1.setName("Preisverlauf Kebab")

# 2. Series erstellen, wenn keine QDatetime gesetzt wäre, selbst Datum setzen (QLineSeries)
#        self.series2 = QLineSeries()
#        self.series2.append(2024, 8)
#        self.series2.append(2026, 3.5)
#        self.series2.append(2028, 6)
#        self.series2.append(2030, 10)
#        self.series2.append(2032, 4)
#        self.chart.addSeries(self.series2)
#        self.series2.attachAxis(self.date_axis)
#        self.series2.attachAxis(self.value_axis)
#        self.series2.setName("Preisverlauf Burger")

        # 3. Series mit click to draw
        #self.series3 = QSplineSeries()
        #self.series3.setName("Manuell")
        #self.series3.setColor(QColor("green"))
        #self.chart.addSeries(self.series3)
        #self.series3.attachAxis(self.date_axis)
        #self.series3.attachAxis(self.value_axis)

    # mousePressEvent für series3, genau so wie mouseReleaseEvent
    def mousePressEvent(self, event) -> None:
        my_point = self.chart.mapToValue(event.pos().toPointF(), self.series3)
        self.series3.append(my_point)