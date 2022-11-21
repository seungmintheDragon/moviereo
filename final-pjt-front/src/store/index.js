import Vue from "vue";
import Vuex from "vuex";
import article from "@/store/modules/article";
import movie from "@/store/modules/movie";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    is_logined: false,
    user_movie_list: null,
  },
  getters: {},
  mutations: {
     like_movie_list(state) {
       axios({
         method: 'get',
         url:`http://127.0.0.1:8000/movies/likemovie/`,
         headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
       })
         .then((res) =>{
           state.user_movie_list = res.data
         })
         .catch((err)=> {
           console.log(err);
         })
     },
        // 무비 리스트 불러오기
    logins(state) {
      if (localStorage.getItem("jwt")) {
        state.is_logined = true;
        axios({
          method: 'get',
          url:`http://127.0.0.1:8000/movies/likemovie/`,
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
        })
          .then((res) =>{
            state.user_movie_list = res.data
          })
          .catch((err)=> {
            console.log(err);
          })
      } else {
        state.is_logined = false;
      }
    },
    // 로그아웃기능
    logout(state) {
      localStorage.removeItem('jwt')
      state.is_logined = false
      state.user_movie_list = null
    },
  },
  actions: {
      movie_list_create(context, payload) {
        axios({
          method: 'POST',
          url: `http://127.0.0.1:8000/movies/likemovielist/${payload.movie_id}/${payload.list_id}/`,
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`},
          data: {
            'title': payload.title,
          }
        })
          .then(() => {
            context.commit('like_movie_list')
          })
          .catch((err) => {
            console.log(err);
          })
      },
      movie_list_new(context, payload) {
        axios({
          method: 'POST',
          url: `http://127.0.0.1:8000/movies/likemovienew/${payload.movie_id}/`,
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`},
          data: {
            'title': payload.title,
          }
        })
          .then(() => {
            context.commit('like_movie_list')
          })
          .catch((err) => {
            console.log(err);
          })
      },
      
  },
  modules: {
    article,
    movie,
  },
});
