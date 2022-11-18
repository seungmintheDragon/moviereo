<template>
  <div class="detail">
    <div>
    <img class="backdropimg"  :src="`https://image.tmdb.org/t/p/original${movie_detail?.backdrop_path}`" alt="">
    </div>

    <div class="info">
        <img class="poseterimg"  :src="`https://image.tmdb.org/t/p/original${movie_detail?.poster_path}`" alt="">
        <span class="detail_title"> {{movie_detail?.title}} </span>

    </div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MovieDetailView',
    data(){
        return{
            movie_detail: null,
        }
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
    },
    created(){
        this.getMovieDetail(this.$route.params.movie_pk)
    }
    
}
</script>

<style>
.detail{
    position: relative;
}
.backdropimg{
    width: 100%;
    opacity: 0.1;
    mask-image: linear-gradient(to top, transparent 5%, black 100%);

}
.poseterimg{
    width: 300px;
    border-radius: 30px;
}
.info{
    position: absolute;
    display: flex;
    top: 5%;
    margin: 5%;
    background-color:transparent;

}

.detail_title{
    font-family: NeoLT;
    font-size: 3rem;
    width:500px;
    background-color:transparent;
    margin-left: 10%;


}

</style>