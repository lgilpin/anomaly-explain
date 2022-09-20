;; LHG started in 2022 for PAX project

(define query '(candidateinferencecontent (cifn 1 7 (matcherfn 18 0)) (subtask (isabove b d) (ison b c))))

(define Graph 
  '((A (B E))
    (B (E F))
    (C (D))
    (D ())
    (E (C F))
    (F (D G))
    (G ())))

(define (make-tree analogy)
              (if (null? analogy)
                  '()
                   (cons (explain (car analogy)) (make-tree (cdr
                                                             analogy)))))

(define (tree-explainer-bad analogy)
              (if (not (list? analogy))
                  (list analogy)
                  (list (car analogy) 
                        (tree-explainer (cadr analogy))
                        (tree-explainer (caddr analogy)))))

(define (tree-explainer analogy layer)
  (if (null? analogy)
      '()
      (if (list? analogy)
          (if (list? (car analogy))
                  (cons (explain analogy) (tree-explainer (cdr
                                                           analogy) (+
                                                                     layer
                                                                     1)))
                  (cons (car analogy) (tree-explainer (cdr
                                                       analogy) (+
                                                                 layer
                                                                 1))))
          )
      )
  )

(define (explain-last analogy)
  (if (null? analogy)
      '()
      (let ((first (car analogy))
            (second (cdr analogy)))
        (if (null? second)
            first
            (explain-last second)))))

(define (unpack single-list)
  (cdr single-list))

(define (explain-placeholder anything)
  (cons "explaining" (car anything)))

;; (reduce-right list '() query)

(define (flatten mylist)
  (cond ((null? mylist) '())
        ((list? (car mylist)) (append (flatten (car mylist))
                                      (flatten (cdr mylist))))
        (else (cons (car mylist) (flatten (cdr mylist))))))
                                          

;; Part of the explain code to find a list or sublist
(define (present? item list)
    (cond ((or (not (list? list)) (null? list)) #f)
          ((let ((x (car list))) (or (eqv? item x) (present? item x))) #t)
          (else (present? item (cdr list)))))

(define (present-list? item list)
    (cond ((or (not (list? list)) (null? list)) '())
          ((let ((x (car list)))
             (or (eqv? item x) (present-list? item x))) x)
          (else (present-list? item (cdr list)))))

(define (read-lines . args)
  (let ((p (cond ((null? args) (current-input-port))
                 ((port? (car args)) (car args))
                 ((string? (car args)) (open-input-file (car args)))
                 (else (error 'read-lines "bad argument")))))
    (let loop ((line (read-line p)) (lines (list)))
      (if (eof-object? line)
          (begin (if (and (pair? args) (string? (car args)))
                   (close-input-port p))
                 (reverse lines))
          (loop (read-line p) (cons line lines))))))

(define raw-kb (read-lines "sme_relations_b_above_d.txt"))

(define (clean-kb kb)
  (if (null? kb) '()
      (let ((current (string-downcase (string-trim (car kb)))))
        (if (or (equal? current  "") (string-prefix? ";;" (car kb)))
                (clean-kb (cdr kb))
                (cons current (clean-kb (cdr kb)))))))

(define (search-for-substring sublist full-kb)
  (if (null? full-kb) '()
      (let ((current (car full-kb)))
        (if (substring? sublist current)
            (cons current (search-for-substring sublist (cdr full-kb)))
            (search-for-substring sublist (cdr full-kb))))))

(define (explain anything)
  (cons "explaining" (search-for-substring (string (car anything)) kb)))

;; Explaining part for demo
(define kb (clean-kb raw-kb))
(tree-explainer query 0)

;; This is a test, it works!
;;(search-for-substring (string (cadr query)) kb)
        

;;(define present?
;;  (lambda (x list)
;;    (cond ((or (not (list? list)) (null? list)) #f)
;;      ((or (eqv? x (car list)) (present? x (car list))) #t)
;;      (else (present? x (cdr list))))))

;; Testing
;; (not (assert (present? 0 '(1 2 3 4))))
;; => #f
;;(assert (present? 3 '(1 2 3 4)))
;; => #t
;;(present? 0 '((1 2) (3 4)))
;; => #f
;; (present? 3 '((1 2) (3 4)))
;; => (3 4)

;; (search-for-substring (cadr query) kb)

;; start from the end

(define (intersection first second)
  (if (null? first
