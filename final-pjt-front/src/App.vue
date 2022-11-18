<template>
  <div id="app">
    <nav>
      <router-link to="/">메인</router-link> |
      <router-link to="/recommand">영화 추천</router-link> |
      <router-link to="/about">마이페이지</router-link> |
      <input class="searchbar" type="text" placeholder="search bar" /> |
      <span :class="{ dinone: is_logined }">
        <router-link to="/login">로그인</router-link> |
        <router-link to="/signup">회원 가입</router-link>
      </span>
      <span :class="{ dinone: !is_logined }">
        <router-link to="/logout">로그아웃</router-link> |
        내정보
      </span>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "app",
  computed: {
    is_logined() {
      return this.$store.state.is_logined;
    },
  },
  methods: {
    islogin() {
      console.log("here");
      this.$store.commit("logins");
    },
  },
  created() {
    this.islogin();
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
}

nav a {
  font-family: "NeoBD";
  text-decoration: none;
  color: #e0e0e0;
}

nav a.router-link-exact-active {
  color: #ffdb3b;
}

.searchbar {
  border-radius: 30px;
  opacity: 50%;
  border: #e0e0e0;
}

@font-face {
  font-family: "NeoHV";
  src: url("../src/assets/fonts/NanumSquareNeoOTF-eHv.otf");
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

.dinone {
  display: none;
}
</style>
