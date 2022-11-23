import RecoMainView from '@/views/reco_vue/RecoMainView'
import ResultRecoView from '@/views/reco_vue/ResultRecoView'
import SearchView from '@/views/SearchView'


export default [
    {
      path: '/recomain',
      name: 'recomaintview',
      component: RecoMainView
    },
    {
      path: '/recores',
      name: 'resultrecoview',
      component: ResultRecoView
    },
    {
      path:'/search/res',
      name: 'searchview',
      component: SearchView,
    },
]