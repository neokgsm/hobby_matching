import random
import streamlit as st
import pandas as pd

hobbies = ['スポーツ', '語学', '音楽', '読書', '旅行', 'ゲーム']
name = ['Taro', 'Hanako', 'John', 'Emma', 'Yuki', 'Michael', 'Shun', 'Sakura', 'Ryo', 'Mizuki']

def sample(n, max_hobby, name):
    users = []
    for a in range(n):
        random_num = random.sample(range(len(hobbies)), k=random.randint(1, max_hobby))
        nickname = f'{name[random.randint(1, len(name)-1)]}'
        users.append({'userID':a,
                      'user_nickname':nickname+f'#{a}',
                      'user_hobbies':[hobbies[b] for b in random_num],
                      'sns_acc':f'@{nickname}_{a}'})
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



users = sample(10,5,name)


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
        'Nickname':[users[result[a]]['user_nickname'] for a in range(len(result))],
        'Hobbies':[str(users[result[a]]['user_hobbies'])[1:-1].replace("'","") for a in range(len(result))],
        'Contact':[users[result[a]]['sns_acc'] for a in range(len(result))]
    }))
     
