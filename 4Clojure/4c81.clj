(defn my-intersection
    [s1 s2]
  	(loop [s1 s1, s2 s2, res #{}]
        (if (seq s1)
            (if (contains? s2 (first s1))
                (recur (rest s1) (disj s2 (first s1)) (conj res (first s1)))
                (recur (rest s1) s2 res))
            res)))


(println (my-intersection #{0 1 2 3} #{2 3 4 5}))
;; => #{2 3}

(println (my-intersection #{0 1 2} #{3 4 5}))
;; => #{}

(println (my-intersection #{:a :b :c :d} #{:c :e :a :f :d}))
;; => #{:a :c :d}
