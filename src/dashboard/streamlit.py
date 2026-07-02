import streamlit as st
from src.db.data_base import (
    get_daily_metrics,
    simulated_result_of_weeks,
    simulated_result_of_months
)
from src.agents.executive_agent import run_executive_agent
from src.agents.investigator_agent import investigate

st.set_page_config(page_title="Smart Traffic Analytics", layout="wide")
st.title("Smart Traffic Analytics")

metrics = get_daily_metrics()

total_vehicles = sum(x["vehicles"] for x in metrics)
avg_confidence = (
    sum(x["confidence"] for x in metrics) / len(metrics) * 100
    if metrics else 0
)
avg_per_day = total_vehicles / len(metrics) if metrics else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total of Vehicles", total_vehicles)
col2.metric("Avarage Confidence", f"{avg_confidence:.1f}%")
col3.metric("Average per Day", f"{avg_per_day:.0f}")

st.subheader("Vehicles per Day")
st.line_chart({row["date"]: row["vehicles"] for row in metrics})

col_w, col_m = st.columns(2)
with col_w:
    st.subheader("By Week")
    weekly = simulated_result_of_weeks()
    st.bar_chart({str(r[0]): r[1] for r in weekly})
with col_m:
    st.subheader("By Month")
    monthly = simulated_result_of_months()
    st.bar_chart({str(r[0]): r[1] for r in monthly})

st.divider()