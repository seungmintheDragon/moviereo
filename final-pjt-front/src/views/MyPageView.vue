<template>
  <div class="mypage_wrap">
    <div class="mypage">
      <div class="profile_area">
        <!-- 이미지 -->
        <div class="user_profile_box">
          <img class="user_profile_img" src="../assets/default_source/cat.jpg" alt="profile">
        </div>
        <div class="user_name"> {{user_data.username}} 님 </div>
        <br>
        <!-- 선택 -->
        <button class="btn btn-success"> 내가 쓴 댓글 </button> <br>
        <button class="btn btn-primary"> 영화 컬렉션 </button>
      </div>

      <div class="mycontent">
        <MovieCollection
        v-for="movie_list in userMovieList"
        :key="movie_list.id"
        :movie_list=movie_list
        />

        <div
        v-for="comment in commentLists"
        :key="comment.id"
        >
        {{comment.movie}}
        {{comment.comment}}
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCollection from '@/components/MovieCollection.vue'

export default {
    name:'MyPageView',
    data(){
      return{
        user_data:null,
        commentLists:null,
      }
    },
    computed:{
      userMovieList(){
            return this.$store.state.user_movie_list;
        }
    },
    components:{
      MovieCollection
    },
    methods:{
      commentList(){
        axios({
          method:'get',
          url:"http://127.0.0.1:8000/movies/comment/",
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
        })
        .then((res)=>{
          console.log(res)
          this.commentLists = res.data
        })
        .catch((err)=>{
          console.log('commenterror');
          console.log(err)
        })
      },
      userProfile(){
        axios({
          method:'get',
          url:"http://127.0.0.1:8000/accounts/profile/",
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
        })
        .then((res)=>{
          this.user_data = res.data
        })
        .catch(()=>{
          this.$router.push({name:'login'})
        })
      }
    },
    created(){
      this.userProfile()
      this.commentList()
    }
}
</script>

<style>
.mypage{
  display: block;
}
/* 프로필 */
.profile_area{
  float:left;
  width:20%;
  height: auto;
  margin-left:2rem;
  border: solid 0.1rem white;
  border-radius: 2rem;
}

/* 유저 */

.user_profile_box{
  width:13rem;
  height: 13rem;
  border-radius: 70%;
  overflow: hidden;
  margin:auto;
  margin-top: 1rem;
}
.user_profile_img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.user_name{
  font-family: PreS;
  font-size: 1.5rem;
  margin-top:0.5rem;
}

/* 콘텐츠 */

.mycontent{
  float:right;
  width:65%;
  border: solid 0.1rem white;

}

/* 배경 */
.mypage_wrap{
  background-image: url('../assets/profile_back.jpg');
}
</style>