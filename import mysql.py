import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# MySQL database connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Harish@2005",
    "database": "attendance",
}

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch attendance data from the database
query = "SELECT * FROM attendance"
cursor.execute(query)
data = cursor.fetchall()

# Create a PDF report
pdf_filename = "attendance_report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
elements = []

# Create a table to display the data
table_data = [["SNO", "STUDENT_ID", "STUDENT_NAME", "ATTENDANCE"]]
table_data.extend(data)
table = Table(table_data)

# Apply table styles
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
    ("TEXTCOLOR", (0, 0), (-1, 0), (1, 1, 1)),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
    ("GRID", (0, 0), (-1, -1), 1, (0, 0, 0)),
]))

elements.append(table)
doc.build(elements)

# Close the database connection
cursor.close()
conn.close()

print(f"PDF report '{pdf_filename}' generated successfully.")
