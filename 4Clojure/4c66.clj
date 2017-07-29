(fn pgcd
    [a b]
  	(loop [a a, b b, reminder (rem a b)]
        (if (zero? reminder)
            b
          	(recur b reminder (rem b reminder)))))

