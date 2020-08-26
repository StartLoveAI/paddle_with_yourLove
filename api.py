import paddlehub as hub

module = hub.Module(name="ernie_gen_lover_words")

texts = input('')
test_texts = [str(texts)]
results = module.generate(texts=test_texts, use_gpu=True, beam_width=1)
for result in results:
    print(result)
