<template>
  <div style="background-color:transparent">
    <span class="collection_title" style="background-color:transparent"> 
        {{movie_list.title}}
    </span>
    
    <MovieCollectionCard
    style="background-color:transparent"
    v-for="movie in movie_list.movies"
    :key="movie.id"
    :movie="movie"/>
    </div>

</template>

<script>
import axios from 'axios'
import MovieCollectionCard from './MovieCollectionCard.vue';

export default {
    components: { MovieCollectionCard },
    name:'MovieCollection',
    data(){
        return{
            movies:null,
        }
    },
    props:{
        movie_list:Object,
    },
    methods:{
    deletelist() {
        axios({
            method: "delete",
            url: `http://127.0.0.1:8000/movies/likemovielist/${this.movie_id}/append/${this.movie_list.id}/`,
            headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        })
            .then(() => {
            this.$store.commit("like_movie_list");
            })
            .catch((err) => {
            console.log(err);
            });
    },
    }
}
</script>

<style>
.collection_title{
    font-family: NeoBD;
    font-size:2vW;
}
</style>