import { ref } from 'vue';
import type { Event, Node } from './types/types';

export const store = {
  openedMultiselectId: ref<number | null>(null),
  originalEvents: ref<Event[]>([]),
  currentEvents: ref<Event[]>([]),
  nodes: ref<Node[]>([]),
  graph_url: ref<string | null>(null),
};
