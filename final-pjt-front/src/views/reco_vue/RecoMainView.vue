<template>
  <div>
    <span style="font-family: NeoBD; font-size: 3vW;"> 좋아하는 영화 선택</span>
    <pre style="font-family: NeoRG; font-size: 0.8vW;color: gray;"> 좋아하는 영화를 최대 7개 골라주세요
    영화를 검색하거나, 랜덤으로 추천받을 수 있어요!</pre>
    <div class="recommand-head">
      <div class="input-group">
        <input
          type="text"
          class="
          reco_search_bar"
          placeholder=" 영화를 찾아보세요!"
          aria-label=""
          v-model="input_value"
          @keyup.enter="find_movie"
        />
        <button
          class="reco_search_btn"
          type="button"
          @click="find_movie"
        >
          검색
        </button>
      </div>

      <!-- <button
        class="btn btn-outline-secondary"
        type="button"
        @click="recomandrandom"
      >
        없어요! 랜덤 추천!
      </button> -->

    </div>
    <!-- 선택된 영화 보여주기 -->
    <div>
      <div v-for="cart_list in movie_cart" :key="cart_list.id">
        <p>
          {{ cart_list.title }}
        </p>
        <button type="button" class="btn btn-primary" @click="cart(cart_list)">
          삭제
        </button>
      </div>
      <button
        type="button"
        class=""
        v-if="movie_cart.length"
        @click="recomive"
      >
        영화 추천!
      </button>
    </div>
    <!-- 선택할 영화 카드 보여주기 -->
    <div>
      <div class="recommand_movie1">
        <h3 style="font-family: NeoBD" v-if="search_list">
          영화를 골라주세요!
        </h3>
        <div
          class="row row-cols row-cols-md-5 g-5 outcard"
          style="margin-top: 5px"
        >
          <movie-list-item
            v-for="recomovie in search_list"
            :key="recomovie.id"
            :recomovie="recomovie"
            :movie_cart="movie_cart"
            @cart="cart"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from "../../components/MovieListItem.vue";
export default {
  components: { MovieListItem },
  name: "RecoMainView",
  data() {
    return {
      input_value: null,
      movie_cart: [],
    };
  },
  computed: {
    genre() {
      return this.$store.state.movie.genre;
    },
    search_list() {
      return this.$store.state.movie.searchmovie;
    },
  },
  methods: {
    find_movie() {
      this.$store.dispatch("movie/search_movie", this.input_value);
    },
    cart(movie) {
      if (this.movie_cart.indexOf(movie) === -1) {
        if (this.movie_cart.length === 7) {
          return alert("7개만 선택해 주세요!");
        }
        this.movie_cart.push(movie);
      } else {
        this.movie_cart.splice(this.movie_cart.indexOf(movie), 1);
      }
    },
    recomive() {
      this.$store.dispatch("movie/recommand_movie", this.movie_cart);
    },
    // 개수 조정 최소 10개정도
    recomandrandom() {
      this.$store.dispatch("movie/random_recommnad");
    },
  },
  created(){
    this.recomandrandom()
  }
};
</script>

<style>
.recommand-head{
width:30rem;
margin: auto;
}
.input-group{
  border-radius: 1rem;
  /* box-shadow: 0.3rem 0.3rem black ; */
}
/* 검색 바  */
.reco_search_bar{
  border-radius: 0.7rem;
  font-family: NeoRG;
  width:85%;
  border:none;
  background-color: white;

}
.reco_search_bar::placeholder{
  font-family: NeoRG;
  font-size:0.8vW;
  text-align: center;
  background-color: white;

}
.reco_search_btn{
  border-radius: 0.7rem;
  font-family: NeoRG;
  color:white;
  width:15%;
  border:none;
  background-color: rgb(34, 111, 255);

}
</style>