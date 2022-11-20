<template>
<div>

    <div class="detail">
        <div>
            <img class="backdropimg"  :src="`https://image.tmdb.org/t/p/original${movie_detail?.backdrop_path}`" alt="">
        </div>
        <!-- movie 기본 정보 -->
        <div class="info">
            <!-- 포스터 -->
            <div style="background-color:transparent;">
              <img class="poseterimg"  
              v-if="movie_detail.poster_path"
              :src="`https://image.tmdb.org/t/p/original${movie_detail?.poster_path}`" alt="">
              <img 
                v-else
                src="../assets/null_image.jpg"
                class="d_profile_img">
            </div>

            <!-- 이미지 외 텍스트 정보 -->
            <div class="info_text">
                <span class="detail_title"> {{movie_detail?.title}} </span>
                <br> 
                <!-- 연도 및 평점 -->
                <div class="date">
                    {{movie_detail?.release_date.substr(0,4)}}
                </div>
                <div class="vote">
                    ★ {{movie_detail?.vote_average}}
                    <span class="vote" 
                    style="font-size:0.5rem;font-family: NeoLT;
                    "> (TMDB) </span>
                </div>
                <!-- 장르 -->
                <div class="movie_genre"
                    v-for="genre in movie_detail.genres"
                    :key="genre.id">
                    <button class="genre_btn" > {{genre.name}} </button>
                </div>
                <br>
                <br>
                <!-- 줄거리 -->
                <details v-if="movie_detail.overview">
                    <summary style="font-family: PreR;
                    font-size: 1rem;
                    "> 줄거리 </summary>
                    <div class="overview" >
                        {{movie_detail?.overview}}
                        <hr>
                    </div>
                </details>
                <div v-else class="none_overview"> 

                </div>
                <hr style="margin-top:5rem;">
                <!-- 감독 및 출연 -->
                
                <div class="staff">
                    <!-- 감독  -->
                    <div class="director" style="display: inline-block; float: left;background-color:transparent;">
                        <div class="staff_title">
                            감독
                        </div>
                        <div class="d_profile">
                            <div class="d_profile_box">
                                <img
                                v-if="movie_detail.director[0].profile_path"
                                class="d_profile_img" 
                                :src="`https://image.tmdb.org/t/p/original${movie_detail.director[0].profile_path}`" alt="">
                                <img 
                                v-else
                                src="../assets/none-profile.png"
                                class="d_profile_img">
                            </div>
                            <div class="d_profile_name">
                                {{movie_detail.director[0].name}}    
                            </div>  
                        </div>
                    </div>
                     <!-- 배우 -->
                    <div class="actor" style="display:inline-block; float: left; background-color:transparent;">
                        <div class="staff_title">
                            출연
                        </div>
                        <div v-for="actor in movie_detail.actor" :key="actor.id" class="profile">
                            <div class="profile_box">
                                <img
                                v-if="actor.profile_path"
                                class="profile_img" 
                                :src="`https://image.tmdb.org/t/p/original${actor?.profile_path}`" alt="">
                                <img 
                                v-else
                                src="../assets/none-profile.png"
                                class="profile_img">
                            </div>
                            <div class="profile_name">
                            {{actor.name}}    
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="">
            <button> 예고편 보기 </button>
            </div>
        </div>
        <hr>
            <span>
            </span>

            <!-- 코멘트 -->
            <form @submit.prevent="movieComment(movie_detail?.id)">

                <div @mouseleave="showCurrentRating(0)" style="display:inline-block;">
                        <star-rating :show-rating="false" @current-rating="showCurrentRating" @rating-selected="setCurrentSelectedRating" :increment="0.5"></star-rating>
                </div>
                <div style="margin-top:10px;font-weight:bold;">{{currentRating}}</div>
                <input type="text" v-model="movie_comment">
            </form>
        
        <!-- comment -->
        <div class="comment_box">
            <hr>
            <p style="font-family:NeoBD; font-size:1.5rem;"> 영화 감상평 </p>
            <hr>
            <div 
            v-for="comment in movie_detail.comment"
            :key="comment.id"
            >
            <span><star-rating  :inline="true" :rating="comment.rate/2" :read-only="true" :increment="0.01" :star-size="20" :show-rating="false"></star-rating>{{ comment.rate }}</span>

            <div class="comment_user">
            {{comment.user.username}}
            </div>
            <br>
            <span class="comment_content">
            {{comment.comment}}     
            </span>

            </div>
        </div>



  </div>

</div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

export default {
    name: 'MovieDetailView',
    data(){
        return{
            movie_detail: null,
            movie_comment:null,
            currentRating: null,
            currentSelectedRating: null,
            rate: null,

        }
    },
    components: {
    StarRating
    },
    methods:{
        getMovieDetail(movie_pk){
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/movies/${movie_pk}`,
            })
            .then((res)=>{
                this.movie_detail= res.data
            })
            .catch((err)=>console.log(err))
        },
        movieComment(movie_pk){
            axios({
                method:'post',
                url:`http://127.0.0.1:8000/movies/${movie_pk}/comment/`,
                data:{
                    'comment' : this.movie_comment,
                    'rate' : this.rate
                },
                headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
            })
            .then((res)=>{
                console.log(res)
            })
            .catch((err)=>{
                console.log(err)
            })
            
        },
        // 별점
        setRating: function(rating) {
            this.rating = rating;
        },
        showCurrentRating: function(rating) {
            this.currentRating = (rating === 0) ? this.currentSelectedRating : rating * 2 + "점"
        },
        setCurrentSelectedRating: function(rating) {
            this.currentSelectedRating = rating * 2 + "점";
            this.rate = rating * 2
        }
    },
    created(){
        this.getMovieDetail(this.$route.params.movie_pk)
    }
    
}
</script>

<style>

.detail{
    position: relative;
    display: block;
}
.backdropimg{
    width: 100%;
    opacity: 0.4;
    mask-image: linear-gradient(to top, transparent 5%, black 100%);

}
.poseterimg{
    width: 300px;
    border-radius: 30px;
    background-color:transparent;

}
.info{
    position: absolute;
    display: flex;
    top: 5%;
    margin: 5%;
    background-color:transparent;

}

/* 세부 디테일 */
.info_text{
    display: block;
    text-align: left;
    background-color:transparent;
    margin-left: 30px;
}
/* 영화제목 */
.detail_title{
    font-family: NeoBD;
    font-size: 4rem;
    width:500px;
    background-color:transparent;
}
/* 연도 및 평점 */
.date{
    float:left;
    font-family: NeoRG;
    font-size: 1rem;
    opacity: 0.7;
    background-color:transparent;
    margin-right: 2rem;
    margin-bottom: 0.3rem;

}
.vote{
    font-family: NeoRG;
    font-size: 1rem;
    color: rgb(255, 222, 38);
    opacity: 0.8;
    background-color:transparent;
    margin-bottom: 0.3rem;

}
/* 장르 */
.movie_genre{
    /* 블럭요소 가로정렬 */
    float:left;
    background-color:transparent;
    margin-top: 0.5rem;
    margin-bottom: 0.2rem;
}
.genre_btn{
    font-family: NeoBD;
    font-size: 1rem;
    border-radius: 15px;
    border: solid 1px rgb(153, 153, 153) ;
    color:rgb(153, 153, 153) ;
    background-color:transparent;
    margin: 0.2rem;
    padding: 0.4rem;
}
.genre_btn:hover{
    font-family: NeoBD;
    font-size: 1rem;
    border-radius: 15px;
    color:white;
    background-color: rgb(153, 153, 153) ;
    margin: 0.2rem;
    padding: 0.4rem;
}
/* 줄거리 */
.overview{
    float:left;
    background-color:transparent;
    font-family: NeoLT;
    width: 50rem;
    -webkit-line-clamp: 3;
    margin-bottom: 2rem;
}
.none-overview{
    width:7rem;
    height:10rem;
    border: solid 1px black;
}
.more {
  display: none;
  cursor: pointer;
  margin-top: 1rem;
}
/* 분류 */
.staff{
    display: block;
    background-color:transparent;
}
.staff_title{
    font-family: NeoBD;
    font-size: 1.2rem;
    background-color:transparent;
}
/* 감독 */
.d_profile{
    float:left;
    align-items: center;
    background-color:transparent;
    margin: 1rem;
}
.d_profile_box{
    width: 5.5rem;
    height: 5.5rem;
    border-radius:70%;
    overflow: hidden;
}
.d_profile_img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.d_profile_name{
    font-family: "PreS";
    font-size:1rem;
    color: rgb(223, 223, 223) ;
    text-align: center;
    width: 100px;
    word-break: keep-all;
    background-color:transparent;
    margin-top: 0.3rem;
    transform: translate(-10%, 0);
}

/* 배우 */
.profile{
    float:left;
    align-items: center;
    background-color:transparent;
    margin: 1rem;
}
.profile_box{
    width: 5.5rem;
    height: 5.5rem;
    border-radius:70%;
    overflow: hidden;
}
.profile_img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.profile_name{
    font-family: "PreS";
    font-size:1rem;
    color: rgb(223, 223, 223) ;
    text-align: center;
    width: 100px;
    word-break: keep-all;
    background-color:transparent;
    margin-top: 0.3rem;
    transform: translate(-10%, 0);
}
/* 코멘트 */
.comment_box{
    /* position: absolute; */
    margin-left: 5%;
    text-align: left;
}

.comment_user{
    font-family: NeoLT;

}


/* 테스트 */

details {
    margin-bottom: 1rem;
    background-color:transparent;

}

details > summary {
    background-color:transparent;
    padding: 1rem;
    cursor: pointer;
}

details > summary::-webkit-details-marker {
    color: transparent;
    transform: rotate3d(0, 0, 1, 90deg);
    transition: transform 0.25s;
    background-color:transparent;

}

details[open] > summary::-webkit-details-marker {
    transform: rotate3d(0, 0, 1, 180deg);
}

details[open] > summary {
    background-color:transparent;
}

/* details[open] > summary ~ * {
    animation: reveal 0.5s;
} */

@keyframes reveal {
    from {
        opacity: 0;
        transform: translate3d(0, -10px, 0);
    }

    to {
        opacity: 1;
        transform: translate3d(0, 0, 0);
    }
}
</style>