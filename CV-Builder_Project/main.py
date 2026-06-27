
import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from cv_builder_ui import Ui_MainWindow
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from reportlab.platypus import Image


class CVApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.photo_path = ""

        # Connect buttons
        self.ui.btn_save.clicked.connect(self.save_data)
        self.ui.btn_load.clicked.connect(self.load_data)
        self.ui.btn_export.clicked.connect(self.export_dummy)
        self.ui.btn_clear.clicked.connect(self.clear_data)
        self.ui.btn_photo.clicked.connect(self.upload_photo)

        # Live preview connections
        self.ui.lineEdit_name.textChanged.connect(self.update_preview)
        self.ui.lineEdit_email.textChanged.connect(self.update_preview)
        self.ui.lineEdit_phone.textChanged.connect(self.update_preview)
        self.ui.textEdit_address.textChanged.connect(self.update_preview)
        self.ui.textEdit_education.textChanged.connect(self.update_preview)
        self.ui.textEdit_skills.textChanged.connect(self.update_preview)
        self.ui.textEditexperience.textChanged.connect(self.update_preview)
        self.ui.comboBox.currentIndexChanged.connect(self.update_preview)

    def update_preview(self):
        name = self.ui.lineEdit_name.text()
        email = self.ui.lineEdit_email.text()
        phone = self.ui.lineEdit_phone.text()
        cnic = self.ui.lineEdit_cnic.text()
        address = self.ui.textEdit_address.toPlainText()
        education = self.ui.textEdit_education.toPlainText()
        skills = self.ui.textEdit_skills.toPlainText()
        experience = self.ui.textEditexperience.toPlainText()
        template = self.ui.comboBox.currentText()

        if template == "CLASSIC":

            preview = f"""
                <div style="font-family: Segoe UI; color:#2C3E50;"> 
                <table width="100%"> 
                <tr> 
                <td> <h1>{name}</h1><br>
                <b>Email:</b> {email}<br> 
                <b>Phone:</b> {phone}<br> 
                <b>CNIC:</b> {cnic} 
                </td> 
                <td align="right"> PHOTO </td> 
                </tr> 
                </table> 
                <hr> 
                <b>Address:</b> {address}<br> 
                <hr> 
                <h2 style="color:#3498DB;">Education</h2> {education.replace(chr(10), "<br>")} 
                <hr> 
                <h2 style="color:#3498DB;">Skills</h2> {skills.replace(chr(10), "<br>")} 
                <hr> 
                <h2 style="color:#3498DB;">Experience</h2> {experience.replace(chr(10), "<br>")} 
                </div>"""
        else:
            preview = f"""
            <table width="100%" cellspacing="0" cellpadding="10">
            <tr>
            <td width="30%" bgcolor="#2C3E50">
            <font color="white">
            <h2>CONTACT</h2>
            <br>
            <br>
            <b>Email</b><br>
            {email}
            <br><br>
            <b>Phone</b><br>
            {phone}
            <br><br>
            <b>CNIC</b><br>
            {cnic}
            <br>
            <h2>SKILLS</h2>
            {skills.replace(chr(10), "<br>")}
            </font>
            </td>
            <td width="70%">
            <h1>{name}</h1>
            <hr>
            <h2 style="color:#3498DB;">Education</h2>
            {education.replace(chr(10), "<br>")}
            <hr>
            <h2 style="color:#3498DB;">Experience</h2>
            {experience.replace(chr(10), "<br>")}
            <hr>
            <h2 style="color:#3498DB;">Address</h2>
            {address}
            </td>
            </tr>
            </table>
            """
        self.ui.textBrowser_preview.setHtml(preview)

    def save_data(self):
        data = {
            "name": self.ui.lineEdit_name.text(),
            "email": self.ui.lineEdit_email.text(),
            "phone": self.ui.lineEdit_phone.text(),
            "cnic": self.ui.lineEdit_cnic.text(),
            "address": self.ui.textEdit_address.toPlainText(),
            "education": self.ui.textEdit_education.toPlainText(),
            "skills": self.ui.textEdit_skills.toPlainText(),
            "experience": self.ui.textEditexperience.toPlainText(),
            "photo": self.photo_path,
        }
        QMessageBox.information(
            self,
            "Success",
            "Data Saved Successfully")
        
        with open("cv_data.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open("cv_data.json", "r") as f:
                data = json.load(f)

            self.ui.lineEdit_name.setText(data["name"])
            self.ui.lineEdit_email.setText(data["email"])
            self.ui.lineEdit_phone.setText(data["phone"])
            self.ui.lineEdit_cnic.setText(data["cnic"])
            self.ui.textEdit_address.setPlainText(data["address"])
            self.ui.textEdit_education.setPlainText(data["education"])
            self.ui.textEdit_skills.setPlainText(data["skills"])
            self.ui.textEditexperience.setPlainText(data["experience"])
            self.photo_path = data["photo"]
            pixmap = QPixmap(self.photo_path)
            self.ui.label_photo.setPixmap(
            pixmap.scaled(
            self.ui.label_photo.width(),
            self.ui.label_photo.height()))
            QMessageBox.information(
                self,
            "Success",
            "Data Loaded Successfully")

        except FileNotFoundError:
            print("No saved file found")

    def export_dummy(self):
        pdf = SimpleDocTemplate("My_CV.pdf")
        styles = getSampleStyleSheet()
        from reportlab.lib import colors
        from reportlab.lib.styles import ParagraphStyle
        title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        textColor=colors.darkblue,
        spaceAfter=20)
        heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        textColor=colors.blue,
        spaceBefore=10,
        spaceAfter=10)
        
        content = []
        content.append(
            Paragraph(
                self.ui.lineEdit_name.text(),
                title_style
            )
        )
        if self.photo_path:
            img = Image(
            self.photo_path,
            width=100,
            height=100)
            content.append(img)
            content.append(Spacer(1, 10))
        content.append(Spacer(1, 12))
        content.append(
            Paragraph(
                f"Email: {self.ui.lineEdit_email.text()}",
                styles['Normal']
            )
        )
        content.append(
            Paragraph(
                f"Phone: {self.ui.lineEdit_phone.text()}",
                styles['Normal']
            )
        )
        content.append(
            Paragraph(
                f"CNIC: {self.ui.lineEdit_cnic.text()}",
                styles['Normal']
            )
        )
        content.append(Spacer(1, 12))
        content.append(
            Paragraph("EDUCATION", heading_style)
        )
        education = self.ui.textEdit_education.toPlainText().replace("\n", "<br/>")
        Paragraph(education, styles['Normal'])
        content.append(
            Paragraph(
            education,
            styles['Normal']
            )
        )
        content.append(Spacer(1, 12))
        content.append(
            Paragraph("SKILLS", heading_style)
        )
        skills = self.ui.textEdit_skills.toPlainText().replace("\n", "<br/>")
        Paragraph(skills, styles['Normal'])
        content.append(
            Paragraph(
            skills,
            styles['Normal']
            )
        )
        content.append(Spacer(1, 12))
        content.append(
            Paragraph("EXPERIENCE", heading_style)
        )
        experience = self.ui.textEditexperience.toPlainText().replace("\n", "<br/>")
        Paragraph(experience, styles['Normal'])
        content.append(
            Paragraph(
            experience,
            styles['Normal']
            )
        )
        pdf.build(content)
        QMessageBox.information(
            self,
            "Success",
        "PDF Exported Successfully!")

    def clear_data(self):
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_phone.clear()
        self.ui.lineEdit_cnic.clear()
        self.ui.textEdit_address.clear()
        self.ui.textEdit_education.clear()
        self.ui.textEdit_skills.clear()
        self.ui.textEditexperience.clear()
        self.photo_path = ""
        self.ui.label_photo.clear()
        self.ui.label_photo.setText("Photo")

    def upload_photo(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Photo",
            "",
            "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.photo_path = file_name
            pixmap = QPixmap(file_name)
            self.ui.label_photo.setPixmap(
                pixmap.scaled(
                    self.ui.label_photo.width(),
                    self.ui.label_photo.height()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CVApp()
    window.show()
    sys.exit(app.exec_())
