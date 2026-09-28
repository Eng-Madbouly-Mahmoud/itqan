import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="نظام إتقان الإلكتروني", page_icon="💎", layout="wide")

# تثبيت ألوان النصوص لمنع مشاكل الوضع الداكن في الموبايل
st.markdown("""
    <style>
        :root { color-scheme: light !important; }
        .stMarkdown p, .stMarkdown b, .stMarkdown span { color: #1F2937 !important; }
    </style>
""", unsafe_allow_html=True)

# تصميم الهيدر الرئيسي
st.markdown("""
    <div style='background-color: #0F172A; padding: 20px; border-radius: 10px; text-align: center; border-bottom: 4px solid #0284C7;'>
        <h1 style='color: white !important; margin: 0;'>💎 منصة إتقان الرقمية 💎</h1>
        <p style='color: #94A3B8; margin: 10px 0 0 0;'>أهلاً بك يا هندسة في النظام الجديد - جاري التجهيز للرفع والربط</p>
    </div>
""", unsafe_allow_html=True)

st.write("") 
st.success("🚀 تم تشغيل ورفع السيرفر بنجاح يا هندسة!")
