;; Write a function which returns a personalized greeting.

;; (= (__ "Dave") "Hello, Dave!")
;; (= (__ "Jenn") "Hello, Jenn!")
;; (= (__ "Rhea") "Hello, Rhea!")

;; True function
(defn greeting
    "Say hello to everyone except John. Fuck John."
    [^String name]
    (if (= name "John")
        (str "Fuck you, " name ".")
        (str "Hello, " name "!"))
    )

;; Working code
(fn greeting
    [^String name]
    (if (= name "John")
        (str "Fuck you, " name ".")
        (str "Hello, " name "!"))
    )