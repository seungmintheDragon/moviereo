<template>
<div>
    <div class="col" style="background-color:transparent;">
    <div class="card card-container border-0 colcard "  @click="movie_detail" style="background-color:transparent; ">
        <div style="background-color:transparent;">
            <p class="col-title">{{movie.title}} </p>
            <img class="col_image" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" alt="" style="background-color:transparent; width:20rem;height:auto;    margin-left: 10rem;
">
        </div>
        <!-- <span style="background-color:transparent;color:black; font-family: NeoBD;"> 
            {{movie.title}}
        </span> -->

    </div>
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
}
.colcard{
    margin-top:4rem;
    margin-left: -8rem;
    width: 80rem;
    background-color: black;

}
.colcard:hover {
  background-color:transparent;
}

.col_image:hover{
  opacity: 0.3;
}

.col-title{
  position: absolute;
  text-align: center;
  top: 110%;
  left: 25%;
  color:black;
  transform: translate(-50%, -50%);
  font-family: NeoBD;
  font-size: 1.2rem;
  background-color:transparent;
  word-wrap: break-word;

  }



</style>