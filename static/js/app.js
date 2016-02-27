var vue = new Vue({
  el: '#app',
  data: {
    focused: -1,
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
      this.sentences.splice(this.focused, 1);
      this.focused = -1;
      $.ajax({url: '/ajax/delete', data: sentence});
    },
    addNewSentence: function () {
      var that = this,
          textInput = $("#new-sentence-text");
      $.ajax({
        url: '/ajax/add_new_sentence',
        data: {'text': textInput.val()},
        success: function (sentence) {
          sentence.recording = false;
          that.sentences.push(sentence);
          textInput.val('');
        }
      });
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
