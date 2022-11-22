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
      <button class="btn btn-outline-secondary" type="button">없어요!</button>
    </div>

    <div>
      <div class="recommand_movie1">
        <h3 style="font-family: NeoBD" v-if="search_list">영화를 골라주세요!</h3>
        <div
          class="row row-cols row-cols-md-5 g-5 outcard"
          style="margin-top: 5px"
        >
          <movie-list-item
            v-for="recomovie in search_list"
            :key="recomovie.id"
            :recomovie="recomovie"
						@click="recommand_movie(removie)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '../../components/MovieListItem.vue';
export default {
  components: { MovieListItem },
  name: "RecoMainView",
  data() {
    return {
      input_value: null,
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
		recommand_movie(movie) {
			this.$store.dispatch("movie/recommend_move", movie)
		},
  },
};
</script>

<style>
</style>