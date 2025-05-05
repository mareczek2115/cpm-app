import { mount } from '@vue/test-utils';
import Event from '../components/Event.vue';
import { describe, it, expect } from 'vitest';

describe('Event.vue', () => {
  const baseEvent = {
    id: 42,
    name: 'Test Event',
    duration: 10,
    predecessors: [],
  };

  const fakeEvents = [
    { id: 1, name: 'Event 1' },
    { id: 2, name: 'Event 2' },
  ];

  it('renders inputs with correct initial values', () => {
    const wrapper = mount(Event, {
      props: {
        event: { ...baseEvent },
        allEvents: fakeEvents,
      },
    });

    const input = wrapper.findAll('input');
    expect(input[0].element.value).toBe('Test Event');
    expect(input[1].element.value).toBe('10');
  });

  it('updates event data when input changes', async () => {
    const eventCopy = { ...baseEvent };
    const wrapper = mount(Event, {
      props: {
        event: eventCopy,
        allEvents: fakeEvents,
      },
    });

    const nameInput = wrapper.findAll('input')[0];
    const durationInput = wrapper.findAll('input')[1];

    await nameInput.setValue('New event');
    await durationInput.setValue(3);

    expect(eventCopy.name).toBe('New event');
    expect(eventCopy.duration).toBe('3');
  });

  it('emits remove-event with correct ID on CloseCircle click', async () => {
    const wrapper = mount(Event, {
      props: {
        event: { ...baseEvent },
        allEvents: fakeEvents,
      },
    });

    const closeBtn = wrapper.find('.close-circle');
    await closeBtn.trigger('click');

    expect(wrapper.emitted()).toHaveProperty('remove-event');
    expect(wrapper.emitted('remove-event')![0]).toEqual([42]);
  });
});
