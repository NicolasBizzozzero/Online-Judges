;; Regex patterns are supported with a special reader macro.

;; (= __ (apply str (re-seq #"[A-Z]+" "bA1B3Ce ")))

;; The apply function allows you to take a sequence of arguments and "unpack" them so you can pass them directly to a function as positional arguments. For example, (apply f [a b c]) is equivalent to (f a b c).
;; In this case, re-seq will return a sequence variable, but we want a String variable. So by using (apply str REGEX), we're converting the sequence into a String.

;; The regex will match every capital letter
"ABC"