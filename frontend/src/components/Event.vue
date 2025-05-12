<script setup lang="ts">
import CloseCircle from 'vue-material-design-icons/CloseCircle.vue';
import Multiselect from './Multiselect.vue';
import type { Event, BaseEvent } from '../types/types';

const emit = defineEmits<{
  (e: 'remove-event', id: number): void;
}>();

defineProps<{
  event: Event;
  allEvents: BaseEvent[];
}>();
</script>
<template>
  <div class="event-entry">
    <CloseCircle
      class="close-circle"
      :size="30"
      @click="emit('remove-event', event.id)"
    />
    <input type="text" v-model="event.name" />
    <input type="text" v-model="event.duration" />
    <Multiselect :event="event" :allEvents="allEvents" />
  </div>
</template>
<style scoped>
.event-entry {
  display: grid;
  grid-template-columns: 50px 2fr 1fr 2fr;
  gap: 10px;
  align-items: center;
  padding: 12px 15px;
}
.close-circle {
  cursor: pointer;
  transition: opacity 0.2s;
}
.close-circle:hover {
  opacity: 0.6;
}
input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}
</style>
