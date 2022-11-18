<template>
    <div v-if="!success" class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
    </div>
</template>

<script>
export default {
    name: 'LogoutView',
    computed: {
        is_login() {
            return this.$store.state.is_logined
        },
    },
    methods: {
        logout() {
            if (this.is_login) {
                this.$store.commit('logout')
                this,this.$router.push({name:'home'})
            } else {
                this.$router.push({name:'login'})
            }
        },
    },
    created() {
        this.logout()
    },
}
</script>

<style>

</style>