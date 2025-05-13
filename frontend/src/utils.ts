import type { Event } from './types/types';

export const areEventsEqual = (events1: Event[], events2: Event[]): boolean => {
  if (events1.length !== events2.length) return false;

  for (let i = 0; i < events1.length; i++) {
    const a = events1[i];
    const b = events2[i];

    if (
      a.id !== b.id ||
      a.name !== b.name ||
      a.duration !== b.duration ||
      a.predecessors.length !== b.predecessors.length ||
      !a.predecessors.every(v => b.predecessors.includes(v))
    ) {
      return false;
    }
  }

  return true;
};
