export interface BaseEvent {
  id: number;
  name: string;
}

export interface Event extends BaseEvent {
  duration: number;
  predecessors: Array<number>;
}
