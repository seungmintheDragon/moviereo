<template>
  <div>
    <div class="signup_back">
      
        <div class="main" style="background-color: rgba(0, 0, 0, 0.7);">
            <div class="signup" style="background-color:transparent;" >
              <form @submit.prevent="signup()" style="background-color:transparent;">
                <label class="label_sign" style="background-color:transparent;" >Sign up</label>
                <input class="input_sign" type="text" name="txt" placeholder="User name" required="" v-model="username">
                <input class="input_sign" type="password" name="pswd"  placeholder="비밀번호" required="" v-model="password1" >
                <input class="input_sign" type="password" name="pswd" placeholder="비밀번호 확인" required="" v-model="password2">
                <button type="submit" class="button_sign">Sign up</button>
                <p v-if="err_msg"
                class="err_msg"
                >
                {{err_msg}}</p>
              </form>
            </div>
        </div>
    
    </div>
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
      err_msg:null,
    };
  },
  methods: {
    signup: function () {
      const username = this.username;
      const password = this.password1;
      const password2 = this.password2;

      if(this.password1 != this.password2){
            return alert('비밀번호가 다릅니다!')
          }
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
          console.log(error.response.data)
          if(error.response.data.username[0] === "A user with that username already exists."){
            this.err_msg = "⚠️이미 등록된 사용자 이름입니다."
          }
        });
    },
  },
};
</script>

<style>


/* 테스트 */
#form
{
background-color: transparent;
}
.signup_back{
  background-image: url(../assets/movie_back.jpg);
  background-size: cover;
  width: 100%;
  height: 900px;

}
.main{
	position: fixed;
	width: 350px;
	height: 500px;
	overflow: hidden;
	border-radius: 5rem;
	box-shadow: 1rem 4rem 8rem #000;
  left: 40%;
  margin-top:2rem;
}

.label_sign{
  font-family:PreM;
	color: #fff;
	font-size: 2rem;
	justify-content: center;
	display: flex;
	margin: 60px;
	font-weight: bold;
	cursor: pointer;
	transition: .5s ease-in-out;
}
.input_sign{
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
  font-family:NeoBD;

}
.button_sign{
  font-family:PreT;
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
	transition: .2s ease-in;
	cursor: pointer;
  background-color: transparent;
}
.button_sign:hover{
	background: #226efc;
}

.err_msg{
  width: auto;
  height: auto;
  background-color:transparent;
  font-family:NeoBD;
  color: #FF5F5F; margin-top:1rem;
}
.err_msg.vibration {
  animation: vibration .1s infinite;
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
