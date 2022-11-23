<template>
  <div style="background-color: transparent;" class="check_whole">
    <div class="form-check check_area" @click="makelist" style="padding:0.2rem; background-color: transparent;">
      <input
        class="form-check-input"
        type="checkbox"
        v-model="torf"
        @click="addList"
        :id="movie_list.id"
      />
      <label
        class="form-check-label"
        :for="movie_list.id"
        style="background-color: transparent;
        font-family: PreL;"
      >
        {{ movie_list.title }}
      </label>
        <hr>
    </div>
    <!-- <div>
      <button class="collection_del_button" @click="deletelist"> X </button>
    </div> -->
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieListCheck",
  data(){
    return{
      
    }
  },
  props: {
    movie_list: Object,
    movie_id: Number,
  },
  computed: {
    torf: {
      get() {
        const res = this.movie_list.movies.some((x) => {
          return x.id === this.movie_id;
        });
        return res;
      },
      set() {
        const res = this.movie_list.movies.some((x) => {
          return x.id === this.movie_id;
        });
        return res;
      },
    },
  },
  methods: {
    // 컬렉션에 담았을 때 메세지 출력
    addList(){
      this.$emit('add-list', this.torf)

    },
    makelist() {
      if (this.torf) {
        axios({
          method: "put",
          url: `http://127.0.0.1:8000/movies/likemovielist/${this.movie_id}/append/${this.movie_list.id}/`,
          headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        })
          .then(() => {
            this.$store.commit("like_movie_list")
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        axios({
          method: "post",
          url: `http://127.0.0.1:8000/movies/likemovielist/${this.movie_id}/append/${this.movie_list.id}/`,
          headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
        })
          .then(() => {
            this.$store.commit("like_movie_list")
            ;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
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
  },
};
</script>

<style>
.check_whole{
  display: flex;
}
.check_area{

}
/* .collection_del_button{
  color:white;
  border: none;
  font-family: NeoLT;
} */
</style>