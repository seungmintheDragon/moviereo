<template>
  <div>
    <!-- <h1 style="font-family: NeoBD" >검색결과</h1> -->
    <div class="recommand_movie1">
      <div style="text-align:center;">
      <div class="box">
      <div class="loader1">
      </div>
      </div> <br>

        <span style="font-family: NeoBD; color:gray; font-size:1.3rem;">{{ searchelength }}</span><span style="font-family: NeoRG;color:gray;font-size:1.3rem;">개의 영화를 찾았습니다.</span> <br> 
        <span style="font-family: NeoBD;font-size:2rem;"> {{ searchinput }}</span>
        <span style="font-family: NeoLT;font-size:2rem;">의 검색결과</span>
      </div>
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
		},
    searchinput() {
      return this.$store.state.movie.search_input
    }
	}
};
</script>

<style>
.loader1{
  position: relative;
  height: 80px;
  width: 80px;
  border-radius: 80px;
  border: 3px solid  rgba(255,255,255, .7);

  top: 28%;
  top: -webkit-calc(50% - 43px);
  top: calc(50% - 43px);
  left: 35%;
  left: -webkit-calc(50% - 43px);
  left: calc(50% - 43px);

  -webkit-transform-origin: 50% 50%;
      transform-origin: 50% 50%;
  -webkit-animation: loader1 3s linear infinite;
      animation: loader1 3s linear infinite;
}

.loader1:after{
  content: "";
  position: absolute;
  top: -5px;
  left: 20px;
  width: 11px;
  height: 11px;
  border-radius: 10px;
  background-color: #fff;
}

@-webkit-keyframes loader1{
    0%{-webkit-transform:rotate(0deg);}
    100%{-webkit-transform:rotate(360deg);}
}

@keyframes loader1{
    0%{transform:rotate(0deg);}
    100%{transform:rotate(360deg);}
}

</style>