(defn dec-int->bin-str
    "Convert the decimal number `n` into his string binary representation"
    [n]
    (Integer/valueOf n 2))



(println (dec-int->bin-str 0))
;; => "0"

(println (dec-int->bin-str 7))
;; => "111"

(println (dec-int->bin-str 8))
;; => "1000"

(println (dec-int->bin-str 9))
;; => "1001"

(println (dec-int->bin-str 255))
;; => "11111111"

(println (dec-int->bin-str 1365))
;; => "10101010101"

(println (dec-int->bin-str 65535))
;; => "1111111111111111"
