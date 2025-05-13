<template>
  <div id="caption">
    <div id="box">
      <div class="small-box">ES</div>
      <div class="small-box">T</div>
      <div class="small-box">EF</div>
      <div class="name-box">Nazwa</div>
      <div class="small-box">LS</div>
      <div class="small-box">R</div>
      <div class="small-box">LF</div>
    </div>
    <span>T - Czas trwania</span>
    <span>ES - Early Start</span>
    <span>EF - Early Finish</span>
    <span>LS - Late Start</span>
    <span>LF - Late Finish</span>
    <span>R - Rezerwa</span>
  </div>
</template>

<style scoped lang="scss">
#caption {
  position: absolute;
  top: 50px;
  right: 50px;
  display: flex;
  flex-direction: column;
  > span:first-of-type {
    margin-top: 20px;
  }
  span {
    width: 70%;
    align-self: center;
    margin: 2px 0;
  }
}
#box {
  width: 185px;
  height: 120px;
  border: solid 1px black;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  :nth-child(2),
  :nth-child(6) {
    border-left: solid 1px black;
    border-right: solid 1px black;
  }
}
.small-box {
  width: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.name-box {
  width: 185px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: solid 1px black;
  border-bottom: solid 1px black;
}
</style>
