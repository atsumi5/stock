import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.markdown("# 株式市場の気になる銘柄")

st.markdown(""""
<style>
.stTextInput div[data-testid="InputInstructions"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

symbol = st.text_input("銘柄コードを入力後、検索ボタンをクリック：", "",key="stock_input",placeholder="例: 7203 (トヨタ自動車)")
search = st.button("検索")

if search:
    if not symbol.endswith(".T"):
        symbol += ".T" #東証銘柄コードに

    stock = yf.Ticker(symbol) #yfinanceで株式データを取得

    try:
            name = stock.info.get("longName")or stock.info.get("shortName") or symbol
    except: #銘柄名を取得
            name = symbol
    data = stock.history(period="1d", interval="5m") #直近1日間の株価データを取得

    if len(data) >= 2:
        today = data["Close"].iloc[-1]#今日の終値
        yesterday = data["Close"].iloc[-2] #昨日の終値
        diff = today - yesterday #今日と昨日の株価の差を計算
        code = symbol[:-2] #銘柄コードから".T"を除去
        open_price = data["Open"].iloc[-1] #今日の始値
        high_price = data["High"].iloc[-1] #今日の高値
        low_price = data["Low"].iloc[-1] #今日の安値
        close_yesterday = data["Close"].iloc[-2] #昨日の終値

        if diff > 0:
            st.markdown(f"**{symbol} ({name})| 株価:{today:.1f} | 変動: :red[+{diff:.1f}]**")
        elif diff < 0:
            st.markdown(f"**{symbol} ({name}) | 株価:{today:.1f} | 変動: :blue[{diff:.1f}]**")
        else:
            st.markdown(f"**{symbol} ({name}) | 株価:{today:.1f} | 変動: 0**")

        st.write(f"始値: {open_price:.1f} ")
        st.write(f"高値: {high_price:.1f} ")
        st.write(f"安値: {low_price:.1f} ")
        st.write(f"前日終値: {close_yesterday:.1f}")

        st.subheader("株価チャート（過去1日/1時間）")
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            increasing_line_color="red",
            decreasing_line_color="blue",
        )])
        fig.update_layout(
             yaxis=dict(
                dtick=10,
                range=[data["Low"].min() - 10, data["High"].max() + 10]
             ),
             xaxis_title="時間",
             yaxis_title="株価",
             xaxis_rangeslider_visible=False
        )
        st.plotly_chart(fig)
    else:
        st.write("データが取得できませんでした")