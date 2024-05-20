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
data_name = ['danh sách sinh viên', 'bảng điểm']

# Chọn tệp dữ liệu từ danh sách
selected_file = st.selectbox('Data file:', data_name)

if selected_file == 'danh sách sinh viên':
    data_file = 'dssinhvien_DQ_score.csv'
    data_sample = 'dssinhvien_scored.csv'
elif selected_file == 'bảng điểm':
    data_file = 'diem_DQ_score.csv'
    data_sample = 'diem_scored.csv'

# Đường dẫn của tệp dữ liệu được chọn
data_file_path = os.path.join(report_dir, data_file)
data_sample_file_path = os.path.join(report_dir, data_sample)


# Đọc dữ liệu từ tệp dữ liệu được chọn
data = pd.read_csv(data_file_path)
dataset_sample = pd.read_csv(data_sample_file_path)

# Danh sách các cột chứa dấu phẩy cần xóa
columns_with_comma = ['masv']

# Kiểm tra xem cột 'nienkhoa' có trong DataFrame không trước khi thực hiện thao tác xử lý
if 'nienkhoa' in dataset_sample.columns:
    columns_with_comma.append('nienkhoa')
if 'namhoc' in dataset_sample.columns:
    columns_with_comma.append('namhoc')
# Lặp qua từng cột và xóa dấu phẩy
for col in columns_with_comma:
    dataset_sample[col] = dataset_sample[col].astype(str).str.replace(',', '')


# Hiển thị dữ liệu điểm chất lượng
st.subheader("Data Quality Assessment")
st.write(data)
# st.write(dataset_sample)

# Giả định các cột điểm chất lượng dữ liệu trong DataFrame
dimension_scores = ['completeness', 'consistency','timeliness', 'validity']

# Kiểm tra xem các cột điểm chất lượng có trong DataFrame không
if all(col in dataset_sample.columns for col in dimension_scores):
    print('yes')
    # Lọc các dòng có bất kỳ điểm chất lượng nào bằng 0
    rows_with_zero_scores = dataset_sample[(dataset_sample[dimension_scores] == 0).any(axis=1)]
    count = rows_with_zero_scores.shape[0]
    st.subheader("Rows with any dimension is 0:")
    st.write("Count: ", count, "rows")
    if not rows_with_zero_scores.empty:
        # Tạo một bản sao của DataFrame với định dạng
        styled_df = rows_with_zero_scores.style

        # Áp dụng màu nền cho các ô dữ liệu điểm dimension bằng 0
        styled_df = styled_df.apply(lambda x: ['background: #FF9B9B' if x.name in rows_with_zero_scores.index else '' for i in x], axis=1)

        st.write(rows_with_zero_scores)
    else:
        st.write("Không có dòng dữ liệu nào có điểm chất lượng bằng 0.")
else:
    st.write("Không tìm thấy các cột điểm chất lượng trong tệp dữ liệu.")
