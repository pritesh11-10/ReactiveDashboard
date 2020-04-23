import streamlit as st
import plotly.express as px
from .preprocess import matches, list_of_teams, m_winner
import pandas as pd
from uuid import uuid4


def plot(fig):
    st.plotly_chart(fig, use_container_width=True)


def overall_best(matches):
    df = matches["winner"].value_counts().reset_index()
    fig = px.bar(df.head(), x="index", y="winner", barmode="group")
    plot(fig)


def best_team_yoy(matches, year: int):
    query = f"season == {year}"
    df = matches.query(query)["winner"].value_counts().reset_index()
    df.columns = ["Team name", "No. of Wins"]
    fig = px.bar(df, x="Team name", y="No. of Wins", barmode="group",)
    plot(fig)


def best_mvp_yoy(matches, year: int):
    query = f"season == {year}"
    mom_yoy = (
        pd.pivot_table(
            matches.query(query),
            values=["date"],
            index=["player_of_match"],
            aggfunc="count",
        )
        .sort_values(["date"], ascending=[False])
        .reset_index()
    )  # PoM yoy basis
    fig = px.bar(mom_yoy, x="player_of_match", y="date", barmode="group",)
    plot(fig)

def toss_dec(matches):
    df = matches['toss_decision'].value_counts().reset_index()
    df.columns = ['toss_decision','count']
    fig = px.pie(df, values='count', names='toss_decision')
    plot(fig)

def toss_win_match_win(m_winner, year : int):
    query = f"season == {year}"
    toss_winner_match = (
        pd.pivot_table(
            m_winner.query(query),
            values=["date"],
            index=["season","winner"],
            aggfunc="count").sort_values(["date"], ascending=[False]).reset_index())
    fig = px.bar(toss_winner_match, x="winner", y="date", barmode="group",)
    plot(fig)

def lost_match_to(matches, team : str):
    matches = matches.replace({'Rising Pune Supergiant':'Rising Pune Supergiants','Delhi Daredevils':'Delhi Capitals','Deccan Chargers':'Sunrisers Hyderabad'})
    x = matches[(matches['team1'] == team)]
    y = matches[(matches['team2'] == team)]
    z = pd.concat([x,y])
    z1 = z['winner'].value_counts().reset_index()
    z1.columns = ['name','count']
    z1.drop(z1[z1['name'] == team].index, inplace = True)
    fig = px.bar(z1, x="name", y="count", barmode="group",)
    plot(fig)

def stadium(matches):
    loc = pd.pivot_table(matches, index=['city','venue'], values = 'date',aggfunc='count').reset_index()
    loc = loc.rename(columns={'date':'count'})
    loc = loc.sort_values('count',ascending=False)
    fig = px.sunburst(
            loc.head(20),
            path=["city", "venue"],
            values="count",
            color="city",
            hover_data=["venue"],
        )
    plot(fig)




def main():

    #overall best performing team
    st.header("1. Which team has the best overall performance?")
    overall_best(matches)

    #best performing team per year
    year_best_team = st.slider(
        label="Select Year",
        min_value=int(matches["season"].min()),
        max_value=int(matches["season"].max()),
    )
    st.header(f"2. Which is the Best performing Team in {year_best_team}?")
    best_team_yoy(matches, year_best_team)

    #Best player per year
    year_mvp = st.slider(
        label="Select Year for Best Team",
        min_value=int(matches["season"].min()),
        max_value=int(matches["season"].max()),
    )
    st.header(f"3. Best player or MVP in {year_mvp}?")
    best_mvp_yoy(matches, year_mvp)

    #decision after toss
    st.header("4.Decision after winning the toss?")
    toss_dec(matches)
    
    #Team who won match after winning toss    
    win_toss_match = st.slider(
        label="Year",
        min_value=int(matches["season"].min()),
        max_value=int(matches["season"].max()),
    )
    st.header(f"5. Which is the team who won match after winning toss {win_toss_match}?")
    toss_win_match_win(m_winner, win_toss_match)

    team_selected = st.selectbox(label="Select the team!",options=['Mumbai Indians','Delhi Capitals','Rajasthan Royals', 'Chennai super Kings', 'Sunrisers Hyderabad','Royal Challengers Bangalore','Kolkata Knight Riders','Kings XI Punjab'])
    st.header(f"6. {team_selected} lost most matches to which team?")
    lost_match_to(matches, team_selected)

    st.header("7. Top 20 stadiums which hosted most number of matches along with city")
    st.header("Click on city to see visualization changes")
    stadium(matches)


        

    

    

