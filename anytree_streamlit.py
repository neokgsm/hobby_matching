import streamlit as st
import anytree
from anytree import Node, RenderTree
import random

### 趣味 ###

Hobbies = Node("趣味", parent=None)

Sports = Node("スポーツ", parent=Hobbies)
Baseball = Node("野球", parent=Sports)
Soccer = Node("サッカー", parent=Sports)
Basketball = Node("バスケットボール", parent=Sports)
Tennis = Node("テニス", parent=Sports)

LanguageLearning = Node("語学", parent=Hobbies)
English = Node("英語", parent=LanguageLearning)
TOEIC = Node("TOEIC", parent=English)
TOEFL = Node("TOEFL", parent=English)
French = Node("フランス語", parent=LanguageLearning)
Chinese = Node("中国語", parent=LanguageLearning)

Music = Node("音楽", parent=Hobbies)
Rock = Node("ロック", parent=Music)
Jazz = Node("ジャズ", parent=Music)
HipHop = Node("ヒップホップ", parent=Music)

Reading = Node("読書", parent=Hobbies)
Novel = Node("小説", parent=Reading)
Comic = Node("マンガ", parent=Reading)

Game = Node("ゲーム", parent=Hobbies)
RPG = Node("RPG", parent=Game)
FPS = Node("FPS", parent=Game)



### 趣味をランダムに選択する関数 ###
@st.cache
def random_hobby_selection():
    curr_gen = Hobbies # Node object
    while curr_gen.children!=():
        curr_gen = curr_gen.children[random.randint(0, len(curr_gen.children)-1)]
    return curr_gen



### ランダムなユーザーを生成する関数 ( n人分, 趣味はmax_hobby個まで ) ###
@st.cache
def sample(n, max_hobby):
    users = []
    for a in range(n):
        random_num = random.randint(1, max_hobby)
        users.append({'userID':a, 'user_hobbies':set([random_hobby_selection() for _ in range(random_num)])})
    return users



### 100人分, 趣味は5個まで ###
users=sample(100,5)



#絞り込み用関数本体は一番最後 (search_users())



### 完全一致絞り込み関数 ###
# 引数users: 絞り込み対象のユーザー, sample(n)で生成したユーザー
# 引数search_by: 指定された趣味のリスト
# 変数judge: 趣味が合致しているかの判定 (0:合致している, 1:合致していない)
#@st.cache
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



#### 部分一致絞り込み関数 ###
# 引数users: 絞り込み対象のユーザー, sample(n)で生成したユーザー
# 引数search_by: 指定された趣味のリスト
# 変数judge: 趣味が合致しているかの判定 (0:合致している, 1:合致していない)
#@st.cache
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



### ユーザー絞り込み用関数 ###
# sample(n)で生成したユーザーのうち、
# 自分と共通な趣味を持つ人の userID をリストに格納して返す
# 引数users: 絞り込み対象のユーザー, sample(n)で生成したユーザー
# 引数mode: 絞り込みモード (perfect: 完全一致, partial: 部分一致)
#@st.cache
def search_user(users, mode, hobby_selection_list):
    #search_input = input('趣味:').split(" ")
    search_by = []

    for hobby in hobby_selection_list:
        search_by.append(anytree.search.findall_by_attr(hobbies, hobby)[0])
    st.write(search_by)
    if mode == "perfect":
        #完全一致絞り込み関数へ
        search_result = perfect_search(users, search_by)
        
    elif mode == "partial":
        #部分一致絞り込み関数へ
        search_result = partial_search(users, search_by)            
    
    return search_result





### Webサイトの動作 ###

st.title('Match by hobbies')
#st.header('')
st.subheader('同じ趣味をもつ人を探そう！')
st.write('This is a prototype app!') # markdown

#@st.cache
def Node_selection():
    hobby_selection = Hobbies
    while hobby_selection.children != ():
        button_selection = st.selectbox('What are your hobbies?', [hobby.name for hobby in hobby_selection.children])
        hobby_selection = anytree.search.findall_by_attr(Hobbies, button_selection)[0]
    return hobby_selection
    st.write(hobby_selection.name)

if "selected" not in st.session_state:
    st.session_state.selected = []

while len(st.session_state.selected) <= 5:
    if st.button('OK',key='selected') == True:
        st.session_state.selected.append(Node_selection().name)

#@st.cache
#if st.button('OK', key='selected') == True:
    #st.session_state.selected.append(Node_selection().name)
#st.write(st.session_state.selected)
        
mode = st.radio("Select search mode", ('Perfect', 'Partial'))



if st.button('Search users', key = 'search_button') == True:
    st.write(f'{mode} search result:')
    result = search_user(users, mode, hobby_selection_list)
    #st.write(result)
    st.table(pd.DataFrame({
        'userID':[users[result[a]]['userID'] for a in range(len(result))],
        'Hobbies':[str(users[result[a]]['user_hobbies']) for a in range(len(result))]
    }))
