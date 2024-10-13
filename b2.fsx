let isMagicSquare (matrix: int[,]) =
    let n = matrix.GetLength(0)
    
    // Suma de la primera fila como referencia
    let targetSum = Array.sum [| for j in 0 .. n - 1 -> matrix.[0, j] |]

    // Verificar filas
    let rowsMagic = 
        [| for i in 0 .. n - 1 -> Array.sum [| for j in 0 .. n - 1 -> matrix.[i, j] |] |]
        |> Array.forall ((=) targetSum)

    // Verificar columnas
    let colsMagic = 
        [| for j in 0 .. n - 1 -> Array.sum [| for i in 0 .. n - 1 -> matrix.[i, j] |] |]
        |> Array.forall ((=) targetSum)

    // Verificar diagonales
    let diag1Magic = 
        Array.sum [| for i in 0 .. n - 1 -> matrix.[i, i] |] = targetSum

    let diag2Magic = 
        Array.sum [| for i in 0 .. n - 1 -> matrix.[i, n - 1 - i] |] = targetSum

    rowsMagic && colsMagic && diag1Magic && diag2Magic

// Ejemplo de uso
let matrix = array2D [ [8; 1; 6]; [3; 5; 7]; [4; 9; 2] ]
let result = isMagicSquare matrix
printfn "La matriz es mágica: %b" result