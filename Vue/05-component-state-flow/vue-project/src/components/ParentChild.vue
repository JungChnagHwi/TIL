<template>
  <div>
    <p>{{ myMsg }}</p>
    <ParentGrandChild :my-msg="myMsg"/>
    <p>{{ dynamicProps }}</p>

    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
    
  </div>
</template>

<script setup>
// const props= defineProps({
//   myMsg: String
// })
// console.log(props)
// console.log(props.myMsg)

import ParentGrandChild from './ParentGrandChild.vue';
defineProps({
  myMsg: String,
  dynamicProps: String,
})


const emit = defineEmits(['someEvent', 'emitArgs',])
const buttonClick = function () {
  emit('someEvent')
}

const emitArgs =function (){
  emit('emitArgs',1,2,3)
}


</script>

<style scoped>

</style>