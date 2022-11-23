<template>
      <div
        class="moviecard_2"
        @click="getMovieId()"
      >
        <p class="movie-title2">{{ similar_movie.title }}</p>
        <img
          v-if="similar_movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w500${similar_movie.poster_path}`"
          class="card-img-top cardimg"
          alt="..."
          style="width: 14rem; height: 21rem"
        />
        <img
          v-else
          src="../assets/null_image.jpg"
          style="width: 14rem; height: 21rem"
        />
      </div>
</template>

<script>
export default {
  name: "MovieSimilarCard",
  props: { similar_movie: Object },
  methods: {
    getMovieId() {
      // this.$router.push({name:'moviedetail', params:{movie_pk:this.similar_movie}}).catch((err) => {console.log(err);})
      this.$router.go(
        this.$router
          .push({
            name: "moviedetail",
            params: { movie_pk: this.similar_movie.id },
          })
          .catch((err) => {
            console.log(err);
          })
      );
    },
  },
};
</script>

<style>
.moviecard_2 {
  border-radius: 1rem;
  background-color: transparent;
  padding: 1rem;
}
.movie-title2 {
  width: 5.5rem;
  position: absolute;
  opacity: 0;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(50%, -50%);
  font-family: NeoEB;
  font-size: 1rem;
  background-color: transparent;
  word-wrap: break-word;
}
.moviecard:hover .movie-title2 {
  opacity: 1;
  color: white;
  word-break: keep-all;
}
</style>