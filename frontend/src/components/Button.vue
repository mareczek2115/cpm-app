<script setup lang="ts">
const emit = defineEmits<{
  (e: 'onclick'): void;
}>();

defineProps<{
  title: string;
}>();
</script>
<template>
  <button class="button" @click="emit('onclick')">{{ title }}</button>
</template>
<style scoped>
.button {
  display: inline-block;
  padding: 12px 24px;
  font-family: 'Inter', 'Arial', sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(135deg, #6e8efb, #4a6cf7);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1),
    inset 0 1px 1px rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  text-decoration: none;
  text-align: center;
  height: 45px;
  width: fit-content;
  margin: 10px 0;
}
.button:hover {
  background: linear-gradient(135deg, #5a7df4, #3a5af5);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
  transform: translateY(-1px);
}
</style>
