<template>
  <div style="background-color: transparent;">
    <div class="col" style="background-color: transparent; " >
      <div
        class="card card-container border-0 movie-list-card"
        style="width: 16rem; height: 24rem; "
        :class="{ ba }"
      >
        <img
          :src="`https://image.tmdb.org/t/p/w500${recomovie.poster_path}`"
          class="card-img-top cardimg"
          :class="{select:torf}"
          alt="..."
          @click="recommand_movie(recomovie)"
          style="width: 16rem; height: 24rem"
        />
        <img v-if="torf" class="check_sign" src="../assets/iconimg/check-mark-dark.png" alt="-"/>
      </div>
    </div>
    <p class="movie-list-title">
      {{ recomovie.title }}
    </p>
  </div>
</template>

<script>
export default {
  name: "MovieListitem",
  props: { recomovie: Object, movie_cart: Array },
  methods: {
    recommand_movie(movie) {
      this.$emit("cart", movie);
    },
  },
  computed: {
    torf() {
      const res = this.movie_cart.some((x) => {
        console.log(x);
        return x.title === this.recomovie.title;
      });
      return res;
    },
  },
};
</script>

<style>
.movie-list-card {
  background-color: black;
  position: relative;
}

.card-container {
  position: relative;
  background-color: transparent;
}

.movie-list-card:hover {
  animation: up .3s ;
  background-color:transparent;

}

.cardimg:hover {
  position: relative;
  opacity: 0.3;
}

.movie-list-title{
  position:absolute;
  margin-top:0.5rem;
  width:16rem;
  text-align: center;
  height:auto;
  font-family: NeoRG;
  word-break: keep-all;

}

.select {
  background-color:black;
  opacity: 0.3;

}
.check_sign{
  position: absolute;
  width:5rem;
  top:10rem;
  left:5.5rem;
  background-color: transparent;

}
@keyframes up { /* @keyframes를 이용해 shake의 각도를 좌우 15deg로 조정 */
    0%{
      top:0;
    }
    100%{
      top:-1rem;
    }
    
}
</style>