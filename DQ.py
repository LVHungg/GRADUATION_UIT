import pandas as pd
import os

# Thực hiện đánh giá chất lượng dữ liệu và lưu kết quả vào DataFrame
quality_results = {
    'Dimension': ['Accuracy', 'Completeness', 'Consistency', 'Validity', 'Uniqueness'],
    'Score': [0.85, 0.95, 0.75, 0.90, 0.80]  # Điểm số cho mỗi chiều
}
quality_df = pd.DataFrame(quality_results)

# Lưu kết quả vào tệp CSV hoặc Excel trong thư mục report
report_dir = 'report'
report_file = 'data_quality_report.csv'
quality_df.to_csv(os.path.join(report_dir, report_file), index=False)