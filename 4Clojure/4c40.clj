(defn my-interpose
    ""
    [item s]
    (loop [s s, res []]
        (if (seq s)
            (if (>= (count s) 2)
                (recur (rest s) (conj (conj res (first s)) item))
                (conj res (last s)))
            res)))


(println (my-interpose 0 [1 2 3]))
;; => [1 0 2 0 3]

(println (apply str (my-interpose ", " ["one" "two" "three"])))
;; => "one, two, three"

(println (my-interpose :z [:a :b :c :d]))
;; => [:a :z :b :z :c :z :d]
