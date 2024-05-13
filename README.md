# SensexdataDownload
The Sensex Data PDF Downloader is a simple web application built using Python and Flask framework. This application allows users to download a PDF file containing the Sensex data for the years 2023 and 2025 in a graphical format.


Features:

Data Visualization: The application generates a graphical plot of the Sensex data for the years 2023 and 2025 using Matplotlib, a Python plotting library.

PDF Generation: The graphical plot is then converted into a PDF file using the ReportLab library, which is a powerful PDF generation tool for Python.

User Interaction: Users can interact with the web application through a user-friendly interface provided by Flask. Upon accessing the application, users are presented with a homepage where they can initiate the download process.

PDF Download: When users click the "Download PDF" button, the application generates the PDF file containing the Sensex data plot and prompts the user to download it. The PDF file is automatically downloaded with the filename "Sensex_Data_2023_2025.pdf".

Usage:

Access the web application through the provided URL.
Click the "Download PDF" button to initiate the PDF download process.
The PDF file containing the Sensex data plot for the years 2023 and 2025 will be downloaded automatically.
Dependencies:

Flask: A micro web framework for Python.
Pandas: A data manipulation and analysis library for Python.
Matplotlib: A plotting library for Python.
ReportLab: A PDF generation library for Python.
Note: The application uses simulated Sensex data for demonstration purposes. In a real-world scenario, the Sensex data would be retrieved from an external source or database.
