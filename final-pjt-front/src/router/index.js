import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RecommandView from '../views/RecommandView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogoutView from '@/views/LogoutView'
import MovieDetailView from '@/views/MovieDetailView'
import MyPageView from '@/views/MyPageView'
import recommand_index from '@/router/recommand_index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/recommand',
    name: 'recommand',
    component: RecommandView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/moviedetail/:movie_pk',
    name: 'moviedetail',
    component: MovieDetailView
  },
  ...recommand_index,
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
