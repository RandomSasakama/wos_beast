import streamlit as st
import pandas as pd
from datetime import timedelta

st.set_page_config(page_title="討伐計算ツール", layout="centered")
st.title("討伐計算ツール")
#st.sub
st.text("野獣・巨獣の平均行軍時間、缶詰の数、使う行軍数を入力してください\n総ポイントと所要時間が出ます\nやっててよかったなかし式")

b_travel = st.number_input("\n野獣行軍時間（秒） ", min_value=0, step=1)*2
r_travel = st.number_input("巨獣行軍時間（秒）", min_value=0, step=1)
sta_num = st.number_input("缶詰の数 ", min_value=0, step=1)*10
use_for_total = st.number_input("行軍数 ", min_value=0, step=1)
val = []



#1時間の討伐数、体力
def per_hr(travel_time, use_for, b_r):
    try :
        if b_r == "b":
            win_num = 3600/travel_time*use_for
            use_sta = 10*win_num
        else:
            win_num = 3600/travel_time*use_for
            use_sta = win_num/use_for*20 + (win_num - win_num/use_for)*25
    except ZeroDivisionError:
        win_num = 0
        use_sta = 0
    
    return win_num, use_sta


#use_for_bは5行目で仮置き
def cal_total(use_for_b):
    b_hr_win_num, b_hr_use_sta = per_hr(b_travel, use_for_b, "b")
    r_hr_win_num, r_hr_use_sta = per_hr(r_travel, use_for_total -use_for_b, "r" )
    hr_sta = b_hr_use_sta + r_hr_use_sta
    total_time_cal = sta_num/hr_sta
    total_score = int(total_time_cal*b_hr_win_num + total_time_cal*r_hr_win_num*3)
    total_time = str(timedelta(hours=total_time_cal))[:7]
    return total_score, total_time

if st.button("計算する"):
    val = []
    for i in range(int(use_for_total) + 1):
        score, time = cal_total(i)
        val.append({
            "野獣行軍数": i,
            "巨獣行軍数": use_for_total - i,
            "ポイント": score,
            "時間": time
        })

    df = pd.DataFrame(val)
    st.dataframe(df, use_container_width=True, hide_index=True)












