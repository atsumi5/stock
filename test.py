print("ようこそ東証株式市場へ！")
print("株式投資はリスクが伴います,十分な情報収集と慎重な判断が必要です。投資は全て自己責任で行ってください。")
print("株式市場は変動が激しいため、投資の結果は予測できません。")
print("投資を始める前に、十分な知識と経験を積むことが重要です。")
print("投資は長期的な視点で行うことが望ましいです。短期的な利益を追求することはリスクが高いです。")
print("投資は分散投資が重要です。一つの銘柄に集中することはリスクが高いです。")
print("投資は自己責任で行うことが重要です。投資の結果は予測できません。")
print("投資はリスクが伴います。十分な情報収集と慎重な判断が必要です。")

#name = input("銘柄コードを入力してください： ")
#print(name, "を監視開始")
import streamlit as st
import yfinance as yf

st.title("株式市場のおすすめ銘柄")
symbol = st.text_input("銘柄コードを入力してください：", "9984.T") #デフォルトはソフトバンクグループ
if symbol:
    stock = yf.Ticker(symbol)
    data = stock.history(period="5d", interval="1d") #過去5日間の株価データを取得


if len(data) > 2:
    today = data["Close"].iloc[-1]#今日の終値
    yesterday = data["Close"].iloc[-2] #昨日の終値
    diff = today - yesterday #今日と昨日の株価の差を計算
    code = symbol

    if diff > 0:
        st.markdown(f"**{code} | 株価:{today} | 変動: :red[+{diff}]**")
    elif diff < 0:
        st.markdown(f"**{code} | 株価:{today} | 変動: :blue[{diff}]**")
    else:
        st.markdown(f"**{code} | 株価:{today} | 変動: [0]**")
else:
    st.wraite("株価データが取得できませんでした")

#else:
    #st.markdown(f"**{code} | 株価:{today} | 変動: [0]**")
        #name = stock.info.get("shortName", "不明な銘柄")

        #if diff > 0:
            #status = "↑ おすすめ"
        #elif diff < 0:
            #status = "↓ マジふざけんじゃねえよ。なんか知らないけど下げてんの！意味不明"
        #else:
            #status = "→ 変わらず"

        #st.write(f"{symbol} ({name}| 株価: {today:.2f}  | 変動： {diff:+.2f} | {status}")
#codes = ["9984.T", #ソフトバンクグループ"1605.T", #INPEX

#recommended = [] #おすすめ銘柄のリスト

#for code in codes:
    #stock = yf.Ticker(code) #yfinanceを使用して株価を取得
    #data = stock.history(period="5d") #株価の履歴を取得
    
    #if len(data) < 2:
        #print(code, ": の株価データが不足しています。")
        #continue

    #today = data["Close"].iloc[-1]#今日の終値
    #yesterday = data["Close"].iloc[-2] #昨日の終値

    #diff = today - yesterday #今日と昨日の株価の差を計算
    name = stock.info.get("shortName", "不明な銘柄") #銘柄名を取得

    #if diff > 0:
        #status = "↑ おすすめ"
        #recommended.append((code, name, diff)) #おすすめ銘柄のリストに追加
    #elif diff < 0:
        #status = "↓ マジふざけんじゃねえよ。なんか知らないけど下げてんの！意味不明"
    #else:
        #status = "→ 変わらず"

    #print(f"{code} ({name}| 株価: {today:.2f}  | 変動： {diff:+.2f} | {status}")

#recommended.sort(key=lambda x: x[2], reverse=True) #おすすめ銘柄を変動の大きい順にソート
#print("\n-----上昇ランキング-----")
#for r in recommended:
    #print(r[0], r[1], f"{r[2]:+}")
