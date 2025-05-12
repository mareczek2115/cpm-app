<script setup lang="ts">
import { store } from '../store';

console.log(store.nodes.value);
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
      <tr v-for="node in store.nodes.value">
        <td>{{ node.name }}</td>
        <td>{{ node.duration }}</td>
        <td>{{ node.early_start }}</td>
        <td>{{ node.early_finish }}</td>
        <td>{{ node.late_start }}</td>
        <td>{{ node.late_finish }}</td>
        <td>{{ node.reserve }}</td>
        <td>
          {{
            store.events.value
              .filter(e => node.predecessors.includes(e.id))
              .map(e => e.name)
              .join(', ')
          }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped lang="scss">
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
</style>
