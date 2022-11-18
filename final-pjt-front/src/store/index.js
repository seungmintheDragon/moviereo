import Vue from "vue";
import Vuex from "vuex";
import article from "@/store/modules/article";
import movie from "@/store/modules/movie";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    is_logined: false,
  },
  getters: {},
  mutations: {
    logins(state) {
      if (localStorage.getItem("jwt")) {
        state.is_logined = true;
      } else {
        state.is_logined = false;
      }
    },
    // 로그아웃기능
    logout(state) {
      localStorage.removeItem('jwt')
      state.is_logined = false
    },
  },
  actions: {},
  modules: {
    article,
    movie,
  },
});
