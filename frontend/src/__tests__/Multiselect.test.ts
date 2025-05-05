import { mount } from '@vue/test-utils';
import Multiselect from '../components/Multiselect.vue';
import { store } from '../store';
import { beforeEach, describe, expect, it } from 'vitest';
import { BaseEvent } from '../types';

describe('Multiselect.vue', () => {
  const fakeEvents: BaseEvent[] = [
    { id: 1, name: 'Event 1' },
    { id: 2, name: 'Event 2' },
  ];

  const baseEvent = {
    id: 123,
    name: 'Main Evenet',
    duration: 5,
    predecessors: [],
  };

  beforeEach(() => {
    store.openedMultiselectId.value = null;
  });

  it('renders all options', () => {
    const wrapper = mount(Multiselect, {
      props: {
        event: { ...baseEvent },
        allEvents: fakeEvents,
      },
    });

    expect(wrapper.find('.dropdown').isVisible()).toBe(false);

    const labels = wrapper.findAll('label');
    expect(labels.length).toBe(2);
    expect(labels[0].text()).toContain('Event 1');
  });

  it('updates selected list and predecessors', async () => {
    const eventCopy = { ...baseEvent };
    const wrapper = mount(Multiselect, {
      props: {
        event: eventCopy,
        allEvents: fakeEvents,
      },
    });

    wrapper.find('.selected').trigger('click');
    const checkbox = wrapper.find('input[type="checkbox"]');

    await checkbox.setValue(true);
    expect(eventCopy.predecessors).toContain(1);

    await checkbox.setValue(false);
    expect(eventCopy.predecessors).not.toContain(1);
  });
});
