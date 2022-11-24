<template>
<div>
<link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css">
<main class="profile-page">
  <section class="relative block h-500-px">
    <div class="absolute top-0 w-full h-full bg-center bg-cover" style="
            background-image: url('https://images.unsplash.com/photo-1485846234645-a62644f84728?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1159&q=80');
            mask-image: linear-gradient(to top, transparent 5%, black 30%);

            ">
      <span id="blackOverlay" class="w-full h-full absolute opacity-50 bg-black" style="left:0;"></span>
    </div>

  </section>

  <section class="relative py-16 "  >
    <div class="container mx-auto px-4" style="border-radius: 1rem;background-color:transparent;" >
      <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64"  style="background-color:transparent" >
        <div class="px-6"  style="background-color:transparent;border:none;" >
          <div class="flex flex-wrap justify-center"  style="background-color:transparent" >
            <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center"  style="background-color:transparent;border:none;" >
              <div class="relative "  style="background-color:transparent;border:none;">
                <img alt="..." src="../assets/default_source/profile_cat.png" class="shadow-xl rounded-full h-auto align-middle border-whi absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" 
                style="border:none;">
              </div>
            </div>

            <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center" style="background-color:transparent">
              <div class="py-6 px-3 mt-32 sm:mt-0"  style="background-color:transparent" >
                <button 
                @click="contents_click"
                class="btn btn-primary m-2" type="button" style="font-family:NeoLT;background-color: dodgerblue;border:none;">
                  내 댓글
                </button>
                <button 
                @click="collections_click"
                class="btn btn-primary" type="button" style="font-family:NeoLT;background-color:steelblue;border:none;">
                  내 컬렉션
                </button>
              </div>
            </div>
            <div class="w-full lg:w-4/12 px-4 lg:order-1" style="background-color:transparent">
              <div class="text-center mt-12" style="background-color:transparent">
                <p class="user_name" style="background-color:transparent;font-family: PreB;color:darkslategrey">
                  {{user_data.username}}'s Profile
                </p>
              </div>
              <div class="flex justify-center py-4 lg:pt-4 pt-8" style="background-color:transparent">
                <div class="mr-4 p-3 text-center" style="background-color:transparent">
                  <span class="text-xl  block uppercase tracking-wide text-blueGray-600" style="background-color:transparent">{{commentListsLength}}</span><span class="text-sm text-blueGray-400" style="font-family:PreM;background-color:transparent;">댓글</span>
                </div>
                <div class="mr-4 p-3 text-center" style="background-color:transparent">
                  <span class="text-xl block uppercase tracking-wide text-blueGray-600" style="background-color:transparent" >{{userMovieListLength}}</span><span class="text-sm text-blueGray-400" style="font-family:PreM;background-color:transparent;">컬렉션</span>
                </div>
              </div>
            </div>
          </div>

          <div
          class="create_collections" id="create_collections"
          style="background-color:transparent">
          <MovieCollection
          v-for="movie_list in userMovieList"
          :key="movie_list.id"
          :movie_list=movie_list
          style="background-color:transparent;"
          />
          </div>

          
          <div class="mycontent" id="mycontent" style="position: absolute;background-color:transparent;">
            <movie-comment-list
            v-for="comments in commentLists"
            :key="comments.id"
            :comments=comments
            
            />
          </div>

        </div>
      </div>
    </div>
  </section>
</main>
</div>
    <!-- <div class="mypage_wrap">
      <div class="mypage">
        <div class="profile_area">
          <div class="user_profile_box">
            <img class="user_profile_img" src="../assets/default_source/cat.jpg" alt="profile">
          </div>
          <div class="user_name"> {{user_data.username}} 님 </div>
          <br>
          <button class="btn btn-success"> 내가 쓴 댓글 </button> <br>
          <button class="btn btn-primary"> 영화 컬렉션 </button>
        </div>

        <div class="mycontent">
          <div
          v-for="comment in commentLists"
          :key="comment.id"
          >
          {{comment.movie}}
          {{comment.comment}}
          </div>
        </div>

      </div>
    </div> -->
</template>

<script>
import axios from 'axios'
import MovieCollection from '@/components/MovieCollection.vue'
import MovieCommentList from '../components/MovieCommentList.vue'

export default {
    name:'MyPageView',
    data(){
      return{
        user_data:null,
        commentLists:null,
        commentListsLength:null,
      }
    },
    computed:{
      userMovieList(){
            return this.$store.state.user_movie_list;
      },
      userMovieListLength() {
        return this.$store.state.user_movie_list.length
      },
    },
    components:{
      MovieCollection,
      MovieCommentList,
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
          this.commentListsLength = res.data.length
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
      },
      collections_click() {
        const create_collections = document.getElementById("create_collections");
        const mycontent = document.getElementById("mycontent");

        if (create_collections.style.visibility !== "visible") {
          create_collections.style.visibility = "visible";
        } 
        else {
          create_collections.style.visibility = "hidden";
        }
          if(mycontent.style.visibility != "hidden"){
            mycontent.style.visibility = "hidden";
          }
      },
      contents_click() {
        const mycontent = document.getElementById("mycontent");
        const create_collections = document.getElementById("create_collections");

        if(create_collections.style.visibility != "hidden"){
        create_collections.style.visibility = "hidden";

        }
        if (mycontent.style.visibility !== "visible") {
          mycontent.style.visibility = "visible";
        } 
        else {
          mycontent.style.visibility = "hidden";
        }
      },
      
    },
    // 컬렉션 클릭
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
}

/* 콘텐츠 */

.mycontent{
  top:30%;
  left:30%;
  width:65%;
  border: solid 0.1rem white;
  visibility: hidden;


}

/* 배경 */
.mypage_wrap{
  background-image: url('../assets/profile_back.jpg');
}

.create_collections{
  visibility: visible;
}
</style>