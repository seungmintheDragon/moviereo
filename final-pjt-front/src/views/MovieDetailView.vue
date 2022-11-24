<template>
  <div>
    <div class="detail">
      <!-- 배경 포스터 -->
      <div>
        <img
          class="backdropimg"
          :src="`https://image.tmdb.org/t/p/original${movie_detail?.backdrop_path}`"
          alt=""
        />
      </div>

      <!-- movie 기본 정보 -->
      <div class="info">
        <!-- 포스터 -->
        <div style="background-color: transparent">
          <img
            class="poseterimg"
            v-if="movie_detail.poster_path"
            :src="`https://image.tmdb.org/t/p/original${movie_detail?.poster_path}`"
            alt=""
          />
          <img v-else src="../assets/null_image.jpg" class="d_profile_img" />
        </div>

        <!-- 이미지 외 텍스트 정보 -->
        <div class="info_text">
          <span class="detail_title"> {{ movie_detail?.title }} </span>
          <br />
          <!-- 연도 및 평점 -->
          <div class="date">
            {{ movie_detail?.release_date.substr(0, 4) }}
          </div>
          <div class="vote">
            ★ {{ movie_detail?.vote_average }}
            <span class="vote" style="font-size: 0.5rem; font-family: NeoLT">
              (TMDB)
            </span>
          </div>
          <!-- 장르 -->
          <div
            class="movie_genre"
            v-for="genre in movie_detail.genres"
            :key="genre.id"
            @click="search_genre(genre.id, genre.name)"
          >
            <button class="genre_btn">{{ genre.name }}</button>
          </div>
          <br />
          <br />
          <!-- 줄거리 -->
          <details v-if="movie_detail.overview">
            <summary style="font-family: PreR; font-size: 1rem">줄거리</summary>
            <div class="overview">
              {{ movie_detail?.overview }}
            </div>
          </details>
          <div v-else class="none_overview"></div>
          <hr style="margin-top: 5rem; width: 50rem" />

          <!-- 스태프-->
          <div class="staff">
            <!-- 감독  -->
            <div
              class="director"
              @click="
                search_director(
                  movie_detail.director[0].id,
                  movie_detail.director[0].name
                )
              "
              style="
                float: left;
                display: inline-block;
                background-color: transparent;
              "
            >
              <div class="staff_title">감독</div>
              <div class="d_profile">
                <div class="d_profile_box">
                  <img
                    v-if="movie_detail.director[0].profile_path"
                    class="d_profile_img"
                    :src="`https://image.tmdb.org/t/p/original${movie_detail.director[0]?.profile_path}`"
                    alt=""
                  />
                  <img
                    v-else
                    src="../assets/none-profile.png"
                    class="d_profile_img"
                  />
                </div>
                <div class="d_profile_name">
                  {{ movie_detail.director[0].name }}
                </div>
              </div>
            </div>
            <!-- 배우 -->
            <div
              class="actor"
              style="
                display: inline-block;
                float: left;
                background-color: transparent;
              "
            >
              <div class="staff_title">출연</div>
              <div
                v-for="actor in movie_detail.actor"
                :key="actor.id"
                class="profile"
                @click="search_actor(actor.id, actor.name)"
              >
                <div class="profile_box">
                  <img
                    v-if="actor?.profile_path"
                    class="profile_img"
                    :src="`https://image.tmdb.org/t/p/original${actor?.profile_path}`"
                    alt=""
                  />
                  <img
                    v-else
                    src="../assets/none-profile.png"
                    class="profile_img"
                  />
                </div>
                <div class="profile_name">
                  {{ actor?.name }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 사이드 바 -->
        <div class="sidebar">
          <!-- 영상보기 -->
          <div>
            <a
              href="#"
              title="Button border orange"
              class="button btnFloat_trailer btnOrange"
            ></a>
          </div>
          <!-- 댓글 보기 -->
          <div>
            <a
              href="#comments"
              title="Button border orange"
              class="button btnFloat_comment btnOrange"
            ></a>
            <!-- <button onclick="location.href='#comments'"> 댓글 보기 </button> -->
          </div>
          <!-- 댓글 작성 -->
          <!-- 코멘트 모달 테스트 -->
          <div style="background: transparent" >
            <button
              type="button"
              class="button btn_write"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              data-bs-whatever="@getbootstrap"
              v-if="islogin"
            >
              🖊️댓글 작성
            </button>
            <div
              class="modal fade"
              id="exampleModal"
              tabindex="-1"
              aria-labelledby="exampleModalLabel"
              aria-hidden="true"
              style="background-color: rgba(0, 0, 0, 0.3)"
            >
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1
                      class="modal-title fs-5"
                      id="exampleModalLabel"
                      style="font-family: NeoLT"
                    >
                      ✒️Movie Comments
                    </h1>
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                      style="background-color: white"
                    ></button>
                  </div>
                  <div class="modal-body">
                    <div
                      style="
                        font-family: NeoBD;
                        font-size: 2rem;
                        margin-bottom: 1rem;
                      "
                    >
                      {{ movie_detail?.title }}
                    </div>
                    <div class="mb-3">
                      <div
                        @mouseleave="showCurrentRating(0)"
                        style="display: inline-block"
                      >
                        <star-rating
                          :star-size="30"
                          :show-rating="false"
                          @current-rating="showCurrentRating"
                          @rating-selected="setCurrentSelectedRating"
                          :increment="0.5"
                        ></star-rating>
                      </div>
                      <span style="margin-left: 1rem; font-family: NeoLT">{{
                        currentRating
                      }}</span>
                      <div>
                        <label
                          for="recipient-name"
                          class="col-form-label"
                          style="font-family: NeoLT; color: lightgray"
                          >별점을 선택하세요</label
                        >
                        <br />
                      </div>
                    </div>
                    <hr />
                    <div class="mb-3">
                      <label for="message-text" class="col-form-label"></label>
                      <textarea
                        class="form-control"
                        id="message-text"
                        style="font-family: NeoRG"
                        placeholder="댓글을 작성해주세요!"
                        v-model="movie_comment"
                      ></textarea>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      data-bs-dismiss="modal"
                      style="font-family: NeoBD; border-radius: 1rem"
                    >
                      닫기
                    </button>
                    <button
                      class="btn btn-primary"
                      style="font-family: NeoBD; border-radius: 1rem"
                      @click="movieComment(movie_detail?.id)"
                      data-bs-dismiss="modal"
                    >
                      작성
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 컬렉션 버튼  -->
          <div style="background-color: transparent" v-if="islogin">
            <button @click="modal_click" class="btn_like">+</button>
            <div class="modal_like" id="modal_like">
              <!-- 헤더로 -->
              <div class="like_header" style="background-color: transparent">
                <div class="like_title">🛒 컬렉션에 담기</div>
                <!-- 닫기 버튼 -->
                <div style="background-color: transparent">
                  <button
                    @click="modal_click"
                    class="btn like_btn_close"
                    style="color: white"
                  >
                    X
                  </button>
                </div>
              </div>
              <!-- 컬렉션 체크 리스트로 -->
              <div
                id="checklist"
                style="margin: 1rem; background-color: transparent"
              >
                <movie-list-check
                  class="form-check"
                  v-for="movie_list in user_movie_list"
                  :key="movie_list.id"
                  :movie_list="movie_list"
                  :movie_id="movie_detail.id"
                  @add-list="addList"
                >
                </movie-list-check>
              </div>
              <!-- 새 컬렉션 만들기 -->
              <div style="background-color: transparent">
                <button @click="collection_click" class="btn_crate_collection">
                  새 컬렉션
                </button>
                <!-- 컬렉션 입력 받기 -->
                <div class="create_collection" id="create_collection">
                  <label class="create_collection_label">Collection Name</label
                  ><br />
                  <input
                    class="input_title"
                    @keyup.enter="likeMovieNew"
                    type="text"
                    v-model="collection_title"
                    placeholder="컬렉션 제목을 입력하세요."
                    style="color: white"
                  />
                  <div class="create_title_btn">
                    <span
                      @click="likeMovieNew"
                      style="
                        font-family: PreB;
                        font-size: 0.8vw;
                        background-color: transparent;
                        padding: 0.1rem;
                        margin: 0;
                      "
                    >
                      생성
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div></div>
      </div>
      <!-- 비슷한 영화 -->
      <div>
        <div class="similar_movie">
          <h3
            style="
              font-family: NeoBD;
              background-color: transparent;
              text-align: left;
            "
          >
            비슷한 영화
          </h3>
          <div
            class="row row-cols row-cols-md-3 g-3"
            style="margin-top:5px
                    background-color:transparent;width:14rem; height:21rem;"
          >
            <movie-similar-card
              v-for="similar_movie in movie_detail.relate_movie"
              :key="similar_movie.pk"
              :similar_movie="similar_movie"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- 재생목록 추가 예정 -->

    <!-- 댓글 확인란-->
    <div id="comments" class="comment_box">
      <hr />
      <p style="font-family: NeoBD; font-size: 1.5rem">영화 감상평</p>
      <hr />
      <div>
        <div v-for="comment in movie_detail.comment" :key="comment.id">
          <div class="comment_user">
            {{ comment.user.username }}
            <span
              ><star-rating
                :inline="true"
                :rating="comment.rate"
                :read-only="true"
                :increment="0.01"
                :star-size="10"
                :show-rating="false"
              ></star-rating
            ></span>
          </div>
          <span class="comment_content">
            {{ comment.comment }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StarRating from "vue-star-rating";
import MovieSimilarCard from "../components/MovieSimilarCard.vue";
import MovieListCheck from "../components/MovieListCheck.vue";

export default {
  name: "MovieDetailView",
  data() {
    return {
      movie_detail: null,
      movie_comment: null,
      currentRating: null,
      currentSelectedRating: null,
      rate: null,
      isclicked: false,
      collection_title: null,
      islogin: true,
    };
  },
  components: {
    StarRating,
    MovieSimilarCard,
    MovieListCheck,
  },
  computed: {
    user_movie_list() {
      return this.$store.state.user_movie_list;
    },
  },
  methods: {
    getMovieDetail(movie_pk) {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/movies/${movie_pk}/`,
      })
        .then((res) => {
          this.movie_detail = res.data;
        })
        .catch((err) => {
          console.log(err);
          window.open(`https://www.themoviedb.org/movie/${movie_pk}`);
          this.$router.push({ name: "home" });
        });
    },
    movieComment(movie_pk) {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/movies/${movie_pk}/comment/`,
        data: {
          comment: this.movie_comment,
          rate: this.rate,
        },
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
      })
        .then(() => {
          this.getMovieDetail(movie_pk);
          this.movie_comment = null;
          this.currentSelectedRating = null;
          this.rate = null;
          this.currentRating = null;
          this.scrollBehavior();
        })
        .catch((err) => {
          console.log(err);
        });
      // location.href = "#comments"
    },
    deleteComment(movie_pk) {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/movies/${movie_pk}/comment/`,
        data: {
          comment: this.movie_comment,
          rate: this.rate,
        },
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
      });
    },
    updateComment(movie_pk) {
      axios({
        method: "put",
        url: `http://127.0.0.1:8000/movies/${movie_pk}/comment/`,
        data: {
          comment: this.movie_comment,
          rate: this.rate,
        },
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
      });
    },
    // 모달 클릭 여부
    modal_click() {
      // 로그인 여부
      if (!this.islogin) {
        return alert('로그인 해주세요.')
      }
      // 토글 할 버튼 선택 (btn1)
      const modal_like = document.getElementById("modal_like");
      const create_collection = document.getElementById("create_collection");

      // 숨기기 (visibility: hidden)
      if (modal_like.style.visibility !== "visible") {
        modal_like.style.visibility = "visible";
      }
      // 보이기 (visibility: visible)
      else {
        modal_like.style.visibility = "hidden";
      }
      if(create_collection.style.visibility == "visible"){
        create_collection.style.visibility = "hidden";
      }
    },
    collection_click() {
      const create_collection = document.getElementById("create_collection");
      if (create_collection.style.visibility !== "visible") {
        create_collection.style.visibility = "visible";
      } else {
        create_collection.style.visibility = "hidden";
      }
    },
    //

    // 별점
    setRating: function (rating) {
      this.rating = rating;
    },
    showCurrentRating: function (rating) {
      this.currentRating = rating === 0 ? this.currentSelectedRating : rating;
    },
    setCurrentSelectedRating: function (rating) {
      this.currentSelectedRating = rating;
      this.rate = rating;
    },
    // 스크롤
    // 좋아요
    likeMovieNew() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/movies/likemovienew/",
        data: {
          title: this.collection_title,
        },
        headers: { Authorization: `Bearer ${localStorage.getItem("jwt")}` },
      })
        .then(() => {
          this.$store.commit("like_movie_list");
          this.collection_title = null;
          this.collection_click();
        })
        .catch((err) => console.log(err));
    },
    similar_detail(similar_movie_pk) {
      console.log(similar_movie_pk);
    },
    // 컬렉션 추가 메세지
    addList(addmsg) {
      if (!addmsg) {
        alert("컬렉션에 담겼습니다.");
      } else {
        alert("컬렉션에서 삭제되었습니다.");
      }
    },
    search_director(searchinput, name) {
      this.$store.commit("movie/SEARCH_INPUT", `감독 ${name}`);
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/movies/director/${searchinput}/`,
      })
        .then((res) => {
          console.log(res.data);
          this.$store.commit("movie/SEARCHRES", res.data);
        })
        .then(() => {
          this.$router.push({ name: "searchview" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    search_actor(searchinput, name) {
      this.$store.commit("movie/SEARCH_INPUT", `배우 ${name}`);
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/movies/actor/${searchinput}/`,
      })
        .then((res) => {
          console.log(res.data);
          this.$store.commit("movie/SEARCHRES", res.data);
        })
        .then(() => {
          this.$router.push({ name: "searchview" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    search_genre(id, name) {
      this.$store.commit("movie/SEARCH_INPUT", `장르 ${name}`);
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/movies/genre/${id}/`,
      })
        .then((res) => {
          console.log(res.data);
          this.$store.commit("movie/SEARCHRES", res.data);
        })
        .then(() => {
          this.$router.push({ name: "searchview" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  created() {
    this.getMovieDetail(this.$route.params.movie_pk);
    // 로그인 검사
    axios({
          method:'get',
          url:"http://127.0.0.1:8000/accounts/profile/",
          headers:{ 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
        })
        .then(()=>{
          this.islogin = true
        })
        .catch(()=>{
          this.islogin = false
        })
  },
};
</script>

<style>
.detail {
  position: relative;
  display: block;
}
.backdropimg {
  width: 100%;
  opacity: 0.2;
  mask-image: linear-gradient(to top, transparent 5%, black 100%);
}
.poseterimg {
  width: 300px;
  border-radius: 30px;
  background-color: transparent;
}
.info {
  position: absolute;
  display: flex;
  top: 2%;
  left: 10rem;
  margin: 5%;
  background-color: transparent;
}

/* 세부 디테일 */
.info_text {
  display: block;
  text-align: left;
  background-color: transparent;
  margin-left: 30px;
}
/* 영화제목 */
.detail_title {
  font-family: NeoBD;
  font-size: 4rem;
  width: auto;
  background-color: transparent;
}
/* 연도 및 평점 */
.date {
  float: left;
  font-family: NeoRG;
  font-size: 1rem;
  opacity: 0.7;
  background-color: transparent;
  margin-right: 2rem;
  margin-bottom: 0.3rem;
}
.vote {
  font-family: NeoRG;
  font-size: 1rem;
  color: rgb(255, 222, 38);
  opacity: 0.8;
  background-color: transparent;
  margin-bottom: 0.3rem;
}
/* 장르 */
.movie_genre {
  /* 블럭요소 가로정렬 */
  float: left;
  background-color: transparent;
  margin-top: 0.5rem;
  margin-bottom: 0.2rem;
}
.genre_btn {
  font-family: NeoBD;
  font-size: 1rem;
  border-radius: 15px;
  border: solid 0.15rem rgb(77, 77, 77);
  color: rgb(209, 209, 209);
  background-color: transparent;
  margin: 0.2rem;
  padding: 0.4rem;
}
.genre_btn:hover {
  font-family: NeoBD;
  font-size: 1rem;
  border-radius: 15px;
  border: solid 0.15rem rgb(77, 77, 77);
  color: white;
  background-color: rgb(77, 77, 77);
  margin: 0.2rem;
  padding: 0.4rem;
}
/* 줄거리 */
.overview {
  float: left;
  background-color: transparent;
  font-family: NeoLT;
  width: 50rem;
  /* -webkit-line-clamp: 3; */
  margin-bottom: 2rem;
  word-break: keep-all;
  line-height: 1.8rem;
}
.none-overview {
  width: 7rem;
  height: 10rem;
  border: solid 1px black;
}
.more {
  display: none;
  cursor: pointer;
  margin-top: 1rem;
}
/* 분류 */
.staff {
  display: block;
  background-color: transparent;
}
.staff_title {
  font-family: NeoBD;
  font-size: 1.2rem;
  background-color: transparent;
}
/* 감독 */
.d_profile {
  float: left;
  align-items: center;
  background-color: transparent;
  margin: 1rem;
}
.d_profile_box {
  width: 5.5rem;
  height: 5.5rem;
  border-radius: 70%;
  overflow: hidden;
}
.d_profile_img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.d_profile_name {
  font-family: "PreS";
  font-size: 1rem;
  color: rgb(223, 223, 223);
  text-align: center;
  width: 100px;
  word-break: keep-all;
  background-color: transparent;
  margin-top: 0.3rem;
  transform: translate(-10%, 0);
}

/* 배우 */
.profile {
  float: left;
  align-items: center;
  background-color: transparent;
  margin: 1rem;
}
.profile_box {
  width: 5.5rem;
  height: 5.5rem;
  border-radius: 70%;
  overflow: hidden;
}
.profile_img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.profile_name {
  font-family: "PreS";
  font-size: 1rem;
  color: rgb(223, 223, 223);
  text-align: center;
  width: 100px;
  word-break: keep-all;
  background-color: transparent;
  margin-top: 0.3rem;
  transform: translate(-10%, 0);
}
/* 코멘트 */
.comment_box {
  /* position: absolute; */
  margin-left: 5%;
  text-align: left;
}

.comment_user {
  font-family: PreR;
}

.comment_content {
  font-family: NeoLT;
}

/* 줄거리 */

details {
  margin-bottom: 1rem;
  background-color: transparent;
}

details > summary {
  background-color: transparent;
  padding: 1rem;
  cursor: pointer;
}

details > summary::-webkit-details-marker {
  color: transparent;
  transform: rotate3d(0, 0, 1, 90deg);
  transition: transform 0.25s;
  background-color: transparent;
}

details[open] > summary::-webkit-details-marker {
  transform: rotate3d(0, 0, 1, 180deg);
}

details[open] > summary {
  background-color: transparent;
}

details[open] > summary ~ * {
  animation: reveal 0.5s;
}

@keyframes reveal {
  from {
    opacity: 0;
    transform: translate3d(0, -10px, 0);
  }

  to {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
/* 비슷한 영화 */
.similar_movie {
  background-color: transparent;
  /* position: absolute; */
  top: 50rem;
  left: 10rem;
}
/* 사이드바 */
.sidebar {
  /* float: left; */
  background-color: transparent;
}

/* 버튼 */
a.button {
  display: block;
  position: relative;
  float: left;
  width: 120px;
  padding: 0;
  margin-left: 5rem;
  margin: 2rem;
  font-weight: 600;
  text-align: center;
  line-height: 50px;
  color: #fff;
  border-radius: 2rem;
  transition: all 0.2s;
}

.btnFloat {
  background: none;
  box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.5);
}
.btnFloat_comment:before {
  content: "🗨️ 댓글 보기";
  font-family: NeoLT;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 120px;
  height: 50px;
  border-radius: 2rem;
  transition: all 0.2s;
  background-color: #3b3b3b;
}
.btnFloat_trailer:before {
  content: "🎬 영상 보기";
  font-family: NeoLT;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 120px;
  height: 50px;
  border-radius: 2rem;
  transition: all 0.2s;
  /* border: 2px solid #585858; */
  background-color: #3b3b3b;
}

.btnOrange.btnFloat:before {
  background: transparent;
}

.btnFloat:before {
  box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.4);
}

.btnFloat_comment:hover:before {
  background-color: #226efc;
  color: #fff;
  margin-top: -2px;
  margin-left: 0px;
  transform: scale(1.1, 1.1);
  -ms-transform: scale(1.1, 1.1);
  -webkit-transform: scale(1.1, 1.1);
  box-shadow: 0px 5px 5px -2px rgba(0, 0, 0, 0.25);
}
.btnFloat_trailer:hover:before {
  background-color: #0142bb;
  color: #fff;
  margin-top: -2px;
  margin-left: 0px;
  transform: scale(1.1, 1.1);
  -ms-transform: scale(1.1, 1.1);
  -webkit-transform: scale(1.1, 1.1);
  box-shadow: 0px 5px 5px -2px rgba(0, 0, 0, 0.25);
}

.btn_write {
  width: 120px;
  height: 50px;
  border-radius: 2rem;
  background-color: #3b3b3b;
  margin-top: 2rem;
  border: none;
  color: #fff;
  font-family: NeoBD;
}

.btn_write:hover {
  background-color: #3d81ff;
  color: #fff;
  margin-left: 0px;
  transform: scale(0.1.1, 1.1);
  -webkit-transform: scale(1.1, 1.1);
  -ms-transform: scale(1.1, 1.1);
  box-shadow: 0px 5px 5px -2px rgba(0, 0, 0, 0.25);
  transition: all 0.2s;
}

/* 컬렉션에 추가하기 */
.btn_like {
  width: 120px;
  height: 50px;
  border-radius: 2rem;
  background-color: #fffdfd;
  margin-top: 1rem;
  border: none;
  color: rgb(36, 36, 36);
  font-family: NeoBD;
}
.btn_like:hover {
  background-color: #fffdfd;
  color: rgb(36, 36, 36);
  transform: scale(0.1.1, 1.1);
  -webkit-transform: scale(1.1, 1.1);
  -ms-transform: scale(1.1, 1.1);
  box-shadow: 0px 5px 5px -2px rgba(0, 0, 0, 0.25);
  transition: all 0.2s;
}

.modal_like {
  position: fixed;
  display: block;
  visibility: hidden;
  z-index: 200;
  top: auto;
  height: auto;
  right: 2%;
  bottom: 10%;
  background-color: #121213;
  border-radius: 10%;
  box-shadow: 3px 3px 10px rgba(5, 5, 5, 0.5);
}

/* 새로운 컬렉션 추가하기 */
.create_collection {
  display: block;
  visibility: hidden;
  margin-top: 1rem;
}
.like_header {
  background-color: transparent;
  display: flex;
  font-size: 20px;
  padding: 0.5rem;
}
.like_title {
  left: 0.7rem;
  font-family: PreR;
  font-size: 1.4vw;
  background-color: transparent;
  margin-left: 3vw;
}
.like_btn_close {
  background-color: rgb(110, 110, 110);
  font-family: NeoBD;
  border: none;
  border-radius: 2rem;
  margin-left: 1vw;
}
.btn_crate_collection {
  color: rgb(255, 255, 255);
  font-family: PreM;
  font-size: 1rem;
  border: none;
  border-radius: 8rem;
  width: 7rem;
  height: 2rem;
  background-color: #226efc;
}
.create_collection_label {
  font-family: NeoLT;
  font-size: 0.3vw;
  color: #6c6c6c;
  font-weight: bold;
  letter-spacing: 1px;
}
.create_title_btn {
  color: #226efc;
  text-align: right;
  margin-right: 2rem;
  margin-bottom: 1rem;
}
.create_title_btn:hover {
  color: white;
}
.input_title {
  background-color: transparent;
  border: none;
  border-bottom: 2px solid #226efc;
  border-top: 0px;
  border-radius: 0px;
  font-family: NeoLT;
  font-weight: bold;
  outline: 0;
  margin-bottom: 20px;
  padding-left: 0px;
  color: #ecf0f5;
}
::placeholder {
  font-size: 0.8vw;
  margin: auto;
}
</style>