<template>
<div class="recommand">
  <!-- 로그인이 되어있으면 뜨고, 안되어 있으면 로그인 페이지로 이동한다 -->
  <!-- 로그인 시 유저에 맞는 추천 페이지 -->
  <router-link :to="{ name:'recomaintview'}">추천 받으시겟어요?</router-link>
  <div>
    <router-view />
  </div>
</div>
  
</template>

<script>
export default {
  data() {
    return {
      genre: {
        '모험': 12,
        '판타지': 14,
        '애니메이션':16,
        '드라마': 18,
        '공포': 27,
        '액션':28,
        '코미디': 35,
        '역사': 36,
        '서부':37,
        '스릴러':53,
        '범죄': 80,
        '다큐멘터리': 99,
        'SF' : 878,
        '미스테리':9648,
        '음악':10402,
        '로맨스':10749,
        '가족':10751,
        '전쟁':10752,
        'TV 영화': 10770,
      },
    }
  },
  computed: {
    search_list() {
      return this.$store.state.searchmovie
    }
    
  },
  methods: {

  }

}
</script>

<style>

</style>
