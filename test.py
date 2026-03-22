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

import yfinance as yf
import time

code = input("銘柄コードを入力してください:")

print(code, "の株価を取得します")

Start_price = None #株価の初期値を保存する変数
last_price = None #前回の株価を保存する変数

while True: #無限ループを使用して株価の変動を監視
    stock = yf.Ticker(code) #yfinanceを使用して株価を取得
    data = stock.history(period="1d") #株価の履歴を取得
    
    if data.empty: #データが空でない場合
        print("データ取得できません（市場が閉まっていますor銘柄コードが間違っています）")
    else:
        price = data["Close"].iloc[-1] #最新の株価を取得
        
        if Start_price is None: #株価の初期値が保存されていない場合
            Start_price = price #株価の初期値を保存
        
        diff = price - Start_price #株価の変動を計算

        if  price !=last_price: #株価が前回の株価と異なる場合
            print(f"現在の株価：{price}, 損益：{diff:+}") #現在の株価を表示
            last_price = price
            #最新の株価を保存

    time.sleep(5) #5秒待機

#for i in range(20): #forループを使用して株価の変動をシミュレート(20回繰り返す)
    #change = random.randint(-100, 100) #株価の変動
    #new_price = price + change
    #diff = new_price - start_price

    #if new_price > price:
        #print("Up", new_price, f"損益: {diff:+}")
    #elif new_price < price:
        #print("Down", new_price, f"損益: {diff:+}")
    #else:
        #print("Same", new_price, f"損益: {diff:+}")
    #pricediff = new_price - start_price
    #time.sleep(1) #1秒待機
#print("変動:", change) #if,elif,else文に組み込んでるので、変動の表示は不要
