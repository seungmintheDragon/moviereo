<template>
  <div class="home">


    <!-- 테스트 -->

    <div class="title">
      <div class="slider">
        <div class="slides">
          <div id="slide-1" class="user-wrap">
            <p class="movie_title">{{title_movie1?.title}}</p>
            <p class="movie_date">{{title_movie1?.release_date.substr(0,4)}}</p>
            <p class="movie_vote">⭐{{title_movie1?.vote_average}}</p>
            <img  class="titleimg" :src="`https://image.tmdb.org/t/p/original${title_movie1?.backdrop_path}`" alt="">
            </div>

          <div id="slide-2" class="user-wrap">
            <p class="movie_title">{{title_movie2?.title}}</p>
            <p class="movie_date">{{title_movie2?.release_date.substr(0,4)}}</p>
            <p class="movie_vote">⭐{{title_movie2?.vote_average}}</p>
            
            <img class="titleimg"  :src="`https://image.tmdb.org/t/p/original${title_movie2?.backdrop_path}`"  alt=""></div>

          <div id="slide-3" class="user-wrap">
            <p class="movie_title">{{title_movie3?.title}}</p>
            <p class="movie_date">{{title_movie3?.release_date.substr(0,4)}}</p>
            <p class="movie_vote">⭐{{title_movie3?.vote_average}}</p>
            <img  class="titleimg"  :src="`https://image.tmdb.org/t/p/original${title_movie3?.backdrop_path}`" alt="">
            </div>

        </div>

        <a href="#slide-1"></a>
        <a href="#slide-2"></a>
        <a href="#slide-3"></a>
      </div>
    </div>



    <!-- 상위 랜덤 영화 보여주기 -->
    <div>

      <!-- <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="false" style="margin:30px;" >
        <div class="carousel-indicators" >
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img :src="`https://image.tmdb.org/t/p/original${random_movies[0].backdrop_path}`"  class="w-50 titleimage" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random_movies[0].title}}</h5>
              <p>Some representative placeholder content for the first slide.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img :src="`https://image.tmdb.org/t/p/original${random_movies[1].backdrop_path}`" class="w-50 titleimage" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random_movies[1].title}}</h5>
              <p>Some representative placeholder content for the second slide.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img :src="`https://image.tmdb.org/t/p/original${random_movies[2].backdrop_path}`" class="w-50 titleimage" alt="...">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{random_movies[2].title}}</h5>
              <p>Some representative placeholder content for the third slide.</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div> -->
      <!-- 상위 끝  -->

      <!-- 추천 영화 -->
      <div class='recommand_movie1'>
        <h3 style="font-family: NeoBD;"> 당신을 위한 추천 영화 </h3>
        <div class= "row row-cols row-cols-md-5 g-5 outcard" style="margin-top:5px">
          <movie-recommand-card
          v-for="recomovie in random_movies"
          :key="recomovie.id"
          :recomovie="recomovie"
          />
        </div>
      </div>
    </div>



  </div>
</template>

<script>
// import MovieCarousel from '../components/MovieCarousel.vue'
import axios from 'axios'
import MovieRecommandCard from '../components/MovieRecommandCard.vue'

export default {
  components: { MovieRecommandCard },
  name: 'HomeView',
  data(){
    return{
      random_movies: null,
      title_movie1:null,
      title_movie2:null,
      title_movie3:null,
    }
  },
  // components: {MovieCarousel},
  methods:{
    getTitleRandomMovie(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/',
      })
      .then((res)=>{
        this.random_movies = res.data
        this.title_movie1 = res.data[0]
        this.title_movie2 = res.data[1]
        this.title_movie3 = res.data[2]
      })
      .catch((err)=>console.log(err))
    },


  },
  created(){
    this.getTitleRandomMovie()
  }
}
</script>

<style>

.recommand_movie1{
  text-align: left;
  margin: 5%;
}

.category{
  font-family: NeoBD;
}

.user_wrap{
  position:relative;
}

.movie_title{
  font-family: NeoLT;
  font-size: 2.5rem;
  color: rgb(255, 255, 255);
  background: none;
  position: absolute;
  left:100px;
  top:400px;
}
.movie_date{
  font-family: NeoLT;
  font-size: 1.2rem;
  color: rgb(255, 255, 255);
  background: none;
  position: absolute;
  left:105px;
  top:465px;
}
.movie_vote{
  font-family: NeoLT;
  font-size: 1.2rem;
  color: rgb(255, 222, 36);
  background: none;
  position: absolute;
  left:170px;
  top:465px;
}

.outcard{
}

/* 상위 carousel 관련 CSS*/
  .title {
      box-sizing: border-box;
    }
  
  .slider {
    width: 100%;
    text-align: center;
    overflow: hidden;
    margin-bottom: -70px;
  }
  
  .slides {
    display: flex;
    overflow-x: 100%;
    overflow: hidden;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }




  .slides::-webkit-scrollbar {
    width: 10px;
    height: 10px;
     }
  .slides::-webkit-scrollbar-thumb {
    background: rgb(34, 34, 34);
  }
  .slides::-webkit-scrollbar-track {
    background: transparent;
 
  }
  .slides > div {
    scroll-snap-align: start;
    flex-shrink: 0;
    width: 100%;
    height: 600px;
    overflow: hidden;
    background: rgb(22, 22, 22);
    transform-origin: center center;
    transform: scale(1);
    transition: transform 0.8s;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 100px;
    mask-image: linear-gradient(to top, transparent 5%, black 50%);

  }
  .slides img {
  width: 90%;
  height: 100%;
  justify-content: right;
  object-fit: cover;
  -webkit-mask-image: linear-gradient(to right, transparent 5%, black 100%);
  mask-image: linear-gradient(to right, transparent 5%, black 100%);

} 

  .author-info {
    background: rgba(0, 0, 0, 0.75);
    color: rgb(0, 0, 0);
    padding: 0.75rem;
    text-align: center;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    margin: 0;
  }  
  .author-info a {
    color: white;
  } 
  .titleimg {
    object-fit: cover;
    object-position:10% 15% ;
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-mask-image: linear-gradient(to top, transparent 5%, black 100%);
    mask-image: linear-gradient(to top, transparent 5%, black 100%);
  }
  
  .slider > a {
    display: inline-flex;
    opacity: 20%;
    width: 1.5rem;
    height: 1.5rem;
    background: rgb(61, 61, 61);
    text-decoration: none;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    margin: 0 1rem 1rem 0;
    position: relative;
  }
  .slider > a:active {
    top: 0px;
  }
  .slider > a:focus {
    background: rgb(80, 79, 79);
  }
  
/* 이미지 테스트 */
/* .testimg {
  max-width: 100%;
  display: block;
}

.container {
  max-width: 400px;
  height: 300px;
  position: relative;
  
}

.container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-mask-image: linear-gradient(to top, transparent 5%, black 100%);
  mask-image: linear-gradient(to top, transparent 5%, black 100%);
}  */
</style>