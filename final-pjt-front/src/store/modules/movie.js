import axios from "axios";
import router from '../../router';

const state = () => {
  return {
    genre: {
      모험: 12,
      판타지: 14,
      애니메이션: 16,
      드라마: 18,
      공포: 27,
      액션: 28,
      코미디: 35,
      역사: 36,
      서부: 37,
      스릴러: 53,
      범죄: 80,
      다큐멘터리: 99,
      SF: 878,
      미스테리: 9648,
      음악: 10402,
      로맨스: 10749,
      가족: 10751,
      전쟁: 10752,
      "TV 영화": 10770,
    },
    searchmovie: null,
    recommandation: null,
    searchres: null,
  };
};

const getters = {};
const mutations = {
  SEARCH_MOVIE(state, res) {
    state.searchmovie = res
  },
  RECO_MOVIE(state, res) {
    state.recommandation = res
  },
  SEARCHRES(state, res) {
    state.searchres = res
  },
};
const actions = {
  search_movie(context, searchinput) {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/movies/search/${searchinput}/`,
    })
      .then((res) => {
        context.commit("SEARCH_MOVIE", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  recommand_movie(context, movie) {
    axios({
      method: "POST",
      url: 'http://127.0.0.1:8000/movies/recommend/',
      data: {
        'movies': movie,
      },
      headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
    })
      .then((res) => {
        context.commit("RECO_MOVIE", res.data)
      })
      .then(() => {
        router.push({ name:'resultrecoview'})
      })
      .catch(()=>{
        alert('영화를 더 골라주세요.')
      })
  },
  random_recommnad(context) {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/',
    })
    .then((res)=>{
      context.commit("SEARCH_MOVIE", res.data);
    })
    .catch((err)=>console.log(err))
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
