
import sys

from PySide6.QtWidgets import QApplication,QMainWindow
from my_convertor import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        # Add items to the unit conversion combobox
        self.ui.c_units.addItems(["Length", "Weight", "Temperature", "Digital"])

        # Set the initial category and update the units accordingly
        self.ui.c_units.setCurrentText("Weight")
        self.update_units(self.ui.c_units.currentIndex())

        # Connect the signal for combobox item change
        self.ui.c_units.currentIndexChanged.connect(self.update_units)
        self.ui.btn_calculate.clicked.connect(self.convertor)

    def update_units(self, index):
        # Clear previous items in unit comboboxes
        self.ui.c_unit_from.clear()
        self.ui.c_unit_to.clear()

        # Define unit conversion options based on selected category
        unit_options = {
            "Length": ["Millimeter", "Centimeter", "Meter", "Kilometer", "Inch"],
            "Weight": ["Gram", "Kilogram", "Ton", "Pound"],
            "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
            "Digital": ["Bit", "Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]
        }

        # Add items to the unit comboboxes based on selected category
        self.ui.c_unit_from.addItems(unit_options[self.ui.c_units.currentText()])
        self.ui.c_unit_to.addItems(unit_options[self.ui.c_units.currentText()])


    def convertor(self):
        input_unit = self.ui.c_unit_from.currentText()
        output_unit = self.ui.c_unit_to.currentText()
        input_num = float(self.ui.linE_input.text())

        if input_unit == output_unit:
            self.ui.linE_output.setText(str(input_num))

        elif self.ui.c_units.currentText() == "Length":
            output_num = self.length_converter(input_unit, output_unit, input_num)

        elif self.ui.c_units.currentText() == "Weight":
            output_num = self.weight_converter(input_unit, output_unit, input_num)

        elif self.ui.c_units.currentText() == "Temperature":
            output_num = self.temperature_converter(input_unit, output_unit, input_num)

        elif self.ui.c_units.currentText() == "Digital":
            output_num = self.digital_converter(input_unit, output_unit, input_num)


        self.ui.linE_output.setText(str(output_num))



    def length_converter(self, input_unit, output_unit, input_num):
        
        print(input_unit,output_unit,input_num)
        conversion_table = {
            "Millimeter": {"Centimeter": lambda x: x / 10, "Meter": lambda x: x / 1000, "Kilometer": lambda x: x / 1e+6, "Inch": lambda x: x * 0.0393701},
            "Centimeter": {"Millimeter": lambda x: x * 10, "Meter": lambda x: x / 100, "Kilometer": lambda x: x / 100000, "Inch": lambda x: x * 0.393701},
            "Meter": {"Millimeter": lambda x: x * 1000, "Centimeter": lambda x: x * 100, "Kilometer": lambda x: x / 1000, "Inch": lambda x: x * 39.3701},
            "Kilometer": {"Millimeter": lambda x: x * 1e+6, "Centimeter": lambda x: x * 100000, "Meter": lambda x: x * 1000, "Inch": lambda x: x * 39370.1},
            "Inch": {"Millimeter": lambda x: x * 25.4, "Centimeter": lambda x: x * 2.54, "Meter": lambda x: x * 0.0254, "Kilometer": lambda x: x * 2.54e-5}
        }
    
        # انجام تبدیل
        result = conversion_table[input_unit][output_unit](input_num)
        return result


    def weight_converter(self, input_unit, output_unit, input_num):
        # توابع تبدیل وزن را اضافه کنید
        conversion_table = {
            "Gram": {"Kilogram": lambda x: x / 1000, "Ton": lambda x: x / 1000000, "Pound": lambda x: x * 0.00220462},
            "Kilogram": {"Gram": lambda x: x * 1000, "Ton": lambda x: x / 1000, "Pound": lambda x: x * 2.20462},
            "Ton": {"Gram": lambda x: x * 1000000, "Kilogram": lambda x: x * 1000, "Pound": lambda x: x * 2204.62},
            "Pound": {"Gram": lambda x: x * 453.592, "Kilogram": lambda x: x * 0.453592, "Ton": lambda x: x * 0.000453592}
        }


        result = conversion_table[input_unit][output_unit](input_num)
        return result
  
    def temperature_converter(self, input_unit, output_unit, input_num):
    # توابع تبدیل دما را اضافه کنید
        if input_unit == "Celsius" and output_unit == "Fahrenheit":
            result = (input_num * 9/5) + 32
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            result = input_num + 273.15
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            result = (input_num - 32) * 5/9
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            result = (input_num - 32) * 5/9 + 273.15
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            result = input_num - 273.15
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            result = (input_num - 273.15) * 9/5 + 32
        else:
            result = input_num  
        return result

    
    def digital_converter(self, input_unit, output_unit, input_num):

        conversion_table = {
            "Bit": {"Byte": lambda x: x / 8, "Kilobyte": lambda x: x / 8192, "Megabyte": lambda x: x / 8388608, "Gigabyte": lambda x: x / 8589934592, "Terabyte": lambda x: x / 8796093022208},
            "Byte": {"Bit": lambda x: x * 8, "Kilobyte": lambda x: x / 1024, "Megabyte": lambda x: x / 1048576, "Gigabyte": lambda x: x / 1073741824, "Terabyte": lambda x: x / 1099511627776},
            "Kilobyte": {"Bit": lambda x: x * 8192, "Byte": lambda x: x * 1024, "Megabyte": lambda x: x / 1024, "Gigabyte": lambda x: x / 1048576, "Terabyte": lambda x: x / 1073741824},
            "Megabyte": {"Bit": lambda x: x * 8388608, "Byte": lambda x: x * 1048576, "Kilobyte": lambda x: x * 1024, "Gigabyte": lambda x: x / 1024, "Terabyte": lambda x: x / 1048576},
            "Gigabyte": {"Bit": lambda x: x * 8589934592, "Byte": lambda x: x * 1073741824, "Kilobyte": lambda x: x * 1048576, "Megabyte": lambda x: x * 1024, "Terabyte": lambda x: x / 1024},
            "Terabyte": {"Bit": lambda x: x * 8796093022208, "Byte": lambda x: x * 1099511627776, "Kilobyte": lambda x: x * 1073741824, "Megabyte": lambda x: x * 1048576, "Gigabyte": lambda x: x * 1024}
        }

        result = conversion_table[input_unit][output_unit](input_num)
        return result

    

my_app = QApplication(sys.argv)

my_window = MainWindow()

my_window.show()
my_window.ui.btn_calculate.clicked.connect(my_window.convertor)

my_app.exec()
