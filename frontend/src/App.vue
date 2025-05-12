<script setup lang="ts">
import { ref } from 'vue';
import EventsList from './components/EventsList.vue';
import NodesTable from './components/NodesTable.vue';

import { store } from './store';

type ViewTarget = 'Table' | 'Events';

const showNodesTable = ref<boolean>(false);

function switchViews(target: ViewTarget) {
  showNodesTable.value = target === 'Table';
}
</script>

<template>
  <div id="app-lower">
    <div
      v-if="store.nodes.value.length > 0 && !showNodesTable"
      class="arrow-right"
      @click="() => switchViews('Table')"
    >
      ➡️
    </div>
    <div
      v-if="showNodesTable"
      class="arrow-left"
      @click="() => switchViews('Events')"
    >
      ⬅️
    </div>

    <EventsList v-if="!showNodesTable" />
    <NodesTable v-if="showNodesTable" />
  </div>
</template>

<style scoped>
#app-lower {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.arrow-left,
.arrow-right {
  position: fixed;
  top: 10px;
  font-size: 24px;
  cursor: pointer;
}

.arrow-left {
  left: 10px;
}
.arrow-right {
  right: 10px;
}
</style>
