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



# genres_datas = {
#     12 : '모험',
#     14 : '판타지',
#     16 : '애니메이션',
#     18 : '드라마',
#     27 : '공포',
#     28 : '액션',
#     35 : '코미디',
#     36 : '역사',
#     37 : '서부',
#     53 : '스릴러',
#     80 : '범죄',
#     99 : '다큐멘터리',
#     878 : 'SF',
#     9648 : '미스테리',
#     10402 : '음악',
#     10749 : '로맨스',
#     10751 : '가족',
#     10752 : '전쟁',
#     10770 : 'TV 영화'
# }
# # 영화 데이터 json 파일을 csv파일로 변경
# with open('movie_data_json.json', 'rt', encoding='UTF-8') as input_file, open('movie.csv', 'w', newline= '', encoding='UTF-8') as output_file:
#     data = json.load(input_file)

#     f = csv.writer(output_file)

#     f.writerow(["title", "release_date", "popularity","vote_count","vote_average","genres","actor","director"])

#     for datum in data:
#         temp_list = []

#         for g in datum["genres"]:
#             temp_list.append({
#                 "id" : g,
#                 "name": genres_datas[g]
#             })

#         f.writerow([datum["title"], datum["release_date"], datum["popularity"], datum["vote_count"], datum["vote_average"], temp_list, datum["actor"], datum["director"]])


# 추천영화
def find_movie(movie):
    pd.set_option('display.max_rows', 580) # 행을 최대 100개까지 출력
    pd.set_option('display.max_columns', 8) # 열을 최대 100개 까지 출력
    pd.set_option('display.width', 1000) #출력 창 넓이 설정

    data = pd.read_csv('movie.csv', encoding='UTF-8')

    data = data[["title", "release_date", "popularity","vote_count","vote_average","genres","actor","director"]]

    m = data["vote_count"].quantile(0.9)
    print(m)
    data = data.loc[data["vote_count"] >= m]
    C = data['vote_average'].mean()

    def weighted_rating(x,m=m,C=C):
        v=x["vote_count"]
        R=x['vote_average']
        return (v/(v+m)*R)+(m/(m+v)*C)

    data['recommed_count']=data.apply(weighted_rating,axis=1)
    data['genres'] = data['genres'].apply(literal_eval)
    data['genres']=data['genres'].apply(lambda x : [d['name'] for d in x]).apply(lambda x: " ".join(x))

    count_vector = CountVectorizer(ngram_range=(1,3))
    c_vector_genres = count_vector.fit_transform(data['genres'])

    genre_c_sim = cosine_similarity(c_vector_genres,c_vector_genres).argsort()[:,::-1]

    def get_recommend_movie_list(df, movie_title, top=30):
        target_movie_index = df[df['title']==movie_title].index.values 
        sim_index = genre_c_sim[target_movie_index, :top].reshape(-1)

        sim_index=sim_index[sim_index != target_movie_index]
        result = df.iloc[sim_index].sort_values('recommed_count', ascending=False)[:10]
        
        return result


    print('마음에들엇던영화의 제목')
    movie = input()
    temp = get_recommend_movie_list(data,movie_title=movie)
    ans = []
    ans = temp.values.tolist()
    ans = array(ans)

    return ans