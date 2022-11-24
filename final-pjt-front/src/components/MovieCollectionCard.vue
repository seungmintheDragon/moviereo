<template>
<div>
    <div class="" @click="movie_detail">
        <div>
            <img class="col_image" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" alt="">
        </div>
        {{movie.title}}

    </div>
</div>
</template>

<script>
export default {
    name:"MovieCollectionCard",
    props:{
        movie:Object,
    },
    methods: {
        movie_detail() {
        this.$router.push({name:'moviedetail', params:{movie_pk:this.movie.id}})
    },
    }
}
</script>

<style>
.col_image{
    border-radius: 1rem;
    width:25rem;
    height: 14rem;
    box-shadow: 0.3rem 0.3rem 0.6rem black;
}
</style>