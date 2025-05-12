<script setup lang="ts">
import EventComponent from './Event.vue';
import Button from './Button.vue';

import axios from 'axios';
import type { Node } from '../types/types.ts';
import { store } from '../store.ts';

const addNewEvent = () => {
  store.events.value.push({
    id: store.events.value.length,
    name: `Zdarzenie nr ${store.events.value.length + 1}`,
    duration: 0,
    predecessors: [],
  });
};

const removeEvent = (id: number) => {
  const eventIndex = store.events.value.findIndex(event => event.id === id);

  store.events.value.splice(eventIndex, 1);
};

const fetchCriticalPath = async () => {
  try {
    if (store.events.value.some(e => Number.isNaN(Number(e.duration))))
      throw new Error('Czas trwania musi być liczbą!');

    const res = await axios.post<Node[]>(
      'http://localhost:8000/api/cpm',
      JSON.stringify(store.events.value),
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );

    store.nodes.value = res.data;
  } catch (error) {
    if (error instanceof Error) alert(error.message);
  }
};
</script>

<template>
  <div id="list-container">
    <span id="top-tab">
      <h1>Lista zdarzeń</h1>
      <Button title="Dodaj nowy event" @onclick="addNewEvent" />
    </span>

    <div id="list-header">
      <div></div>
      <h3>Nazwa zdarzenia</h3>
      <h3>Czas trwania</h3>
      <h3>Poprzednicy</h3>
    </div>

    <EventComponent
      v-for="event in store.events.value"
      :key="event.id"
      :event="event"
      :allEvents="
        store.events.value
          .filter(e => e.id !== event.id)
          .map(e => {
            const { id, name } = e;
            return { id, name };
          })
      "
      @remove-event="removeEvent"
      class="list-row"
    />

    <Button title="Stwórz diagram CPM" @click="fetchCriticalPath" />
  </div>
</template>

<style scoped lang="scss">
#list-container {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  align-self: flex-start;
}
#top-tab {
  display: flex;
  height: fit-content;
  align-items: center;
  width: 100%;
  justify-content: space-around;
}
#list-header {
  width: 100%;
  display: grid;
  grid-template-columns: 70px 2fr 1fr 2fr;
  gap: 10px;
  align-items: center;
  padding: 12px 15px;
  > div:first-child {
    height: 100%;
  }
}
#list-header {
  background-color: #f5f5f5;
  border-bottom: 2px solid #ddd;
}
</style>
