import streamlit as st
import random

st.set_page_config(page_title="가위✌️ 바위✊ 보✋ 게임", page_icon="🎮", layout="centered")

# 🌟 타이틀
st.markdown(
    "<h1 style='text-align: center; color: #f63366;'>🎮 가위✌️ 바위✊ 보✋ 게임!</h1>",
    unsafe_allow_html=True
)

# 🌈 설명
st.markdown("""
<div style='text-align: center; font-size: 20px;'>
당신의 선택은?! 🤔<br><br>
<strong>가위 ✌️ / 바위 ✊ / 보 ✋</strong> 중 하나를 선택하세요!<br><br>
컴퓨터와 한 판 승부! 🧠💥
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 🎲 컴퓨터 랜덤 선택
choices = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}
user_choice = st.selectbox("👉 당신의 선택은?", options=list(choices.keys()))
play = st.button("🎰 게임 시작!")

if play:
    comp_choice = random.choice(list(choices.keys()))
    
    # 🧮 결과 판별
    result = ""
    if user_choice == comp_choice:
        result = "😐 무승부!"
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \
         (user_choice == "보" and comp_choice == "바위"):
        result = "🎉 당신의 승리!"
    else:
        result = "💀 당신의 패배..."

    # 🎨 결과 출력
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>🧑‍💻 당신: {choices[user_choice]}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>🤖 컴퓨터: {choices[comp_choice]}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: #ffaa00;'>{result}</h1>", unsafe_allow_html=True)

# 👣 푸터
st.markdown("""
<hr>
<div style='text-align: center; font-size: 14px; color: gray;'>
Made with ❤️ using Streamlit<br>
by ChatGPT
</div>
""", unsafe_allow_html=True)

