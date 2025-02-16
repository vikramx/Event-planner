import streamlit as st
from scipy.special import comb,perm

st.title("Event planner 🗓️")

st.header("Group formation")

n=st.number_input("Enter total amount of people:",min_value=1,max_value=100)
r=st.number_input("Enter number of people in each group:",min_value=1,max_value=5)

if st.button("Calculate groups:"):
    ans=comb(n,r)
    st.write(f"The arrangement is {int(ans)}")

st.header("Seating arrangement of speakers 🎙️🎤")

num=st.number_input("Enter number of speakers:",min_value=1)
if st.button("Calculate the arrangements:"):
    ans=perm(num,num)
    ans=int(ans)
    st.write(f"They can be arranged in {ans} ways")

st.header("How many ways you can win a lottery 💰🪙💴")
n=st.number_input("Enter total number of people signing up for lottery:",min_value=1)
r=st.number_input("Enter number of winners here:",min_value=1)
if st.button("Calculate number of ways to win"):
    ans=comb(n,r)
    ans=int(ans)
    st.write(f"You can win the lottery in {ans} ways")
