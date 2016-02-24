var vue = new Vue({
  el: '#app',
  data: {
    focused: 0,
    sentences: []
  },
  methods: {
    focus: function (sentence) {
      this.focused = this.sentences.indexOf(sentence);
    },
    recordStart: function (sentence) {
      sentence.recording = true;
      $.ajax({url: '/ajax/record_start', data: sentence});
    },
    recordStop: function (sentence) {
      sentence.recording = false;
      $.ajax({url: '/ajax/record_stop', data: sentence});
    },
    delete: function (sentence) {
      $.ajax({url: '/ajax/delete', data: sentence});
      this.sentences.splice(this.focused, 1);
    }
  }
});

// Init sentences with ajax call
$.ajax({
  url: '/ajax/sentences',
  success: function (data) {
    for (sentence of data) {
      sentence.recording = false;
    }
    vue.sentences = data;
  }
});
