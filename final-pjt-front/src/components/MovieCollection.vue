<template>
  <div  class="colbox">
    <p 
    style="font-family:NeoLT;
    padding:0.5rem;
    margin-bottom:1rem;
    text-align:left;
    position:absolute;
    width:71.9rem;"> 컬렉션 #{{movie_list.id}}. 
    <span style="font-family:NeoRG;background-color:transparent;">
    {{movie_list.title}}
    </span>
    <button
     @click='deletelist()'
     class="btn btn-secondary btn-sm"
     style="float:right; font-family:PreL"
     > 삭제 </button>
    </p>


    <div
    class="row row-cols row-cols-md-3 g-0 outcard"
    style="background-color:transparent;"
    >
    <MovieCollectionCard
    style="background-color:transparent;
    display:;
    "
    v-for="movie in movie_list.movies"
    :key="movie.id"
    :movie="movie"/>

    </div>
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
.colbox{
  background-color:transparent; 
  border:solid 1px black;
  box-shadow:3px 3px 1px gray;
  margin:1rem;
  overflow-x:scroll;
  overflow-y:hidden;
}
.collection_title{
    font-family: NeoBD;
    font-size:2vW;
}
</style>