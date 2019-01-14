<template>
  <q-page class="flex flex-center">
    <q-list highlight >
      <q-list-header>Task</q-list-header>
      <q-item tag="label" v-for="i in   tasks" :key="i.id">
        <q-item-main>
          <q-item-tile label>{{i.name}}</q-item-tile>
          <q-item-tile sublabel>{{i.description}}</q-item-tile>
        </q-item-main>
      </q-item>
    </q-list>
  </q-page>
</template>
<style>
</style>

<script>
import gql from 'graphql-tag';

const TaskQuery = gql`
  query {
    tasks {
      id
      completed
      name
      description
    }
  }
`;

export default {
  name: 'PageIndex',
  data() {
    return {
      // Initialize your apollo data
      tasks: '',
    };
  },
  apollo: {
    // Simple query that will update the 'hello' vue property
    tasks: TaskQuery,
  },
};

</script>
