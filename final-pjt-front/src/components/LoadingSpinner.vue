<!-- Spinner.vue -->
<template>
    <div>
        <div class="lds-facebook" v-if="loading" style="background-color: transparent">
            <div style="font-family:NeoBD;">
                로
            </div>
            <div style="font-family:NeoBD;">
                딩
            </div>
            <div style="font-family:NeoBD;">
                중
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'LoadingSpinner',
    props: {
        loading: {
            type: Boolean,
            required: true
        }
    }
}
</script>
<style>
.lds-facebook {
    display: inline-block;
    position: absolute;
    width: 120px;
    height: 120px;
    top: 47%;
    left: 47%
}
.lds-facebook div {
    display: inline-block;
    position: absolute;
    left: 10px;
    width: 20px;
    background: #4d7cff;
    animation: lds-facebook 1.2s cubic-bezier(0, 0.5, 0.5, 1) infinite;
}
.lds-facebook div:nth-child(1) {
    left: 10px;
    animation-delay: -0.24s;
}
.lds-facebook div:nth-child(2) {
    left: 40px;
    animation-delay: -0.12s;
}
.lds-facebook div:nth-child(3) {
    left: 70px;
    animation-delay: 0;
}
@keyframes lds-facebook {
    0% {
        top: 6px;
        height: 51px;
    }
    50%, 100% {
        top: 19px;
        height: 25px;
    }
}
</style>