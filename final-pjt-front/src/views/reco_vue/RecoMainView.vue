<template>
  <div>
    <div class="input-group" style="width: 65%">
      <input
        type="text"
        class="form-control"
        placeholder="좋아 하는 영화가 있으십니까? 있으시다면 찾아주세요!"
        aria-label="Recipient's username with two button addons"
        v-model="input_value"
        @keyup.enter="find_movie"
      />
      <button
        class="btn btn-outline-secondary"
        type="button"
        @click="find_movie"
      >
        찾기
      </button>
      <button
        class="btn btn-outline-secondary"
        type="button"
        @click="recomandrandom"
      >
        없어요! 랜덤 추천!
      </button>
    </div>
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
        class="btn btn-success"
        v-if="movie_cart.length"
        @click="recomive"
      >
        영화 추천!
      </button>
    </div>
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
    recomandrandom() {
      this.$store.dispatch("movie/random_recommnad");
    },
  },
};
</script>

<style>
</style>