<template>
  <div class="comment_table" style="background-color:transparent; font-family:NeoRG;">
    <table class="type09" style="background-color:transparent;margin:1rem;">
      <thead style="background-color:transparent;">
        <tr style="background-color:transparent;">
          <th scope="cols" style="background-color:transparent;">영화 제목</th>
          <th scope="cols" style="background-color:transparent;">내용</th>
        </tr>
      </thead>
        <tbody style="background-color:transparent;">
          <tr style="background-color:transparent;">
            <th scope="row" style="color:black;">{{comments.movie.title}}</th>
            <td style="background-color:transparent;color:black;">{{comments.comment}}

              <button @click="deleteComment(movie_pk)" class="btn btn-primary"
              style="float:right;"> 삭제 </button>
            </td>
          </tr>
        </tbody>
    </table>
    <div>

      
    </div>



  </div>
</template>

<script>
import axios from'axios'
export default {
    name:'MovieCommentList',
    data(){
      return{
        comment:null,
        rate:null,
      }
    },
    props:{
        comments:Object
    },
    methods:{
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
    }
}
</script>

<style>
.comment_table{
  top:53%;
}
table.type09 {
  border-collapse: collapse;
  text-align: left;
  line-height: 1.5;

}
table.type09 thead th {
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  color: #369;
  border-bottom: 3px solid #036;
}
table.type09 tbody th {
  width: 150px;
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
  background: #f3f6f7;
}
table.type09 td {
  width: 350px;
  padding: 10px;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
}
</style>