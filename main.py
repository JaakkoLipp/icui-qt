import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

def button_clicked():
  print("Button clicked!")

if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = QMainWindow()
  window.setWindowTitle("PySide6 Example")

  button = QPushButton("Click me!", window)
  button.clicked.connect(button_clicked)
  button.setGeometry(50, 50, 100, 30)

  window.show()

  sys.exit(app.exec())