<script setup lang="ts">
import NodesTable from './NodesTable.vue';
import Caption from './Caption.vue';
</script>

<template>
  <Caption />
  <div id="cpm-calculated">
    <NodesTable />
  </div>
</template>

<style scoped lang="scss">
#cpm-calculated {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-self: flex-start;
}
</style>
