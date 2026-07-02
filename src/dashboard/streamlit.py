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