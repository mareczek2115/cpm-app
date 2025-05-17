<script setup lang="ts">
import EventComponent from './Event.vue';
import Button from './Button.vue';

import axios from 'axios';
import type { Node } from '../types/types.ts';
import { store } from '../store.ts';
import { areEventsEqual, hasCycle } from '../utils.ts';

interface Response {
  nodes: Node[];
  image_url: string;
}

const { originalEvents, currentEvents } = store;

const emit = defineEmits(['showTable']);

const addNewEvent = () => {
  currentEvents.value.push({
    id: currentEvents.value[currentEvents.value.length - 1]?.id + 1 || 0,
    name: `Zdarzenie nr ${
      currentEvents.value[currentEvents.value.length - 1]?.id + 2 || 1
    }`,
    duration: 0,
    predecessors: [],
  });
};

const removeEvent = (id: number) => {
  const eventIndex = currentEvents.value.findIndex(event => event.id === id);

  currentEvents.value.splice(eventIndex, 1);

  currentEvents.value.forEach(e => {
    e.predecessors = e.predecessors.filter(p => p !== id);
  });
};

const fetchCriticalPath = async () => {
  try {
    currentEvents.value.forEach((e, i) => {
      e.id = i;
      e.duration = Number(e.duration);
    });

    if (currentEvents.value.some(e => Number.isNaN(e.duration)))
      throw new Error('Czas trwania musi być liczbą!');

    if (hasCycle(currentEvents.value))
      throw new Error('W grafie występuje cykl!');

    if (!areEventsEqual(currentEvents.value, originalEvents.value)) {
      const res = await axios.post<Response>(
        'http://localhost:8000/api/cpm',
        JSON.stringify(currentEvents.value),
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );

      store.nodes.value = res.data.nodes;
      store.graph_url.value = res.data.image_url;
      originalEvents.value = currentEvents.value.map(e => ({ ...e }));
    }

    emit('showTable');
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
      v-for="event in currentEvents"
      :key="event.id"
      :event="event"
      :allEvents="
        currentEvents
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
