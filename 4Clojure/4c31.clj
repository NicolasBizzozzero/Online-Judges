(defn pack-consecutives
    [coll]
    (partition-by identity coll))


(println (pack-consecutives [1 1 2 1 1 1 3 3]))
;; => '((1 1) (2) (1 1 1) (3 3))
