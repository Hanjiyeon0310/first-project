import streamlit as st
import random
from datetime import datetime

# 🎨 페이지 설정
st.set_page_config(page_title="🔮 오늘의 운세 뽑기", page_icon="🧙", layout="centered")

# 🌟 제목
st.markdown("<h1 style='text-align: center; color: #8e44ad;'>🔮 오늘의 운세 뽑기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>하루에 한 번, 당신의 운세를 확인해보세요! 🍀</p>", unsafe_allow_html=True)

st.markdown("---")

# 📅 날짜 표시
today = datetime.now().strftime("%Y-%m-%d")
st.markdown(f"📅 <b>오늘 날짜:</b> {today}", unsafe_allow_html=True)

# 🔮 운세 리스트
fortunes = [
    ("🌞 대박 운세", "오늘은 당신의 날이에요! 무슨 일이든 잘 풀릴 거예요! ✨"),
    ("🍀 행운이 가득해요", "작은 일에도 좋은 결과가 따를 거예요. 가볍게 미소 지어봐요 😊"),
    ("🌈 무난한 하루", "크게 나쁘지도, 좋지도 않은 평온한 하루가 될 거예요."),
    ("🌧 살짝 조심하세요", "작은 실수가 큰 문제가 될 수 있어요. 침착하게 행동하세요."),
    ("🔥 도전의 날", "새로운 일에 도전해보세요! 생각보다 잘 풀릴지도 몰라요 💪"),
    ("💤 휴식이 필요한 하루", "무리하지 말고 자신을 돌보는 하루로 만들어보세요 🛌"),
    ("🌀 생각 많은 날", "마음이 복잡할 수 있어요. 차 한 잔 하며 정리해보는 건 어때요? 🍵"),
    ("💎 뜻밖의 선물", "예상치 못한 좋은 일이 생길 수도 있어요! 기대해보세요 🎁"),
]

# 🧙‍♂️ 운세 뽑기 버튼
if st.button("🔮 운세 뽑기"):
    fortune = random.choice(fortunes)
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>{fortune[0]}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size:20px;'>{fortune[1]}</p>", unsafe_allow_html=True)

# 🧾 푸터
st.markdown("""
<hr>
<div style='text-align: center; font-size: 14px; color: gray;'>
오늘의 운세는 재미로만 봐주세요 😉<br>
Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
