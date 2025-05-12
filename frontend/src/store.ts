import { ref } from 'vue';
import type { Event, Node } from './types/types';

export const store = {
  openedMultiselectId: ref<number | null>(null),
  events: ref<Event[]>([]),
  nodes: ref<Node[]>([]),
};
