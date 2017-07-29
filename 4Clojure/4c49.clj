(defn my-split-at
  [n s]
  (vector (take n s) (drop n s)))


(println (my-split-at 3 [1 2 3 4 5 6]))
;; => [[1 2 3] [4 5 6]]
