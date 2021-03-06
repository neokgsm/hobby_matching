import random
import streamlit as st
import pandas as pd

import anytree
from anytree import Node, RenderTree


hobbies = Node("趣味", parent=None)

G1_sports = Node("スポーツ", parent=hobbies)
G2_baseball = Node("野球", parent=G1_sports)
G2_soccer = Node("サッカー", parent=G1_sports)
G2_basketball = Node("バスケットボール", parent=G1_sports)
G2_tennis = Node("テニス", parent=G1_sports)

G1_langlearn = Node("語学", parent=hobbies)
G2_english = Node("英語", parent=G1_langlearn)
G3_toeic = Node("TOEIC", parent=G2_english)
G3_toefl = Node("TOEFL", parent=G2_english)
G2_french = Node("フランス語", parent=G1_langlearn)
G2_chinese = Node("中国語", parent=G1_langlearn)

G1_music = Node("音楽", parent=hobbies)
G2_rock = Node("ロック", parent=G1_music)
G2_jazz = Node("ジャズ", parent=G1_music)
G2_hiphop = Node("ヒップホップ", parent=G1_music)

G1_reading = Node("読書", parent=hobbies)
G2_novel = Node("小説", parent=G1_reading)
G2_comic = Node("マンガ", parent=G1_reading)

G1_game = Node("ゲーム", parent=hobbies)
G2_rpg = Node("RPG", parent=G1_game)
G2_FPS = Node("FPS", parent=G1_game)

name = ['Taro', 'Hanako', 'John', 'Emma', 'Yuki', 'Michael', 'Shun', 'Sakura', 'Ryo', 'Mizuki']



def sample(n, max_hobby, hobbies, name):
    users = []
    hobby_count = len(hobbies.leaves)
    for a in range(n):
        random_num = random.randint(1, max_hobby)
        nickname = f'{name[random.randint(0, len(name)-1)]}'
        users.append({'userID':a,
                      'user_nickname':nickname+f'#{a}',
                      'user_hobbies':set([hobbies.leaves[random.randint(0, hobby_count-1)] for _ in range(random_num)]),
                      'sns_acc':f'@{nickname}_{a}'})
    return users



def perfect_search(users, search_by):
    search_result_perfect = []
    for user in users:
        judge = 1
        for hobby in search_by:
            if hobby in user['user_hobbies']:
                judge = 0
            else:
                judge = 1
                break
        if judge == 0:
            search_result_perfect.append(user['userID'])
            
    return search_result_perfect


def partial_search(users, search_by):
    search_result_partial = []
    for user in users:
        judge = 1
        for hobby in search_by:
            if hobby in user['user_hobbies']:
                judge = 0
                break
            #else:
                #judge = 1
        if judge == 0:
            search_result_partial.append(user['userID'])
            
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


#絞り込み結果のうち、頻繁に表れる趣味を見つける
def suggest(hobby_selection, result): 
    counter = {f'{hobby.name}':0 for hobby in hobbies.leaves}

    for id in result:
        remaining = []
        for hobby in list(users[id]['user_hobbies']):
            if hobby not in hobby_selection:
                remaining.append(hobby)
        for hobby in hobbies.leaves:
            if hobby in remaining:
                counter[hobby.name] += 1

    counter_sorted =  sorted(counter.items(), key=lambda i: i[1], reverse=True)
    return counter_sorted


sample_num = 100

users = sample(sample_num,5,hobbies,name)


st.title('つながるくん')
#st.header('')
st.subheader('同じ趣味をもつ人を探そう！')
st.write('This is a demo version!') # markdown
st.write(f'ユーザー数：{sample_num}')

#st.table(pd.DataFrame({
    #'userID':[users[a]['userID'] for a in range(len(users))],
    #'hobbies':[str(users[a]['user_hobbies']) for a in range(len(users))]
#}))


selected_str = st.multiselect('What are your hobbies?',
                                 [n.name for n in hobbies.leaves],
                                 [])

hobby_selection = [anytree.search.findall_by_attr(hobbies, str_h)[0] for str_h in selected_str]


mode = st.radio("Select search mode", ('Perfect', 'Partial'))

if st.button('Search users') == True:
    st.write(f'{mode} search result:')
    if hobby_selection == []:
        result = [i for i in range(sample_num)]
    else:
        result = search_user(users, mode, hobby_selection)

        
    st.table(pd.DataFrame({
        'Nickname':[users[a]['user_nickname'] for a in result],
        'Hobbies':[str([h.name for h in list(users[a]['user_hobbies'])])[1:-1].replace("'","") for a in result],
        'Contact':[users[a]['sns_acc'] for a in result]
    }))
    
    
    st.write('あなたと同じ趣味をもっている人はこんなことにも興味があるようです。')
    suggestion = suggest(hobby_selection, result)
    for i in range(5):
        st.write(f'{i+1}. {suggestion[i][0]} ({suggestion[i][1]}人)')
                 
