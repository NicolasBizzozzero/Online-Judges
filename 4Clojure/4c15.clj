;; Write a function which doubles a number.

;; (= (__ 2) 4)
;; (= (__ 3) 6)
;; (= (__ 11) 22)
;; (= (__ 7) 14)

;; This is the function required
(fn double-number
    "Return the double of a number"
    [^double n]
    (* n 2))

;; But only th following code will work on 4clojure.com
(fn double-number
    [^double n]
    (* n 2))