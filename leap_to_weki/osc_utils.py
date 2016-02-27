from pythonosc.osc_message_builder import OscMessageBuilder


def build_osc_message(array):
    builder = OscMessageBuilder(address='/wek/inputs')
    for val in array:
        builder.add_arg(val)
    return builder.build()
