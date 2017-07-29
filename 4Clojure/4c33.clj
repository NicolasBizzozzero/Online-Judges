(defn repeat-elems
    "Replicate `n` times each element of `s`."
    [s n]
    (mapcat #(take n (repeat %)) s))


(println (repeat-elems [:a :b] 4))
;; => '(:a :a :a :a :b :b :b :b)
