<script setup lang="ts">
import { ref, watch } from 'vue';
import type { BaseEvent, Event } from '../types/types.ts';
import { store } from '../store.ts';
const { event, allEvents } = defineProps<{
  event: Event;
  allEvents: BaseEvent[];
}>();

const dropdownVisible = ref(false);
const selected = ref<number[]>([]);

function toggleDropdown() {
  if (store.openedMultiselectId.value === event.id) {
    store.openedMultiselectId.value = null;
  } else {
    store.openedMultiselectId.value = event.id;
  }
}

const handleClickOutside = (e: MouseEvent) => {
  const target = e.target as HTMLElement;
  if (!target.closest('.custom-multiselect')) {
    dropdownVisible.value = false;
    store.openedMultiselectId.value = null;
  }
};

watch(
  () => store.openedMultiselectId.value,
  val => {
    dropdownVisible.value = val === event.id;
  }
);

watch(dropdownVisible, val => {
  if (val) document.addEventListener('click', handleClickOutside);
  else document.removeEventListener('click', handleClickOutside);
});

function updateSelected(id: number) {
  const index = selected.value.indexOf(id);

  if (index !== -1) {
    selected.value.splice(index, 1);
  } else {
    selected.value.push(id);
  }

  event.predecessors.splice(0, event.predecessors.length, ...selected.value);
}
</script>

<template>
  <div class="custom-multiselect">
    <div class="selected" @click="toggleDropdown">Wybierz opcje ▼</div>
    <div class="dropdown" v-show="dropdownVisible">
      <label v-for="base in allEvents" :key="base.id">
        <input
          type="checkbox"
          :checked="event.predecessors.includes(base.id)"
          :value="base.id"
          :id="base.id.toString()"
          @change="() => updateSelected(base.id)"
        />
        {{ base.name }}
      </label>
    </div>
  </div>
</template>

<style>
.custom-multiselect {
  position: relative;
  width: 260px;
}

.selected {
  border: 1px solid #ccc;
  padding: 10px;
  cursor: pointer;
  background: white;
}

.dropdown {
  display: block;
  position: absolute;
  width: 100%;
  border: 1px solid #ccc;
  background: white;
  max-height: 200px;
  overflow-y: auto;
  z-index: 1;
}

.dropdown label {
  display: block;
  padding: 8px;
}

.dropdown label:hover {
  background: #f0f0f0;
}

.selected-items {
  margin-top: 5px;
  font-size: 0.9em;
  color: #666;
}
</style>
