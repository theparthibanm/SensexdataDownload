# app.py
from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import random

app = Flask(__name__)

# Example Sensex Data (replace with actual data retrieval)
sensex_data_2023 = pd.DataFrame({'Date': pd.date_range(start='2023-01-01', end='2023-12-31'),
                                 'Sensex': [random.randint(35000, 40000) for _ in range(365)]})
sensex_data_2025 = pd.DataFrame({'Date': pd.date_range(start='2025-01-01', end='2025-12-31'),
                                 'Sensex': [random.randint(40000, 45000) for _ in range(365)]})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_pdf')
def download_pdf():
    # Data Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(sensex_data_2023['Date'], sensex_data_2023['Sensex'], label='Sensex 2023')
    plt.plot(sensex_data_2025['Date'], sensex_data_2025['Sensex'], label='Sensex 2025')
    plt.title('Sensex Data for 2023 and 2025')
    plt.xlabel('Date')
    plt.ylabel('Sensex')
    plt.legend()
    plt.grid(True)
    
    # Generate PDF
    pdf_bytes = BytesIO()
    plt.savefig(pdf_bytes, format='pdf')
    pdf_bytes.seek(0)
    
    # Rewind the buffer
    pdf_bytes.seek(0)
    
    return send_file(pdf_bytes, mimetype='application/pdf', as_attachment=True, download_name='Sensex_Data_2023_2025.pdf')

if __name__ == '__main__':
    app.run(debug=True)
