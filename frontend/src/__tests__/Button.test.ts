import { mount } from '@vue/test-utils';
import Button from '../components/Button.vue';
import { describe, expect, it } from 'vitest';

describe('Button.vue', () => {
  it('renders the title from props', () => {
    const wrapper = mount(Button, {
      props: {
        title: 'Hello World',
      },
    });
    expect(wrapper.text()).toContain('Hello World');
  });

  it('emits onclick event when clicked', async () => {
    const wrapper = mount(Button, {
      props: {
        title: 'Hello World',
      },
    });

    await wrapper.trigger('click');

    expect(wrapper.emitted()).toHaveProperty('onclick');
    expect(wrapper.emitted('onclick')?.length).toBe(1);
  });
});
