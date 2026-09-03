import streamlit as st
import os
from google import genai
from google.genai import types
import PIL.Image

# הגדרת דף
st.set_page_config(
    page_title="מערכת מתקדמת לפתרון תרגילים אקדמיים",
    page_icon="📐",
    layout="wide"
)

# כותרת ראשית
st.title("📐 מערכת מתקדמת לפתרון תרגילים אקדמיים")
st.markdown("מערכת המבוססת על בינה מלאכותית לניתוח מדויק של שאלות, זיהוי דינמי של סעיפים (או שאלות ללא סעיפים) והצגת פתרונות מנומקים.")

# אזור הגדרת מפתח API
api_key = st.text_input("הכנס Google Gemini API Key:", type="password")

if not api_key:
    st.warning("⚠️ מוצר במערכת API לא נמצא מפתח.")
    st.info("כדי להתחיל להשתמש במערכת API אנא הזן מפתח.")
    st.stop()

# אתחול הלקוח של גוגל
client = genai.Client(api_key=api_key)

# העלאת קובץ
uploaded_file = st.file_uploader("העלה תמונה או קובץ של התרגיל", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not jamais if uploaded_file is not None:
    # הצגת התמונה
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption="התרגיל שהועלה", use_container_width=True)
    
    if st.button("פתור תרגיל", type="primary"):
        with st.spinner("מנתח את התרגיל ומייצר פתרון מפורט..."):
            try:
                # פרומפט מובנה לניתוח דינמי ופתרון אקדמי
                prompt = """
                נתח את התמונה המצורפת של התרגיל האקדמי (מתמטיקה/פיזיקה/הנדסה) ובצע את הפעולות הבאות:
                1. זיהוי מבנה השאלה: 
                   - האם יש סעיפים (א, ב, ג...)? 
                   - האם זו שאלה אחידה ללא סעיפים?
                2. מתן פתרון אקדמי מלא:
                   - הצג שלבי פתרון מפורטים, הגיוניים ומתמטיים/פיזיקליים לכל חלק או סעיף שזוהה.
                   - השתמש בסימון מתמטי ברור (LaTeX) היכן שנדרש.
                   - הקפד על דיוק חישובי והסבר מילולי קצר לכל מעבר שלב משמעותי.
                """
                
                # קריאה למודל המתקדם של גוגל (Gemini 2.5 Flash או מודל עדכני תואם)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image, prompt]
                )
                
                st.success("הפתרון נוצר בהצלחה!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"אירעה שגיאה בעת עיבוד הבקשה מול המערכת: {e}")
