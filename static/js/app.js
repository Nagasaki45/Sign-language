var ws = new window.WebSocket("ws://" + location.host + '/ws');

var vue = new Vue({
  el: '#app',
  data: {
    recording: false,
    focused: {text: 'Not loaded yet...'},
    sentences: []
  },
  computed: {
    record_btn_properties: function () {
      if (this.recording) {
        return {cls: 'btn-danger', text: 'Stop recording'};
      } else {
        return {cls: 'btn-success', text: 'Record'};
      }
    }
  },
  methods: {
    focus: function (sentence) {
      var index = this.sentences.indexOf(sentence);
      this.sentences.splice(index, 1);
      if (this.focused != null) {
        this.sentences.push(this.focused);
      }
      this.focused = sentence;
    },
    record: function () {
      if (this.recording) {
      } else {
      }
      this.recording = !this.recording;
    }
  }
});

ws.onopen = (function () {
  var msg = {type: "get_sentences"};
  ws.send(JSON.stringify(msg));
});

ws.onmessage = (function (msg) {
  var handlers = {
    'sentences': function (content) {
      vue.focused = content.pop();
      vue.sentences = content;
    }
  };
  var msg = JSON.parse(msg.data);
  handlers[msg.type](msg.content);
});
