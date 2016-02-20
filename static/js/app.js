var vue = new Vue({
  el: '#app',
  data: {
    recording: false,
    focused: {text: ''},
    sentences: []
  },
  methods: {
    focus: function (sentence) {
      var index = this.sentences.indexOf(sentence);
      this.sentences.splice(index, 1);
      this.unfocus();
      this.focused = sentence;
    },
    unfocus: function () {
      if (this.focused.text != '') {
        this.sentences.push(this.focused);
      }
      this.focused = {text: ''};
    },
    record: function () {
      var data = {sentence_id: vue.focused.id};
      data.state = this.recording ? "stop" : "start"
      $.ajax({url: '/ajax/record', data: data});
      this.recording = !this.recording;
    },
    delete: function() {
      if (this.focused.text != '') {
        $.ajax({url: '/ajax/delete', data: {sentence_id: this.focused.id}});
        this.focused = {text: ''}
      }
    },
  }
});

// Init sentences with ajax call
$.ajax({
  url: '/ajax/sentences',
  success: function (data) {
    vue.sentences = data;
  }
});
