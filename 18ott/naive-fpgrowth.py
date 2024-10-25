class FpGrowth:
    def __init__(self, input: list):
        self.input = input
        self.item_2_label,self.label_2_item,self.label_freq = self.create_labels()
        self.normalized_dataset = self.create_normalized_dataset()
        pass

    def create_labels(self):
        dictionary = dict()
        for tuple_ in self.input:
            for column in tuple_:
                dictionary[column] = (1 + dictionary[column]) if column in dictionary else 1
        sorted_keys = sorted(dictionary.items(), reverse=True, key = lambda item: item[1] )
        item_2_label = { item: label for (label, (item, freq)) in enumerate(sorted_keys) }
        label_2_item = { label: item for (label, (item, freq)) in enumerate(sorted_keys) }
        label_freq = { label: freq for (label, (item, freq)) in enumerate(sorted_keys) }
        return item_2_label, label_2_item, label_freq
    
    def create_normalized_dataset(self):
        dataset = []
        for tuple_ in self.input:
            columns = []
            for column in tuple_:
                columns.append(self.item_2_label[column])
            dataset.append(tuple(set(sorted(columns))))
        return dataset

    def print_normalized_dataset(self):
        for elem in self.normalized_dataset:
            print( tuple(self.label_2_item[label] for label in elem))
    def run(self, min_support = 5, use_colnames=False):
        tuples = dict()
        for elem in self.normalized_dataset:
            # creo l'insieme delle parti
            set_span = 2 ** len(elem)
            for i in range(set_span):
                tuple_ = tuple( elem[j] for j in range(len(elem)) if i & 1 << j )
                if len(tuple_) > 0:
                    tuples[tuple_] = 1 + (tuples[tuple_] if tuple_ in tuples else 0)
            
        result = [ (labels, support) for (labels, support) in tuples.items() if support >= min_support ]
        if use_colnames:
            return [ ( tuple(self.label_2_item[label] for label in labels), support) for (labels, support) in result ]
        else:
            return result

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

alg = FpGrowth(dataset)
alg.print_normalized_dataset()
print(alg.normalized_dataset)
print(alg.label_2_item)
print(alg.label_freq)
min_support = 3
result = alg.run(min_support  )
print(result)
result = alg.run(min_support, use_colnames=True)
print(result)

