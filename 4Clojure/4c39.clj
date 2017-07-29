(defn my-interleave
    [s1 s2]
    (mapcat #(conj [] %1 %2) s1 s2))

(my-interleave [1] [2])
(my-interleave [1 2 3] [:a :b :c])
;; => '(1 :a 2 :b 3 :c)
