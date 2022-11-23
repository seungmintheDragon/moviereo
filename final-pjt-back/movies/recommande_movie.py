import json
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse


'''
genres_datas = {
    12 : '모험',
    14 : '판타지',
    16 : '애니메이션',
    18 : '드라마',
    27 : '공포',
    28 : '액션',
    35 : '코미디',
    36 : '역사',
    37 : '서부',
    53 : '스릴러',
    80 : '범죄',
    99 : '다큐멘터리',
    878 : 'SF',
    9648 : '미스테리',
    10402 : '음악',
    10749 : '로맨스',
    10751 : '가족',
    10752 : '전쟁',
    10770 : 'TV 영화'
}
# 영화 데이터 json 파일을 csv파일로 변경
with open('./fixtures/movie.json', 'rt', encoding='UTF-8') as input_file, open('movieitem.csv', 'w', newline= '', encoding='UTF-8') as output_file:
    data = json.load(input_file)

    f = csv.writer(output_file)

    f.writerow(["title", "release_date", "popularity","vote_count","vote_average","genres","actor","director", "id"])

    for datum in data:
        temp_list = []

        for g in datum["fields"]["genres"]:
            temp_list.append({
                "id" : g,
                "name": genres_datas[g]
            })

        f.writerow([datum["fields"]["title"], datum["fields"]["release_date"], datum["fields"]["popularity"], datum["fields"]["vote_count"], datum["fields"]["vote_average"], temp_list, datum["fields"]["actor"], datum["fields"]["director"], datum["pk"]])
'''

# 추천영화
def find_movie():
    pd.set_option('display.max_rows', 10000) # 행을 최대 100개까지 출력
    pd.set_option('display.max_columns', 10000) # 열을 최대 100개 까지 출력
    pd.set_option('display.width', 10000) #출력 창 넓이 설정

    data = pd.read_csv('movieitem.csv', encoding='UTF-8')
    data = data[["title", "release_date", "popularity","vote_count","vote_average","genres","actor","director","id"]]
    m = data["vote_count"].quantile(0.9)
    # data = data.loc[data["vote_count"] >= m]
    C = data['vote_average'].mean()

    def weighted_rating(x,m=m,C=C):
        v=x["vote_count"]
        R=x['vote_average']
        return (v/(v+m)*R)+(m/(m+v)*C)


    data['recommed_count']=data.apply(weighted_rating,axis=1)
    data['genres'] = data['genres'].apply(literal_eval)
    data['genres']=data['genres'].apply(lambda x : [d['name'] for d in x]).apply(lambda x: " ".join(x))

    data.to_csv('data2.csv')
    count_vector = CountVectorizer(ngram_range=(1,3))
    c_vector = count_vector.fit_transform(data['genres'])
    
    sparse.save_npz("yourmatrix.npz", c_vector)


def get_recommend_movie_list(df, movies, top=30):
    c_vector_genres = sparse.load_npz("yourmatrix.npz")
    genre_c_sim = cosine_similarity(c_vector_genres,c_vector_genres).argsort()[:,::-1]
    recom = dict()
    for movie in movies:
        target_movie_index = df[df['title']==movie['title']].index.values
        sim_index = genre_c_sim[target_movie_index, :top].reshape(-1)
        sim_index=sim_index[sim_index != target_movie_index]
        result = df.iloc[sim_index].sort_values('recommed_count', ascending=False)[:10]
        result = result.values.tolist()
        for i in result:
            if recom.get(i[-2]):
                recom[i[-2]][0] += 1
            else:
                recom[i[-2]] = [1, i[-1]]
    return recom


def resforreco(movies):
    pd.set_option('display.max_rows', 10000) # 행을 최대 100개까지 출력
    pd.set_option('display.max_columns', 10000) # 열을 최대 100개 까지 출력
    pd.set_option('display.width', 2000) #출력 창 넓이 설정

    data = pd.read_csv('data2.csv', encoding='UTF-8')
    temp = get_recommend_movie_list(data, movies)
    # ans = []
    # ans = temp.values.tolist()
    send_res = []
    sorted_temp = sorted(temp.items(), key = lambda item: (item[1][0],item[1][1]), reverse=True)
    for i in sorted_temp:
        send_res.append(i[0])
        if len(send_res) >= 5:
            break
    
    # print(send_res)
    return send_res
