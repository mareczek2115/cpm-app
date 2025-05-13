<script setup lang="ts">
import { store } from '../store';

const { value: currentEvents } = store.currentEvents;
const { value: nodes } = store.nodes;

const highlightNode = (id: number) => {
  const node = Array.from(
    document.querySelectorAll<HTMLElement>('.node-details')
  ).find(n => Number(n.dataset.nodeId) === id);

  node!.classList.add('predecessor-clicked');

  setTimeout(() => {
    node!.classList.remove('predecessor-clicked');
  }, 400);
};
</script>

<template>
  <table id="cpm-nodes">
    <thead>
      <tr>
        <th>Nazwa zdarzenia</th>
        <th>Czas trwania</th>
        <th>ES</th>
        <th>EF</th>
        <th>LS</th>
        <th>LF</th>
        <th>Rezerwa</th>
        <th>Poprzednicy</th>
      </tr>
    </thead>
    <tbody>
      <tr
        class="node-details"
        v-for="node in nodes"
        :key="node.id"
        :data-node-id="node.id"
      >
        <td>{{ node.name }}</td>
        <td>{{ node.duration }}</td>
        <td>{{ node.early_start }}</td>
        <td>{{ node.early_finish }}</td>
        <td>{{ node.late_start }}</td>
        <td>{{ node.late_finish }}</td>
        <td>{{ node.reserve }}</td>
        <td>
          <span
            v-if="node.predecessors.length > 0"
            class="predecessor"
            v-for="event in currentEvents.filter(e =>
              node.predecessors.includes(e.id)
            )"
            :key="event.id"
            @click="() => highlightNode(event.id)"
          >
            {{ event.name }}</span
          >
          <span v-if="node.predecessors.length === 0">-</span>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped lang="scss">
#cpm-nodes {
  margin-top: 50px;
}
table {
  border-collapse: collapse;
}
th,
td {
  border: solid 1.5px black;
  padding: 10px;
}
td {
  text-align: center;
}
.predecessor {
  display: block;
  cursor: pointer;
  border-bottom: solid 1px #bbb;
  transition: background-color 1s linear;
}
.predecessor:last-child {
  border-bottom: none;
}

.predecessor-clicked {
  animation: highlight 0.4s linear;
}

@keyframes highlight {
  0% {
    background-color: #39f;
  }
  50% {
    background-color: #39f;
  }
  100% {
    background-color: #fff;
  }
}
</style>
