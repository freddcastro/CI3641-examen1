let rec modExp a b c =
    if c <= 2 then
        failwith "Error: c must be greater than 2"
    if b = 0 then 1
    else
        let partial = modExp a (b - 1) c
        (a % c * partial % c) % c


// Ejemplo de uso
let a = 3
let b = 4
let c = 4
let result = modExp a b c
printfn "El resultado de %d^%d mod %d es %d" a b c result


