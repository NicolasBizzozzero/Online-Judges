;; Write a function which duplicates each element of a sequence.


(fn seq-double [sequence]
    (loop [sequence sequence, res []]
         (if-not (empty? sequence)
              (recur (rest sequence) (conj res (first sequence) (first sequence)))
               res)))