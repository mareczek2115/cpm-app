<script setup lang="ts">
import NodesTable from './NodesTable.vue';
import Caption from './Caption.vue';
import { store } from '../store';
</script>

<template>
  <Caption />
  <div id="cpm-calculated">
    <NodesTable />
    <img
      id="graph"
      v-if="store.graph_url.value"
      :src="store.graph_url.value"
      alt="CPM Graph"
    />
  </div>
</template>

<style scoped lang="scss">
#cpm-calculated {
  display: flex;
  flex-direction: column;
  align-items: center;
  align-self: flex-start;
}
#graph {
  max-width: calc(20%);
}
</style>
