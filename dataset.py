""" @TODO 
    - support tensorflow_datasets, pytorch dataloader and other built-in datasets
    - batch support
"""
class TextAttackDataset:
    """ A dataset for text attacks.
    
        Any iterable of (label, text_input) pairs qualifies as 
        a TextAttackDataset.
    """
    def __init__(self):
        """ Loads a full dataset from disk. """
        raise NotImplementedException()
    
    def __iter__(self):
        """ Called to iterate through a dataset. """
        return self.examples.__iter__()
    
    def __next__(self):
        """ Called to iterate through a dataset. """
        return self.examples.__next__()
    
    def _load_text_file(self, text_file_name, N=None):
        """ Loads (label, text) pairs from a text file. 
        
            Format must look like:
            
                1 this is a great little ...
                0 "i love hot n juicy .  ...
                0 "\""this world needs a ...
        """
        examples = []
        i = 0
        for raw_line in open(text_file_name, 'r').readlines():
            tokens = raw_line.strip().split()
            label = int(tokens[0])
            text = ' '.join(tokens[1:])
            examples.append((label, text))
            i += 1
            if N and i >= N: break
        return examples