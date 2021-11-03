import random
import streamlit as st
import pandas as pd

hobbies = ['スポーツ', '語学', '音楽', '読書', '旅行', 'ゲーム']

def sample(n, max_hobby):
    users = []
    for a in range(n):
        random_num = random.sample(range(len(hobbies)), k=random.randint(1, max_hobby))
        users.append({'userID':a, 'user_hobbies':[hobbies[b] for b in random_num]})
    return users



def perfect_search(users, search_by):
    search_result_perfect = []
    for a in range(len(users)):
        judge = 1
        for b in range(len(search_by)):
            if search_by[b] in users[a]['user_hobbies']:
                judge = 0
            else:
                judge = 1
                break
        if judge == 0:
            search_result_perfect.append(users[a]['userID'])
            
    return search_result_perfect


def partial_search(users, search_by):
    search_result_partial = []
    for c in range(len(users)):
        judge = 1
        for d in range(len(search_by)):
            if search_by[d] in users[c]['user_hobbies']:
                judge = 0
            #else:
                #judge = 1
        if judge == 0:
            search_result_partial.append(users[c]['userID'])
            
    return search_result_partial


def search_user(users, mode, hobby_selection):
    #print("複数の趣味を指定する際は間に半角スペースを入れてください。")
    search_result = []
    #input_hobby = input('趣味:')
    #search_by = input_hobby.split(" ") #指定された趣味のリスト
    search_by = hobby_selection
    
    if mode == "Perfect":
        #完全一致絞り込み関数へ
        search_result = perfect_search(users, search_by)
        
    elif mode == "Partial":
        #部分一致絞り込み関数へ
        search_result = partial_search(users, search_by)            
    
    return search_result



#users = sample(10,5)

users=[{'userID': 0, 'user_hobbies': ['読書', 'ゲーム']},
    {'userID': 1, 'user_hobbies': ['ゲーム', '旅行', '音楽', '読書']},
    {'userID': 2, 'user_hobbies': ['音楽', '読書', 'スポーツ', 'ゲーム', '語学']},
    {'userID': 3, 'user_hobbies': ['音楽', 'スポーツ']},
    {'userID': 4, 'user_hobbies': ['読書', '語学', 'ゲーム', '音楽', 'スポーツ']},
    {'userID': 5, 'user_hobbies': ['音楽', '旅行', '読書']},
    {'userID': 6, 'user_hobbies': ['旅行', '読書', '音楽', 'スポーツ', 'ゲーム']},
    {'userID': 7, 'user_hobbies': ['ゲーム', '旅行']},
    {'userID': 8, 'user_hobbies': ['語学', '旅行', '読書', '音楽']},
    {'userID': 9, 'user_hobbies': ['音楽', '読書']}]

st.title('Match by hobbies')
#st.header('')
st.subheader('同じ趣味をもつ人を探そう！')
st.write('This is a prototype app!') # markdown

st.table(pd.DataFrame({
    'userID':[users[a]['userID'] for a in range(len(users))],
    'hobbies':[str(users[a]['user_hobbies']) for a in range(len(users))]
}))


hobby_selection = st.multiselect('What are your hobbies?', hobbies,[])
#st.write(str(hobby_selection))


mode = st.radio("Select search mode", ('Perfect', 'Partial'))

if st.button('Search users') == True:
    st.write(f'{mode} search result:')
    result = search_user(users, mode, hobby_selection)
    #st.write(result)
    st.table(pd.DataFrame({
        'userID':[users[result[a]]['userID'] for a in range(len(result))],
        'Hobbies':[str(users[result[a]]['user_hobbies']) for a in range(len(result))]
    }))
     






























