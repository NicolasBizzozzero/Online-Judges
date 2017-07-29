;; The ->> macro threads an expression x through a variable number of forms. First, x is inserted as the last item in the first form, making a list of it if it is not a list already. Then the first form is inserted as the last item in the second form, making a list of that form if necessary. This process continues for all the forms. Using ->> can sometimes make your code more readable.

;; (= (__ (map inc (take 3 (drop 2 [2 5 4 1 3 6]))))
;;   (->> [2 5 4 1 3 6] (drop 2) (take 3) (map inc) (__))
;;   11)

(= (reduce + (map inc (take 3 (drop 2 [2 5 4 1 3 6]))))
   
   (->>
    [2 5 4 1 3 6]
    (drop 2)  ;; (drop 2 [2 5 4 1 3 6]) => [4 1 3 6]
    (take 3)  ;; (take 3 [4 1 3 6]) => [4 1 3]
    (map inc) ;; (map inc [4 1 3]) => [5 2 4]
    (reduce +))  ;; (reduce + [5 2 4]) => 11
 11)

reduce +
