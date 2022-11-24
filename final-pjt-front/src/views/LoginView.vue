<template>
  <div>
    <div class="signup_back">
      <div class="main" style="background-color: rgba(0, 0, 0, 0.7)">
        <div class="signup" style="background-color: transparent">
          <form
            @submit.prevent="login"
            style="background-color: transparent"
          >
            <label class="label_sign" style="background-color: transparent"
              >Login</label
            >
            <input
              class="input_sign"
              type="text"
              name="txt"
              placeholder="User name"
              required=""
              v-model="username"
            />
            <input
              class="input_sign"
              type="password"
              name="pswd"
              placeholder="비밀번호"
              required=""
              v-model="password"
            />

            <button type="submit" class="button_sign">Login</button>
            <p v-if="err_msg" class="err_msg vibration">
              {{ err_msg }}
            </p>
          </form>
        </div>
      </div>
    </div>
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
      err_msg: null,
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
        .catch(() => {
          this.err_msg = '로그인 오류!'
          axios({
            method: "get",
            url: "http://127.0.0.1:8000/movies/nothing/",
          })
            .then(() => {
            })
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

<style>
/* 테스트 */
#form {
  background-color: transparent;
}
.signup_back {
  background-image: url('https://images.unsplash.com/photo-1509822929063-6b6cfc9b42f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80');
  background-size: cover;
  width: 100%;
  height: 900px;
}
.main {
  position: fixed;
  width: 350px;
  height: 500px;
  overflow: hidden;
  border-radius: 5rem;
  box-shadow: 1rem 4rem 8rem #000;
  left: 40%;
  margin-top: 2rem;
}

.label_sign {
  font-family: PreM;
  color: #fff;
  font-size: 2rem;
  justify-content: center;
  display: flex;
  margin: 60px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.5s ease-in-out;
}
.input_sign {
  width: 60%;
  height: 2rem;
  background: #e0dede;
  justify-content: center;
  display: flex;
  margin: 20px auto;
  padding: 10px;
  border: none;
  outline: none;
  border-radius: 0.5rem;
  font-family: NeoBD;
}
.button_sign {
  font-family: PreT;
  width: 60%;
  height: 40px;
  margin: 10px auto;
  justify-content: center;
  display: block;
  color: #fff;
  background: #0142bb;
  font-size: 1em;
  font-weight: bold;
  margin-top: 20px;
  outline: none;
  border: none;
  border-radius: 5px;
  transition: 0.2s ease-in;
  cursor: pointer;
  background-color: transparent;
}
.button_sign:hover {
  background: #226efc;
}

.err_msg {
  width: auto;
  height: auto;
  background-color: transparent;
  font-family: NeoBD;
  color: #ff5f5f;
  margin-top: 1rem;
}
.err_msg.vibration {
  animation: vibration 0.1s;
  animation-iteration-count: 3;
}

@keyframes vibration {
  from {
    transform: rotate(1deg);
  }
  to {
    transform: rotate(-1deg);
  }
}
</style>