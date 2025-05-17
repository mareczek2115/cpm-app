export interface BaseEvent {
  id: number;
  name: string;
}

export interface Event extends BaseEvent {
  duration: number;
  predecessors: Array<number>;
}

export interface Node extends Event {
  early_start: number;
  early_finish: number;
  late_start: number;
  late_finish: number;
  reserve: number;
  successors: Array<number>;
}
