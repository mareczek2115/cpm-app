export interface BaseEvent {
  id: number;
  name: string;
}

export interface Event extends BaseEvent {
  duration: number;
  predecessors: Array<number>;
}

type OptionalNumber = number | null;

export interface Node extends Event {
  early_start: OptionalNumber;
  early_finish: OptionalNumber;
  late_start: OptionalNumber;
  late_finish: OptionalNumber;
  reserve: OptionalNumber;
  successors: Array<number>;
}
