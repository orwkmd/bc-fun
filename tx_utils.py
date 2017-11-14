

class TXUtils:

    @staticmethod
    def make_simple_transaction(inputs, outputs):
        def make_input(data):
            pass
        def make_output(data):
            pass
        formatted_inputs = ''.join(map(make_input, inputs))
        formatted_outputs = ''.join(map(make_output, outputs))
        return ('01000000' + # version (4 bytes)
                '0:02x'.format(inputs.length) + # Number of inputs (1 byte)
                formatted_inputs +
                'ffffffff' + # sequence number (4 bytes)
                '0:02x'.format(outputs.length) + # Number of outputs (1 byte)
                formatted_outputs +
                '00000000') # locktime: 0 (a block height) (4 bytes)