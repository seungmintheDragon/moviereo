<template>
  <div>
    <h1>검색결과</h1>
    <div class="recommand_movie1">
      <h3 style="font-family: NeoBD">{{ searchelength }}개의 영화</h3>
      <div
        class="row row-cols row-cols-md-5 g-5 outcard"
        style="margin-top: 5px"
      >
        <movie-recommand-card
          v-for="recomovie in random_movies"
          :key="recomovie.id"
          :recomovie="recomovie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MovieRecommandCard from '../components/MovieRecommandCard.vue'

export default {
  name: "SearchView",
	components: { MovieRecommandCard },
	computed: {
		random_movies() {
			return this.$store.state.movie.searchres
		},
		searchelength() {
			return this.$store.state.movie.searchres.length
		}
	}
};
</script>

<style>
</style>