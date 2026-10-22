class Printer:
  def print(self, text: str):
    print(f"printing: {text}")

class ReportGenerator: 
  def __init__(self, printer: Printer):
    printer.print(self.content)

printer = Printer()
quarter_report = ReportGenerator("Q1 Academic Performance: Excellent!")

quarter_report.output_report(printer)
