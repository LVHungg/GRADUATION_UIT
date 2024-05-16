import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page configuration
st.set_page_config(
    page_title="Education Data Quality Dashboard",
    layout="wide",
    initial_sidebar_state="expanded")

st.title("Education Data Quality Dashboard")

# Đường dẫn đến thư mục report
report_dir = os.path.join(os.getcwd(), 'report')

# Danh sách các tệp dữ liệu trong thư mục report
data_files = [file for file in os.listdir(report_dir) if file.endswith('.csv')]

# Chọn tệp dữ liệu từ danh sách
selected_file = st.selectbox('Chọn tệp dữ liệu:', data_files)

# Đường dẫn của tệp dữ liệu được chọn
data_file_path = os.path.join(report_dir, selected_file)

# Đọc dữ liệu từ tệp dữ liệu được chọn
data = pd.read_csv(data_file_path)


# st.write('Số lượng dữ liệu:', data.shape[0])
# st.write('Số lượng thuộc tính:', data.shape[1])

# Hiển thị dữ liệu
st.write(data)

