<template>
  <div>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input
        type="text"
        id="username"
        v-model="username"
        class="text-light"
      /><br />

      <label for="password1"> password : </label>
      <input
        type="password"
        id="password1"
        v-model="password1"
        class="text-light"
      /><br />

      <label for="password2"> password confirmation : </label>
      <input
        type="password"
        id="password2"
        v-model="password2"
        class="text-light"
      />
      <input type="submit" value="SignUp" />
    </form>

    <!-- 사인업 -->
    <hr>
    <br>
    <!-- Signup Form -->
    <div class="signup form-peice">
        <form class="signup-form" action="#" method="post">

          <div class="form-group">
              <label for="name">Full Name</label>
              <input type="text" name="username" id="name" class="name">
              <span class="error"></span>
          </div>

          <div class="form-group">
              <label for="email">Email Adderss</label>
              <input type="email" name="emailAdress" id="email" class="email">
              <span class="error"></span>
          </div>

          <div class="form-group">
              <label for="phone">Phone Number - <small>Optional</small></label>
              <input type="text" name="phone" id="phone">
          </div>

          <div class="form-group">
              <label for="password">Password</label>
              <input type="password" name="password" id="password" class="pass">
              <span class="error"></span>
          </div>

          <div class="form-group">
              <label for="passwordCon">Confirm Password</label>
              <input type="password" name="passwordCon" id="passwordCon" class="passConfirm">
              <span class="error"></span>
          </div>

          <div class="CTA">
              <input type="submit" value="Signup Now" id="submit">
              <a href="#" class="switch">I have an account</a>
          </div>
        </form>
    </div><!-- End Signup Form -->




  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUpView",
  data: function () {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signup: function () {
      const username = this.username;
      const password = this.password1;
      const password2 = this.password2;

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: {
          username,
          password,
          password2,
        },
      })
        .then(() => {
          this.$router.push({ name: "home" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
