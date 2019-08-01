import numpy as np

def entropy_calculator(input_path="", type="pure"):
    data = [i.split() for i in open(input_path, "r").readlines()]
                
    # get the corpus
    corpus = []
    for snippet in data:
        for word in snippet:
            corpus.append(word)
            
    # get the alphabet of the corpus        
    alphabet = list(set(corpus))
    #    print(alphabet)
            
    # calculate the number of occurrence of each word in the corpus
    occurrences = {}
    for word in alphabet:
        occurrence = len([i for i, x in enumerate(corpus) if x == word])
        occurrences[word] = occurrence
        
    # calculate the probability of each word in the alphabet
    probability = {}
    for _, word in enumerate(occurrences): 
        prob = occurrences[word]/len(corpus)
        probability[word] = prob
                
    # calculate the entropy of the corpus
    entropy = {}
    entropy_sum = 0
    for _, word in enumerate(occurrences):
        prob = occurrences[word]/len(corpus)
        try:
            entropy[word] = -prob * np.log2(prob)
        except ZeroDivisionError:
                pass
            
        if np.isnan(entropy[word]):
            print("the excepted pair is: {0}--{1}".format(word, entropy[word]))
        else:
            entropy_sum += entropy[word]       
    print("corpus: {0}\n".format(input_path))
    print("shannon entropy of the corpus per word: {0}".format(entropy_sum))
    relative_entropy = np.log2(len(alphabet))
    redundancy_sum = 1 - entropy_sum / relative_entropy
    print("redundancy of the corpus per word: {0}".format(redundancy_sum))
    
    # calculate the redundancy of structural information
    if type == "redundant":
        structural_alphabet = ["class", "public", "static", "void", "function", "obj", "new"]
        structual_entropy = sum([entropy[i] for i in structural_alphabet])
        print("shannon entropy of the structure: {0}".format(structual_entropy))
        relative_entropy_structure = structual_entropy / relative_entropy
        print("relative entropy of the structure: {0}".format(relative_entropy_structure))
    else:
        pass
    
    print("\n")
    
    return alphabet, probability, entropy
        
if __name__ == "__main__":
    corpus_path_redundant = r"/home/bob/Documents/dataset_commaf/redundant/prepro/eval.code"
    corpus_path_pure = r"/home/bob/Documents/dataset_commaf/pure/prepro/eval.code"
    bytecode_path = r"/home/bob/Documents/dataset_commaf/pure/prepro/eval.bcode"
    entropy_calculator(input_path=corpus_path_redundant, type="redundant")
    entropy_calculator(input_path=corpus_path_pure, type="pure")
    entropy_calculator(input_path=bytecode_path, type="pure")