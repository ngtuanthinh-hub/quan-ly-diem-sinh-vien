import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title=“Quản lý điểm sinh viên”, layout=“wide”)

st.title(“QUẢN LÝ ĐIỂM SINH VIÊN”)

data = {
“Ho_ten”: [“Thinh”, “Binh”, “Dung”, “Khoi”, “Tin”, “Lan”, “Minh”, “Nam”, “Phuc”, “Trang”],
“MSSV”: [“001”, “002”, “003”, “004”, “005”, “006”, “007”, “008”, “009”, “010”],
“Chuyen_can”: [8, 9, 7, 10, 8, 6, 9, 7, 8, 10],
“Giua_ky”: [7, 8, 6, 9, 8, 6, 9, 7, 7, 9],
“Cuoi_ky”: [8, 9, 6, 9, 7, 6, 8, 7, 8, 10]
}

df = pd.DataFrame(data)

df[“Tong_ket”] = (
0.2 * df[“Chuyen_can”]
+ 0.3 * df[“Giua_ky”]
+ 0.5 * df[“Cuoi_ky”]
).round(2)

def xep_loai(diem):
if diem >= 8.5:
return “Giỏi”
elif diem >= 7:
return “Khá”
elif diem >= 5:
return “Trung bình”
return “Yếu”

df[“Xep_loai”] = df[“Tong_ket”].apply(xep_loai)

st.subheader(“Bảng điểm”)
st.dataframe(df, use_container_width=True)

st.subheader(“Thống kê lớp”)
st.write(“Điểm trung bình:”, round(df[“Tong_ket”].mean(), 2))
st.write(“Điểm cao nhất:”, df.loc[df[“Tong_ket”].idxmax(), “Ho_ten”],
“-”, df[“Tong_ket”].max())
st.write(“Điểm thấp nhất:”, df.loc[df[“Tong_ket”].idxmin(), “Ho_ten”],
“-”, df[“Tong_ket”].min())
st.write(“Số sinh viên đạt từ 5 điểm:”, int((df[“Tong_ket”] >= 5).sum()))

st.subheader(“Tra cứu sinh viên”)
ten = st.selectbox(“Chọn sinh viên”, df[“Ho_ten”])
sv = df[df[“Ho_ten”] == ten].iloc[0]
st.write(“MSSV:”, sv[“MSSV”])
st.write(“Chuyên cần:”, sv[“Chuyen_can”])
st.write(“Giữa kỳ:”, sv[“Giua_ky”])
st.write(“Cuối kỳ:”, sv[“Cuoi_ky”])
st.write(“Điểm tổng kết:”, sv[“Tong_ket”])
st.write(“Xếp loại:”, sv[“Xep_loai”])

st.subheader(“Biểu đồ điểm tổng kết”)
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df[“Ho_ten”], df[“Tong_ket”])
ax.set_title(“ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN”)
ax.set_xlabel(“Họ tên sinh viên”)
ax.set_ylabel(“Điểm tổng kết”)
ax.set_ylim(0, 10)
ax.grid(axis=“y”, alpha=0.3)
st.pyplot(fig)

st.caption(“Người tạo ứng dụng: Thinh48 | MSSV:("058208007736")
