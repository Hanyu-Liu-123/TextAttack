"""
Word Swap by BERT-Masked LM.
-------------------------------
"""

import itertools
import re

import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer
from transformers import pipeline

from textattack.shared import utils

from .word_swap import WordSwap


class ChineseWordSwapMaskedLM(WordSwap):
    """Generate potential replacements for a word using a masked language
    model.

    Based off of following papers
        - "Robustness to Modification with Shared Words in Paraphrase Identification" (Shi et al., 2019) https://arxiv.org/abs/1909.02560
        - "BAE: BERT-based Adversarial Examples for Text Classification" (Garg et al., 2020) https://arxiv.org/abs/2004.01970
        - "BERT-ATTACK: Adversarial Attack Against BERT Using BERT" (Li et al, 2020) https://arxiv.org/abs/2004.09984
        - "CLARE: Contextualized Perturbation for Textual Adversarial Attack" (Li et al, 2020): https://arxiv.org/abs/2009.07502

    BAE and CLARE simply masks the word we want to replace and selects replacements predicted by the masked language model.

    BERT-Attack instead performs replacement on token level. For words that are consisted of two or more sub-word tokens,
        it takes the top-K replacements for seach sub-word token and produces all possible combinations of the top replacments.
        Then, it selects the top-K combinations based on their perplexity calculated using the masked language model.

    Choose which method to use by specifying "bae" or "bert-attack" for `method` argument.

    Args:
        method (str): the name of replacement method (e.g. "bae", "bert-attack")
        masked_language_model (Union[str|transformers.AutoModelForMaskedLM]): Either the name of pretrained masked language model from `transformers` model hub
            or the actual model. Default is `bert-base-uncased`.
        tokenizer (obj): The tokenizer of the corresponding model. If you passed in name of a pretrained model for `masked_language_model`,
            you can skip this argument as the correct tokenizer can be infered from the name. However, if you're passing the actual model, you must
            provide a tokenizer.
        max_length (int): the max sequence length the masked language model is designed to work with. Default is 512.
        window_size (int): The number of surrounding words to include when making top word prediction.
            For each word to swap, we take `window_size // 2` words to the left and `window_size // 2` words to the right and pass the text within the window
            to the masked language model. Default is `float("inf")`, which is equivalent to using the whole text.
        max_candidates (int): maximum number of candidates to consider as replacements for each word. Replacements are ranked by model's confidence.
        min_confidence (float): minimum confidence threshold each replacement word must pass.
        batch_size (int): Size of batch for "bae" replacement method.

    """

    def __init__(self, **kwargs):
        self.unmasker = pipeline('fill-mask', model='xlm-roberta-base')
        super().__init__(**kwargs)

    def get_replacement_words(self, current_text, indice_to_modify):

        masked_text = current_text.replace_word_at_index(
            indice_to_modify, "<mask>"
        )
        outputs = self.unmasker(masked_text.text)
        words = []
        for dict in outputs:
            take = True
            for char in dict['token_str']:
                if not is_cjk(char):
                    take = False
            if take:
                words.append(dict['token_str'])


        return words

    def _get_transformations(self, current_text, indices_to_modify):
        words = current_text.words
        transformed_texts = []

        for i in indices_to_modify:
            word_to_replace = words[i]
            replacement_words = self.get_replacement_words(current_text, i)
            transformed_texts_idx = []
            for r in replacement_words:
                if r == word_to_replace:
                    continue
                transformed_texts_idx.append(current_text.replace_word_at_index(i, r))
            transformed_texts.extend(transformed_texts_idx)

        return transformed_texts


cjk_ranges = [
    (0x4E00, 0x62FF),
    (0x6300, 0x77FF),
    (0x7800, 0x8CFF),
    (0x8D00, 0x9FCC),
    (0x3400, 0x4DB5),
    (0x20000, 0x215FF),
    (0x21600, 0x230FF),
    (0x23100, 0x245FF),
    (0x24600, 0x260FF),
    (0x26100, 0x275FF),
    (0x27600, 0x290FF),
    (0x29100, 0x2A6DF),
    (0x2A700, 0x2B734),
    (0x2B740, 0x2B81D),
    (0x2B820, 0x2CEAF),
    (0x2CEB0, 0x2EBEF),
    (0x2F800, 0x2FA1F)
]


def is_cjk(char):
    char = ord(char)
    for bottom, top in cjk_ranges:
        if bottom <= char <= top:
            return True
    return False
