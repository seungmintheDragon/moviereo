<template>
  <div>
    <table class="type10">
  <thead>
  <tr>
    <th scope="cols">타이틀</th>
    <th scope="cols">내용</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <th scope="row">항목명</th>
    <td>내용이 들어갑니다.</td>
  </tr>
  <tr>
    <th scope="row" class="even">항목명</th>
    <td class="even">내용이 들어갑니다.</td>
  </tr>
  <tr>
    <th scope="row">항목명</th>
    <td>내용이 들어갑니다.</td>
  </tr>
  </tbody>
</table>

    {{comment}}


  </div>
</template>

<script>
export default {
    nmae:'MovieCommentList',
    props:{
        comment:Object
    }
}
</script>

<style>

</style>