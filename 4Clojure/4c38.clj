;; Write a function which takes a variable number of parameters and returns the maximum value.

;; (= (__ 1 8 3 4) 8)

;; (= (__ 30 20) 30)

;; (= (__ 45 67 11) 67)

(fn [& numbers]
    (reduce (fn [a b] (if (> a b) a b)) numbers))
