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

const buildGraph = (events: Event[]): Record<number, number[]> => {
  const graph: Record<number, number[]> = {};

  for (const event of events) {
    if (!graph[event.id]) graph[event.id] = [];

    for (const predId of event.predecessors) {
      if (!graph[predId]) graph[predId] = [];

      graph[predId].push(event.id);
    }
  }

  return graph;
};

export const hasCycle = (events: Event[]) => {
  const graph = buildGraph(events);

  const visited = new Set<number>();
  const recStack = new Set<number>();

  const dfs = (node: number) => {
    if (recStack.has(node)) return true;
    if (visited.has(node)) return false;

    visited.add(node);
    recStack.add(node);

    for (const neighbor of graph[node] || []) {
      if (dfs(neighbor)) return true;
    }

    recStack.delete(node);
    return false;
  };

  for (const node in graph) {
    if (dfs(Number(node))) return true;
  }

  return false;
};
