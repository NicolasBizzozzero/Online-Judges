;; Write a function which creates a list of all integers in a given range.

(fn my-range [floor ceil]
    (loop [floor floor, res []]
         (if-not (= ceil floor)
              (recur (inc floor) (conj res floor))
               res)))