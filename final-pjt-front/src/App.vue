<template>
  <div id="app" class="container_disable">
    <nav>
      <router-link to="/">메인</router-link> |
      <router-link :to="{ name: 'recomaintview' }">영화 추천</router-link> |
      <router-link to="/mypage">마이페이지</router-link> |
      <input
        class="searchbar"
        type="text"
        placeholder="search bar"
        v-model="searchinput"
        @keyup.enter="search_movie"
      />
      |
      <span :class="{ dinone: is_logined }">
        <router-link to="/login">로그인</router-link> |
        <router-link to="/signup">회원 가입</router-link>
      </span>
      <span :class="{ dinone: !is_logined }">
        <router-link to="/logout">로그아웃</router-link> |
      </span>
    </nav>
    <router-view />
    <loading-spinner :loading="!isLoading" />
  </div>
</template>

<script>
import axios from "axios";
import LoadingSpinner from "./components/LoadingSpinner.vue";
export default {
  components: { LoadingSpinner },
  name: "app",
  data() {
    return {
      searchinput: null,
      isLoading: true,
    };
  },
  computed: {
    is_logined() {
      return this.$store.state.is_logined;
    },
  },
  methods: {
    islogin() {
      this.$store.commit("logins");
      this.$store.dispatch("movie_list_create");
    },
    search_movie() {
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/movies/search/${this.searchinput}/`,
      })
        .then((res) => {
          this.$store.commit("movie/SEARCH_INPUT", this.searchinput);
          this.$store.commit("movie/SEARCHRES", res.data);
        })
        .then(() => {
          this.searchinput = null;
          if (this.$route.path !== "/search/res") {
            this.$router.push({ name: "searchview" });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setLoading(isLoading) {
      console.log("thisisloading", isLoading);
      if (isLoading) {
        this.isLoading = true;
        console.log("inIf", isLoading);
      }
      if (!isLoading) {
        this.isLoading = false;
      }
    },
  },
  created() {
    this.islogin();
    axios.interceptors.request.use(
      (config) => {
        this.setLoading(false);
        return config;
      },
      (error) => {
        this.setLoading(false);
        console.log('here1');
        return Promise.reject(error);
      }
    ),
      axios.interceptors.response.use(
        (response) => {
          this.setLoading(true);
          return response;
        },
        (error) => {
          this.setLoading(false);
          console.log('here2');
          return Promise.reject(error);
        }
      );
  },
};
</script>

<style>
* {
  background-color: #121213;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: rgb(255, 255, 255);
  text-align: center;
}

nav {
  padding: 30px;
  /* margin-bottom: -2.5rem; */
}

nav a {
  font-family: "NeoBD";
  text-decoration: none;
  color: #e0e0e0;
}

nav a.router-link-exact-active {
  color: #ffdb3b;
}
nav a:hover {
  color: #ffdb3b;
}

.searchbar {
  border-radius: 30px;
  opacity: 50%;
  border: #e0e0e0;
}


@font-face {
  font-family: "NeoEB";
  src: url("../src/assets/fonts/NanumSquareNeoOTF-dEb.otf");
}
@font-face {
  font-family: "NeoBD";
  src: url("../src/assets/fonts/NanumSquareNeoOTF-cBd.otf");
}
@font-face {
  font-family: "NeoRG";
  src: url("../src/assets/fonts/NanumSquareNeoOTF-bRg.otf");
}
@font-face {
  font-family: "NeoLT";
  src: url("../src/assets/fonts/NanumSquareNeoOTF-aLt.otf");
}
@font-face {
  font-family: "PreB";
  src: url("../src/assets/fonts/Pretendard-Bold.otf");
}
@font-face {
  font-family: "PreM";
  src: url("../src/assets/fonts/Pretendard-Medium.otf");
}
@font-face {
  font-family: "PreR";
  src: url("../src/assets/fonts/Pretendard-Regular.otf");
}
@font-face {
  font-family: "PreS";
  src: url("../src/assets/fonts/Pretendard-SemiBold.otf");
}
@font-face {
  font-family: "PreL";
  src: url("../src/assets/fonts/Pretendard-Light.otf");
}
@font-face {
  font-family: "PreT";
  src: url("../src/assets/fonts/Pretendard-Thin.otf");
}

.dinone {
  display: none;
}
.container-disable {
  opacity: 0;
  pointer-events: none;
}
</style>
