from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_FileVault(QtCore.QObject):  # Inherit from QObject to use as an event filter
    def setupUi(self, FileVault):
        # Set the main dialog window properties
        FileVault.setObjectName("FileVault")
        FileVault.setFixedSize(900, 600)  # Set the window to a fixed size (900x600)

        # Previous button for backward navigation
        self.previousButton = QtWidgets.QPushButton(parent=FileVault)
        self.previousButton.setGeometry(QtCore.QRect(20, 10, 30, 30))  # Set button position and size
        self.previousButton.setObjectName("PreviousButton")
        self.previousButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.previousButton.installEventFilter(self)  # Install event filter to track hover events

        # Next button for forward navigation
        self.nextButton = QtWidgets.QPushButton(parent=FileVault)
        self.nextButton.setGeometry(QtCore.QRect(60, 10, 30, 30))  # Set button position and size
        self.nextButton.setObjectName("NextButton")
        self.nextButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.nextButton.installEventFilter(self)  # Install event filter

        # Address bar label to display the current directory or file path
        self.addressBar = QtWidgets.QLabel(parent=FileVault)
        self.addressBar.setGeometry(QtCore.QRect(100, 10, 500, 30))  # Set address bar position and size
        self.addressBar.setFrameShape(QtWidgets.QFrame.Shape.Box)  # Add a border to the address bar
        self.addressBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)  # Set shadow effect
        self.addressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.addressBar.setObjectName("AddressBar")

        # Tool button for additional tools or settings
        self.toolsButton = QtWidgets.QToolButton(parent=FileVault)
        self.toolsButton.setGeometry(QtCore.QRect(600, 10, 30, 30))  # Set button position and size
        self.toolsButton.setObjectName("ToolsButton")
        self.toolsButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.toolsButton.installEventFilter(self)  # Install event filter

        # Options button for file or app options
        self.optionsButton = QtWidgets.QPushButton(parent=FileVault)
        self.optionsButton.setGeometry(QtCore.QRect(650, 10, 30, 30))  # Set button position and size
        self.optionsButton.setObjectName("OptionsButton")
        self.optionsButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.optionsButton.installEventFilter(self)  # Install event filter

        # Horizontal line separator to divide top navigation and content areas
        self.horizontalLine = QtWidgets.QFrame(parent=FileVault)
        self.horizontalLine.setGeometry(QtCore.QRect(0, 50, 900, 3))  # Set position and size of the line
        self.horizontalLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)  # Set horizontal line shape
        self.horizontalLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)  # Add shadow effect
        self.horizontalLine.setObjectName("HorizontalLine")

        # Main content area widget where files and folders will be displayed
        self.mainArea = QtWidgets.QWidget(parent=FileVault)
        self.mainArea.setGeometry(QtCore.QRect(180, 50, 722, 550))  # Set main area position and size
        self.mainArea.setObjectName("MainArea")

        # Vertical line separator between the side and main areas
        self.verticalLine = QtWidgets.QFrame(parent=FileVault)
        self.verticalLine.setGeometry(QtCore.QRect(180, 50, 3, 550))  # Set position and size of the vertical line
        self.verticalLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)  # Set vertical line shape
        self.verticalLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)  # Add shadow effect
        self.verticalLine.setObjectName("VerticalLine")

        # Side panel widget where additional options or directory structure could be displayed
        self.sideArea = QtWidgets.QWidget(parent=FileVault)
        self.sideArea.setGeometry(QtCore.QRect(0, 50, 180, 550))  # Set side area position and size
        self.sideArea.setObjectName("SideArea")

        # Tooltip label (hidden by default) that will appear below the buttons
        self.tooltipLabel = QtWidgets.QLabel(parent=FileVault)
        self.tooltipLabel.setStyleSheet("background-color: black; border: 1px solid black;")  # Tooltip styling
        self.tooltipLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tooltipLabel.setVisible(False)  # Initially hidden

        # Setup a QTimer for delayed tooltip appearance
        self.hoverTimer = QtCore.QTimer()
        self.hoverTimer.setSingleShot(True)  # Run only once after timeout
        self.hoverTimer.timeout.connect(self.showTooltip)  # Connect to the method that shows the tooltip
        self.hoveredButton = None  # Store the button being hovered over

        # Setup the window labels, button text, etc.
        self.retranslateUi(FileVault)
        QtCore.QMetaObject.connectSlotsByName(FileVault)

    def retranslateUi(self, FileVault):
        _translate = QtCore.QCoreApplication.translate
        FileVault.setWindowTitle(_translate("FileVault", "FileVault"))
        self.previousButton.setText(_translate("FileVault", "<"))  # Previous button label
        self.nextButton.setText(_translate("FileVault", ">"))  # Next button label
        self.addressBar.setText(_translate("FileVault", "FileVault"))  # Default text in address bar
        self.toolsButton.setText(_translate("FileVault", "..."))  # Tools button label
        self.optionsButton.setText(_translate("FileVault", "O"))  # Options button label

    # Event filter to track hover events and start/stop the timer
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.Enter:
            # Start the timer for showing the tooltip after 1.5 seconds
            self.hoveredButton = obj  # Keep track of the hovered button
            self.hoverTimer.start(500)  # 
        elif event.type() == QtCore.QEvent.Type.Leave:
            # Stop the timer and hide the tooltip if the mouse leaves the button
            self.hoverTimer.stop()
            self.tooltipLabel.setVisible(False)
        return super().eventFilter(obj, event)

    # Method to show the tooltip below the hovered button after the delay
    def showTooltip(self):
        if self.hoveredButton == self.previousButton:
            self.showTooltipAtButton(self.previousButton, "Go to the previous directory")
        elif self.hoveredButton == self.nextButton:
            self.showTooltipAtButton(self.nextButton, "Go to the next directory")
        elif self.hoveredButton == self.toolsButton:
            self.showTooltipAtButton(self.toolsButton, "Open tools menu")
        elif self.hoveredButton == self.optionsButton:
            self.showTooltipAtButton(self.optionsButton, "Open options")

    # Method to position the tooltip below the hovered button and make it visible
    def showTooltipAtButton(self, button, text):
        self.tooltipLabel.setText(text)
        # Position the tooltip below the button
        self.tooltipLabel.move(button.x(), button.y() + button.height() + 5)
        self.tooltipLabel.setVisible(True)

# Main block to run the application if the script is executed directly
if __name__ == "__main__":
    import sys
    # Create an instance of the application
    app = QtWidgets.QApplication(sys.argv)

    # Create a dialog window for the FileVault interface
    FileVault = QtWidgets.QDialog()

    # Create an instance of the Ui_FileVault class and set up the UI
    ui = Ui_FileVault()
    ui.setupUi(FileVault)

    # Show the FileVault dialog window
    FileVault.show()

    # Execute the application's main loop
    sys.exit(app.exec())
