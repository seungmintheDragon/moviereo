<template>
  <div>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input
        type="text"
        id="username"
        v-model="username"
        class="text-light"
      /><br />

      <label for="password"> password : </label>
      <input
        type="password"
        id="password"
        v-model="password"
        class="text-light"
      /><br />

      <input type="submit" value="login" />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data: function () {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    login: function () {
      const username = this.username;
      const password = this.password;

      const payload = {
        username,
        password,
      };
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: payload,
      })
        .then((res) => {
          const jwt = res.data.access;
          window.localStorage.setItem("jwt", jwt);
          this.$emit("login");
          this.$router.push({ name: "home" });
        })
        .then(() => {
          this.$store.commit("logins");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/movies/nothing/",
    })
      .then(() => {
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
