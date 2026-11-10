import streamlit as st

st.set_page_config(
    page_title="Only For My Batman 🦇",
    page_icon="🦇",
    layout="wide"
)

emojis = [
"🦇","🌙","⭐","✨","🌸","🦋","🌷","🌻","🌈","☀️",
"🌹","🍓","🍒","🍉","🍭","🍬","🧸","🐼","🐻","🐰",
"🐱","🐥","🦊","🐨","🐧","🦄","🐢","🐬","🐳","🦚",
"🪐","🌍","🌎","🌏","🔥","⚡","💫","☄️","🌊","❄️",
"🍀","🌿","🍁","🍄","🌵","🌴","🌺","💐","🪻","🪷",
"🎀","👑","💎","🔮","🎧","🎮","🎸","🎹","🎨","🎬",
"🚀","✈️","🚲","🏆","🥇","🎯","🎲","🪄","🧩","🎁",
"🍕","🍟","🍿","🍩","🍪","🧁","🍰","🍫","🍦","🥤",
"🐝","🕊️","🦢","🦜","🦩","🐾","🐣","🦕","🐙","🦔",
"🌠","🌌","🏵️","🪇","🎵","🎶","📸","🛼","🧿","🪩"
]

messages = [f"Love you my Batman {e}" for e in emojis]

st.markdown("""
<style>
.stApp {
    background:
      radial-gradient(circle at 15% 15%, #34204e 0%, transparent 30%),
      radial-gradient(circle at 85% 80%, #24153b 0%, transparent 30%),
      #090711;
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding: 45px 15px;
    border: 1px solid #8d63b8;
    border-radius: 28px;
    background: linear-gradient(140deg, #28183e, #130e20);
    box-shadow: 0 0 35px #8b5cf633;
    position: relative;
    overflow: hidden;
}

.hero h1 {
    color: #f0d9ff;
    font-size: clamp(34px, 6vw, 58px);
    text-shadow: 0 0 20px #c084fc;
    margin: 0;
}

.hero p {
    color: #d8c2ed;
    font-size: 17px;
}

.bat {
    display: inline-block;
    font-size: 25px;
    animation: float 3s ease-in-out infinite;
    margin: 0 12px;
}

@keyframes float {
    0%, 100% { transform: translateY(0) rotate(-8deg); }
    50% { transform: translateY(-12px) rotate(8deg); }
}

.welcome {
    margin: 25px 0;
    padding: 22px;
    text-align: center;
    background: #21172f;
    border: 1px solid #634583;
    border-radius: 20px;
    color: #ead9ff;
    line-height: 1.8;
}

.section-title {
    text-align: center;
    color: #e7c9ff;
    font-size: 28px;
    margin: 35px 0 20px;
}

.message {
    background: linear-gradient(135deg, #261b38, #352349);
    border: 1px solid #654887;
    border-radius: 17px;
    padding: 17px 9px;
    margin: 8px 0;
    text-align: center;
    color: #f7edff;
    font-size: 16px;
    box-shadow: 0 5px 18px #00000033;
    transition: all 0.25s ease;
}

.message:hover {
    transform: translateY(-4px);
    border-color: #d7aaff;
    box-shadow: 0 0 20px #b66aff55;
}

.end-card {
    margin-top: 35px;
    padding: 30px 15px;
    text-align: center;
    border: 1px solid #a77ad0;
    border-radius: 24px;
    background: linear-gradient(135deg, #302044, #1a1028);
    box-shadow: 0 0 25px #9d63cf33;
}

.end-card h2 {
    color: #f0d9ff;
}

.end-card p {
    color: #d9c4ed;
    font-size: 17px;
}

.footer {
    text-align: center;
    padding: 25px 10px;
    color: #9d89b5;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# Main heading
st.markdown("""
<div class="hero">
    <div class="bat">🦇</div>
    <div class="bat">✨</div>
    <h1>My Batman</h1>
    <p>Welcome to your little corner of happiness</p>
    <div class="bat">🌙</div>
    <div class="bat">🦇</div>
</div>
""", unsafe_allow_html=True)

# Welcome note
st.markdown("""
<div class="welcome">
    <h3>Hey, Batman! 🖤</h3>
    This little page is made especially for you.<br>
    No big explanations, just 100 little ways of saying
    <b>Love you!</b> ✨
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">💌 100 Little Love Notes</div>',
    unsafe_allow_html=True
)

# All messages visible
left, right = st.columns(2)

for i, msg in enumerate(messages):
    with (left if i % 2 == 0 else right):
        st.markdown(
            f'<div class="message">{msg}</div>',
            unsafe_allow_html=True
        )

# Ending surprise
st.markdown("""
<div class="end-card">
    <h2>🦇 The End? Never.</h2>
    <p>
        Gotham has its Batman.<br>
        This page has its favourite person. ✨
    </p>
    <div style="font-size:32px;">🌙 🦇 ⭐</div>
</div>

<div class="footer">
    MADE WITH A LITTLE EXTRA THOUGHT · ONLY FOR ONE BATMAN
</div>
""", unsafe_allow_html=True)