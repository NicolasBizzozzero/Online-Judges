(defn xor-etrange
    [& b]
    (if (every? true? b)
        false
        (true? (some true? b))))


(println (truc false))
;; => false

(println (truc true))
;; => false

(println (truc false false))
;; => false

(println (truc false true))
;; => true

(println (truc true false))
;; => true

(println (truc true true))
;; => false
